"""
	适应度值函数管理（类）
	编写人：XingXudong
	邮箱：xd_xing@sina.com
	时间：2018.06.29
	版本：v0.1
"""

import numpy as np


class FitnessFunction:
	"""
		适应度值函数管理系统
	"""

	def __init__(self, dimension):
		"""
		类构造方法
		:param dimension: 特征维度
		"""
		self.dimension = dimension

	def rastrigin(self, position):
		"""
		Rastrigin函数
		:param position: 函数自变量
		:return: 适应度值
		"""
		fitness_value = -10 * self.dimension * \
			np.exp(-0.2 * (np.sum(position ** 2) / 2) ** 0.5) - \
			np.exp(np.sum(np.cos(2 * np.pi * position)) / 2) + \
			10 * self.dimension + np.exp(1)
		return fitness_value


if __name__ == '__main__':
	fun = FitnessFunction(2)
	val = fun.rastrigin(np.array([0, 0]))
	print(val)

