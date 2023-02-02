#!/usr/bin/env python3
from z3 import (Solver, Int, Distinct)

def sudoku_solver(puzzle:str):
    s=Solver()
    # using Python list comprehension , construct array of arrays of Int instances:
    cells=[[Int('cell%d%d' % (r, c)) for c in range(9)] for r in range(9)]
    for r in range(9):
        for c in range(9):
            # process text line:
            if puzzle[r*9+c] != '.':
                s.add(cells[r][c]==int(puzzle[r*9+c]))
            # 0< =cell value <=9
            s.add(cells[r][c]>=1, cells[r][c]<=9)
    # for all 9 rows
    s.add(*[Distinct(*r) for r in cells])
    # for all 9 columns
    s.add(*[Distinct(*c) for c in zip(*cells)])
    # enumerate all 9 squares
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
        # add constraints for each 3*3 square:
            s.add(Distinct(*[cells[r+rr][c+cc] for rr in range(3) for cc in range(3)]))

    if s.check().__repr__() == "sat":
        m=s.model()
        for r in range(9):
            print([m[cells[r][c]] for c in range(9)])
    else:
        print(s.check())

# http://www.norvig.com/sudoku.html
# http://www.mirror.co.uk/news/weird-news/worlds-hardest-sudoku-can-you-242294
puzzle0="..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."
puzzle1=".....6....59.....82....8....45........3........6..3.54...325..6.................."
puzzle2=".....5.8....6.1.43..........1.5........1.6...3.......553.....61........4........."
sudoku_solver(puzzle0)
sudoku_solver(puzzle1)
sudoku_solver(puzzle2)
