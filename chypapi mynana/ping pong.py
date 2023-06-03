from pygame import*

back=(255,200,100)
width=700
height=500


mw=display.set_mode((width,height))
mw.fill(back)

cloak=time.Clock()

game_over=False

while not game_over:
    for e in event.get():
        if e.type==QUIT:
            game_over=True

    display.update()
    cloak.tick(40)        