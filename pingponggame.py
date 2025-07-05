from pygame import *

winheight = 500
winwidth = 600

win = display.set_mode((winwidth, winheight))
win.fill((0, 100, 100))

class Gamesprite(sprite.Sprite):
    def __init__(self, w, h, picture, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class player(Gamesprite):
    def updateleft(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed


    def updateright(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

game = True
finished = False
font.init()
font = font.Font(None, 100)
Lwon = font.render("Left Won!", True, (255, 0, 0))
Rwon = font.render("Right Won!", True, (0, 255, 0))



ball = Gamesprite(100, 100, "ball.png", 250, 150, 5)
speedX = 5
speedY = 5

Lracket = player(50, 150, "Racket.png", 20, 150, 5)
Rracket = player(50, 150, "Racket.png", 480, 150, 5)

clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finished == False:
        win.fill((0,100,100))
        Lracket.updateleft()
        Rracket.updateright()
        ball.rect.x += speedX
        ball.rect.y += speedY

        if sprite.collide_rect(ball, Rracket) or sprite.collide_rect(ball, Lracket):
            speedX *= -1
        if ball.rect.y < 0 or ball.rect.y > winheight:
            speedY *= -1
        if ball.rect.x < 0:
            finished = True
            win.blit(Rwon, (50, 20))
        if ball.rect.x > 500:
            finished = True
            win.blit(Lwon, (50,20))
        ball.reset()
        Lracket.reset()
        Rracket.reset()

    display.update()
    clock.tick(60)          
            




