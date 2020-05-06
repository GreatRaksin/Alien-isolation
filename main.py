import pygame as pg
from settings import Settings
from ship import Ship
import gameFunctions as gf


def startGame():
    setting = Settings()
    pg.init()
    screen = pg.display.set_mode((setting.screen_width, setting.screeen_height))
    pg.display.set_caption('Alien: Isolation')

    ship = Ship(screen)

    while True:
        gf.checkEvents(ship) # цикл обработки событий
        ship.update()

        gf.updateScreen(setting, screen, ship) # функция отрисовки/обновления экрана

startGame()