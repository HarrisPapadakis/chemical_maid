import random   # Για τυχαία επιλογή αριθμών και συμβόλων
import os       # Για καθαρισμό της οθόνης

# Χάρτης για τα 4 σύμβολα τράπουλας
suits = ['\u2665', '\u2666', '\u2663', '\u2660']  # ♥ ♦ ♣ ♠

# Αντιστοίχιση αριθμών με γράμματα προσώπων
faces = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}

# Συνάρτηση καθαρισμού οθόνης (για Windows/Linux)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Συνάρτηση που δημιουργεί και εμφανίζει μια κάρτα
def draw_card():
    number = random.randint(1, 13)     # Αριθμός από 1 έως 13
    suit = random.choice(suits)       # Επιλογή συμβόλου
    value = faces.get(number, str(number))  # Μετατροπή αριθμού σε γράμμα αν χρειάζεται

    # ASCII αναπαράσταση κάρτας
    print("\t\t\t ____________________ ")
    print("\t\t\t|                    |")
    print(f"\t\t\t|   {value:<2}              |")
    print(f"\t\t\t|   {suit:<1}                 |")
    print("\t\t\t|                    |")
    print("\t\t\t|                    |")
    print("\t\t\t|                    |")
    print(f"\t\t\t|        {value:^2}          |")
    print("\t\t\t|                    |")
    print("\t\t\t|                    |")
    print("\t\t\t|                    |")
    print(f"\t\t\t|              {suit:>1}    |")
    print(f"\t\t\t|              {value:>2}   |")
    print("\t\t\t|____________________|")

# Κεντρική ροή προγράμματος
def main():
    while True:
        clear()
        draw_card()
        choice = input("\nΕπόμενη Κάρτα: Ναι (0), Έξοδος (1): ")
        if choice.strip() == '1':
            break

if __name__ == "__main__":
    main()
