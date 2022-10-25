# Our coordinates are here:
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# You can choose your figure here:
a = input('Choose your chess figure now (pawn/king/queen/rook/bishop/knight): ')
# Code for queen
if a == 'queen' and (abs(x1-x2)) == (abs(y1-y2)):
    print('YES')
elif a == 'queen' and (abs(x1-x2) == 0) or abs((y1-y2) == 0):
    print('YES')
# Code for king
elif a == 'king'and abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
    print('YES')
# Code for pawn
elif a == 'pawn' and y2-y1 == 1 or y2-y1 == 2 and x1 == x2:
    print('YES')
# Code for rook
elif a == 'rook' and x1 == x2 or y1 == y2:
    print('YES')
# Code for bishop
elif a == 'bishop' and abs(x1-x2) == abs(y1-y2):
    print('YES')
# Code for knight
elif a == 'knight' and abs(x1-x2) == 1 and abs(y1-y2) == 2:
    print('YES')
elif a == 'knight' and abs(x1-x2) == 2 and abs(y1-y2) == 1:
    print('YES')
else:
    print('NO')