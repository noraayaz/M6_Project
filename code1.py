import random

# Slumpa fram 4 siffror (mellan 0 och 3)
random_numbers = [random.randint(0, 3) for _ in range(4)]

attempts = 0
max_attempts = 10

# Gissningsslinga
while attempts < max_attempts:
    # Här kommer vi att ta användarens gissning (kan lämnas tomt just nu)
    
    # Här kommer vi att kontrollera om användarens gissning är korrekt (kan lämnas tomt just nu)
    
    attempts += 1
    
    # Om gissningen är korrekt, vinner spelaren
    if guess == random_numbers:
        print(f"Congratulations! You guessed the correct sequence in {attempts} attempts.")
        break
else:
    # Om spelaren inte gissar rätt inom 10 försök, avslutas spelet
    print(f"Game over! The correct sequence was {random_numbers}.")