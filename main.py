import pygame
from ball import Ball
from paddle import Paddle
from scorekeeper import ScoreKeeper


PADDLE_SPEED = 10
BALL_DIAMETER = 20


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('pong')

    # Initialise background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    line_start = (screen.get_width() / 2, 0)
    line_end = (screen.get_width() / 2, screen.get_height())
    pygame.draw.line(background, (255, 255, 255), line_start, line_end, width=4)

    # Initialise clock
    clock = pygame.time.Clock()

    # Initialise ball
    ball = Ball(int(BALL_DIAMETER / 2))
    ball_sprite = pygame.sprite.RenderPlain(ball)

    # Initialise paddles
    left_paddle = Paddle('left')
    right_paddle = Paddle('right')
    paddle_sprites = pygame.sprite.RenderPlain((left_paddle, right_paddle))

    # Initialise score
    left_score = ScoreKeeper(screen.get_width() / 4, 30)
    right_score = ScoreKeeper((screen.get_width() / 4) * 3, 30)
    score_sprites = pygame.sprite.RenderPlain((left_score, right_score))

    while True:
        clock.tick(60)  # 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_a:
                    left_paddle.steps = -PADDLE_SPEED  # left paddle up
                elif event.key == pygame.K_z:
                    left_paddle.steps = PADDLE_SPEED  # left paddle down

                if event.key == pygame.K_k:
                    right_paddle.steps = -PADDLE_SPEED  # right paddle up
                elif event.key == pygame.K_m:
                    right_paddle.steps = PADDLE_SPEED  # left paddle down

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_z:
                    left_paddle.steps = 0
                if event.key == pygame.K_k or event.key == pygame.K_m:
                    right_paddle.steps = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.reset()

        screen.blit(background, (0, 0))

        # Check paddle collision
        if pygame.sprite.groupcollide(ball_sprite, paddle_sprites, False, False):
            ball.bounce_x()

        # Check if any side scores
        ball_left = ball.rect.x - ball.radius
        ball_right = ball.rect.x + ball.radius
        if ball_left > screen.get_width():
            left_score.score += 1
            ball.reset()
        if ball_right < 0:
            right_score.score += 1
            ball.reset()

        ball_sprite.update()
        paddle_sprites.update()
        score_sprites.update()

        ball_sprite.draw(screen)
        paddle_sprites.draw(screen)
        score_sprites.draw(screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
