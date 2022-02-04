import random

print("Hello there! welcom to MadLib Game")
print("You will give me some words and I will tell you the story using those words")
print("Ready? Let's start the game...")


def story_teller(a):
    if a == 1:
        adjective = input("Give me an adjective: ")
        food1 = input("Now give me a foods (plural): ")
        verb = input("Good, now give me a verb: ")
        saying = input("OK, now type a popular sentence or saying: ")
        noun = input("Type a noun: ")
        food2 = input("Now give me another foods (plural): ")
        color = input ("Give me a color: ")
        ride = input ("almost there, this time type name of something you would ride in: ")
        animal = input ("Give me an animal: ")
        person = input ("Last one is a person: ")

        story = "Today I went to my favorite Taco Stand called the " + adjective +"-"+ animal + \
        ". Unlike most food stands, they cook and prepare the food in a " + ride + \
        " while you " + verb +". The best thing on the menu is the " + color +" "+ noun + \
        ". Instead of ground beef they fill the taco with " + food2 + \
        ", cheese, and top it off with a salsa made from " + food1 + \
        ". If that doesn't make your mouth water, then it's just like " + person + \
        " always says: " + saying + "!"
        print ("=======================================================================================================")
        return(story)

    elif a == 2:
        job = input("Give me an Occupation (a job): ")
        noun1 = input("Type a noun: ")
        adjective1 = input("Now give an adjective: ")
        noun2 = input("Type another noun: ")
        verb1 = input("Good, now give me a verb: ")
        adjective2 = input("Now type another adjective: ")
        noun3 = input("Good, next noun: ")
        verb2 = input("almost there, this time type second verb: ")
        noun4 = input("Type a name of person: ")
        verb3 = input("Last one is another verb: ")

        story = "Today a " + job +" named "+ noun4 + " came to our school to talk to us about her job" \
        ". She said the most important skill you need to know to do her job is to be able to " + verb2 + \
        " around (a) " + adjective1 + " " + noun3 + \
        ". She said it was easy for her to learn her job because she loved to " + verb1 + \
        " when she was my age--and that helps a lot! If you're considering her profession, " \
        "I hope you can be near (a) " + adjective2 + " " + noun1 + \
        ". That's very important! If you get too distracted in that situation you won't be able to " \
        + verb3 + " next to (a) " + noun2 + "!"

        print ("=======================================================================================================")
        return story

a = random.randint(1, 2)
print(story_teller(a))
print ("=======================================================================================================")
