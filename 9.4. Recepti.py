print("Рецепты")
amountOfFood = int(input())
realFood = []
recipes = []
readyRecipes = []
for i in range(amountOfFood):
    realFood.append(input())
amountOfRecipes = int(input())
for i in range(amountOfRecipes):
    recipes.append(input())
    readyRecipes.append(False)
    amountOfNeeded = int(input())
    isEnough = 0
    for j in range(amountOfNeeded):
        food = input()
        for k in range(amountOfFood):
            if food == realFood[k]:
                isEnough += 1
    if isEnough == amountOfNeeded:
        readyRecipes[i] = True
for i in range(amountOfRecipes):
    if readyRecipes[i]:
        print(recipes[i])