# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Moon 428003554
#               Jake Korthals 530007075
#               Ben Segal 431002007
#				Evan Li 830008246
# Section:      535
# Assignment:   Team Design Project
# Date:         24 November 2020
#

import turtle as t
import random

play_again = True
score_p1 = 0  # keeps track of score for player 1
score_p2 = 0  # keeps track of score for player 2
game_num = 0  # keeps track of number of games

while play_again:
    # ---------------------------------------Rock Paper Scissors Game ---------------------------------------
    ai_q = input("Would you like to play against the AI (Y/N): ")

    while ai_q != 'Y' and ai_q != 'N':  # if invalid input is given, loop until valid input is accepted
        print('Invalid input! Try again')
        ai_q = input("Would you like to against the AI (Y/N): ")


    def game_pve():  # player vs AI rps game
        game_list = ["r", "p", "s"]  # r for rock, p for paper, s for scissor
        player = False
        p1_win = False
        p2_win = False
        print("\nWelcome to Rock Paper Scissor game")
        print("You can enter Rock as r , Paper as p , Scissor as s .")
        print("In this game, r > s , s > p , p > r , for example, player choose r, AI choose s, player win.")
        # gives instructions

        while not player:
            ai = game_list[random.randint(0, 2)]
            player = input("Please enter your choice:")
            if player == ai:
                print("Tie, please try again.", "\n")
            elif player == "r":
                if ai == "p":
                    print("You lose... AI is", ai, "Player is", player)
                    p2_win = True
                    return p1_win, p2_win
                else:
                    print("You win! AI is", ai, "Player is", player)
                    p1_win = True
                    return p1_win, p2_win
            elif player == "p":
                if ai == "s":
                    print("You lose... AI is", ai, "Player is", player)
                    p2_win = True
                    return p1_win, p2_win
                else:
                    print("You win! AI is", ai, "Player is", player)
                    p1_win = True
                    return p1_win, p2_win
            elif player == "s":
                if ai == "r":
                    print("You lose... AI is", ai, "Player is", player)
                    p2_win = True
                    return p1_win, p2_win
                else:
                    print("You win! AI is", ai, "Player is", player)
                    p1_win = True
                    return p1_win, p2_win
            else:
                print("Typing error, please try again.")
            player = False


    def game_pvp():  # player vs player rock paper scissors game
        print("\nWelcome to Rock Paper Scissor game")
        print("You can enter Rock as r , Paper as p , Scissor as s .")
        print("In this game, r > s , s > p , p > r , for example, player 1 choose r, player 2 choose s, player 1 win.")
        # gives instructions
        player_1 = False
        player_2 = False
        p1_win = False
        p2_win = False
        # set two player to false in order to repeat the loop when necessary.
        while not player_1 and not player_2:
            player_1 = input("Player 1 please enter your choice: ")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            print("Lines for separate two enters")
            # lines to separate two enters in order to make it fair
            print()
            player_2 = input("Player 2 please enter your choice: ")
            if player_1 == player_2:
                print("\n", "    Tie, please try again ", "\n")
            elif player_1 == "r":
                if player_2 == "p":
                    print("\n", "    Player 2 win!")
                    p2_win = True
                    return p1_win, p2_win
                else:
                    print("\n", "    Player 1 win!")
                    p1_win = True
                    return p1_win, p2_win
            elif player_1 == "p":
                if player_2 == "s":
                    print("\n", "    Player 2 win!")
                    p2_win = True
                    return p1_win, p2_win
                else:
                    print("\n", "    Player 1 win!")
                    p1_win = True
                    return p1_win, p2_win
            elif player_1 == "s":
                if player_2 == "r":
                    print("\n", "    Player 2 win!")
                    p2_win = True
                    return p1_win, p2_win
                else:
                    print("\n", "    Player 1 win!")
                    p1_win = True
                    return p1_win, p2_win
            else:  # invalid input, print the following message and re-loop
                print("Typing error, please try again", "\n")
                player_1 = False
                player_2 = False


    # if tie or error, loop run again

    if ai_q == "Y":  # determines the winner from the AI rps game
        player1_win, player2_win = game_pve()
    elif ai_q == "N":  # determines the winner from the pvp game
        player1_win, player2_win = game_pvp()

    if player1_win == True:  # if player1 wins, set count to zero
        count = 0
    elif player2_win == True:  # if player2 wins, set count to 1
        count = 1

    #  ---------------------------------------TIC TAC TOE GAME ---------------------------------------

    # Creates the screen for the tic tac toe board with turtle
    t.speed(300)
    t.penup()
    t.hideturtle()
    t.goto(-150, -150)
    t.pendown()
    canvas = t.Screen()
    canvas.setup(1200, 1000)
    canvas.title("Tic Tac Toe Board")

    # scoreboard
    pen = t.Turtle()
    pen.color('black')
    pen.up()
    pen.hideturtle()
    pen.goto(0, 380)
    pen.clear()
    pen.write("Player 1: {}   Player 2: {}".format(score_p1, score_p2), align="center", font=("Courier", 24, "normal"))


    # defining Shapes
    # draws X shape
    def letterX():
        t.hideturtle()
        t.penup()
        t.color()
        t.pendown()
        t.right(45)
        t.forward(90 / 2)
        t.right(180)
        t.forward(90)
        t.right(180)
        t.forward(90 / 2)
        t.left(90)
        t.forward(90 / 2)
        t.right(180)
        t.forward(90)
        t.right(180)
        t.forward(90 / 2)
        t.right(45)
        t.penup()
        t.hideturtle()
        t.setheading(0)


    # draws O shape
    def circ():
        t.hideturtle()
        t.color()
        t.circle(35)


    # draws triangle shape
    def tri():
        t.hideturtle()
        t.color()
        t.forward(85)  # draw base
        t.left(120)
        t.forward(85)
        t.left(120)
        t.forward(85)
        t.setheading(0)


    # draws star shape
    def star():
        for i in range(5):
            t.speed()
            t.hideturtle()
            t.color()
            t.forward(80)
            t.right(144)
        t.setheading(0)


    # Defining shapes positiion in the tic tac toe board
    # draws left top position for letter X
    def LT_x():
        t.penup()
        t.color()
        t.goto(-100, 100)
        t.pendown()
        letterX()


    # draws middle top position for letter X
    def MT_x():
        t.penup()
        t.color()
        t.goto(0, 100)
        t.pendown()
        letterX()


    # draws left right top position for letter X
    def RT_x():
        t.penup()
        t.color()
        t.goto(100, 100)
        t.pendown()
        letterX()


    # draws left middle position for letter X
    def LM_x():
        t.penup()
        t.color()
        t.goto(-100, 0)
        t.pendown()
        letterX()


    # draws middle middle position for letter X
    def MM_x():
        t.penup()
        t.color()
        t.goto(0, 0)
        t.pendown()
        letterX()


    # draws right middle position for letter X
    def RM_x():
        t.penup()
        t.color()
        t.goto(100, 0)
        t.pendown()
        letterX()


    # draws left bottom position for letter X
    def LB_x():
        t.penup()
        t.color()
        t.goto(-100, -100)
        t.pendown()
        letterX()


    # draws middle bottom position for letter X
    def MB_x():
        t.penup()
        t.color()
        t.goto(0, -100)
        t.pendown()
        letterX()


    # draws right bottom position for letter X
    def RB_x():
        t.penup()
        t.color()
        t.goto(100, -100)
        t.pendown()
        letterX()


    # draws left top position for letter O
    def LT_O():
        t.penup()
        t.color()
        t.goto(-100, 65)
        t.pendown()
        circ()


    # draws middle top position for letter O
    def MT_O():
        t.penup()
        t.color()
        t.goto(0, 65)
        t.pendown()
        circ()


    # draws right top position for letter O
    def RT_O():
        t.penup()
        t.color()
        t.goto(100, 65)
        t.pendown()
        circ()


    # draws left middle position for letter O
    def LM_O():
        t.penup()
        t.color()
        t.goto(-100, -35)
        t.pendown()
        circ()


    # draws middle middle position for letter O
    def MM_O():
        t.penup()
        t.color()
        t.goto(0, -35)
        t.pendown()
        circ()


    # draws right middle position for letter O
    def RM_O():
        t.penup()
        t.color()
        t.goto(100, -35)
        t.pendown()
        circ()


    # draws left bottom position for letter O
    def LB_O():
        t.penup()
        t.color()
        t.goto(-100, -135)
        t.pendown()
        circ()


    # draws middle bottom position for letter O
    def MB_O():
        t.penup()
        t.color()
        t.goto(0, -135)
        t.pendown()
        circ()


    # draws right bottom position for letter O
    def RB_O():
        t.penup()
        t.color()
        t.goto(100, -135)
        t.pendown()
        circ()


    # draws left top position for triangle shape
    def LT_tri():
        t.penup()
        t.color()
        t.goto(-142, 65)
        t.pendown()
        tri()


    # draws middle top position for triangle shape
    def MT_tri():
        t.penup()
        t.color()
        t.goto(-42, 65)
        t.pendown()
        tri()


    # draws right top position for triangle shape
    def RT_tri():
        t.penup()
        t.color()
        t.goto(58, 65)
        t.pendown()
        tri()


    # draws left middle position for triangle shape
    def LM_tri():
        t.penup()
        t.color()
        t.goto(-142, -35)
        t.pendown()
        tri()


    # draws middle middle position for triangle shape
    def MM_tri():
        t.penup()
        t.color()
        t.goto(-42, -35)
        t.pendown()
        tri()


    # draws right middle position for triangle shape
    def RM_tri():
        t.penup()
        t.color()
        t.goto(58, -35)
        t.pendown()
        tri()


    # draws left bottom position for triangle shape
    def LB_tri():
        t.penup()
        t.color()
        t.goto(-142, -135)
        t.pendown()
        tri()


    # draws middle bottom position for triangle shape
    def MB_tri():
        t.penup()
        t.color()
        t.goto(-42, -135)
        t.pendown()
        tri()


    # draws right bottom position for triangle shape
    def RB_tri():
        t.penup()
        t.color()
        t.goto(58, -135)
        t.pendown()
        tri()


    # draws left top position for star shape
    def LT_star():
        t.penup()
        t.color()
        t.goto(-140, 110)
        t.pendown()
        star()


    # draws middle top position for star shape
    def MT_star():
        t.penup()
        t.color()
        t.goto(-40, 110)
        t.pendown()
        star()


    # draws right top position for star shape
    def RT_star():
        t.penup()
        t.color()
        t.goto(60, 110)
        t.pendown()
        star()


    # draws left middle position for star shape
    def LM_star():
        t.settiltangle(0)
        t.penup()
        t.color()
        t.goto(-140, 10)
        t.pendown()
        star()


    # draws middle middle position for star shape
    def MM_star():
        t.penup()
        t.color()
        t.goto(-42, 10)
        t.pendown()
        star()


    # draws right middle position for star shape
    def RM_star():
        t.penup()
        t.color()
        t.goto(58, 10)
        t.pendown()
        star()


    # draws left bottom position for star shape
    def LB_star():
        t.penup()
        t.color()
        t.goto(-142, -90)
        t.pendown()
        star()


    # draws middle bottom position for star shape
    def MB_star():
        t.penup()
        t.color()
        t.goto(-42, -90)
        t.pendown()
        star()


    # draws right bottom position for star shape
    def RB_star():
        t.penup()
        t.color()
        t.goto(58, -90)
        t.pendown()
        star()


    # Line to declare 3 in a row
    # Horizontal#
    def three_in_row_H3():  # Top Horizontal
        t.penup()
        t.goto(-150, 100)
        t.pendown()
        t.forward(-20)
        t.forward(340)


    def three_in_row_H2():  # Middle Horizontal
        t.penup()
        t.goto(-150, 0)
        t.pendown()
        t.forward(-20)
        t.forward(340)


    def three_in_row_H1():  # Bottom Horizontal
        t.penup()
        t.goto(-150, -100)
        t.pendown()
        t.forward(-20)
        t.forward(340)


    # Vertical#
    def three_in_a_row_V1():  # Vertical Left
        t.penup()
        t.goto(-100, 170)
        t.pendown()
        t.left(90)
        t.forward(-350)


    def three_in_a_row_V2():  # Vertical Middle
        t.penup()
        t.goto(0, 170)
        t.pendown()
        t.left(90)
        t.forward(-350)


    def three_in_a_row_V3():  # Vertical Right
        t.penup()
        t.goto(100, 170)
        t.pendown()
        t.left(90)
        t.forward(-350)


    # Diagonal
    def pos_slope():  # If slope is going up
        t.penup()
        t.goto(-160, -160)
        t.pendown()
        t.left(45)
        t.forward(450)


    def neg_slope():  # If slope is going down
        t.penup()
        t.goto(160, -160)
        t.pendown()
        t.left(135)
        t.forward(450)


    # making three squares
    def square():
        for i in range(0, 4):
            t.forward(100)
            t.left(90)


    # Making a row of squares
    def row():
        for i in range(0, 3):
            square()
            t.forward(100)


    # creating Tic tac toe board
    def board():
        row(), t.penup(), t.goto(-150, -50), t.pendown()
        row(), t.penup(), t.goto(-150, 50), t.pendown()
        row()


    # function determines the winner
    def find_winner(players_moves):
        # if the player connects the top row, they win
        if "RT" in players_moves and "MT" in players_moves and "LT" in players_moves:
            print(players_moves[0], "WINNER")
            players_moves.append("WINNER")  # append the string "WINNER" into the list to show which player won
            three_in_row_H3()
        # if the player connects the right-most column, they win
        elif "RT" in players_moves and "RM" in players_moves and "RB" in players_moves:
            print(players_moves[0], "WINNER")
            players_moves.append("WINNER")
            three_in_a_row_V3()
        # if the player connects the diagonal, they win
        elif "RT" in players_moves and "MM" in players_moves and "LB" in players_moves:
            print(players_moves[0], "WINNER")
            players_moves.append("WINNER")
            pos_slope()
        # if the player connects the left-most column, they win
        elif "LT" in players_moves and "LM" in players_moves and "LB" in players_moves:
            print(players_moves[0], "WINNER")
            players_moves.append("WINNER")
            three_in_a_row_V1()
        # if the player connects the other diagonal, they win
        elif "LT" in players_moves and "MM" in players_moves and "RB" in players_moves:
            print(players_moves[0], "WINNER")
            players_moves.append("WINNER")
            neg_slope()
        # if the player connects the bottom row, they win
        elif "RB" in players_moves and "MB" in players_moves and "LB" in players_moves:
            print(players_moves[0], "WINNER")
            players_moves.append("WINNER")
            three_in_row_H2()
        # if the player connects the middle column, they win
        elif "MT" in players_moves and "MM" in players_moves and "MB" in players_moves:  #####HAD ERROR AT MB#####
            print(players_moves[0], "WINNER")
            players_moves.append("WINNER")
            three_in_a_row_V2()
        # if the player connects the middle row, they win
        elif "RM" in players_moves and "MM" in players_moves and "LM" in players_moves:
            print(players_moves[0], "WINNER")
            players_moves.append("WINNER")
            three_in_row_H2()


    def draw_X(players_moves):
        if players_moves == "RT":
            RT_x()
        elif players_moves == "MT":
            MT_x()
        elif players_moves == "LT":
            LT_x()
        elif players_moves == "RM":
            RM_x()
        elif players_moves == "MM":
            MM_x()
        elif players_moves == "LM":
            LM_x()
        elif players_moves == "MB":
            MB_x()
        elif players_moves == "RB":
            RB_x()
        elif players_moves == "LB":
            LB_x()


    def draw_O(players_moves):
        if players_moves == "RT":
            RT_O()
        elif players_moves == "MT":
            MT_O()
        elif players_moves == "LT":
            LT_O()
        elif players_moves == "RM":
            RM_O()
        elif players_moves == "MM":
            MM_O()
        elif players_moves == "LM":
            LM_O()
        elif players_moves == "RB":
            RB_O()
        elif players_moves == "MB":
            MB_O()
        elif players_moves == "LB":
            LB_O()


    def draw_triangle(players_moves):
        if players_moves == "RT":
            RT_tri()
        elif players_moves == "MT":
            MT_tri()
        elif players_moves == "LT":
            LT_tri()
        elif players_moves == "RM":
            RM_tri()
        elif players_moves == "MM":
            MM_tri()
        elif players_moves == "LM":
            LM_tri()
        elif players_moves == "MB":
            MB_tri()
        elif players_moves == "RB":
            RB_tri()
        elif players_moves == "LB":
            LB_tri()


    def draw_star(players_moves):
        if players_moves == "RT":
            RT_star()
        elif players_moves == "MT":
            MT_star()
        elif players_moves == "LT":
            LT_star()
        elif players_moves == "RM":
            RM_star()
        elif players_moves == "MM":
            MM_star()
        elif players_moves == "LM":
            LM_star()
        elif players_moves == "MB":
            MB_star()
        elif players_moves == "RB":
            RB_star()
        elif players_moves == "LB":
            LB_star()


    def draw_shape(shape, move):
        if shape == "X":
            draw_X(move)
        elif shape == "O":
            draw_O(move)
        elif shape == "Triangle":
            draw_triangle(move)
        elif shape == "Star":
            draw_star(move)


    board()  # prints the board
    move_options = ["RT", "MT", "LT", "RM", "MM", "LM", "RB", "MB", "LB"]  # list that holds the available positions
    # to move
    winner = False  # boolean variable to facilitate the loop

    player_1_moves = ["PLAYER 1"]  # list that will hold the moves player 1 makes
    player_2_moves = ["PLAYER 2"]  # list that will hold the moves player 2 makes

    player_color_1 = input("Player 1, what is your color: ")
    player_color_2 = input("Player 2, what is your color: ")
    shape_options = ["X", "O", "Star", "Triangle"]
    t.speed(10)
    if ai_q == 'N':  # not playing against AI, Player 1 vs Player 2
        if count == 0:  # Player 1 goes first
            print("Your shape options are", shape_options)
            shape_player_1 = input("Player 1, enter a shape: ")
            while shape_player_1 not in shape_options:  # loop until player 1 enters a valid shape
                print('Invalid shape entered for Player 1! Try again.')
                shape_player_1 = input("Player 1, enter a shape: ")
            shape_options.remove(shape_player_1)
            print("Your shape options are", shape_options)
            shape_player_2 = input("Player 2, enter a shape: ")
            while shape_player_2 not in shape_options:  # loop until player 2 enters a valid shape
                print('Invalid shape entered for Player 2! Try again.')
                shape_player_2 = input("Player 2, enter a shape: ")
            shape_options.remove(shape_player_2)

        if count == 1:  # Player 2 goes first
            print("Your shape options are", shape_options)
            shape_player_2 = input("Player 2, enter a shape:?")
            while shape_player_2 not in shape_options:  # loop until player 2 enters a valid shape
                print('Invalid shape entered for Player 2! Try again.')
                shape_player_2 = input("Player 2, enter a shape:?")
            shape_options.remove(shape_player_2)
            print("Your shape options are", shape_options)
            shape_player_1 = input("Player 1, enter a shape:?")
            while shape_player_1 not in shape_options:  # loop until player 1 enters a valid shape
                print('Invalid shape entered for Player 1! Try again.')
                shape_player_1 = input("Player 1, enter a shape:?")
            shape_options.remove(shape_player_1)

        while not winner:  # loop until a winner is determined
            if count % 2 == 0:  # if statement determines it is player 1s turn
                while player_color_1 != 9999:  # loop the try except statement until a valid color is entered
                    try:
                        t.color(player_color_1)
                        break
                    except:
                        print('Invalid color entered for Player 1! Try again.')
                        player_color_1 = input("Player 1, what is your color: ")

                print("Player 1, your available move options are", move_options)
                move = input("What is your move: ")
                while move in move_options:  # loop while the move variable is in the move_options list
                    move_options.remove(move)  # deletes the move from the move_options list
                    player_1_moves.append(move)  # appends the move to the player 1 moves list
                    draw_shape(shape_player_1, move)
                    find_winner(player_1_moves)  # checks to see if player 1 won
                    count += 1
            elif count % 2 != 0:
                while player_color_2 != 9999:  # loop the try except statement until a valid color is entered
                    try:
                        t.color(player_color_2)
                        break
                    except:
                        print('Invalid color entered for Player 2! Try again.')
                        player_color_2 = input("Player 2, what is your color: ")

                print("Player 2, your available move options are", move_options)
                move = input("What is your move: ")
                while move in move_options:
                    move_options.remove(move)
                    player_2_moves.append(move)
                    draw_shape(shape_player_2, move)
                    find_winner(player_2_moves)
                    count += 1
            if "WINNER" in player_1_moves or "WINNER" in player_2_moves:  # if the winner is determined, break out of the
                # loop
                if "WINNER" in player_1_moves:
                    score_p1 += 1
                    pen.clear()
                    pen.write("Player 1: {}   Player 2: {}".format(score_p1, score_p2), align="center",
                              font=("Courier", 24, "normal"))
                elif "WINNER" in player_2_moves:
                    score_p2 += 1
                    pen.clear()
                    pen.write("Player 1: {}   Player 2: {}".format(score_p1, score_p2), align="center",
                              font=("Courier", 24, "normal"))
                break
            elif not move_options:  # if no winner is found, it is a tie game
                print("TIE GAME")
                break
    elif ai_q == 'Y':  # playing against AI, Player 1 vs AI
        if count == 0:  # Player 1 gets to choose shape first
            print("Your shape options are", shape_options)
            shape_player_1 = input("Player 1, enter a shape:?")
            while shape_player_1 not in shape_options:  # loop until player 1 enters a valid shape
                print('Invalid shape entered for Player 1! Try again.')
                shape_player_1 = input("Player 1, enter a shape:?")
            shape_options.remove(shape_player_1)
            # print("Your shape options are", shape_options)
            ai_shape = random.randint(0, len(
                shape_options) - 1)  # chooses a number from 0 to length of shape options array
            # shape_player_2 = input("Player 2, enter a shape:?")
            shape_player_2 = shape_options[ai_shape]  # assigns the AI's shape to a random element from shape_options
            print("PLAYER 2 SHAPE: ", shape_player_2)  #### DEBUG STATEMENT ####
            shape_options.remove(shape_player_2)

        if count == 1:  # AI gets to choose shape first
            # print("Your shape options are", shape_options)
            ai_shape = random.randint(0, len(
                shape_options) - 1)  # chooses a number from 0 to length of shape options array
            # shape_player_2 = input("Player 2, enter a shape:?")
            shape_player_2 = shape_options[ai_shape]  # assigns the AI's shape to a random element from shape_options
            print("PLAYER 2 SHAPE: ", shape_player_2)  #### DEBUG STATEMENT ####
            shape_options.remove(shape_player_2)
            print("Your shape options are", shape_options)
            shape_player_1 = input("Player 1, enter a shape:?")
            while shape_player_1 not in shape_options:  # loop until player 1 enters a valid shape
                print('Invalid shape entered for Player 1! Try again.')
                shape_player_1 = input("Player 1, enter a shape:?")
            shape_options.remove(shape_player_1)

        while not winner:
            if count % 2 == 0:  # if statement determines it is player 1s turn
                while player_color_1 != 9999:  # loop the try except statement until a valid color is entered
                    try:
                        t.color(player_color_1)
                        break
                    except:
                        print('Invalid color entered for Player 1! Try again.')
                        player_color_1 = input("Player 1, what is your color: ")
                print("Player 1, your available move options are", move_options)
                move = input("What is your move: ")
                while move in move_options:  # loop while the move variable is in the move_options list
                    move_options.remove(move)  # deletes the move from the move_options list
                    player_1_moves.append(move)  # appends the move to the player 1 moves list
                    draw_shape(shape_player_1, move)
                    find_winner(player_1_moves)  # checks to see if player 1 won
                    count += 1
            elif count % 2 != 0:  # if statement determines it is the AI's turn
                while player_color_2 != 9999:  # loop the try except statement until a valid color is entered
                    try:
                        t.color(player_color_2)
                        break
                    except:
                        print('Invalid color entered for Player 2! Try again.')
                        player_color_2 = input("Player 2, what is your color: ")
                # print("Player 2, your available move options are", move_options)
                # move = input("What is your move?")
                ai_move = random.randint(0,
                                         len(move_options) - 1)  # random integer that will be the element number of the
                # move_options list
                move = move_options[ai_move]  # the AI's move is a random element inside the ai_move list
                print('AI MOVE:', move)  #### DEBUG STATEMENT ####
                while move in move_options:
                    move_options.remove(move)
                    player_2_moves.append(move)
                    draw_shape(shape_player_2, move)
                    find_winner(player_2_moves)
                    count += 1
            if "WINNER" in player_1_moves or "WINNER" in player_2_moves:  # if the winner is determined, break out of the
                # loop
                if "WINNER" in player_1_moves:
                    score_p1 += 1
                    pen.clear()
                    pen.write("Player 1: {}   Player 2: {}".format(score_p1, score_p2), align="center",
                              font=("Courier", 24, "normal"))
                if "WINNER" in player_2_moves:
                    score_p2 += 1
                    pen.clear()
                    pen.write("Player 1: {}   Player 2: {}".format(score_p1, score_p2), align="center",
                              font=("Courier", 24, "normal"))
                break

            elif not move_options:  # if no winner is found, it is a tie game
                print("TIE GAME")
                break

    play_again = input('Would you like to play again? (Y/N): ')
    while play_again != 'Y' and play_again != 'N':
        print('Invalid input! Try again.')
        play_again = input('Would you like to play again? (Y/N): ')
    if play_again == 'Y':
        t.reset()
        print('\nReloading game...')
        play_again = True
        game_num += 1
        pen.clear()
    elif play_again == 'N':
        print('\nEnding game...')
        play_again = False

t.bye()



