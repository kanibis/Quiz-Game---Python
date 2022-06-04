print("Welcome to Quiz Game!")

playing = input("Do you want to play the game? Yes/No ")

print(playing)

if playing.lower() != "yes":
    quit()

score = 0

answer = input("What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the President of India? ")
if answer == "ram nath kovind":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which city is known as the \"Pink City\" of India? ")
if answer.lower() == "jaipur":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of CPU? ")
if answer.lower() == "control processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Where is the Gateway of India located? ")
if answer.lower() == "mumbai":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("When is India's Independence Day celebrated? ")
if answer == "15/08/1947":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You answered " + str(score) + " questions!")
print(f'You answered {score} questions!')
print("You answered {} questions!".format(score))
