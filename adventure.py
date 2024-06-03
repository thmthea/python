import random

# gets users name & welcomes them
name = input("What is your name? ")
print(f'\nWelcome to Eldoria {name}, its another day another morning and time for you to make your journey to the city.')

#event 1:
print("\nAs you step out of your cozy village cottage, you encounter Jupiter, a curious villager known for asking unusual questions. Jupiter notices your departure and approaches you with a quizzical expression. \n\n\"Hey there! Where are you headed today?\" Jupiter asks, curiosity gleaming in his eyes.")
print("\nYou pause for a moment, considering how much information you want to share with Jupiter:")
print("a. Tell Jupiter your destination honestly.")
print("b. Give Jupiter a vague answer, not wanting to reveal too much.")
print("c. Brush Jupiter's question and continue on your way.")

#prompt user for valid input only
event1 = input("What do you do? ")
while event1 != 'a' and event1 != 'b' and event1 != 'c':
    event1 = input("What do you do? ")

#branch 1:
if event1 == 'a':
    print("\nYou decide to tell Jupiter your destination honestly. He nods understandingly and wishes you luck on your journey, offering you a small trinket for good fortune.")
elif event1 == 'b':
    print("\nYou choose to give Jupiter a vague answer, not wanting to reveal too much about your plans. He raises an eyebrow but doesn't press further, instead offering you a mysterious map he found in the village square.")
else:
    print("\nYou brush off Jupiter's question, not wanting to engage in small talk. He looks slightly hurt by your dismissal but shrug it off, muttering something about rude adventurers under their breath. You ignore Jupiter and walk away without acknowledging him further. As you continue on your journey, you feel a sense of unease gnawing at the back of your mind, as if you've missed out on an important opportunity.")

#event 2:
print("\nAs you continue your quest, you stumble upon a treacherous ravine blocking your path. However, the portal to the city is on the other side.")
print("\nHow do you cross the ravine?")
print("a. Try to jump across.")
print("b. Look for a safer route around.")

#prompt user for valid input only
event2 = input("What do you do? ")
while event2 != 'a' and event1 != 'b':
    event2 = input("What do you do? ")

#branch 2:
i = random.randint (0, 1)

if event2 == 'a':
    if i == 0:
        print("\nOh no! You fall down and sprain your ankle! Thank god nothing broke, however, now you have to make a detour to the portal. You hobble your way and find a set of winding stairs up to the other side where he portal is. You sigh and make the painful journey up. Then crawl through the portal as your ankle refuses to work any further.")
    else:
        print("\nWhew, you made the jump! That was scary. You head into the portal unscathed and feeling like a winner.")
else:
    if event1 == 'a':
        print("\nThe village magician walking his dog sees you looking around trying to figure out how to safely cross the ravine, he waves his wand and creates a bridge you across the ravine. Its your lucky day! You then get into the portal!")
    elif event1 == 'b':
        print("\nYou try to follow the map to find the old bridge to cross the ravine. You get lost a couple of times but you end up finding your way and crossing the old bridge. You then walk your way to the portal feeling tired and sweaty.")
    else:
        print("\nyou wander around for an hour before finding an old bridge to cross the ravine. Finally after crossing, you wander your way to the portal feeling sweaty and exhausted.")

print("\nHere, towering skyscrapers adorned with enchanting runes soar into the sky, while bustling streets are filled with a colorful array of creatures—humans, elves, dwarves, and more—all going about their daily lives. Amidst the hustle and bustle, you realize that you're not on a quest for ancient relics or mystical artifacts, but rather, you're simply heading to work at your corporate day job.")

#outcome based on event 1 + 2's outcomes:
if event2 == 'a':
    if i == 1:
        print("\nYou entered your office early and have a nice morning coffee to start the day.")
    else:
        print("\nYou were late to work and see your manager grinning sinisterly at you. There goes 20% of your day's paycheck to the late fine.")
else:
    if event1 == 'a':
        print("\nYou entered your office early and have a nice morning coffee to start the day.")
    elif event1 == 'b':
        print("\nYour manager stares you down as you enter the office on the dot, disappointed that she could not fine you for being late.")
    else:
        print("\nYou were late to work and see your manager grinning sinisterly at you. There goes 20% of your day's paycheck to the late fine.")