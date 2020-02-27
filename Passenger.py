import turtle
import random
import json
import time
import Strategies as st
import numpy as np
with open("SEATSMATRIX.txt") as json_file1:
    MATRIX = json.load(json_file1)
win_length = 1324
win_width = 544
turtles = 96
turtle.screensize(win_length,win_width)
class passenger(object):
    def __init__(self,color,pos,seat,state,stowing_time):
        self.pos = pos
        self.color = color
        self.seat = seat
        self.state = state
        self.stowing_time = stowing_time
        self.turt = turtle.Turtle()
        self.turt.hideturtle()
        self.turt.speed(10)
        self.turt.penup()
        # self.turt.home(-572.0,0.0)
        self.turt.shapesize(2,2)
        self.turt.shape('arrow')
        self.turt.color(color)
        self.turt.goto(pos[0],pos[1])
        #self.turt.position()
        self.turt.setheading(0)
    def shuffle(self,possible,othershuffles):
        self.pos = [round(self.turt.position()[0]),round(self.turt.position()[1])]
        self.turt.color('green')
        self.color = 'green'
        if self.pos == self.seat and self.turt.heading() == 180:
            if 90 in possible and 270 in possible:
                self.state = 'alone'
            if self.seat[1] > 0:
                self.turt.setheading(270)
            elif self.seat[1] < 0:
                self.turt.setheading(90)
            if self.turt.heading() in possible:
                self.turt.forward(60)
        elif self.pos[1] != 0:
            if self.turt.heading() in possible:
                self.turt.forward(60)
        elif self.pos[1] == 0:
            if self.turt.heading() != 180 and self.pos[0] == self.seat[0] and (0 not in possible or self.pos[0] + 120 in othershuffles or self.pos[0] + 60 in othershuffles):
                self.turt.setheading(0)
            elif self.pos[0] == self.seat[0] + 60 and self.state == 'alone' and self.turt.heading() == 0:
                self.turt.setheading(180)
                if self.turt.heading() in possible:
                    self.turt.forward(60)
            elif self.pos[0] == self.seat[0] + 120:
                if self.turt.heading() == 0:
                    self.turt.setheading(180)
                if self.turt.heading() in possible:
                    self.turt.forward(60)
            elif self.turt.heading() == 0:
                if self.state == 'alone':
                    self.turt.setheading(180)
                if self.turt.heading() in possible:
                    self.turt.forward(60)
                elif 0 in possible:
                    self.turt.setheading(0)
                    self.turt.forward(60)
            elif self.turt.heading() == 90 and self.seat[1] < 0:
                self.turt.setheading(0)
                if self.turt.heading() in possible:
                    self.turt.forward(60)
            elif self.turt.heading() == 270 and self.seat[1] > 0:
                self.turt.setheading(0)
                if self.turt.heading() in possible:
                    self.turt.forward(60)
            elif (self.turt.heading() == 90 and self.seat[1] > 0) or (self.turt.heading() == 270 and self.seat[1] < 0):
                self.turt.setheading(0)
                if self.turt.heading() in possible:
                    self.turt.forward(60)
            elif self.turt.heading() == 180:
                if self.pos[0] == self.seat[0]:
                    if self.seat[1] < 0:
                        self.turt.setheading(270)
                    elif self.seat[1] > 0:
                        self.turt.setheading(90)
                    if self.turt.heading() in possible:
                        self.turt.forward(60)
                else:
                    if self.turt.heading() in possible:
                        self.turt.forward(60)

    def move(self,possible):
            self.pos = (self.pos[0] ,self.pos[1])
            if self.turt.position()[0] == self.seat[0]:
                self.turt.color('orange')
                self.color = 'orange'
                if self.seat[1] >0:
                    self.turt.setheading(90)
                else:
                    self.turt.setheading(270)
                if self.turt.heading() != 0 and self.turt.heading() in possible:
                    if self.stowing_time <= 0:
                        self.turt.forward(60)
                    else:
                        self.stowing_time -= 1
            elif self.turt.position()[1] != self.seat[1] and self.turt.heading() in possible:
                self.turt.forward(60)
    def reset(self):
        self.turt.setpos(self.pos)
def GetSeatNumber(SEATS):
    seat = SEATS[0]
    del SEATS[0]
    return seat[1]
def checkCollision(position,otherpositions,seatshuffle):
    possible = []
    if (position[0] + 60, position[1]) not in otherpositions and position[1] == 0:
        possible.append(0)
    if (position[0], position[1] + 60) not in otherpositions or not seatshuffle:
        possible.append(90)
    if (position[0] - 60, position[1]) not in otherpositions and position[1] == 0:
        possible.append(180)
    if (position[0], position[1] - 60) not in otherpositions or not seatshuffle:
        possible.append(270)
    return possible
