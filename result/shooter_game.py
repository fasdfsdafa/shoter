from pygame import *
from random import randint
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("осёл")
clock = time.Clock()
score = 0
lost = 0
img_back = "galaxy.jpg"
background = transform.scale(image.load('ufo.png'), (win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        player_speed = 10
    def fire(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(60, win_width - 80)
            self.rect.y = 0
            lost = lost + 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('Ура победа', True, (255, 255, 255))
lose = font1.render('Лащок', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)


player = Player('rocket.png', 300, 400, 70)


monsters = sprite.Group()
for i in range (1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), 50, randint(1, 5))
    monsters.add(monster)


bullets = sprite.Group()
bullet = Bullet('bullet.png', 300, 400, 70)
bullets.add(bullet)


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')


finish = False
donkey = True


while donkey:
    window.blit(background, (0,0))
    for p in event.get():
        if p.type == QUIT:
            donkey = False


    

    if not finish:
        text = font2.render("Счёт: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))


        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        player.update()
        monsters.update()
        # bullet.update()

        player.reset()
        monsters.draw(window)
   

        display.update()
        clock.tick(40)
        time.delay(50)