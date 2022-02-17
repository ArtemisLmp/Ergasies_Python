# Άσκηση 8 Λυμπέρη Βασιλική Άρτεμις p21088

import random
# from random import randint

rook_victories: int = 0  # πύργος
bishop_victories: int = 0  # αξιωματικός
ties: int = 0  # ισοπαλίες


rows = int(input("Εισάγετε τον αριθμό των γραμμών : "))
cols = int(input("Εισάγετε τον αριθμό των στηλών : "))


def game_start(rows, cols):
    global rook_victories
    global bishop_victories
    global ties
    # generate random integer values
    bishop_x = random.randint(1, cols)
    bishop_y = random.randint(1, rows)
    print("bishop_x =", bishop_x, " bishop_y =", bishop_y)
    rook_x = random.randint(1, cols)
    rook_y = random.randint(1, rows)
    print("rook_x =", rook_x, "   rook_y =", rook_y)

#   def rook_can_take_down_bishop(bishop_x, bishop_y, rook_x, rook_y):
    if rook_y == bishop_y or rook_x == bishop_x:
        rook_victories += 1
        print("Rook wins!!!")
    elif rook_x - bishop_x == rook_y - bishop_y:
        bishop_victories += 1
        print("Bishop wins!!!")
    elif -rook_x + bishop_x == rook_y - bishop_y:
        bishop_victories += 1
        print("Bishop wins!!!")
    else:
        ties += 1
        print("It's a tie")


# Creates a list containing 8 lists, each of 8 items, all set to 0
# rows, cols = (8, 8)
    arr = [["_" for x in range(rows)] for y in range(cols)]

    arr[bishop_x-1][bishop_y-1] = 'B'
    arr[rook_x-1][rook_y-1] = 'R'

    for r in arr:
        for c in r:
            print(c, end=" ")
        print()


for i in range(1, 101):
    print("Παιχνίδι νούμερο :", i)
    print("---------------------")
    game_start(rows, cols)
    print("rook_victories =", rook_victories, ", bishop_victories =", bishop_victories, ", Ισοπαλίες =", ties)
    print()