def checkSwap(list):
    stops = []
    for t in list:
        if t.color == 'green' and (t.state == 'shuffle' or t.state == 'alone'):
            stops.append(t.seat[0])
    return stops
def startGame(strategy,STOWINGTIME,SEATSHUFFLE):
    STRATEGY = strategy
    # STOWINGTIME = stowingtime
    tList = []
    # np.random.normal() + 4
    window = turtle.Screen()
    window.title("Airplane Simulator")
    turtle.bgpic('plane.png')
    turtle.tracer(0, 0)
    color = ['Cornflower Blue', 'Dark Slate Blue', 'Slate Blue', 'Medium Slate Blue', 'Light Slate Blue', 'Medium Blue', 'Royal Blue', 'Blue', 'Dodger Blue', 'Deep Sky Blue', 'Sky Blue']
    start = -(win_length/2) + 30
    allPositions = []
    for t in range(turtles):
        newPosX = start - t * 60
        tList.append(passenger(random.choice(color), (newPosX - 60, 0), GetSeatNumber(STRATEGY),'going',STOWINGTIME))
        x = round(tList[t].turt.pos()[0])
        y = round(tList[t].turt.pos()[1])
        allPositions.append((x,y))
        tList[t].turt.showturtle()
    run = True
    timer = 0
    while run:
        timer += 1
        for t in tList:
            if t.state != 'sitting':
                seat = (t.seat[0], t.seat[1])
                position = (round(t.turt.position()[0]), round(t.turt.position()[1]))
                neighbors = 0
                if t.state == 'shuffle' or t.state == 'alone':
                    allPositions.remove(position)
                    t.shuffle(checkCollision(position,allPositions,SEATSHUFFLE),checkSwap(tList))
                    position = (round(t.turt.position()[0]), round(t.turt.position()[1]))
                    allPositions.append((position))
                elif position != seat:
                    if position[0] + 60 in checkSwap(tList) and t.state == 'going':
                        continue
                    shuffling = False
                    for a in tList:
                        a_pos = (round(a.turt.position()[0]), round(a.turt.position()[1]))
                        if t.state == 'going' and (a.state == 'shuffle' or a.state =='alone' or a.color == 'green') and a_pos[1] == 0 and (a_pos[0]-60 == position[0] or a_pos[0]-120 == position[0]):
                            shuffling = True
                            break
                    if shuffling:
                        continue
                    if position[0] == seat[0] - 60:
                        if not SEATSHUFFLE:
                            allPositions.remove(position)
                            t.move(checkCollision(position, allPositions,SEATSHUFFLE))
                            position = (round(t.turt.position()[0]), round(t.turt.position()[1]))
                            allPositions.append(position)
                        elif seat[1] > 0:
                            for a in tList:
                                if a != t:
                                    if a.seat[1] > 0 and a.seat[0] == seat[0] and a.seat[1] < seat[1] and round(a.turt.position()[0]) == seat[0] and round(a.turt.position()[1]) < seat[1]:
                                        if a.state != 'alone':
                                            a.state = 'shuffle'
                                        neighbors += 1
                                        tList[0], tList[tList.index(a)] = tList[tList.index(a)], tList[0]
                        else:
                            for a in tList:
                                if a != t:
                                    if a.seat[1] < 0 and a.seat[0] == seat[0] and a.seat[1] > seat[1] and round(a.turt.position()[0]) == seat[0] and round(a.turt.position()[1]) > seat[1]:
                                        if a.state != 'alone':
                                            a.state = 'shuffle'
                                        neighbors += 1
                                        tList[0], tList[tList.index(a)] = tList[tList.index(a)], tList[0]
                    if neighbors > 0:
                        t.turt.color('black')
                        t.color = 'black'
                        t.state = 'waiting'
                    else:
                        allPositions.remove(position)
                        t.move(checkCollision(position,allPositions,SEATSHUFFLE))
                        position = (round(t.turt.position()[0]), round(t.turt.position()[1]))
                        allPositions.append(position)
                elif t.state == 'waiting':
                    if neighbors == 0:
                        allPositions.remove(position)
                        t.move(checkCollision(position, allPositions,SEATSHUFFLE))
                        position = (round(t.turt.position()[0]), round(t.turt.position()[1]))
                        allPositions.append(position)
                if position == seat:
                    t.state = 'sitting'
                    t.turt.color("red")
                    t.turt.setheading(180)
        seatedpassengers = [t.state for t in tList if t.state == "sitting"]
        if len(seatedpassengers) == 96:
            turtle.clearscreen()
            return timer
        turtle.update()
        time.sleep(0.0)
# startGame(st.SteffenPerfect(MATRIX),3,True)