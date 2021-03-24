print("Новые блюда")
amountOfFood = int(input())
recipes = []
doneRecipes = []
for i in range(amountOfFood):
    recipes.append(input())
    doneRecipes.append(False)
amountOfDays = int(input())
for i in range(amountOfDays):
    amountOfFoodDone = int(input())
    for j in range(amountOfFoodDone):
        food = input()
        for k in range(amountOfFood):
            if food == recipes[k]:
                doneRecipes[k] = True
for i in range(amountOfFood):
    if not doneRecipes[i]:
        print(recipes[i])