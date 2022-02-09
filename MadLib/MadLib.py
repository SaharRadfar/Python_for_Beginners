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

    elif a == 3:
        boy1 = input("Give me a boy's name: ")
        boy2 = input("Type another boy's name: ")
        girl1 = input("Now give a girl's name: ")
        girl2 = input("Type another girl's name: ")
        animal = input("almost there, this time type an animal name: ")
        exclamation = input("Last one is an exclamation:: ")

        story = "Once upon a time, two people,  " + girl1 +" and "+ boy1 + " were walking " \
        "in the park. They were talking about his " + animal + \
        ' . Then 1 exclaimed, "' + exclamation + '!", "What is it, ' + boy1 + \
        '" cried " '+ girl1 + \
        '" I just remembered something, I have this ring in my pocket."' \
        "said " + boy1 + '. "Why would you have that?" asked  ' + girl1 + \
        '. "Will you marry me?"  ' + boy1 + 'asked. ' \
        + girl1 + ' replied, "Ummmmmmm... Yes, I Love You, ' + boy1 + '!" So they left on ' \
        + "1's 50 to their kingdom and had 2 children named " + girl2 + 'and' + boy2 + \
        'and they lived happily ever after as every story should end!'

        print (" ")
        print ("=======================================================================================================")
        return story

    elif a == 4:
        boy = input("Give me a boy's name: ")
        number = input("Input a number: ")
        thing1 = input("Type name of a thing: ")
        thing2 = input("Good, now give me another thing: ")
        thing3 = input("Last one is one more thing: ")

        story = "One day a boy named " + boy + " entered the Children's Lottery hoping to win $" \
        + number + " . He wasn't expecting to win when one day a lady rang telling him " \
        "that he had won.  " + boy + \
        " was very excited and decided to donate to a charity and buy a " \
        + thing1 + ". He also bought a " + thing2 + \
        "and a " + thing3 + " and he was very happy from then on."
        
        print (" ")
        print ("=======================================================================================================")
        return story

    elif a == 5:
        girl = input("Give me a girl's name: ")
        radiostation = input("Input a radio station name: ")
        place = input("Type name of a place: ")
        star = input("Good, now give me name of a famous pop star: ")
        number = input("Last one is a number: ")

        story = "Once " + girl + " was listening to "+ radiostation + \
        " when she heard that " + star + "would be coming to the " + place + \
        " but she didn't have any money to go and see " + star + ". So " + girl + \
        " asked her mom for ideas on how to make some money. Her mom suggested that she should wash" \
        "people's cars and have a garage sale to get rid of some of her old toys." + girl + \
        " did these things and she managed to raise £"  + number + " and got to go and see " + star + \
        " in the end."


        print (" ")
        print ("=======================================================================================================")
        return story


a = random.randint(1, 6)
print(story_teller(a))
print ("=======================================================================================================")
