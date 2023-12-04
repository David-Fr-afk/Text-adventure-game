# Name and age
import random
name = input("What is your name? ")
age = int(input("What is your age? "))


print("Hello, " + name + ". You are " + str(age) + " years old.")

# User's health
health = 10
print("You're starting with", health, "health.")

#death counter
death  = 0

# Abilities
patience = 0
knowledge = 0
options = 0
intimidation = 0
cowardice = 0
confidence = 0

# Loop that checks the user's health
while health > 0:

    # If loop to perform an action when the user's health goes below 0
    if health < 0:
        print(name, "you have failed your kingdom, and your blade. TRY AGAIN.")
        death += 1

    # Story
    print("It's medieval times, and you're relaxing at home, sharpening your blade when you hear a knock, this blade is your most prized possesion, passed down from your father. This was before the war....before his death.")
    print("You live in a small village, Caltadia, with your mother. When suddenly, the higher elves priest contacts you...")
    print("Good day, fellow traveler. You, " + name + ", have been found by the great elves to be in possession of a mystical weapon known as the ")
    special_blade = input("Choose a name for your special blade: ").lower()
    if any(word in special_blade for word in ["dangerous", "strong", "deadly", "powerful", "jagged", "rough", "bloody"]):
        print("Wow, that's a scary weapon, says the priest. +3 intimidation\n")
        intimidation += 3
    print("The priest continues... Now, we could take this blade by force, but your fate is sealed to that weapon. If the blade dies, you die. If the blade is hurt, you get hurt. Therefore, it only makes sense for you to weild it. Now,")

   

    # Checking user's age
    if age >= 18:
        wants_to_play = input("Do you want to start your journey? ").lower()
        if wants_to_play == "yes":
            print("Let's start!\n")
            print("NOTE: when starting your journey certain actions will gain you things like confidence, patience, etc. Doing this will unlock certain paths and allow you to do different things. Keep that in mind.\n ")

            # More history, what needs to be done.
            print("Now, with the great power of the " + special_blade + ", we need you to stop the war between the evil orcs and heavenly high elves.")
            print("In order to do this, you need to infiltrate the orc's castle.")
            print("NOTE: Attacking the evil orcs will put you in the kingdom's favor, while attacking the high elves will put you at battle with the kingdom.")

            # Giving the user options
            # Option 1
            orc_or_elves = input("Now, with the great power of the " + special_blade + ", go forth... make a choice... (orc) or (elves): ")

            # The orcs' path
            if orc_or_elves == "orc":
                # Option 2
                print("You have infiltrated the orc's kingdom; you see two possible entrances...")
                path1 = input("(loud) Through the front gate, or through the roof (silent): ")

                # The first way of getting to the orc boss, loud and undetected
                # NOTE: THIS IS INCOMPLETE, I WANT TO FINISH THE SILENT PART FIRST
                if path1 == "loud":
                    print("You went through the front gate and encountered 4 heavily armored orcs.")
                    attack1 = input("How do you attack? (ST) sword throw, (DS) devastating slice, or (IT) intimidate: ")
                    if attack1 == "ST":
                        print("Your attack worked, killing all 4 orcs in one throw, but one of the orcs had the same idea and hit you with a dull blade.")
                        health -= 2
                        print("After the chaos of battle, you begin to have strong flashbacks.")
                    elif attack1 == "DS":
                        print("You sliced through all 4 orcs in one hit.")
                        print("After the chaos, you begin to feel remorse, not knowing why...")
                    elif attack1 == "IT":
                        if intimidation > 3:
                            print("You successfully intimidated the orcs away.")
                        else:
                            print("You failed and were sliced, but decided to rush through anyways.")
                            health -= 5

                # Silent method, involves many different ways to attack, easter egg, and a quick run to the boss.
                elif path1 == "silent":
                    print("You managed to climb onto the roof. You see a sunroof, when looking inside You see the dining hall with 2 enchanted armored orcs.")
                    exit = False
                    # A for loop so the attempt to investigate twice is actually possible
                    while exit == False:
                        attack2 = input("How do you attack, (SF) through sunroof or (IV) investigate options: ")
                        #silent sunroof method, this eventually leads into 2 methods
                        if attack2 == "SF":
                            exit = True
                            print("You jump through the sunroof in a blaze of glory, killing both orcs. Sadly, you're covered in glass. -3 health.")
                            health -= 3
                            confidence += 1
                            map = input("On the table, you find a piece of paper. (p)ick it up, (l)eave it: ")
                            if map == "p":
                                # MAP method of getting to the orc
                                print("You have picked up the map and find yourself with immense energy. You also instantly know the")
                                print("entire castle's outline. You have gained the power of KNOWLEDGE.")
                                knowledge += 1
                                print("Using the map, you immediately find that the orc boss is simply in the sewer... After sneaking around, you find the staircase to the sewer.")
                                disguise = input("Do you... (g)o down, or (d)isguise yourself then go: ")

                                # MAP method where disguise isn't used
                                if disguise == "g":
                                    print("After going down the stairs, you find the Orc king protected by all the castle's guards. They all charge at you.")
                                    nothingelse = input("What do you do? (c)url up in a ball or (f)ight to the death: ")
                                    # if the user chooses to give up, they will recieve one cowardice, if the user chooses to fight, they will gain confidence.
                                    if nothingelse == "c":
                                        cowardice += 1
                                    if nothingelse == "f":
                                        confidence += 1
                                    if nothingelse == "c" or "f":
                                        print("As the coming guards attempt to surround you, you feel your blade begin to shake. Suddenly, your blade gains sentience. It begins to slice through all the guards, killing them violently. Health:", health)
                                        health -= 2
                                        print("The", special_blade, "gives you its backstory, that it was created by the king orc your trying to fight, before the war, your blade was able to escape into your fathers hand. The king orc found your father, and killed him, but before the king orc could steal his blade your father passed it down to your mom, which then she evntually gave to you.")
                                        print("After defeating the gaurds, your face to face with the king orc, his muddy body towers over you")
                                        #last choice for map route
                                        last_act = input("How do you finish the job..... (b)attle, (k)ill").lower()
                                        #different endings for how you kill him
                                        
                                        if last_act == "k" and confidence == 2:
                                            print("You kill the king orc, gruesomly. Without giving him a chance to fight you run to him, slice his neck, and let his organs and blood slip into the sewer. You win but at what cost. You become feared by the people of you village, your given opportunity to serve the high elves in the massacre the rest of the orcs. You accept, killing every last one in the name of your father")
                                        if last_act == "k" and confidence == 1 and cowardice == 1:
                                            print("As you face the king orc, you run behind him and grab a hold of his neck.....but you hesitate, eventually letting him go, and walking away. Knowning you could kill him was enough for you. Although the high elves werent satisifed, they accepted your win over the king orc as his defenses were immedatily weakned. You live a long, old life. Wondering how things couldve went differently, and if this is what your father would have truly wanted. You bury the sword, hoping no one would have to weild such power ever again.")
                                        if last_act == "b" and confidence == 1:
                                            print("You attempt to convince the orc, during the battle, you gain the upper hand thanks to the sentience of the blade. During the fight the king orc apologizes for the death of your father, THE KING ORC THEN USES this moment of weakness on your side to deliver the leading blow.....your life begins to flash, your parents, your father....you remeber how hard you fought to get to the orc....With the power of confidence you are shocked back to reality, where you give the final deadly blow to the king orc. Ruining his kingdom...and avenging your father")
                                            print("\nAfter killing the king orc, your renowed as a hero, and a medal of honour is bestowed unto you from the high elves. As time goes, you grow old, living a happy life with kids and a beatiful wife. You pass the blade down to your children, hoping one day the blade will protect them as it protected you.")
                                        if last_act == "b" and cowardice == 1:
                                            print("You attempt to convince the orc, during the battle, you gain the upper hand thanks to the sentience of the blade. During the fight the king orc apologizes for the death of your father, the orc uses this moment of weakness on your side to deliver the leading blow.....your life begins to flash, your parents, your father....\nyou remeber how easily you gave up to the weaker orcs earlier....in a instant you dash, running as fast as you can out the kingdom dropping your sword in the process. Your cowardy has saved you, but cursed you. You live a lonely life in the woods, banished from your town, and from the high elv kingdom. A sad end, for a great warrior")
                                        if last_act == "b" and cowardice == 1 and confidence == 1:
                                            print("You attempt to convince the orc, during the battle, you gain the upper hand thanks to the sentience of the blade. During the fight the king orc apologizes for the death of your father, the orc uses this moment of weakness on your side to deliver the leading blow.....your life begins to flash, your parents, your father....\nyou remeber how much confidence you showed at the sunroof, but how much cowardice you showed fighting his earlier minions. With this your shocked back to reality, your flight and fight senses kick in both at once causing you to throw the blade at the king orc killing him, but running away in the process causing you to lose the sword. Your renowed as a hero in the village, and although the high elves despise you for losing the sword you still saved the day. You live a happy life with your mother, consistantly searching new adventures to run towards, or away from.")    
    
                                                
                                            
                                            
                                # Patience route of getting to the orc
                                elif map == "l":
                                    print("You feel a sudden surge of strength. You've gained the power of patience.")
                                    patience += 1

                        elif attack2 == "IV":
                            print("You found nothing.")
                        options += 1
                        exit = True

                    # If the user attempts to investigate more than once, they are given a third way to the orc boss
                    if options == 2:
                        print("Eventually, your investigating pays off. You find a secret underground tunnel.")
                        tunnel = input("Continue? (Y)Yes, (N)No: ").lower()
                        if tunnel == "y":
                            print("You have walked directly into the Orc King's sewer lair. He looks just as disgusting as the people of your village described.")
                            print("He opens his wet, scaly mouth. You see his sharp teeth. He takes a stand and looks over you, towering over you like a fish in his pond.")
                            print("He says... how have you, " + name + ", decided to defeat me, mortal.")
                            last_act = input("(c)onvince, (b)attle: ")
                            if last_act == "c":
                                print("While attempting to talk to the orc, you're filled with a sudden emptiness. Your mind runs dark, and you see the king orc, a younger version. You see him... building the very blade you wield.")
                                last_act2 = input("(i)nquire or (c)ontinue convincing: ")
                                if last_act2 == "i":
                                    print("You ask the orc about this vision; he indeed confirms he is the one that forged that blade.")
                                    # You can add more to this section to create a unique and interesting storyline.

                        elif tunnel == "n":
                            print("You decided not to let your intrigue get the better of you. You gained the power of COWARDICE. COWARDICE + 1")
                            cowardice += 1

# Checking age
    if age >= 14:
        print("You can play, but please bring mommy and daddy to watch!")
    else:
        print("You are not old enough to wield this blade.")