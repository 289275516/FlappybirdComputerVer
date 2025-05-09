import flappy_bird_gymnasium
import gymnasium
import pygame
import time
from custom_env import CustomFlappyBirdEnv
from custom_constants import PIPE_GAP

def play_game():
    # 初始化pygame
    pygame.init()
    
    # 创建自定义环境，设置更大的管道缝隙
    env = CustomFlappyBirdEnv(render_mode="human", use_lidar=False, pipe_gap=PIPE_GAP)
    obs, _ = env.reset()
    
    print("游戏开始！按空格键跳跃，按'q'退出游戏")
    print("注意：当前使用的是更小的碰撞体积和更大的管道缝隙，更容易通过管道")
    
    running = True
    score = 0
    while running:
        # 处理pygame事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        
        # 检查空格键状态
        keys = pygame.key.get_pressed()
        action = 1 if keys[pygame.K_SPACE] else 0
            
        # 执行动作
        obs, reward, terminated, _, info = env.step(action)
        
        # 更新分数
        if reward == 1:  # 通过管道得分
            score += 1
            print(f"得分：{score}")
        
        # 控制游戏速度
        time.sleep(1/30)  # 30FPS
        
        # 检查游戏是否结束
        if terminated:
            print(f"游戏结束！最终得分：{score}")
            running = False
    
    # 清理
    pygame.quit()
    env.close()

if __name__ == "__main__":
    play_game()