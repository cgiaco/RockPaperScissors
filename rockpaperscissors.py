#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = ""
        self.their_move = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            response = input("Rock, paper, scissors? > ").lower()
            if response not in moves:
                print("Sorry, I don't understand.")
            else:
                return response


class ReflectPlayer(Player):
    def move(self):
        if self.their_move == "":
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == "":
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def player_select():
    response = input("Select your opponent: Random, "
                     "Reflect or Cycle? > ").lower()
    if response == 'random':
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif response == 'reflect':
        game = Game(HumanPlayer(), ReflectPlayer())
        game.play_game()
    elif response == 'cycle':
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
    else:
        print("Invalid input")
        player_select()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}.\n"
              f"Opponent played {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("** PLAYER 1 WINS **")
            self.p1score += 1
        elif beats(move2, move1):
            print("** PLAYER 2 WINS **")
            self.p2score += 1
        else:
            print("** DRAW **")
        print(f"Score: Player One {self.p1score}, Player Two {self.p2score}\n")

    def play_game(self):
        try:
            rounds = int(input("How many rounds? (1-10) > "))
            if rounds in range(1, 11):
                print("Let's Go!\n")
                for round in range(rounds):
                    print(f"Round {round} --")
                    self.play_round()
                if self.p1score > self.p2score:
                    print("Congratulations! You are the winner!\n")
                elif self.p1score < self.p2score:
                    print("Your opponent won... better luck next time!\n")
                else:
                    print(f"Still tied after {rounds} rounds...\n")
                print(f"FINAL SCORE: \n"
                      f"Player One {self.p1score}\n"
                      f"Player Two {self.p2score}\n")
                self.play_again()
            else:
                print("Invalid input: enter a number between 1 and 10")
                self.play_game()
        except ValueError:
            print("Invalid input: enter a number between 1 and 10")
            self.play_game()

    def play_again(self):
        response = input("Play again? (yes/no) > ").lower()
        if response == 'yes':
            self.p1score = 0
            self.p2score = 0
            self.play_game()
        elif response == 'no':
            print("Thanks for playing!\n")
        else:
            self.play_again()


if __name__ == '__main__':
    player_select()
