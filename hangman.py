import random

# Lijst van woorden om te raden
woorden = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

# Kies willekeurig een woord uit de lijst
gekozen_woord = random.choice(woorden)
woord_weergave = ['_' for _ in gekozen_woord]  
pogingen = 8  


print("Welkom bij Galgje!")


while pogingen > 0 and '_' in woord_weergave:
    print("\n" + ' '.join(woord_weergave))
    gok = input("Raad een letter: ").lower()


    # Controleer of de geraden letter in het gekozen woord zit
    if gok in gekozen_woord:
        for index, letter in enumerate(gekozen_woord):
            if letter == gok:
                woord_weergave[index] = gok  # laat het letter zien als die goed is


    else:
        print("Die letter komt niet voor in het woord.")
        pogingen -= 1


# Spelafsluiting
if '_' not in woord_weergave:
    print("Je hebt het woord geraden!")
    print(' '.join(woord_weergave))
    print("Je hebt overleefd!")


else:
    print("Je hebt geen pogingen meer. Het woord was: " + gekozen_woord)
    print("Je hebt verloren!")