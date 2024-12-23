import random

class AICompanion:
    def __init__(self, name="SAPIEN-AI"):
        self.name = name

    def give_hint(self, level):
        hints = {
            1: "Fire can be carried using something sturdy like a branch. Avoid flammable or unsafe options.",
            2: "Tools need to be durable and sharp. What material could fulfill this requirement?",
            3: "A wheel requires a smooth, circular shape to roll efficiently. Think about the best material to shape!",
            4: "You can produce food by cultivating plants with help of tools to plough and can use animals, wheels to make the process faster",
            5: "To make your life easier make something useful from the existing resources",
            6: "for transportation to be easier make something that can move on its own"
        }
        return hints.get(level, "I have no hints for this level.")

def start_game(ai):
    print(f"Welcome to 'The Spark of Evolution'! Your companion is {ai.name}.")
    print("A stormy night. A tree is on fire. Animals are fleeing.")
    print("You are an ape observing the scene.")
    first_decision(ai)

def first_decision(ai):
    action = input("What do you do? (run/investigate): ").lower()
    if action == "run":
        print("You run away like the others, missing the chance for discovery.")
        print("GAME OVER")
    elif action == "investigate":
        print("You cautiously approach the fire, noticing it provides light and scares predators.")
        print("You pick up a burning twig and begin to understand fire's power.")
        fire_challenge(ai)
    else:
        print("Invalid choice. Please choose 'run' or 'investigate'.")
        first_decision(ai)

def fire_challenge(ai):
    print("\nChallenge: How will you carry the fire back to your group?")
    print("Options: [1] Leaves [2] Branch [3] Bare hands")
    print(f"Hint: {ai.give_hint(1)}")
    choice = input("Choose an option (1/2/3): ")
    if choice == "1":
        print("The leaves burn quickly, and the fire is lost. Try again!")
        fire_challenge(ai)
    elif choice == "2":
        print("The branch holds the fire well. You carry it back successfully!")
        print("Congratulations! You've unlocked the first milestone: Fire!")
        tools_challenge(ai)
    elif choice == "3":
        print("Ouch! The fire burns your hands. Try again.")
        fire_challenge(ai)
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        fire_challenge(ai)

def tools_challenge(ai):
    print("\nYou and your group realize fire can cook meat. To hunt better, you decide to create tools.")
    print("Challenge: Which material will you use to create tools?")
    print("Options: [1] Stone [2] Leaves [3] Wood")
    print(f"Hint: {ai.give_hint(2)}")
    choice = input("Choose an option (1/2/3): ")
    if choice == "1":
        print("You use stones to create sharp tools for hunting and protection.")
        print("Congratulations! You've unlocked the second milestone: Tools!")
        wheel_challenge(ai)
    elif choice == "2":
        print("Leaves cannot be shaped into tools. Try again!")
        tools_challenge(ai)
    elif choice == "3":
        print("Wood is helpful but not durable enough for tools. Try again!")
        tools_challenge(ai)
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        tools_challenge(ai)

def wheel_challenge(ai):
    print("\nWith tools, your group becomes more efficient. Now, you aim to move heavy objects easily.")
    print("Challenge: How will you create a wheel?")
    print("Options: [1] Shape a stone into a circle [2] Use a large leaf [3] Stack small stones")
    print(f"Hint: {ai.give_hint(3)}")
    choice = input("Choose an option (1/2/3): ")
    if choice == "1":
        print("You create the first wheel! This invention transforms how you live and work.")
        print("Congratulations! You've unlocked the third milestone: The Wheel!")
        agriculture_challenge(ai)
    elif choice == "2":
        print("A leaf cannot function as a wheel. Try again!")
        wheel_challenge(ai)
    elif choice == "3":
        print("Stacked stones won't roll properly. Try again!")
        wheel_challenge(ai)
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        wheel_challenge(ai)

def agriculture_challenge(ai):
    print('\nAs you have invented the wheel and tools, Now you aim to produce food on your own rather than depending on animals.')
    print('\nChallange:Produce your own food')
    print('\n[1] Get food from trees in the forest [2] Grow plants which give food by using the tools and wheels')
    print(f'Hint: {ai.give_hint(4)}')
    choice = input("choose an option (1/2)")
    if choice=='1':
        print('on continuous retrival of food from forest the resources may deplete. Try again')
        agriculture_challenge(ai)
    elif choice=='2':
        print("You now do agriculture with the help of tools, wheel and cattle animals")
        print("Congratulations! You've unlocked the fourth milestone: Agriculture!")
        #fill
        industrial_challenge_basics(ai)
    else:
        print("Invalid choice. please select 1 or 2")
        agriculture_challenge(ai)
    
def industrial_challenge_basics(ai):
    print("\nYou have acheived farming too now . Next you aim to make your life more comfortable and easy.")
    print("\nChallenge:Make your life more comfortable and easy")
    print("\n[1]Make something new from wheel [2] Make something new from tools")
    print(f'Hint: {ai.give_hint(5)}')
    choice = input("choose an optionn 1/2")
    if choice=='1':
        print("You now can make some machines with the gear.")
        print("congratulations you have made a gear from the wheel. Now make advancements in industrial revolution.")
        #fill
        industrial_challenge_advanced(ai)
    elif choice=='2':
        print("you cant make machines from tools try again!")
        industrial_challenge_basics(ai)
    else:
        print("Invalid choice. please select 1 or 2")
        industrial_challenge_basics(ai)
    
def industrial_challenge_advanced(ai):
    print("\nYou have acheived some advancements in industrial revolution . Next you aim to make your life more comfortable and easy for transport.")
    print("\nChallenge:Make your transport easier")
    print("\n[1]Try to make a boat from the wood [2] Make a engine from the gear and wheel [3]make animals to pull the carts")
    print(f'Hint: {ai.give_hint(6)}')
    choice = input("choose an option 1/2/3")
    if choice=='1':
        print("You now can make a boat from the wood.But on land trasport cannot be acheived by boats Try again!")
        industrial_challenge_advanced(ai)
    elif choice=='2':
        print("You now made an engine which will help for transportation")
        end_game(ai)

def end_game(ai):
    print("\nYou have successfully unlocked the key milestones in human evolution!")
    print("Fire, Tools, and The Wheel have set the foundation for agriculture, industry, and modern technology.")
    print(f"Congratulations, with the help of {ai.name}, you have completed 'The Spark of Evolution'!")
    print("Thank you for playing!")

# Instantiate AI companion and start the game
ai_companion = AICompanion()
start_game(ai_companion)
