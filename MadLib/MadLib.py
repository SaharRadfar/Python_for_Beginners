print("Hello there! welcom to MadLib Game")
print("You will give me some words and I will tell you the story using those words")
print("Ready? Let's start the game...")


def story_teller():
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

print(story_teller())
print ("=======================================================================================================")
