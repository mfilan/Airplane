import Passenger
import Strategies as st
import json
import numpy as np
with open("SEATSMATRIX.txt") as json_file1:
    MATRIX = json.load(json_file1)
RANDOMEXPERIMENT = []
BACKTOFRONTEXPERIMENT =[]
# for k in range(100):
#     for i in range(10):
#         SEATSHUFFLE, STOWINGBAGS = Passenger.startGame(st.Random(MATRIX), 0, True), Passenger.startGame(st.Random(MATRIX), i, False)
#         if STOWINGBAGS > SEATSHUFFLE:
#             RANDOMEXPERIMENT.append(i)
#             break
#     print(RANDOMEXPERIMENT)
# for k in range(100):
#     for i in range(10):
#         SEATSHUFFLE, STOWINGBAGS = Passenger.startGame(st.BackToFront_4GROUPS(MATRIX), 0, True), Passenger.startGame(st.BackToFront_4GROUPS(MATRIX), i, False)
#         if STOWINGBAGS > SEATSHUFFLE:
#             BACKTOFRONTEXPERIMENT.append(i)
#             break
#     print(BACKTOFRONTEXPERIMENT)
m = [4, 5, 5, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 4, 5, 5, 4, 4, 5, 5, 4, 6, 5, 4, 5, 5, 5, 4, 5, 4, 5, 4, 4, 4, 5, 6, 5, 4, 5, 4, 5, 4, 5, 5, 5, 4, 4, 4, 6, 5, 4, 5, 4, 5, 5, 4, 6, 4, 5, 5, 5, 4, 5, 6, 4, 5, 5, 5, 5, 6, 5, 4, 4, 4, 5, 5, 5, 4, 4, 5, 5, 4, 5, 5, 5, 4, 5, 6, 4, 4, 5, 4, 4, 5, 5, 5, 5, 4, 5, 6]
k = [6, 6, 5, 5, 5, 4, 5, 4, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 6, 4, 5, 4, 5, 5, 4, 4, 4, 4, 5,6, 6, 5, 5, 6, 5, 4, 5, 4, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 6, 4, 5, 4, 5, 5, 4, 4, 4, 4, 5,6, 6, 5, 5, 6, 5, 4, 5, 4, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 6, 4, 5, 4, 5, 5, 5]
print(np.mean(m),np.mean(k))