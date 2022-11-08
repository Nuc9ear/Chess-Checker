# Chess-Checker
This code allows you to understand how to move a piece in chess. 
Given a set of different chess boards. A program that determines whether cells can be detected on the second turn. The program receives four numbers from 1 to 8 each day, specifying the column number and row number, first for the first cell, then for the second cell. The program should lead to "YES" if the bishop's move from the first cell can get to the second one or "NO" if it occurs.

Bishop.
Input data format:
The input to the program is four numbers from 1 to 8.

Output:
The program should display the text in accordance with the condition of the problem.

Note. The chess bishop moves diagonally.

From code:
elif a == 'bishop' and abs(x1-x2) == abs(y1-y2):
    print('YES')
