import pygame


# Contains data and methods on snake itself.
class Snake:
    x, y = 0, 0
    speed = 1

    def moveright(self):
        self.x += 1

    def moveleft(self):
        self.x -= 1

    def moveup(self):
        self.y += 1

    def movedown(self):
        self.y -= 1

    def addsegment(self):
        print("TODO: add system to add an item to the list of segments. make segment positions move up each frame.")


class Grid:
    pixelscale = 1  # How many pixels big a single item on our grid is.
    xsize, ysize = 16, 16  # The dimensions of our grid
    items = None # Contains actual 2D array of items. Backend data.

    def __init__(self, pixelscale, xsize, ysize):
        self.pixelscale = pixelscale
        self.xsize = xsize
        self.ysize = ysize
        self.items = [[0 for i in range(xsize)] for j in range(ysize)]


# Contains all the game logic.
class Game:

    running = False
    grid = Grid(4, 16, 16)
    snake = Snake()

    def textrender(self):
        print("Rendering!")

    def render(self):
        screen = pygame.display.set_mode((1280, 720))

        # Set up screen
        renderedimage = pygame.Surface(screen.get_size())  # Makes a surface the size of the screen.
        renderedimage = renderedimage.convert()
        renderedimage.fill((0, 97, 255))
        for c, carray in enumerate(self.grid.items):
            for r, rval in enumerate(carray):
                if rval == 0:
                    pygame.draw.rect(renderedimage, (255, 255, 255), (c, r, 1, 1))

        # Renders screen
        screen.blit(renderedimage, (0, 0))
        pygame.display.flip()

    def start(self):
        pygame.init()
        self.running = True
        print("Starting game")

    def update(self):
        pygame.event.pump()
        self.render()
        events = pygame.event.get()

        # Handle input
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    print("Quitting game.")

                if event.key == pygame.K_a:
                    print("You have pushed the key A")


# Actual program entry point.
if __name__ == '__main__':
    snakegame = Game()
    snakegame.start()

    while snakegame.running:
        snakegame.update()