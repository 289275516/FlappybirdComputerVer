from flappy_bird_gymnasium.envs.constants import *

# 进一步减小鸟的尺寸
PLAYER_WIDTH = 20  # 原来是24
PLAYER_HEIGHT = 14  # 原来是18

# 重新计算私有区域大小，进一步减小
PLAYER_PRIVATE_ZONE = (max(PLAYER_WIDTH, PLAYER_HEIGHT) + 15) / 2  # 原来是20

# 更新激光雷达最大距离
LIDAR_MAX_DISTANCE = int(288 * 0.8) - PLAYER_WIDTH

# 增加管道缝隙
PIPE_GAP = 150  # 默认是100 