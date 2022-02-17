# Άσκηση 5 Λυμπέρη Βασιλική Άρτεμις p21088

filename = input("Δώσε το όνομα του αρχείου:")
# ελέγχει αν το όνομα του αρχείου είναι σωστό
check = False
while check == False:
    try:
        file = open(filename, 'r')
        check = True
    except:
        print("Δεν υπάρχει αρχείο με αυτό το όνομα.")
        print()
        filename = input("Δώσε σωστό όνομα αρχείου:")
text = file.read()
low_letters = text.lower()  # μετατρέπει όλα τα γράμματα σε πεζά

# χωρίζει το κείμενο σε λέξεις, σύμφωνα με το κενό
words = low_letters.split()

# βρίσκει το δημοφιλέστερο στοιχείο μιας λίστας


def most_frequent(lista, i):
    frequent = max(set(lista), key=lista.count)
    print(i, frequent)
    # διαγράφει το ήδη δημοφιλέστερο για να βρει το αμέσως επόμενο
    j = 0
    while j < len(lista):
        if lista[j] == frequent:
            lista.remove(frequent)
        j = j + 1

# οι 10 δημοφιλέστερες λέξεις
print()
print("Οι 10 δημοφιλέστερες λέξεις του κειμένου είναι:")
temp_words = words
for i in range(1, 11):
    most_frequent(temp_words, i)


# βρίσκει τα 2 πρώτα γράμματα κάθε λέξης
two_chars = [x[:2] for x in words]
print()
print("Οι 3 δημοφιλέστεροι συνδυασμοί των 2 πρώτων γραμμάτων είναι:")
for i in range(1, 4):
    most_frequent(two_chars, i)


# βρίσκει τα 3 πρώτα γράμματα κάθε λέξης
three_chars = [x[:3] for x in words]
print()
print("Οι 3 δημοφιλέστεροι συνδυασμοί των 3 πρώτων γραμμάτων είναι:")
for i in range(1, 4):
    most_frequent(three_chars, i)
