#!/usr/bin/env python3

import sys
import os
import argparse

class Sudoku():
    setboard = False
    board = []

    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.board = []
        for i in range(9):
            self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.setboard = False
    
    def load_file(self, filename):
        with open(filename) as fin:
            row = 0
            for line in fin:
                if line.startswith('#'):
                    continue
                num = line.split()
                if len(num) != 9:
                    print("ERROR: parse line row:{} contents:{}".format(row, line))
                    return False
                if row >= 9:
                    print("ERROR: parse line over 9 line:{}".format(line))
                    return False
                for i in range(9):
                    n = 0
                    if num[i] >= '1' and num[i] <= '9':
                        n = int(num[i])
                    self.board[row][i] = n
                row += 1
        if row != 9:
            print("ERROR: parse error line counts:{}".format(row))
            return False
        self.setboard = True
        return True

    def print(self):
        if not self.setboard:
            print("ERROR: board is not correctly set")
            return False
        print("+---------+---------+---------+")
        for row in range(9):
            sys.stdout.write('|')
            for col in range(9):
                n = self.board[row][col]
                if n >= 1 and n <= 9:
                    sys.stdout.write(" {} ".format(n))
                else:
                    sys.stdout.write(' . ')
                if col % 3 == 2:
                    sys.stdout.write('|')
            sys.stdout.write('\n')
            if row % 3 == 2:
                print("+---------+---------+---------+")
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sudoku Solver')
    parser.add_argument('board', help='filename of the board to be solved')
    args = parser.parse_args()
    
    board = Sudoku()
    board.load_file(args.board)
    board.print()
