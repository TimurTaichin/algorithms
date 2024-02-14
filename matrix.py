"""
На вход программе подаются два натуральных числа n и m. 
Напишите программу, которая создает матрицу размером n х m, 
заполнив ее 1-ми внутри и снаружи 0-ми до n x m. 
Матрица получится следующего вида.

0 0 0 0 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
или
0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0

for row in range(5):
    
    for col in range(5):
      if row == col == 2:
        print('x', end='  ')
      else:
        print(0, end='  ')

    print()
"""

def check(row, col):
    if row < col:
        return row == 0 and col == 4
    elif row > col:
        return row == 4 and col == 0
    elif row == col:
        return row == 0 or row == 2 or row == 4
    

for row in range(5):
    for col in range(5):

        if check(row, col):
            print("x", end="  ")
        else:
            print(0, end="  ")
    print()
        
'''
x  0  0  0  x 
0  0  0  0  0  
0  0  x  0  0
0  0  0  0  0
x  0  0  0  x
'''































