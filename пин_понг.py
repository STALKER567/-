from pygame import *

window = display.set_mode((600, 600))
back = (155, 23, 125)



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -50:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 520:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -50:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 520:
            self.rect.y += self.speed

clock = time.Clock()


game = True
finish = False

speed_x = 3
speed_y = 3

rocket1 = Player('меч.png', 20, 250, 5, 90, 200)
rocket2 = Player('меч.png', 450, 250, 5, 90, 200)
ball = Player('Red-Shining-Apple-PNG-transformed.png', 250, 250, 5, 50, 50)

font.init()
font = font.Font(None, 50)
lose = font.render('1 игрок проиграл!', True, (150, 0, 0))
lose2 = font.render('2 игрок проиграл!', True, (150, 0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rocket1.reset()
        rocket2.reset()
        ball.reset()
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


    if sprite .collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
        speed_x *= -1
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        game = True
    if ball.rect.x > 450:
        finish = True
        window.blit(lose2, (200, 200))
        game = True


    

    display.update()
    clock.tick(60)


