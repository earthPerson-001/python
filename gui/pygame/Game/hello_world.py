import pygame

pygame.init()

win = pygame.display.set_mode(size=(500, 480))
pygame.display.set_caption('My first game.')

right_img = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

left_img = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'),
            pygame.image.load('l4.png'), pygame.image.load('l5.png'), pygame.image.load('l6.png'),
            pygame.image.load('l7.png'), pygame.image.load('l8.png'), pygame.image.load('l9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

score = 0

font1 = pygame.font.SysFont("comicsans", 30, True)
font2 = pygame.font.SysFont('times', 10, True)


class Projectile:
    def __init__(self, color, x, y, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = 5 * facing
        self.facing = facing
        self.color = color


class Player:
    def __init__(self, x, y, width, height, v):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.v = v
        self.jump_count = 10
        self.jumping = False
        self.moving_left = False
        self.moving_right = False
        self.walkcount = 0
        self.hitbox = (self.x + 20, self.y + 10, 30, 50)
        self.standing = True
        self.right = True
        self.left = False

    def collision(self):
        global score
        score -= 5
        self.x = 10
        self.y = 350
        i = 0
        while i < 30:
            pygame.time.delay(20)
            i += 1
            if event.type == pygame.QUIT:
                i = 30
                pygame.quit()

    def game_drawer(self):
        win.blit(bg, (0, 0))
        if self.walkcount > 7:
            self.walkcount = 0
        if self.moving_right:
            self.x += self.v
            self.walkcount += 1
            win.blit(right_img[self.walkcount], (self.x, self.y))
            recto.moving_right = False
            self.standing = True
        elif self.moving_left:
            self.x -= self.v
            self.walkcount += 1
            win.blit(left_img[self.walkcount], (self.x, self.y))
            recto.moving_left = False
            self.standing = True
        else:
            if self.standing:
                if self.right:
                    win.blit(right_img[self.walkcount], (self.x, self.y))
                elif self.left:
                    win.blit(left_img[self.walkcount], (self.x, self.y))
            self.walkcount = 0
        for bullet in bullets:
            pygame.draw.circle(win, bullet.color, (bullet.x, bullet.y), bullet.radius)

        if self.jumping:
            if self.jump_count >= -10:
                self.y -= (abs(self.jump_count) * self.jump_count) // 4
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.y = 350
                self.jumping = False
        self.hitbox = (self.x + 17, self.y + 10, 27, 50)
        # pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
        # pygame.draw.rect(win, (255, 0, 0), enemy_1.hitbox, 2)
        for bullet in bullets :
            if bullet.x > 0 and bullet.x < 500:
                bullet.x += bullet.vel
                pygame.draw.circle(win, bullet.color, (bullet.x, bullet.y), bullet.radius)
            else:
                bullets.pop(bullets.index(bullet))

        if recto.hitbox[1] + recto.hitbox[3] >= enemy_1.hitbox[1]:
            if (recto.hitbox[0] > enemy_1.hitbox[0] and recto.hitbox[0] < (enemy_1.hitbox[0] + enemy_1.hitbox[2])) or ((recto.hitbox[0] + recto.hitbox[2]) > enemy_1.hitbox[0] and recto.hitbox[0] < enemy_1.hitbox[0] + enemy_1.hitbox[3]):
                print('hit')
                self.collision()

        score1 = font1.render('score :' + str(score), 1, (255, 0, 0))
        win.blit(score1, (20, 20))

        pygame.display.update()


class Enemy:
    left_img = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    right_img = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]

    def __init__(self, x, y, width, height, v, start, end):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.v = v
        self.moving_left = False
        self.moving_right = False
        self.walkcount = 0
        self.start = start
        self.end = end
        self.hitbox = (self.x + 5, self.y + 10, 30, 50)

    def mov_enemy(self):
        if self.walkcount > 9:
            self.walkcount = 0
        if self.x - self.v < self.start:
            self.v = abs(self.v)
            self.moving_right = True
            self.moving_left = False
        elif self.x + self.v > self.end:
            self.v = -self.v
            self.moving_right = False
            self.moving_left = True
        self.x += self.v
        if self.moving_right:
            self.walkcount += 0.2
            win.blit(self.right_img[int(self.walkcount)], (self.x, self.y))
        elif self.moving_left:
            self.walkcount += 0.2
            win.blit(self.left_img[int(self.walkcount)], (self.x, self.y))
        self.hitbox = (self.x + 25, self.y + 10, 27, 50)
        pygame.display.update()


recto = Player(10, 350, 40, 40, 5)
enemy_1 = Enemy(420, 355, 40, 40, 4, 200, 440)
bullets = []

game_running = True

while game_running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    for bullet in bullets:
        if bullet.x > 0 and bullet.x < 500:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE]:
        if recto.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile((0, 0, 0), round(recto.x + recto.width//2), round(recto.y + recto.width//2), 5, facing))
            pygame.time.delay(200)

    if pressed_keys[pygame.K_UP]:
        recto.jumping = True

    if pressed_keys[pygame.K_LEFT] and recto.x > recto.v - 1:
        recto.moving_left = True
        recto.left = True
        recto.standing = False
        recto.right = False

    if pressed_keys[pygame.K_RIGHT] and recto.x < 396:
        recto.moving_right = True
        recto.right = True
        recto.left = False
        recto.standing = False
    recto.game_drawer()
    enemy_1.mov_enemy()

pygame.quit()
