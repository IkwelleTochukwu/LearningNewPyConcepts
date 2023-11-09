# ':=' assigns values to variables as part of a larger expression
# the walrus operator is also known as the assignment expression
foods = list()
#while True:
    #food = input("What foods do you like to eat?: ")
    #if food == "quit":
   #     break
  #  foods.append(food)
#print(foods)

# to use the walrus operator:
while food := input("What foods do you like to eat?: "):
    if food == "quit":
        break
    foods.append(food)
print(foods)

