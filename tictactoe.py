# Tic-Tac-Toe
# Global variables
import time
av = '0123456789' # available moves, space for unavailable
gb = ' '*10 # game board current status
end_game = False
winner = ''
turn = 1

# Drawing board function
# Take status of available cells and current game board
# Return print of the boards
def draw_board(av,gb):
    print ('\n'*100)
    print(' Available\n'+
          '   moves       Game Board\n\n'
          ' '+av[1]+' | '+av[2]+' | '+av[3]+'      '+gb[1]+' | '+gb[2]+' | '+gb[3]+' \n'
          '-----------    -----------\n'
          ' '+av[4]+' | '+av[5]+' | '+av[6]+'      '+gb[4]+' | '+gb[5]+' | '+gb[6]+' \n'
          '-----------    -----------\n'
          ' '+av[7]+' | '+av[8]+' | '+av[9]+'      '+gb[7]+' | '+gb[8]+' | '+gb[9]+' \n\n'
          )

# Take user input function
def user_input():
    pass

# Set marker status
def set_marker():
    pass

# Check the score
# Take status of game board
# Return if a user wins
def check_score(gb_status):
    win_comb = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]] #All variants of winning combinations to chech against
    for comb in win_comb:
        if gb_status[comb[0]] == 'X' and gb_status[comb[1]] == 'X' and gb_status[comb[2]] == 'X':
            print('User X wins!')
            end_game = True
            winner = p1_name
            break
        elif gb_status[comb[0]] == 'O' and gb_status[comb[1]] == 'O' and gb_status[comb[2]] == 'O':
            print('User O wins!')
            end_game = True
            winner = p2_name
            break
    else:
        print("Let's go on...\n")
        time.sleep(1)

# Main game loop
print ('Hi, and welcome to the Tic Tac Toe game')
print ('Player1, please choose your name:')
p1_name = input ('---> ')
print ('\nOK, '+p1_name+', your marker is X\n\n')
time.sleep(1)
print ('Now, Player2, please choose your name:')
p2_name = input ('---> ')
print ('\nOK, '+p2_name+' your marker is O\n\n')
time.sleep(2)
draw_board(av,gb)
while not end_game:
    if turn == 1 and end_game == False:
        print ('Please choose the number of cell for your next move, '+p1_name+'\n')
        move = int(input ('---> '))
        gb = gb[:move]+'X'+gb[move+1:]
        av = av[:move]+' '+av[move+1:]
        draw_board(av,gb)
        check_score(gb)
        turn = 2
    elif turn == 2 and end_game == False:
        print ('Please choose the number of cell for your next move, '+p2_name+'\n')
        move = int(input ('---> '))
        gb = gb[:move]+'O'+gb[move+1:]
        av = av[:move]+' '+av[move+1:]
        draw_board(av,gb)
        check_score(gb)
        turn = 1
    else:
        print('\n'*100)
        print('GAME OVER!')
        print('The Winner is '+winner)        

