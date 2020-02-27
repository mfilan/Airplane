import Passenger
import Strategies as st
import json
f = open('STATS.txt','w')
stats = []
with open("SEATSMATRIX.txt") as json_file1:
    MATRIX = json.load(json_file1)
for i in range(100):
    stats.append([Passenger.startGame(st.Random(MATRIX)),Passenger.startGame(st.BackToFront(MATRIX)),Passenger.startGame(st.FrontToBack(MATRIX)),Passenger.startGame(st.BackToFront_4GROUPS(MATRIX)),Passenger.startGame(st.FrontToBack_4GROUPS(MATRIX)),Passenger.startGame(st.WindowMiddleAisle(MATRIX)),Passenger.startGame(st.SteffenPerfect(MATRIX)),Passenger.startGame(st.SteffenModified(MATRIX))])
f.write(json.dumps(stats))
f.close()


