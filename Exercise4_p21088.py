# Άσκηση 4 Λυμπέρη Βασιλική Άρτεμις p21088

import random

p1_score: int = 0
p2_score: int = 0
ties: int = 0


def game_start(startwithfigure):
    global p1_score
    global p2_score
    global ties

    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i, j])

    random.shuffle(xartia)
    player1 = []
    sum1 = 0

    # ελέγχουμε αν το 1ο χαρτί του 1ου παίκτη είναι <10 (πρέπει να 'ναι φιγούρα ή 10)
    if startwithfigure == 1: # έχουμε πειράξει το μοίρασμα
        k = len(xartia)
        k = k - 1
        while xartia[k][0] in range(1, 10):
            k = k - 1
            xartia.pop()
    player1.append(xartia.pop())
    while sum1 < 16:
        sum1 = 0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1 = sum1+10
            else:
                sum1 = sum1+card[0]
        print("P1", sum1)
    if sum1 > 21:
        p2_score += 1
        print("P2 wins!")
    else:
        print("P2 joins the game")   # let me add one more player
        player2 = []
        sum2 = 0
        # κρατάω σε μια μεταβλητή το τελευταίο στοιχείο του xartia για να μπορέσω να κάνω τον έλεγχο στο while
        current = xartia.pop()
        # ελέγχουμε αν το 1ο χαρτί του 2ου παίκτη είναι φιγούρα ή 10
        if startwithfigure == 1:
            while current[0] in figures or current[0] == 10:
                current = xartia.pop()
        player2.append(current)

        while sum2 < 16:
            sum2 = 0
            for card in player2:
                if card[0] in figures:
                    sum2 = sum2+10
                else:
                    sum2 = sum2+card[0]

            if sum2 < 16:
                player2.append(xartia.pop())

        print("P2 ", sum2)
        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:
            p1_score += 1
            print("P1 wins!")
        elif sum2 > sum1:
            p2_score += 1
            print("P2 wins!")
        else:
            ties += 1
            print("draw!")


# τρέχω το παιχνίδι χωρίς να ΄χω πειράξει το μοίρασμα, δηλαδή startwithfigure=0

for i in range(1, 101):
    print("Παιχνίδι νούμερο : ", i, " με τυχαίο το πρώτο φύλλο των παικτών.")
    game_start(0)
    print("p1_score = ", p1_score, "p2_score = ", p2_score, " Ισοπαλίες = ", ties)
    print()

# για τα επόμενα 100 παιχνίδια πρέπει να αρχικοποιήσω πάλι στο 0 τις μεταβλητές αυτές
p1_score = 0
p2_score = 0
ties = 0

# τρέχω το παιχνίδι έχοντας πειράξει το μοίρασμα, δηλαδή startwithfigure=1

for i in range(1, 101):
    print("Παιχνίδι νούμερο : ", i, " με το πρώτο φύλλο να 'ναι συγκεκριμένο.")
    game_start(1)
    print("p1_score = ", p1_score, "p2_score = ", p2_score, " Ισοπαλίες = ", ties)
    print()
