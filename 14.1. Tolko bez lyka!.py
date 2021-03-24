print("Только без лука!")
amount = int(input())
recipe = []
for i in range(amount):
    recipe.append(input())
for i in range(len((recipe))):
    if "лук" not in recipe[i] and i!=len(recipe)-1:
        print(recipe[i], ", ", sep="", end="")
    elif "лук" not in recipe[i]:
        print(recipe[i])