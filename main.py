# print("Welcome to the Band Name Generator")
# name = input("what is the name of the city you grew up ?")
# city = input("what is the love music group name? ")
# print("you are a " + name + "ish" + city)
#
# print(len(input("what is you name? ")))

# a = 10
# b = 20
#
# print( +  a + "b = " + b )
#
# c = a
# a = b
#
# b = c
#
# print("a = " + a + "b = " + b )
# ---------------------------------------------------------------------------

# number = input("what is you number: ")
#
# print(len(number))
#
# numbers = int(848545454584)
# print(len(numbers))

# numberChar = len(input("what is your name; "))
# print("tour name has " + str(numberChar) + " characters")
# ----------------------------------------------------------------------------
# print("welcome to the tip calculator")
# total = input("what was total bill? ")
# people = input("how many people to split the bill? ")
# tip = input("what percentage tip you want to pay 10, 12 or 15? ")
# if tip == 10:
#     tip = total * tip / 100
# elif tip == 12:
#     tip == total * tip / 100
# elif tip == 15:
#     tip == total * 15 / 100
# else:
#     print("tip is not defined ")
#
#
# print("every person should pay: ", int(total) / int(people) + (int(tip) / 5))

# ----------------------------------------------------------------------------

# number = input("enter two digit number: ")
# print(int(number[0]) + int(number[1]))

# ----------------------------------------------------------------------------
# import math
#
# weight = input("enter your wieght(kg): ")
# height = input("enter your height(cm): ")
# result = (float(weight) / (int(height) ** 2)) * 10000
# print("your BMI is :" + str(math.floor (result)))
#
# if result > 30:
#     print("you are obesity!!! loose some weight")
# elif result < 30 and result > 28:
#     print("you are overweight! lose a little weight")
# elif result < 28 and result > 20:
#     print("Congrats! you are normal ( :")
# else:
#     print("you are underweight, gain some weight!!!!!")

# ----------------------------------------------------------------------------

# name = input("whats yor name: ")
# height = input("how long are you: ")
#
# print(f"Hello {name} and you are {height} years old, which is great!!! congrats ")

# ----------------------------------------------------------------------------

# totalYears = 65
# totalMonth = 780
# totalWeeks = 3120
# totalDays = 23725
#
# yearsOld = int(input("how old are you? "))
#
# dayOld = totalDays - (yearsOld * 365)
# weekOld = totalWeeks - (yearsOld * 12 * 4)
# monthOld = totalMonth - (yearsOld * 12)
#
#
#
# print(f"yoy have {dayOld} days, {weekOld} weeks and {monthOld} month remain")


# ----------------------------------------------------------------------------

# weekDay = int(input("enter the number of the day of the week: "))
# if weekDay > 7 or weekDay < 1:
#     print("your day number is not valid! try again")
# elif weekDay % 2 == 0:
#     print("the day is even")
# else:
#     print("the day is odd")

# ----------------------------------------------------------------------------

# totalAmount = 0;
#
# print("Welcome to pizza bakery of Mehrdadioni!!!")
#
# print('small pizza: $15 ')
# print('medium pizza: $15 ')
# print('large pizza: $15 ')
#
# pizzaSize = input("what size of pizza do you want? 'S' for small 'M' for medium, 'L' for large? ")
#
# if pizzaSize == "S":
#     totalAmount += 15
# elif pizzaSize == "M":
#     totalAmount += 20
# elif pizzaSize == "L":
#     totalAmount += 25
# else:
#     print("please enter just a letter between S, M and L")
#
# pepperoni = input(
#     "do you want to add pepperoni for the pizza? adding pepperoni cost +$2, if yes press 'Y' or No press 'N'")
# if pepperoni == "Y":
#     if pizzaSize == "M":
#         totalAmount += 2
#     else:
#         totalAmount += 3
#
# extraCheeze = input("Do you want extra cheeze for your pizza? if yes press 'Y' if not press 'N'")
# if extraCheeze == "Y":
#     totalAmount += 1
# else:
#     totalAmount += 0
#
# print(f"you want a pizza and total amount equal to: {totalAmount}")

# ----------------------------------------------------------------------------

