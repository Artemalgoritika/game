# Создай собственный Шутер!
from pygame import *
from random import *

#! класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #todo конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       #? каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       #? каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
   #? движение врага
   def update(self):
       self.rect.y -= self.speed
       if self.rect.y < 0:
           self.kill()


#! класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
   def fire(self):
       #? Создай пулю и помести её в группу
       bullet = Bullet('Bimba.png', self.rect.x, self.rect.y, 3)
       #todo Добавление пули в группу
       bullets.add(bullet)
    

class Ufo(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = 100
# Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))
#? Персонажи игры - создание:
player = Player('rocket.png', 5, win_height - 80, 4)

game = True
finish = False
clock = time.Clock()
FPS = 60
#todo Создание групп
meteors = sprite.Group()
monsters = sprite.Group()
bullets = sprite.Group()
players = sprite.Group()
for i in range(10):
    monster = Ufo('ufo.png', randint(20, win_width), 20, randint(1, 3))
    monsters.add(monster)
for i in range(4):
    asteroid = GameSprite('asteroid.png', randint(20, win_width), randint(20,300), randint(1, 5))
    meteors.add(asteroid)
players.add(player)
font.init()
font2 = font.Font(None, 72)
text = font2.render('', 1, (255, 255, 255))
while game:
    for e in event.get(): 
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
            elif e.key == K_UP:
                player.fire()
            elif e.key == K_w:
                player.fire()

  
    if finish != True:
        window.blit(background,(0, 0))
        players.update()
        players.draw(window)
        monsters.draw(window)
        monsters.update()
        meteors.draw(window)
        bullets.draw(window)
        bullets.update()
    collides = sprite.groupcollide(monsters, bullets, True, False)
    for c in collides:
        monster = Ufo('ufo.png', randint(80, 600), randint(-20, 20), randint(1, 3))
        monsters.add(monster)
    collides = sprite.groupcollide(monsters, players, True, False)
    for c in collides:
        text = font2.render('Вы сдохли :(', 1, (255, 255, 255))
        players.remove(player)
    window.blit(text,(150,200))
    display.update()
    clock.tick(FPS)



#TODO ПРОВЕРКИ


#! КРАСНЫЙ (Классы)
#TODO ОРАНЖЕВЫЙ (Группы)
# ЗЕЛЕНЫЙ (Начало)
#? СИНИЙ (Персонажи)
# * ЗЕЛЕНЕНЬКИЙ