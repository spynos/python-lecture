import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE, K_r

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()
pygame.key.set_repeat(5, 5) #key가 눌리는 간격이 5 ms

def main():
    # 기본설정
    walls = 80 # 80개의 세로줄 벽으로 동굴이 구성
    ship_y = 250
    velocity = 0
    score = 0
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("ship.png")
    ship_image = pygame.transform.rotate(ship_image, 270) # 우주선 방향 전환
    bang_image = pygame.image.load("bang.png")
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400)) # 기본 구멍 뚫기
    game_over = False

    while True:
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True
                elif event.key == K_r:
                    main()

        # 우주선 이동
        if not game_over:
            score += 10
            velocity += -1 if is_space_down else 1
            ship_y += velocity

            # 앞으로 이동 (동굴을 뒤로 스크롤)
            edge = holes[-1].copy() # 마지막 구멍
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = randint(1, 6) * (-1 if slope > 0 else 1)
                edge.inflate_ip(0, -20)
            edge.move_ip(10, slope)
            holes.append(edge)
            del holes[0]
            holes = [x.move(-10, 0) for x in holes]

            # 충돌 검사
            if holes[0].top > ship_y + 40 or \
               holes[0].bottom < ship_y + 80:
                game_over = True

        
        # 화면 그리기
        SURFACE.fill((200, 200, 100))
        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)
        SURFACE.blit(ship_image, (0, ship_y))
        score_image = sysfont.render("score {}".format(score), True, (0,0,255))
        SURFACE.blit(score_image, (600, 20))

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y))
            game_over_image = pygame.font.SysFont(None, 100).render("GAME OVER", True, (255,0,0))
            SURFACE.blit(game_over_image, (200, 300))

        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == '__main__':
    main()
