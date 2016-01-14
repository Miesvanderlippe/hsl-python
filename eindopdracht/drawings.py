__author__ = 'Mies'

mannetje = [
    ['          ','          ','          ',
     '          ','          ','         '],
    ['          ','  |       ','  |       ',
     '  |       ','  |       ',' / \     '],
    ['   ____   ','  |/      ','  |       ',
     '  |       ','  |       ',' / \     '],
    ['   ____   ','  |/   |  ','  |       ',
     '  |       ','  |       ',' / \     '],
    ['   ____   ','  |/   |  ','  |    O  ',
     '  |       ','  |       ',' / \     '],
    ['   ____   ','  |/   |  ','  |    O  ',
     '  |    |  ','  |       ',' / \     '],
    ['   ____   ','  |/   |  ','  |   \O  ',
     '  |    |  ','  |       ',' / \     '],
    ['   ____   ','  |/   |  ','  |   \O/ ',
     '  |    |  ','  |       ',' / \     '],
    ['   ____   ','  |/   |  ','  |   \O/ ',
     '  |    |  ','  |   /   ',' / \     '],
    ['   ____   ','  |/   |  ','  |   \O/ ',
     '  |    |  ','  |   / \ ',' / \     ']
]

class Drawing:

    end_x    = 0
    end_y    = 0
    x        = 0
    y        = 0
    drawing  = []

    def __init__(self, x:int, y:int, drawing:list):
        self.end_x = x + longest_in_list(drawing)
        self.end_y = y + len(drawing)
        self.x = x
        self.y = y
        self.drawing = drawing

        self.convert_to_all_strings()
        self.fill_drawing_to_longest()

    def fill_drawing_to_longest(self):
        for key, line in enumerate(self.drawing):
            spaces_to_add = ' ' * (self.end_x - len(line))
            self.drawing[key] = line + spaces_to_add

    def convert_to_all_strings(self):
        self.drawing = [str(x) for x in self.drawing]

    def get_line(self, index: int):
        return self.drawing[index-1]


class MultiItemDrawing:

    objects_to_draw = []
    max_x = 180
    max_y = 80

    # constructor
    # def __init__(self):

    def add_drawing(self, to_draw: list, x: int, y: int):

        d = Drawing(x, y, to_draw)

        if x < 0 or y < 0 or d.end_x > self.max_x or d.end_y > self.max_y:
            return False, 'Drawing out of bounds'

        self.objects_to_draw.append(d)

    def get_art_width_height(self):
        drawing_width = 0
        lines_in_drawing = 0

        for drawing in self.objects_to_draw:
            # Sorta useless for now
            if drawing.end_x > drawing_width:
                drawing_width = drawing.end_x

            if drawing.end_y > lines_in_drawing:
                lines_in_drawing = drawing.end_y

        return drawing_width, lines_in_drawing

    def line_drawing_line(self):
        start_drawing_line = {}
        for ind, drawing in enumerate(self.objects_to_draw):
            for line in range(1 , drawing.end_y - drawing.y + 1):

                if line + drawing.y in start_drawing_line:
                    start_drawing_line[line + drawing.y][drawing.x] = drawing.get_line(line)
                else:
                    start_drawing_line[line + drawing.y] = {drawing.x:drawing.get_line(line)}

                # start_drawing_line[line+drawing.y][drawing.x] = drawing.get_line(line)

        return start_drawing_line

    def get_drawable_string(self):
        drawing_width, lines_in_drawing = self.get_art_width_height()
        line_drawing_line = self.line_drawing_line()
        drawable = []

        for terminal_line in range(1, lines_in_drawing):
            curr_line = ''

            if terminal_line in line_drawing_line:
                for key in sorted(line_drawing_line[terminal_line]):
                    print(key, len(curr_line))
                    curr_line += ' ' * (key-len(curr_line))
                    curr_line += line_drawing_line[terminal_line][key]
            else:
                curr_line = ''

            drawable.append(curr_line)

        return '\r\n'.join(drawable)


def longest_in_list(list_to_count:list):
    longest_row = 0

    for row in list_to_count:
        row_length = len(row)

        if row_length > longest_row:
            longest_row = row_length

    return longest_row


def main():
    drawing = MultiItemDrawing()

    d2 = ['Geraden letters', 'x x x x x x x x x', 'xxx x  x x x x A']
    d3 = ['Het te raden woord', '___Y___']

    drawing.add_drawing(mannetje[9], 3, 3)
    drawing.add_drawing(d2, 120, 10)
    drawing.add_drawing(d2, 180, 4)
    drawing.add_drawing(d2, 60, 4)

    print(drawing.get_drawable_string())

if __name__ == '__main__':
    main()