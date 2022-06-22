from turtle import Screen, Turtle
from random import randint, choice
import numpy as np


def draw_hexagon(coord, color):
    """Draw hexagon"""
    turtle.penup()
    turtle.goto(coord)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(30)
        turtle.left(60)
    turtle.end_fill()


def get_hexagon_coordinates(size):
    coord_field = []
    for y in range(size[1]):
        coord_field.append([])
        for x in range(size[0]):
            if x % 2 == 0:
                coord_field[y].append((x * 45 - 100, 25 + y * 50 - 250))
            else:
                coord_field[y].append((x * 45 - 100, y * 50 - 250))
    return coord_field


def generate_empty_field(coord_field):
    for y_coord in coord_field:
        for x_coord in y_coord:
            draw_hexagon(x_coord, 'white')
            draw_hexagon(x_coord, 'white')


def move_is_possible(path, new_field):
    if (new_field in path) or \
            (new_field[1] < 0) or \
            (new_field[0] > field_size[0] - 1) or \
            (new_field[0] < 0):
        print(f'{new_field} not allowed')
        return False
    else:
        return True


def get_random_path(size):
    y_coord = 0
    counter = 21
    possible_moves = ['left', 'diagonally left', 'straight', 'diagonally right', 'right']

    while (size[1] - 1) > y_coord:
        if counter > 20:
            y_coord = 0
            blocked_move = []
            path = [(randint(0, size[0] - 1), y_coord)]
            counter = 0

        prev_field = path[-1]
        x_is_even = (prev_field[0] % 2 == 0)

        curr_move = choice(possible_moves)
        while curr_move in blocked_move:
            curr_move = choice(possible_moves)

        if curr_move == 'left':
            if x_is_even:
                curr_field = (prev_field[0] - 1, y_coord)
            else:
                curr_field = (prev_field[0] - 1, y_coord - 1)
            if move_is_possible(path, curr_field):
                path.append(curr_field)
                y_coord = curr_field[1]
                blocked_move = ['straight', 'right']
            else:
                counter += 1

        elif curr_move == 'diagonally left':
            if x_is_even:
                curr_field = (prev_field[0] - 1, y_coord + 1)
            else:
                curr_field = (prev_field[0] - 1, y_coord)
            if move_is_possible(path, curr_field):
                path.append(curr_field)
                y_coord = curr_field[1]
                blocked_move = ['diagonally right']
            else:
                counter += 1

        elif curr_move == 'straight':
            curr_field = (prev_field[0], y_coord + 1)
            if move_is_possible(path, curr_field):
                path.append(curr_field)
                y_coord = curr_field[1]
                blocked_move = ['left', 'right']
            else:
                counter += 1

        elif curr_move == 'diagonally right':
            if x_is_even:
                curr_field = (prev_field[0] + 1, y_coord + 1)
            else:
                curr_field = (prev_field[0] + 1, y_coord)
            if move_is_possible(path, curr_field):
                path.append(curr_field)
                y_coord = curr_field[1]
                blocked_move = ['diagonally left']
            else:
                counter += 1

        elif curr_move == 'right':
            if x_is_even:
                curr_field = (prev_field[0] + 1, y_coord)
            else:
                curr_field = (prev_field[0] + 1, y_coord - 1)
            if move_is_possible(path, curr_field):
                path.append(curr_field)
                y_coord = curr_field[1]
                blocked_move = ['straight', 'left']
            else:
                counter += 1
        else:
            print("Wrong direction")
    return path


def draw_path():
    try:
        for x_coord, y_coord in random_path:
            draw_hexagon(hex_coord[y_coord][x_coord], 'red')
    except IndexError:
        print('index error')


difficulty = 'hard'
field_size = {'hard': (5, 10),
              'medium': (4, 8),
              'easy': (3, 6)}[difficulty]

screen = Screen()
screen.setup(width=500, height=700)
screen.tracer(False)

turtle = Turtle()

hex_coord = get_hexagon_coordinates(field_size)
generate_empty_field(hex_coord)
random_path = get_random_path(field_size)
draw_path()


def start_game():
    generate_empty_field()
    x_start, y_start = random_path[0]
    draw_hexagon(x_start, y_start, 'red')
    print('start')


def move_left():
    print('move_left')

def move_diagonally_left():
    print('move_diagonally_left')

def move_straight():
    print('move_straight')

def move_diagonally_right():
    print('move_diagonally_right')

def move_right():
    print('move_right')

screen.onkey(start_game, 'space')
screen.onkey(move_left, 'a')
screen.onkey(move_diagonally_left, 'q')
screen.onkey(move_straight, 'w')
screen.onkey(move_diagonally_right, 'e')
screen.onkey(move_right, 'd')

turtle.hideturtle()
turtle.resizemode('auto')

screen.listen()
screen.exitonclick()

