from enum import Enum

class Gap_Buffer:
    def __init__(self):
        self.gap_size = 3
        self.buffer = [type_of_cell.GAP] * self.gap_size
        self.curr_gap_size = self.gap_size
        self.cursor = 0

    def write(self, text: str) -> None:
        for ch in text:
            self.buffer[self.cursor] = ch
            self.cursor += 1
            self.curr_gap_size -= 1


            if self.curr_gap_size <= 0:
                last_index = len(self.buffer) - 1
                self.curr_gap_size = self.gap_size
                self.buffer += [type_of_cell.GAP] * self.gap_size
                for i in range((last_index + 1) - self.cursor):
                    start = last_index - i
                    end = last_index + self.gap_size - i
                    self.buffer[start], self.buffer[end] = self.buffer[end], self.buffer[start]

    def move_cursor(self, x: int) -> None:
        if x == 0:
            return
        elif x > 0:
            missed_space = self.cursor + self.curr_gap_size + x - len(self.buffer)
            if missed_space > 0:
                return
            start = self.cursor
            end = self.cursor + self.curr_gap_size
            for _ in range(x):
                self.buffer[start] = self.buffer[end]
                self.buffer[end] = type_of_cell.GAP
                start += 1
                end += 1
            self.cursor += x
        else:
            start = self.cursor - 1
            end = self.cursor + self.curr_gap_size - 1
            for _ in range(-x):
                if self.cursor <= 0:
                    break
                self.cursor -= 1
                self.buffer[end] = self.buffer[start]
                self.buffer[start] = type_of_cell.GAP
                start -= 1
                end -= 1

    def delete(self, amount: int) -> None:
        if amount > 0:
            self.buffer = self.buffer[:max(self.cursor - amount, 0)] + self.buffer[self.cursor:]
            self.cursor -= amount
            if self.cursor < 0:
                self.cursor = 0

    def get_char(self, index: int) -> None:
        if index == len(self.buffer):
            return type_of_cell.ENDFILE
        return self.buffer[index]

    def clear(self) -> None:
        self.buffer.clear()
        self.buffer = [type_of_cell.GAP] * self.gap_size
        self.curr_gap_size = self.gap_size
        self.cursor = 0

    def load(self, data: str) -> None:
        self.clear()
        self.buffer += list(data)

    def get_text(self) -> str:
        res = ''
        for cell in self.buffer:
            if type(cell) == str:
                res += cell
        return res

class type_of_cell(Enum):
    GAP = 0.01
    ENDFILE = 1
