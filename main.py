import time
import pygame
import sys

from screeninfo import get_monitors

from lib.Color import Color
from system.SimulationEngine import SimulationEngine

pygame.init()

for m in get_monitors():
    if m.is_primary:
        monitor = m

w_width = monitor.width
w_height = monitor.height
w_title = "Conway's Game of Life"
w_flags = pygame.FULLSCREEN

DISPLAY = pygame.display.set_mode((w_width, w_height), w_flags)
pygame.display.set_caption(w_title)

fps = 30

simulator = SimulationEngine(DISPLAY)

if __name__ == "__main__":
    while True:
        if simulator.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        simulator.running = False
                    if event.key == pygame.K_PLUS:
                        fps += 10
                    if event.key == pygame.K_MINUS:
                        fps -= 10
                    if event.key == pygame.K_BACKSPACE:
                        simulator.reset()

            DISPLAY.fill(Color().BLACK)

            simulator.next_gen()

            print(f"Generation: {simulator.gen}")
            print(f"Number of alive cells: {simulator.alive_cells}")
            
            pygame.display.update()
            pygame.display.flip()
            time.sleep(1/fps)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        simulator.running = True
                    # if event.key == pygame.K_LEFT:
                    #     simulator.previous_gen()
                    if event.key == pygame.K_RIGHT:
                        simulator.next_gen()
                    if event.key == pygame.K_BACKSPACE:
                        simulator.reset()

            DISPLAY.fill(Color().BLACK)

            simulator.grid.update()

            print(f"Generation: {simulator.gen}")
            print(f"Number of alive cells: {simulator.alive_cells}")
            
            pygame.display.update()
            pygame.display.flip()
            time.sleep(1/30)