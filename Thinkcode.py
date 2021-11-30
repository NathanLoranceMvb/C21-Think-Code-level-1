def intro():
    print ("Hello here I will show my top 3 games")

def outro():
    print ("thank you for checking this out hope you check these games out and find somthing fun to play")

def top3():
    print ("My number 3 would be the division 2 because of the action and the nice world building")

def top2():
    print ("My number 2 would be portal 2 its the first game I've played on my pc that I bought myself and its nostalgic and fun")

def top1():
    print ("My favorite game is just cause 3 the base libaration, grappeling and flying around is like no other game.")

print("Hi!")
name = input("What's your name? ")

print("It's nice to meet you,", name)
answer = input("Are you ready to read? ")


if answer == "Yes":
    print("Okay here we go")
    intro()
    top3()
    top2()
    top1()
    outro()
    
else:
    print("Oh no! That makes me sad!")





