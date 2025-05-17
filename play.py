import flappy_bird_gymnasium
import gymnasium
import pygame
import time
from custom_env import CustomFlappyBirdEnv
from custom_constants import PIPE_GAP

def game_loop(env):
    obs, _ = env.reset()
    running = True
    paused = False
    score = 0
    
    while running:
        # 处理pygame事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # 返回False表示完全退出游戏
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False  # 返回False表示完全退出游戏
                elif event.key == pygame.K_a:  # 添加暂停切换
                    paused = not paused
                    if paused:
                        print("游戏已暂停")
                        pygame.display.iconify()  # 最小化窗口
                    else:
                        print("游戏继续")
                        pygame.display.update()  # 恢复窗口显示
        
        if not paused:  # 只在非暂停状态下执行游戏逻辑
            # 检查空格键状态
            keys = pygame.key.get_pressed()
            action = 1 if keys[pygame.K_SPACE] else 0
                
            # 执行动作
            obs, reward, terminated, _, info = env.step(action)
            
            # 更新分数
            if reward == 1:  # 通过管道得分
                score += 1
                print(f"得分：{score}")
            
            # 检查游戏是否结束
            if terminated:
                print(f"游戏结束！最终得分：{score}")
                return True  # 返回True表示需要重新开始游戏
        
        # 控制游戏速度
        time.sleep(1/30)  # 30FPS
    
    return False

def play_game():
    # 初始化pygame
    pygame.init()
    
    # 创建自定义环境，设置更大的管道缝隙
    env = CustomFlappyBirdEnv(render_mode="human", use_lidar=False, pipe_gap=PIPE_GAP)
    
    print("游戏开始！按空格键跳跃，按'a'暂停游戏，按'q'退出游戏")
    print("注意：当前使用的是更小的碰撞体积和更大的管道缝隙，更容易通过管道")
    
    while True:
        should_continue = game_loop(env)
        if not should_continue:
            break
    
    # 清理
    pygame.quit()
    env.close()

if __name__ == "__main__":
    play_game()