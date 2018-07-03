"""
	基本粒子（类）
	编写人：邢旭东
	邮箱：xd_xing@sina.com
	时间：2018.06.29
	版本：v0.1
"""

from numpy import random as nr


class Particle:
	"""
		粒子的类构造系统
	"""

	def __init__(self, dimension, max_position, min_position, max_velocity, min_velocity):
		"""
		对象构造方法
		:param dimension: 特征维度
		:param max_position: 位置最大值（标量）
		:param min_position: 位置最小值（标量）
		:param max_velocity: 速度最大值（标量）
		:param min_velocity: 速度最小值（标量）
		"""
		self.dimension = dimension
		self.max_position = max_position
		self.min_position = min_position
		self.max_velocity = max_velocity
		self.min_velocity = min_velocity
		self.position = self.min_position + (self.max_position - self.min_position) * nr.uniform(0, 1, size=(1, self.dimension))
		self.velocity = self.min_velocity + (self.max_velocity - self.min_velocity) * nr.uniform(-1, 1, size=(1, self.dimension))

	def correction(self):
		"""
		偏移修正方法
			对超移动位置和速度大小超出阈值的粒子进行修正
		:return: 无
		"""
		self.position[self.position > self.max_position] = self.max_position
		self.position[self.position < self.min_position] = self.min_position
		self.velocity[self.velocity > self.max_velocity] = self.max_velocity
		self.velocity[self.velocity < self.min_velocity] = self.min_velocity

	def update_velocity(self, c1, c2, personal_best, global_best):
		"""
		粒子速度更新方法
		:param c1: 个体历史最优学习系数c1
		:param c2: 种群全局最优学习系数c2
		:param personal_best: 个体历史最优位置
		:param global_best: 种群全局最优位置
		:return: 无
		"""
		self.velocity = self.velocity + \
			c1 * nr.uniform(0, 1) * (personal_best - self.position) + \
			c2 * nr.uniform(0, 1) * (global_best - self.position)

	def update_position(self):
		"""
		粒子位置更新方法
		:return: 无
		"""
		self.position = self.position + self.velocity

