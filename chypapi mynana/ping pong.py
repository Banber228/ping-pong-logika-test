from pygame import*
back=(255,200,100)
width=700
height=500
class GameSptite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,widht,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
     def update_l(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
window=display.set_mode((width,height))
window.fill(back)
win_height=500
win_width=700

mw=display.set_mode((width,height))
mw.fill(back)





cloak=time.Clock()
ball = GameSprite('tenis-ball.png', 200, 200, 4, 50, 50)
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)

game_over=False

speed_x=3
speed_y=3

while not game_over:
    for e in event.get():
        if e.type==QUIT:
            game_over=True
            
    if game_over!=True:
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
    
    if ball.rect.y>width-50 or ball.rect.y<0:
        speed_y*-=1
    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racker2,ball):
        speed_y*-=1
    
    racket1.reset()
    racket2.reset()
    
    racket1.update_r()
    racket2.update_l()
    
    ball.reset()
    display.update()
    cloak.tick(40)        
