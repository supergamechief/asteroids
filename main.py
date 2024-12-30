# this allows us to use code from the open-source pygame library throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));

def main():
	pygame.init()
	print("Starting asteroids!");
	print("Screen width: 1280");
	print("Screen height: 720");
	
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)

	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		
		for i in updatable:
			i.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()
		
			for shot in shots:
				if asteroid.collides_with(shot):
					shot.kill()
					asteroid.kill()
		
		player.update(dt)
		
		screen.fill("black")
		
		for i in drawable:
			i.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
