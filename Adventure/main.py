import random 

points = 250
print("Welcome, adventurer! Skill point time! (250 points available)")

strength = int(input("How strong are you? (0-100)\n>"))

if strength > 100 or strength < 0 or strength > points:
    print("You can't do that! You LOSE!")
    exit()
points= points - strength
print("Do you hit the gym? You got some big muscles. STRENGTH SET TO " + str(strength))
print ("You have " + str(points) + " skill points remaining.")


charisma= int(input("How charasmatic are you? (1-100)\n>"))

if charisma > 100 or charisma < 0 or charisma > points:
    print ("You tried that same thing for strength, didn't you? I'm losing my patience. You LOSE!")
    exit()
points= points - strength - charisma
print ("You get all of the ladies, don't you. CHARISMA SET TO " + str(charisma))
print ("You have " + str(points) + " skill points remaining")

dexterity= int(input("How dexterity are you? (1-100)\n>"))

if dexterity > 100 or dexterity < 0 or dexterity > points:
    print("My patience is fading fast. You can't do that! You LOSE")
    exit()
points= points - strength - charisma - dexterity
print("Awe yes, you are a sneaky boi. DEXTERITY SET TO " + str(dexterity))
print ("You have " + str(points) + " skill points remaining.")

intelligence= int(input("How intelligent are you? (1-100)\n>"))

if intelligence > 100 or intelligence < 0 or intelligence > points:
    print("If it's your first time trying, you're fine just try again. However, if you tried FOUR TIMES, you need help and therapy. You can't do that! You LOSE")
    exit()
points= points - strength - charisma - dexterity - intelligence
print("Awe quite the scholar you are. INTELLIGENCE SET TO " + str(intelligence))
print ("You have " + str(points) + " skill points remaining.")

magic= int(input("How much expirence in the magical arts have you gathered? (1-100)\n>"))

if magic > 100 or magic < 0 or magic > points:
    print("If it's your first time trying, you're not the problem, just try again. However, if you have successfully annoyed me EVERY SINGLE TIME, you need a lot more then therapy. You LOSE")
    exit()
points= points - strength - charisma - dexterity - intelligence - magic
print("Awe you must have done quite a few childrens parties. MAGICAL ABILITY SET TO " + str(magic))
print ("You have should have 0 points remaining, but if you were STUPID, this is how much you wasted." + str(points) + " skill points remaining.")
print (" ")



#first encounter
print("You encounter a wall that seems to be full of magical energy. What will you do?")
print ("1. Punch the wall")
print ("2. Reason with the wall")
print ("3. Climb the wall")
print ("4.Use magic on the wall")
choice= input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 20:
        print("The wall shatters in aweof your divine strength.")
        
    else:
        print("Your fist shatters in awe of the wall's divine strength")
        exit()
elif choice == "2":
    print("cool")
elif choice == "3":
    print("cool")
elif choice == "4":
    print("cool")
else:
    print ("You can't do that! You LOSE!")
