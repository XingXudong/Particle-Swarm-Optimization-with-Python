"""
	PSO算法的主逻辑脚本
	编写人：XingXudong
	邮箱：xd_xing@sina.com
	时间：2018.06.29
	版本：v0.1
"""

import numpy as np
import fitness_function as ff
import standard_particle as sp
import matplotlib.pyplot as plt

dimension = 2   # 优化问题特征维度

# 算法超参数设置
c1 = 2
c2 = 2
iteration_num = 50
particle_num = 100
max_velocity = 0.005
min_velocity = 0.001
max_position = 50
min_position = -50

# 种群初始化
particle_swarm = []
for i in range(particle_num):
	particle_swarm.append(sp.Particle(dimension, max_position, min_position, max_velocity, min_velocity))

# 适应度值计算
fitness_function = ff.FitnessFunction(dimension)    # 创建适应度函数对象
fitness_value = []  # 适应度值
personal_best = []  # 个体历史最优位置
fitness_personal_best = []  # 个体历史最优适应度值
for particle in particle_swarm:
	fitness_value.append(fitness_function.rastrigin(particle.position))
	personal_best.append(particle.position)
	fitness_personal_best.append(fitness_function.rastrigin(particle.position))

global_best = personal_best[int(np.argmax(fitness_personal_best))]  # 种群全局最优位置
fitness_global_best = np.amax(fitness_personal_best)    # 种群全局最优适应度值

yy = []
for i in range(iteration_num):

	for particle_index, particle in enumerate(particle_swarm):
		particle.update_velocity(c1, c2, personal_best[particle_index], global_best)    # 速度更新
		particle.update_position()  # 位置更新
		particle.correction()   # 搜索范围和搜索速度修正
		fitness_value[particle_index] = fitness_function.rastrigin(particle.position)   # 适应度值更新

	for particle_index, particle in enumerate(particle_swarm):
		if fitness_value[particle_index] < fitness_personal_best[particle_index]:
			fitness_personal_best[particle_index] = fitness_value[particle_index]
			personal_best[particle_index] = particle.position
		if fitness_value[particle_index] < fitness_global_best:
			fitness_global_best = fitness_value[particle_index]
			global_best = particle.position

	yy.append(fitness_global_best)

# 结果可视化
plt.figure()
plt.plot(range(1, iteration_num + 1), yy)
plt.xlabel('iterate')
plt.ylabel('fitness value')
plt.title('PSO algorithm for 2D Rastrigin')
plt.show()