# myName = input("what is you name: ")
#
# herName = input("what is her name? ")
#
# print(f"my name is: {myName} and her name is: {herName}")
#
# nameString = myName + herName
#
# nameString.lower()
#
# t = nameString.count("t")
# r = nameString.count("r")
# u = nameString.count("u")
# e = nameString.count("e")
#
# true = t + r + u + e
#
# l = nameString.count("l")
# o = nameString.count("o")
# v = nameString.count("v")
# e = nameString.count("e")
#
# love = l + o + v + e
#
# loveScore = str(true) + str(love)
#
# print(loveScore)


# ----------------------------------------------------------------------------

# print("Welcome to treasure nightClub")
# theWay = input("which way do you choose after entering to treaure building? 'left' or 'right': ").lower()
# if theWay == 'right':
#     print("you exit from the treaure and loose all pussies! GameOver")
# else:
#     door = input("OK, you go through to way and see 3 door! which one color door you will choose? 'red', 'blue' or 'yellow' ").lower()
#     if door == "red":
#         print("you get into the fire!!! GameOver...")
#     elif door == "blue":
#         print("you catched by a big black dick... Oh... GameOver")
#     elif door == "yellow":
#         print("Yaaaaay you catch a juicy pussy YAAAAY!!!! Good guess and have fun with that💕💕")

# ----------------------------------------------------------------------------

# import random
#
# talPale = int(input('give me you want tale or pale? 1 for tale and 2 for pale '))
# talePalernd = random.randint(1, 2)
#
# if talPale == talePalernd:
#     print("YAY you guess right")
# else:
#     print("Oh No you were wring!")

# ----------------------------------------------------------------------------

# us_state = ["delaware", "california", "New york"];
#
# print(us_state)
#
# us_state.append("Texas")
#
# print(us_state)
#
# us_state.extend(["Utah", "montana"])
#
# print(us_state)
#
# us_state.remove("Texas")
# print(us_state)

# ----------------------------------------------------------------------------
# import random
#
# names = input("enter name of the treats and seperating names bu comma: ")
# name = names.split(", ")
#
# numberOfPoeple = len(name)
# rndPoeple = random.randint(1, numberOfPoeple -1)
# rndHelper = random.choice(name);
# print(f"{name[rndPoeple]} is going to pay the bill and {rndHelper} is help him/her")

# ----------------------------------------------------------------------------
#
# treasure = "🪙"
#
# row1 = ["✅", "✅", "✅"]
# row2 = ["✅", "✅", "✅"]
# row3 = ["✅", "✅", "✅"]
# table = [row1, row2, row3]
# table[1][1] = treasure
#
# print(f"{row1} \n{row2} \n{row3}")

# ----------------------------------------------------------------------------

import random

print("welcome to the rock scissors paper Game...")
guess = int(input("choose one: 0 for rock, 1 for scissors and 2 for paper: "))

rockSign = "🤏 "
scissorsSign = "✌️ "
paperSign = "🖐️"

cpuGuess = random.randint(0, 2)

if guess == 0 and cpuGuess == 0:
    print(f"you: {guess} {rockSign} \ncpu: {cpuGuess} {rockSign} \ndraw")
elif guess == 1 and cpuGuess == 1:
    print(f"you: {guess} {scissorsSign} \ncpu: {cpuGuess} {scissorsSign} \ndraw")
elif guess == 2 and cpuGuess == 2:
    print(f"you: {guess} {paperSign} \ncpu: {cpuGuess} {paperSign} \ndraw")
elif guess == 0 and cpuGuess == 1:
    print(f"you: {guess} {rockSign} \ncpu: {cpuGuess} {scissorsSign} \nyou win")
elif guess == 0 and cpuGuess == 2:
    print(f"you: {guess} {rockSign} \ncpu: {cpuGuess} {paperSign} \ncpu win")
elif guess == 1 and cpuGuess == 0:
    print(f"you: {guess} {scissorsSign} \ncpu: {cpuGuess} {rockSign} \ncpu win")
elif guess == 1 and cpuGuess == 2:
    print(f"you: {guess} {scissorsSign} \ncpu: {cpuGuess} {paperSign} \nyou win")
elif guess == 2 and cpuGuess == 0:
    print(f"you: {guess} {paperSign} \ncpu: {cpuGuess} {rockSign} \nyou win")
elif guess == 2 and cpuGuess == 1:
    print(f"you: {guess} {paperSign} \ncpu: {cpuGuess} {scissorsSign} \ncpu win")











