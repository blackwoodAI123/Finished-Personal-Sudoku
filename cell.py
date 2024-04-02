import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def get_value(self):
        return self.value

    #Sets Array value in backend
    def set_cell_value(self, value):
        self.value = value

    #Sets Array value in frontend
    def set_sketched_value(self, value):
        self.value = value

    def draw(self, selected):
        #DRAWS THE CELL AND THE VALUE

        if selected is True:
            color = (255, 0, 0)
        else:
            color = (0, 0, 0)

        pygame.draw.line(self.screen, color,
                         (self.row + 80, self.col + 80),
                         (self.row + 160,  self.col + 80), 4)

        pygame.draw.line(self.screen, color,
                         (self.row + 160, self.col + 80),
                         (self.row + 160, self.col + 160), 4)

        pygame.draw.line(self.screen, color,
                         (self.row + 160, self.col + 160),
                         (self.row + 80, self.col + 160), 4)

        pygame.draw.line(self.screen, color,
                         (self.row + 80, self.col + 160),
                         (self.row + 80, self.col + 80), 4)

        font = pygame.font.SysFont("Times New Roman", 50, True, False)

        if self.value != 0:
            string_value_copy = str(self.value)
            value = font.render(string_value_copy, False, (0, 0, 0))
            self.screen.blit(value, (self.row + 107, self.col + 90))

