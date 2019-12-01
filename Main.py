### FLAPPY BIRD ###

# import Libraries
import pygame, random, time, collections

# window and variable init
pygame.init()
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("I.ico")
pygame.display.set_icon(icon)
window_h = 600
window_w = 400
window = pygame.display.set_mode((window_w, window_h))

def Text(word, color=pygame.Color("black"), c1=200, c2=250):
	font = pygame.font.Font("freesansbold.ttf", 32)
	pygame.font.Font.set_underline(font, True)
	text = font.render(word, True, color)
	textRect = text.get_rect()
	textRect.center = (c1, c2) 
	window.blit(text, textRect)

def main():
	window.fill(pygame.Color("white"))
	wall_colors = [pygame.Color("red"), pygame.Color("yellow"), pygame.Color("green"),
	pygame.Color("blue"), pygame.Color("purple"), pygame.Color("pink"), pygame.Color("orange"), pygame.Color("black"), pygame.Color("black")]
	Point = collections.namedtuple('Point', ['x', 'y', "w", "h"])
	list_of_wall_lengths = range(25, 400)
	wall_velocity = 0.25
	num = 0

	# class to make a moveable sprite
	class Player:
		def __init__(self, w, h, x, y, color):
			# defining args as self variables
			self.w = w
			self.h = h
			self.x = x
			self.y = y
			self.c = color
			self.draw() # initiate draw

		def draw(self):
			pygame.draw.rect(window, self.c, (self.x, round(self.y), self.w, self.h)) # draw the square of the sprite

		def plot(self, y): # takes the new y
			window.fill(pygame.Color("white"), (self.x, round(self.y), self.w, self.h)) # fills in the old space of the sprite
			self.y = y # reset the old x to the new x
			if self.y <= 0:
				self.y = 0
				self.y += 1
			self.draw() # redo the draw with a new (and higher) y 

	def touching(obj1, obj2, Amode=False):
		if not Amode:
			if obj1.x + obj1.w > obj2.x and obj1.x + obj1.w < obj2.x + obj2.w or obj1.x > obj2.x and obj1.x < obj2.x + obj2.w:
				if obj1.y < obj2.y + obj2.h:
					return True
		if Amode:
			if obj1.x + obj1.w > obj2.x and obj1.x + obj1.w < obj2.x + obj2.w or obj1.x > obj2.x and obj1.x < obj2.x + obj2.w:
				if obj1.y > obj2.y + obj2.h or obj1.y + obj1.h  > obj2.y:
					return True



	class Wall:
		def __init__(self, w, h):
			self.w = w
			self.h = h
			self.x = 400-w
			self.y = 1
			self.c = random.choice(wall_colors)
			self.draw()

		def draw(self):
			pygame.draw.rect(window, self.c, (round(self.x), round(self.y), self.w, self.h))

		def update(self, v):
			window.fill(pygame.Color("white"), (round(self.x), round(self.y), self.w, self.h))
			self.x -= v
			if self.x + self.w < 0:
				return True
			self.draw()

	class Wall2:
		def __init__(self, wall1):
			self.w = wall1.w
			self.h = 600-wall1.h-200
			self.x = wall1.x
			self.y = wall1.y+200+wall1.h
			self.c = wall1.c
			self.draw()

		def draw(self):
			pygame.draw.rect(window, self.c, (round(self.x), round(self.y), self.w, self.h))


		def update(self, v):
			window.fill(pygame.Color("white"), (round(self.x), round(self.y), self.w, self.h))
			self.x -= v
			if self.x + self.w < 0:
				return True
			self.draw()



	# creating sprite object
	Sprite = Player(35, 35, 60, 20, pygame.Color("black"))

	wall_list = []
	def Walls(remove=False):
		if remove:
			for i in range(len(wall_list)):
				wall_list.remove(wall_list[0])
		wall = Wall(40, random.choice(list_of_wall_lengths))
		wall2 = Wall2(wall)
		wall_list.append(wall)
		wall_list.append(wall2)
	Walls()

	fall = True # if fall is true it will continue to fall at a rate of 1 pixel per cycle
	fallc = 0 # fallc (fall count)
	while True:
		num += 0.002
		### This segment allows the sprite to hesitate when it "jumps" up ###
		if fall: # if fall is true plot x with y+1
			Sprite.plot(Sprite.y+0.5)

		if fall == False: # if fall is false fallc will increase by 0.5
			fallc +=0.013

		if fallc >= 1.0: # when fallc has reached 1 it will reset both fall and fallc
			fallc = 0
			fall = True
		pygame.display.update() # updates the display
		for i in range(len(wall_list)):
			if wall_list[i].update(0.3+((num/15)* 0.03)):
					Walls(True)
			if i == 0 and touching(Point(Sprite.x, Sprite.y, Sprite.w, Sprite.h), Point(wall_list[i].x, wall_list[i].y, wall_list[i].w, wall_list[i].h)) or Sprite.y>600-Sprite.h:
				time.sleep(0.75)
				Main_Menu()
			elif i == 1 and touching(Point(Sprite.x, Sprite.y, Sprite.w, Sprite.h), Point(wall_list[i].x, wall_list[i].y, wall_list[i].w, wall_list[i].h), Amode=True) or Sprite.y>600-Sprite.h:
				time.sleep(0.75)
				Main_Menu()
		for event in pygame.event.get(): # get events
			if event.type == pygame.QUIT: # if the event is the close window button
				quit()
			elif event.type == pygame.KEYDOWN: # if a key is pressed
				if event.key == pygame.K_SPACE or event.key == pygame.K_UP: #if that key is down arrow
					for i in range(1, 10):
						Sprite.plot(Sprite.y-11)
					fall = False # start the delay cycle

def Main_Menu():
	window.fill(pygame.Color("white"))
	Text("Press Space To Play")
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					main()

if __name__ == "__main__":
	Main_Menu()
