from flappy_bird_gymnasium.envs.flappy_bird_env import FlappyBirdEnv
from custom_constants import *

class CustomFlappyBirdEnv(FlappyBirdEnv):
    """自定义的Flappy Bird环境，使用更小的碰撞体积"""
    
    def __init__(self, *args, **kwargs):
        # 在调用父类初始化之前，确保使用我们的自定义常量
        self.PLAYER_WIDTH = PLAYER_WIDTH
        self.PLAYER_HEIGHT = PLAYER_HEIGHT
        self.PLAYER_PRIVATE_ZONE = PLAYER_PRIVATE_ZONE
        self.LIDAR_MAX_DISTANCE = LIDAR_MAX_DISTANCE
        
        super().__init__(*args, **kwargs) 