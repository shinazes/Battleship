# Battleship


import random
#label -> index
def cordinate_index(cordinate):
letter = cordinate[0]
number = cordinate[1:]
row = ord(letter)-ord('A')
collum = int(number)-1
return row, collum
#player board
def display_board(b):
output =' '
for i in range(len(b[0])):
output+=' ' + str(i+1)
print(output)
for i in range(len(b)):
output = chr(i+ord('A'))
for value in b[ i ]:
if value < 2:
output += ' '
elif value == 2:
output += ' o'
else:
output += ' x'
print(output)

#admin board
def debug_board(b):
output =' '
for i in range(len(b[0])):
output+=' ' + str(i+1)
print(output)
for i in range(len(b)):
output = chr(i+ord('A'))
for value in b[ i ]:
output += ' '+str( value )
print(output)

random position
def gen_pos(b,size):
oriantation = random.randint(0,1)

if oriantation == 0:
row = random.randint(0,len(b)-1)
col = random.randint(0,len(b[0])-size)
else:
row = random.randint(0,len(b)-size)
col = random.randint(0,len(b[0])-1)
return row , col, oriantation

#check colision

def check_colision(b,row,col,size,oriantation):
for off_set in range(size):
if oriantation == 0:

if b[row][col+ off_set] != 0:
return False
else:
if b[row + off_set][col] != 0:
return False
return True

#place ship
def place_ship(b,row,col,size,oriantation):
for off_set in range(size):
if oriantation == 0:
b[row][col+off_set] = 1
else:
b[row+off_set][col] = 1


board = [
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]
]
#c = input('enter your cordinate')

#print(cordinate_index(c))
#display_board(board)

debug_board(board)
