import pygame
import random


#Вводим глобалы
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HEIGHT = 600
WIDTH = 800
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip()
CLOCK = pygame.time.Clock()
FPS = 60



class Racket(pygame.sprite.Sprite):# создание платформ(ракеток)
    def __init__(self, centery, centerx, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 60))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx# центр поля по х
        self.rect.centery = centery# центр поля по у
        self.speedy = 0
        self.player = player

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        #Движение платформ
        if self.player == 2:# правая платформа
            if keystate[pygame.K_UP]:
                self.speedy -= 5
            elif keystate[pygame.K_DOWN]:
                self.speedy += 5
            self.rect.y += self.speedy
        elif self.player == 1:# левая платформа или бот
            if ball.speedx < 0:
                if ball.rect.centery == self.rect.centery:
                    self.speedy = 0
                elif ball.rect.centery > self.rect.centery:
                    self.speedy += 5
                elif ball.rect.centery < self.rect.centery:
                    self.speedy -= 5

        #Прокомментируйте выше (где первый игрок) и используйте это вместо, если вы хотите играть против другого игрока.
            #if keystate[pygame.K_w]:
            #    self.speedy -= 5
            #if keystate[pygame.K_s]:
            #    self.speedy += 5
            self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Ball(pygame.sprite.Sprite):# создание мячика
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.ballspeed = 2
        self.speedx = random.choice([2, -2])
        self.speedy = 2


    def update(self):
        self.speedy = self.speedy
        self.speedx = self.speedx
        if self.rect.top < 0: #чтобы мячик не вылетал с поля
            self.speedy = -self.speedy
        elif self.rect.bottom > HEIGHT:
            self.speedy = -self.speedy
        if pygame.sprite.collide_rect(self, racket):# столкновение с платформой, увеличение скорости
            self.speedx = -(self.speedx)
            self.speedx += .5
        elif pygame.sprite.collide_rect(self, racket2):
            self.speedx = -(self.speedx)
            self.speedx -= .5
        self.rect.y += self.speedy# движение мяча
        self.rect.x += self.speedx
        if self.rect.right > WIDTH or self.rect.left < 0:# если платформа не отбила мячик
            print('game_over')
            self.rect.centerx = WIDTH/2# возвращение мяча в центр
            self.rect.centery = HEIGHT/2
            self.speedx = random.choice([2, -2])

if __name__ == '__main__':
    #Создаем группу спрайтов и добавляем наши ракетки и мяч
    all_sprites = pygame.sprite.Group()
    racket = Racket(HEIGHT/2, 10, 1)
    racket2 = Racket(HEIGHT/2, WIDTH - 10, 2)
    ball = Ball()
    all_sprites.add(racket)
    all_sprites.add(racket2)
    all_sprites.add(ball)

    #Игровой цикл
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        #обновление спрайтов
        all_sprites.update()
        #выводим все на поле
        DISPLAY.fill(WHITE)
        all_sprites.draw(DISPLAY)
        pygame.display.flip()
        CLOCK.tick(FPS)
    pygame.quit()
    quit()
