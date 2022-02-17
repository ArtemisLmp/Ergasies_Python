# Άσκηση 2 Λυμπέρη Βασιλική Άρτεμις p21088

import random

mov = 0  # κρατάει τις κινήσεις κάθε παιχνιδιού μέχρι να σχηματιστεί τρίλιζα ή να τελειώσουν τα καπάκια
totalmoves = 0  # κρατάει το άθροισμα των κινήσεων για τα 100 παιχνίδια
winner = -1  # γίνεται 1 όταν σχηματιστεί τρίλιζα

# Ελέγχει αν σχηματίστηκε τρίλιζα είτε οριζόντια είτε κατακόρυφα είτε διαγώνια και αν έχει γίνει
# τρίλιζα, θέτει τη μεταβλητή WINNER ίση με 1 και τυπώνει πού σχηματίστηκε η τρίλιζα


def check_winner(arr):
    global winner
    global mov

    if ((arr[0][0] == arr[0][1] == arr[0][2]) and arr[0][0] != 0) \
            or (arr[0][0] == 1 and arr[0][1] == 2 and arr[0][2] == 3):
        winner = 1
        print("ΤΡΙΛΙΖΑ 1η ΓΡΑΜΜΗ")
    elif ((arr[1][0] == arr[1][1] == arr[1][2]) and arr[1][0] != 0) \
            or (arr[1][0] == 1 and arr[1][1] == 2 and arr[1][2] == 3):
        winner = 1
        print("ΤΡΙΛΙΖΑ 2η ΓΡΑΜΜΗ")
    elif (arr[2][0] == arr[2][1] == arr[2][2] and arr[2][0] != 0) \
            or (arr[2][0] == 1 and arr[2][1] == 2 and arr[2][2] == 3):
        winner = 1
        print("ΤΡΙΛΙΖΑ 3η ΓΡΑΜΜΗ")
    elif (arr[0][0] == arr[1][0] == arr[2][0] and arr[0][0] != 0) \
            or (arr[0][0] == 1 and arr[1][0] == 2 and arr[2][0] == 3):
        winner = 1
        print("ΤΡΙΛΙΖΑ 1η ΣΤΗΛΗ")
    elif (arr[0][1] == arr[1][1] == arr[2][1] and arr[0][1] != 0) \
            or (arr[0][1] == 1 and arr[1][1] == 2 and arr[2][1] == 3):
        winner = 1
        print("ΤΡΙΛΙΖΑ 2η ΣΤΗΛΗ")
    elif (arr[0][2] == arr[1][2] == arr[2][2] and arr[0][2] != 0) \
            or (arr[0][2] == 1 and arr[1][2] == 2 and arr[2][2] == 3):
        winner = 1
        print("ΤΡΙΛΙΖΑ 3η ΣΤΗΛΗ")
    elif (arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0] != 0) \
            or (arr[0][0] == 1 and arr[1][1] == 2 and arr[2][2] == 3):
        winner = 1
        print("ΤΡΙΛΙΖΑ 1η ΔΙΑΓΩΝΙΟΣ")
    elif (arr[0][2] == arr[1][1] == arr[2][0] and arr[0][2] != 0) \
            or (arr[0][2] == 1 and arr[1][1] == 2 and arr[2][0] == 3):
        winner = 1
        print("ΤΡΙΛΙΖΑ 2η ΔΙΑΓΩΝΙΟΣ")


def game_start(win, moves):
    global arr
    global taps
    global winner
    global totalmoves
    global mov

    winner = win
    mov = moves
    # ο πίνακας με τα 27 καπάκια, 9 για το small(=1), 9 για το medium(=2), 9 για το large(=3)
    taps = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    # ο πίνακας 3*3 (9 τετράγωνα)
    arr = [[0 for x in range(3)] for y in range(3)]

    random.shuffle(taps)
    print("Αρχικός Πίνακας")
    for r in arr:
        for c in r:
            print(c, end=" ")
        print()

    # όσο δεν έχει σχηματιστεί τρίλιζα και όσο υπάρχουν ακόμα καπάκια αφαιρεί κάθε φορά
    # το τελευταίο καπάκι και το τοποθετεί σε τυχαία θέση του 3x3 πίνακα
    while winner == -1 and taps:
        #  random.shuffle(taps) αν θέλουμε να ανακατέψουμε ξανά τον πίνακα
        current = taps.pop()        # αφαιρεί το τελευταίο στοιχείο του πίνακα με τα καπάκια

        # print("inside while mov = ", mov, " cur = ", current, " winner = ", winner)
        x = random.randint(0, 2)    # επιλέγει τυχαία την γραμμή του πίνακα
        y = random.randint(0, 2)    # επιλέγει τυχαία τη στήλη του πίνακα

        # ελέγχει αν το τετράγωνο είναι άδειο ή αν υπάρχει καπάκι μικρότερου μεγέθους κι αν ναι, τοποθετεί το current
        if arr[x][y] == 0 or arr[x][y] < current:
            arr[x][y] = current

        mov += 1  # αυξάνουμε τις κινήσεις κατά 1
        check_winner(arr)  # μετά από κάθε κίνηση ελέγχουμε αν σχηματίστηκε τρίλιζα

    print("Τελικός Πίνακας μετά από ", mov, " κινήσεις:")

    for r in arr:
        for c in r:
            print(c, end=" ")
        print()

    totalmoves += mov


for i in range(1, 101):
    print("----------- Παιχνίδι νούμερο :", i, "-----------")
    game_start(-1, 0)

print("TotalMoves = ", totalmoves)
print("Average = ", totalmoves/100)
