import sys
import pygame as pg


def checkEvents(ship):

  for event in pg.event.get():
    if event.type == pg.QUIT:
          sys.exit()
    elif event.type == pg.KEYDOWN:
      if event.key == pg.K_RIGHT:
        ship.moving_right = True
      elif event.key == pg.K_LEFT:
        ship.moving_left = True
    elif event.type == pg.KEYUP:
      if event.key == pg.K_RIGHT:
        ship.moving_right = False
      elif event.key == pg.K_LEFT:
        ship.moving_left = False


def updateScreen(settings, screen, ship):
  screen.fill(settings.bg_color)
  ship.blitme()

  pg.display.flip()