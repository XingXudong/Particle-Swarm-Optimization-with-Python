# Particle-Swarm-Optimization-with-Python
粒子群优化算法的Python实现

充分利用Python面向对象的特点将粒子的位置属性、速度属性等以及搜索逻辑封装至一个class中（standard_particle.py）；将粒子属性、待优化问题（目标函数）完全解耦，最后在主脚本（pso_main_script）中调用粒子类和优化问题类创建相应的对象实现算法的应用。也方便了算法逻辑与优化问题的改进或扩展，欢迎大佬们指点。

目前待优化问题代码中（fitness_function.py）只写了一个Rastrigin函数（可以设置任意优化维度），感兴趣的话可以下载下来多写几种优化函数玩玩，算法是求最小化问题的。
