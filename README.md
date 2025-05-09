# Flappy Bird 电脑版

魔改于这个项目(https://github.com/markub3327/flappy-bird-gymnasium) ，增加了水管空隙距离 ，减小了小鸟的碰撞体积，减小游戏难度。有助于强化学习相关项目训练的收敛（此代码不包含强化学习）。其中custom_constants.py和custom_env.py是修改原版本碰撞体积之类的参数的，如果觉得难度高或低可自行修改，play.py是用来玩这个游戏的，默认使用空格键跳跃，修改action部分的逻辑可以接入强化学习项目，剩下的请参考原本项目的链接(https://github.com/markub3327/flappy-bird-gymnasium) 。
