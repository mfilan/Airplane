import random
import json
with open("SEATSMATRIX.txt") as json_file1:
    MATRIX = json.load(json_file1)
def FrontToBack(MATRIX):
    row = []
    seats = []
    for i in range(16):
        row = []
        row += ([k[i] for k in MATRIX])
        seats += random.sample(row,len(row))
    return seats
def FrontToBack_4GROUPS (MATRIX):
    Group1 = []
    Group2 = []
    Group3 = []
    Group4 = []
    for i in range(0,4):
        Group1 += ([k[i] for k in MATRIX])
    for i in range(4,8):
        Group2 += ([k[i] for k in MATRIX])
    for i in range(8,12):
        Group3 += ([k[i] for k in MATRIX])
    for i in range(12,16):
        Group4 += ([k[i] for k in MATRIX])
    Group1 = random.sample(Group1,len(Group1))
    Group2 = random.sample(Group2, len(Group2))
    Group3 = random.sample(Group3, len(Group3))
    Group4 = random.sample(Group4, len(Group4))
    return Group1 + Group2 + Group3 + Group4
def BackToFront(MATRIX):
    row = []
    seats = []
    for i in range(15,-1,-1):
        # print(i)
        row = []
        row += ([k[i] for k in MATRIX])
        seats += random.sample(row,len(row))
    return seats

def BackToFront_4GROUPS (MATRIX):
    Group1 = []
    Group2 = []
    Group3 = []
    Group4 = []
    for i in range(0,4):
        Group1 += ([k[i] for k in MATRIX])
    # print(Group1)
    for i in range(4,8):
        Group2 += ([k[i] for k in MATRIX])
    for i in range(8,12):
        Group3 += ([k[i] for k in MATRIX])
    for i in range(12,16):
        Group4 += ([k[i] for k in MATRIX])
    Group1 = random.sample(Group1,len(Group1))
    Group2 = random.sample(Group2, len(Group2))
    Group3 = random.sample(Group3, len(Group3))
    Group4 = random.sample(Group4, len(Group4))
    return Group4 + Group3 + Group2 + Group1

def WindowMiddleAisle (MATRIX):
    WINDOW = []
    MIDDLE = []
    AISLE = []
    for idx,i in enumerate(MATRIX):
        if idx == 0 or idx == 5:
            WINDOW += i
        if idx == 1 or idx == 4:
            MIDDLE += i
        if idx == 2 or idx == 3:
            AISLE += i
    WINDOW = random.sample(WINDOW,len(WINDOW))
    MIDDLE = random.sample(MIDDLE,len(MIDDLE))
    AISLE = random.sample(AISLE,len(AISLE))
    return WINDOW + MIDDLE + AISLE
def SteffenPerfect(MATRIX):
    WINDOW = []
    MIDDLE = []
    AISLE = []
    for idx,i in enumerate(MATRIX):
        if idx == 0 or idx == 5:
            WINDOW += i
        if idx == 1 or idx == 4:
            MIDDLE += i
        if idx == 2 or idx == 3:
            AISLE += i
    numbers = []
    lst = []
    for i in WINDOW:
        if i[0] % 6 == 1 and i[0] % 12 == 7:
            lst.append(i)
    lst = lst [::-1]
    numbers += lst
    lst = []

    for i in WINDOW:
        if i[0] % 6 == 4 and i[0] % 12 == 10:
            lst.append(i)
    lst = lst [::-1]
    numbers += lst
    lst = []

    for i in WINDOW:
        if i[0] % 6 == 1 and i[0] % 12 == 1:
            lst.append(i)
    lst = lst[::-1]
    numbers += lst
    lst = []
    for i in WINDOW:
        if i[0] % 6 == 4 and i[0] % 12 == 4:
            lst.append(i)
    lst = lst[::-1]
    numbers += lst
    lst = []
    for i in MIDDLE:
        if i[0] % 6 == 2 and i[0] % 12 == 8:
            lst.append(i)
    lst = lst[::-1]
    numbers += lst
    lst = []
    for i in MIDDLE:
        if i[0] % 6 == 5 and i[0] % 12 == 11:
            lst.append(i)
    lst = lst [::-1]
    numbers += lst
    lst = []
    for i in MIDDLE:
        if i[0] % 6 == 2 and i[0] % 12 == 2:
            lst.append(i)
    lst = lst[::-1]
    numbers += lst
    lst = []
    for i in MIDDLE:
        if i[0] % 6 == 5 and i[0] % 12 == 5:
            lst.append(i)
    lst = lst[::-1]
    numbers += lst
    lst = []
    for i in AISLE:
        if i[0] % 6 == 0 and i[0] % 12 == 0:
            lst.append(i)
    lst = lst[::-1]
    numbers += lst
    lst = []
    for i in AISLE:
        if i[0] % 6 == 3 and i[0] % 12 == 9:
            lst.append(i)
    lst = lst [::-1]
    numbers += lst
    lst = []

    for i in AISLE:
        if i[0] % 6 == 0 and i[0] % 12 ==6:
            lst.append(i)
    lst = lst[::-1]
    numbers += lst
    lst = []
    for i in AISLE:
        if i[0] % 6 == 3 and i[0] % 12 == 3:
            lst.append(i)
    lst = lst[::-1]
    numbers += lst
    return numbers

def SteffenModified(MATRIX):
    seats = []
    MATRIX2 = MATRIX[3:]
    lst = []
    for i in range(15,-1,-2):
        lst  += ([k[i] for k in MATRIX[:3]])
    lst = random.sample(lst,len(lst))
    seats += lst
    lst = []
    for i in range(15,-1,-2):
        lst += ([k[i] for k in MATRIX2[::-1]])
    lst = random.sample(lst,len(lst))
    seats += lst
    lst = []
    for i in range(14,-1,-2):
        lst += ([k[i] for k in MATRIX[:3]])
    lst = random.sample(lst,len(lst))
    seats += lst
    lst = []
    for i in range(14,-1,-2):
        lst += ([k[i] for k in MATRIX2[::-1]])
    lst = random.sample(lst,len(lst))
    seats += lst
    lst = []
    return seats
def SteffenModified2(MATRIX):
    seats = []
    MATRIX2 = MATRIX[3:]
    for i in range(15,-1,-2):
        seats += ([k[i] for k in MATRIX[:3]])
    for i in range(15,-1,-2):
        seats += ([k[i] for k in MATRIX2[::-1]])
    for i in range(14,-1,-2):
        seats += ([k[i] for k in MATRIX[:3]])
    for i in range(14,-1,-2):
        seats += ([k[i] for k in MATRIX2[::-1]])
    return seats
def Random(MATRIX):
    seats = []
    for i in MATRIX:
        seats += i
    seat = random.sample(seats,len(seats))
    return seat
def test(MATRIX):
    column = []
    lst = []
    column += [i[0] for i in MATRIX]
    for i in [3,2,4,1,5,0]:
        lst.append(column[i])
    return lst

