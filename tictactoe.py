# Tic-Tac-Toe

import time

av = '0123456789' # available moves, space for unavailable
gb = ' '*10 # game board current status
p1_name = ''
p2_name = ''

# Get names of the players
def get_names():
    global p1_name, p2_name
    print ('Player #1, please choose your name:')
    p1_name = input ('---> ')
    print ('\nOK, '+p1_name+', your marker is X\n\n')
    time.sleep(0.5)
    print ('Now, Player #2, please choose your name:')
    p2_name = input ('---> ')
    print ('\nOK, '+p2_name+' your marker is O\n\n')
    time.sleep(0.5)

# Drawing board function
# Take status of available cells and current game board
# Return print of the boards
def draw_board(av,gb):
    print ('\n'*100)
    print(' Available\n'+
          '   moves       Game Board\n\n'
          ' '+av[1]+' | '+av[2]+' | '+av[3]+'      '+gb[1]+' | '+gb[2]+' | '+gb[3]+' \n'
          '-----------    -----------        '+p1_name+' plays with "X"\n'
          ' '+av[4]+' | '+av[5]+' | '+av[6]+'      '+gb[4]+' | '+gb[5]+' | '+gb[6]+' \n'
          '-----------    -----------        '+p2_name+' plays with "O"\n'
          ' '+av[7]+' | '+av[8]+' | '+av[9]+'      '+gb[7]+' | '+gb[8]+' | '+gb[9]+' \n\n'
          )

# Check if the cell is busy. Free = "True". Busy = "False"
def check_cell(move):
    return gb[move] == ' '

# Take user and verify input 
def user_input(av,gb):
    move = 0
    while move not in range(1,10) or not check_cell(move):
        try:
            move = int(input ('---> '))
            if move not in range(1,10) or not check_cell(move):
                print ('Wrong! Please choose free cell with number from 1 to 9:')
        except:
            print ('Wrong! Please choose free cell with number from 1 to 9:')
    return move

# Check the score or draw
def check_score(gb):
    win_comb = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]] #All winning combinations
    for comb in win_comb:
        if gb[comb[0]] == 'X' and gb[comb[1]] == 'X' and gb[comb[2]] == 'X':
            return p1_name
        elif gb[comb[0]] == 'O' and gb[comb[1]] == 'O' and gb[comb[2]] == 'O':
            return p2_name

def check_full(gb):
    return ' ' not in gb[1:]

# End game - continue or exit
def replay():
    print ('Do you want to start new game? (y/n)?')
    return input('--->').lower().startswith('y')

# Main execution

while True: # Endless loop, until break
    print ('\n'*100) # clear board
    print ('Hi, and welcome to the Tic Tac Toe game')
    get_names()
    turn = 1
    playing = True
    while playing:
        draw_board(av,gb)
        if turn == 1:
           marker = 'X'
           print ('Please type the number (1-9) of cell for your next move, '+p1_name+'\n')
        else:
           marker = 'O'
           print ('Please type the number (1-9) of cell for your next move, '+p2_name+'\n')
        move = user_input(av,gb)
        gb = gb[:move]+marker+gb[move+1:]
        av = av[:move]+' '+av[move+1:]
        winner = check_score(gb)
        if winner != None:
            draw_board(av,gb)
            print('GAME OVER!')
            print(winner+' wins!\n')
            playing = False
        else:
            if check_full(gb):
                draw_board(av,gb)
                print ('DRAW - no more moves')
                playing = False
                break
            else:
                turn *= -1
    av = '0123456789' # available moves, space for unavailable
    gb = ' '*10 # game board current status
    if not replay():
        break