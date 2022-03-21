import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.messagebox import showinfo
from gapbuffer import Gap_Buffer, type_of_cell
from typing import List, Optional
import pygame
import os

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

class MainTerminal():
    def __init__(self, text: str, pos: List[int], width: Optional[int] = None, height: Optional[int] = None):
        self.pos = pos
        self.width = width
        self.height = height
        self.font = pygame.font.Font(os.path.join(WORKING_DIR, 'C:\PYTHON\gapbuffer\Mefikademo-owEAq.ttf'), 40)
        self.option_text = self.font.render(text, True, (255, 255, 0))

        if width is None:
            self.width = self.option_text.get_rect().width
        if height is None:
            self.height = self.option_text.get_rect().height
        self.rect = pygame.Rect(pos[0], pos[1], self.width, self.height)

        self.is_clicked = False
        self.clicked = False

        self.hovering = False

    def eventcatch(self, events: List[pygame.event.Event]) -> None:
        mouse = pygame.mouse.get_pos()
        self.hovering = self.rect.collidepoint(mouse[0], mouse[1])
        self.clicked = False
        self.is_clicked = False
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if self.hovering:
                    self.clicked = True
        if self.hovering and pygame.mouse.get_pressed()[0]:
            self.is_clicked = True

    def click(self) -> bool:
        return self.clicked

    def draw(self, window) -> None:
        if self.is_clicked:
            pygame.draw.rect(window, (255, 0, 0), self.rect)
        else:
            pygame.draw.rect(window, (50,150 if self.hovering else 0, 120), self.rect)
        window.blit(self.option_text, self.option_text.get_rect(center=(self.pos[0] + self.width//2, self.pos[1] + self.height//2)))


class Terminal:
    def __init__(self):
        self.menu_height = 500
        self.width = 1000
        self.height = 100 + self.menu_height
        self.cell_size = 50
        self.cells_width = self.width // self.cell_size
        self.cells_height = (self.height - self.menu_height) // self.cell_size
        self.buffer = Gap_Buffer()
        self.debug_mode = False
        self.starting()

    def starting(self) -> None:
        pygame.init()
        window = pygame.display.set_mode((self.width, self.height))
        font = pygame.font.Font(os.path.join(WORKING_DIR, "C:\PYTHON\gapbuffer\TimesRoman.ttf"), 50)
        exit_button = MainTerminal('EXIT', (0, 0), self.width/4, self.cell_size)
        load_button = MainTerminal('OPEN', (self.width * (1/4), 0), self.width/4, self.cell_size)
        save_button = MainTerminal('SAVE', (self.width * (2/4), 0), self.width/4, self.cell_size)
        debug_mode_button = MainTerminal('DEBUG', (self.width * (3/4), 0), self.width/4, self.cell_size)
        tk = tkinter.Tk()
        tk.withdraw()
        clock = pygame.time.Clock()
        run = True
        while run:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    run = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RIGHT:
                        self.buffer.move_cursor(1)
                    elif e.key == pygame.K_LEFT:
                        self.buffer.move_cursor(-1)
                    elif e.key == pygame.K_BACKSPACE:
                        self.buffer.delete(1)
                    else:
                        self.buffer.write(e.unicode)

            exit_button.eventcatch(events)
            load_button.eventcatch(events)
            save_button.eventcatch(events)
            debug_mode_button.eventcatch(events)

            if exit_button.click():
                run = False
            if load_button.click():
                self.load_file()
            if save_button.click():
                self.save_file()
            if debug_mode_button.click():
                self.debug_mode = not self.debug_mode

            window.fill((0, 0, 0))
            stop_draw = False
            buffer_index = -1

            for y in range(0, self.cells_height):
                for x in range(0, self.cells_width):
                    pos = [x * self.cell_size, (y + 1) * self.cell_size]
                    new_line = False
                    try:
                        while True:
                            buffer_index += 1
                            char = self.buffer.get_char(buffer_index)

                            if self.buffer.cursor == buffer_index:
                                pygame.draw.line(
                                    window, (255, 255, 250),
                                    (pos[0] + 1, pos[1] + 1),
                                    (pos[0] + 1, pos[1] + self.cell_size - 1)
                                )

                            if self.debug_mode and char == type_of_cell.GAP:
                                char = ''
                                break
                            if type(char) == str:
                                if ord(char) in [10, 13]:  
                                    new_line = True
                                break
                    except IndexError:
                        stop_draw = True
                        break

                    if new_line:
                        break

                    surface = font.render(char, True, (255, 255, 255))
                    surface = pygame.transform.scale(surface, (int(surface.get_rect().width * (9/10)), self.cell_size))
                    window.blit(surface, surface.get_rect(center=(pos[0] + self.cell_size//2, pos[1] + self.cell_size//2)))

                    if self.debug_mode:
                        pygame.draw.rect(window, (100, 100, 100), pygame.Rect(pos[0], pos[1], self.cell_size, self.cell_size), 1)
                        if buffer_index in range(self.buffer.cursor, self.buffer.cursor + self.buffer.curr_gap_size):
                            pygame.draw.line(
                                window, (0, 0, 255),
                                (pos[0], pos[1] + self.cell_size - 1),
                                (pos[0] + self.cell_size, pos[1] + self.cell_size - 1)
                            )
                        if buffer_index == self.buffer.cursor:
                            pygame.draw.line(
                                window, (255, 0, 0),
                                (pos[0], pos[1] + self.cell_size - 1),
                                (pos[0] + self.cell_size, pos[1] + self.cell_size - 1)
                            )
                if stop_draw:
                    break

            exit_button.draw(window)
            load_button.draw(window)
            save_button.draw(window)
            debug_mode_button.draw(window)
            pygame.display.flip()
            clock.tick_busy_loop(60)

    def load_file(self) -> bool:
        path = askopenfilename()
        if type(path) != str:
            return False
        try:
            with open(path) as file:
                try:
                    text = file.read()
                except UnicodeDecodeError:
                    showinfo('Error', f'Can\'t load {path}')
                    return
                self.buffer.load(text)
                return True
        except FileNotFoundError:
            return False
        return False

    def save_file(self) -> bool:
        file = asksaveasfile()
        if file is None:
            return False
        file.write(self.buffer.get_text())
        return True