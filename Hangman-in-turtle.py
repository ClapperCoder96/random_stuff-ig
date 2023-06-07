"""We all know that turtle is one of the worst and best python libraries there is. I kind of like it, and think it is a great
way to improve your skill in overall coding as well as styilistic and library dependent sources. Anyways, this takes the functions of my 
word-guesser.py file and made it into a fun interactive game for python!"""
import random
from time import sleep

thang = turtle.Turtle()
body = turtle.Turtle()
thang.hideturtle()
speed(0)
hide_turtle()
penup()
bgcolor("lightblue")
speed(0)

def gallow(thang):
    thang.penup()
    thang.setposition(-120,-170)
    thang.pendown()
    thang.pensize(5)
    thang.forward(300)
    thang.penup()
    thang.forward(-150)
    thang.left(90)
    thang.pendown()
    thang.forward(200)
    thang.left(90)
    thang.forward(50)
    thang.left(90)
    thang.forward(30)

body.color("red")
body.pensize(5)
body.penup()
body.setposition(-15, 0)
body.pendown()
def head(body):
    body.dot(20,255,0,0,1)
def torso(body):
    right(45)
    body.forward(80)
def leg1(body):
    body.left(45)
    body.forward(50)
    body.forward(-50)
def leg2(body):    
    body.right(90)
    body.forward(50)
    body.forward(-50)
def arms1(body):    
    body.right(-45)
    body.right(180)
    body.forward(35)
    body.right(90)
    body.forward(50)
def arms2(body):   
    body.left(180)
    body.forward(100)


def choose_word():
    words = ["box", "puppy", "bag", "air", "head", "gum", "banana", "rat"]
    word = random.choice(words).lower()
    return word


def word_in_progress(word, guesses):
    word_in_progress = ""
    for letter in word:
        if letter in guesses:
            word_in_progress += letter
        else:
            word_in_progress += "*"
    return word_in_progress


def main(word):
    lettersguessed = []
    tries = 6

    while tries != 0:
            thang.speed(0)
            thang.penup()
            thang.setposition(-120,-170)
            gallow(thang)
            thang.right(90)
            thang.right(180)
            clear()
            setposition(-110, 170)
            write("\nYou have " + str(tries) + " tries left.", font=('Impact', 18, 'normal'))
            setposition(-100, 140)
            write("Word so far " + word_in_progress(word, lettersguessed), font=('Comic sans', 20, 'normal'))
            setposition(-200, 120)
            write("Letters guessed: " + str(lettersguessed), font=('Comic sans', 15, 'normal'))
            guess = input("Guess: ").lower()[0]

            if guess not in lettersguessed:
                lettersguessed.append(guess)

            if word_in_progress(word, lettersguessed) == word:
                setposition(-200, 80)
                write("\nCongratulations! You got the right word: " + word, font=('Comic Sans', 15, 'normal'))
                sleep(3)
                quit()

            else:
                if guess in word:
                    print("Correct letter!")
                else:
                    tries -= 1
                    print("WRONG!")
                    if tries == 5:
                        head(body)
                    if tries == 4:
                        body.right(90)
                        torso(body)
                    if tries == 3:
                        leg1(body)
                    if tries == 2:
                        leg2(body)
                    if tries == 1:
                        arms1(body)
                    if tries == 0:
                        arms2(body)
                        body.setposition(-100, 100)
                        write("\nOops you ran out of guesses. The correct word was " + word, font=('Comic Sans', 25, 'normal'))
                        sleep(3)
                        quit()

word = choose_word()
main(word)
