from Utils.Constants import ChallengeNumber
from Utils import Printer
from Challenges import AllChallenges

#
# HELLO AND WELCOME TO PYTHON PROGRAMMING CHALLENGES!
#
# I created these challenges for my friends who want to get back into programming but are rusty and need a place to start from!
#
# Your code for each challenge will go in the StartChallenge.py file inside each of the Challenges > Challenge[Number] folders.
# Inside you'll find a function called runChallengeCode, where you'll find a TODO area to put your code in.
#
# Once you're ready to take on the challenges, change the challengeToRun variable below to select which challenge you want to take on.
#
challengeToRun = ChallengeNumber.CHALLENGE_1


Printer.printProgramStart(challengeToRun)
match challengeToRun:
    case ChallengeNumber.CHALLENGE_1:
        # Start Challenge1
        AllChallenges.Challenge1.start()
    case ChallengeNumber.CHALLENGE_2:
        # Start Challenge 2
        print("Todo")
Printer.printProgramEnd()