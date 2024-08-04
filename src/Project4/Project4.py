ingredients = ["A", "B", "C", "D"]
points = 0
ingredient = input("Guess the first ingredient: ")
## First trial
if ingredient in ingredients:
    points += 1
    ingredients.remove(ingredient)
    print("Pravo! You did the first question")
else:
    print("You guessed wrong")

##Second trial
ingredient = input("Guess the second ingredient: ")

if ingredient in ingredients:
    points += 1
    ingredients.remove(ingredient)
    print("Pravo! You did the second question")
else:
    print("You guessed wrong")


##Third trial
ingredient = input("Guess the third ingredient: ")

if ingredient in ingredients:
    points += 1
    ingredients.remove(ingredient)
    print("Pravo! You did the third question")
else:
    print("You guessed wrong")

##Print results
print("You scored: "+ str(points))
