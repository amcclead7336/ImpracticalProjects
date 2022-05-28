"""Silly program that creates funny sidekick names"""
import random

OUTPUT = "\033[1;92m{}\033[0m"

def main():
    """Selects a firstname and last name from two tuples and presents
    them to the user. Repeats until user enter exit code"""
    firstnames = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
                  "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
                  'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
                  'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns', 'Cleet',
                  'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
                  'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
                  'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
                  'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
                  'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
                  'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks',
                  'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
                  'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo',
                  'Scratchensniff', 'Scut', "Sid 'The Squirts'", 'Skidmark',
                  'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
                  'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
                  'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

    lastnames = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
                 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
                 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
                 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
                 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt',
                 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine',
                 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck',
                 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
                 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
                 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
                 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer',
                 'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger',
                 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch',
                 'Woolysocks', 'Goodensmith', 'Hoosenater', 'Johnson',
                 'Nettles', 'Overturf', 'Weewax', 'Tippins', 'Winterkorn')

    print("Welcome to the funny sidekick name generator!")

    while True:
        sel_first = random.choice(firstnames)
        sel_last = random.choice(lastnames)

        print()
        print(OUTPUT.format(sel_first + " " + sel_last))

        choice = input("Would you like to run again? (n/Y)\n")
        if choice.lower() in ("exit", "quit", "q", "no", "n"):
            break


if __name__ == "__main__":
    main()
