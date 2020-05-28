"""
rewrite of Hannah's cool buzzfeed quiz program.

J. Knerr
May 2020
"""

def main():
    print("\nHello and welcome to HMK's buzzfeed based Knerr Family Quiz!\n")
    qnum = 0
    scores = {"mom":0, "dad":0, "courtney":0, "aidan":0, "hannah":0}
    line = "\n" + "="*30

    q = "Would you like to play? "
    if getYN(q):
        print("Hooray! Let's go:")
        print(line)
        q1 = "What are your dietary preferenes?"
        answers = ["Vegan","Vegetarian","Something in between","Omnivore"]
        results = [["courtney"],["aidan"],["mom","dad"],["hannah"]]
        ask(q1,answers,results,scores)
        print(line)
        q2 = "Who is your favorite dog?"
        answers = ["Abby","Max","Lily","Sammy"]
        results = [["dad"],["mom"],["courtney"],["aidan","hannah"]]
        ask(q2,answers,results,scores)
        print(line)
        q3 = "Where would you take your partner on a date?" 
        answers = ["Swimming Pool","Birding","Brewery","Rhett Miller Concert"]
        results = [["aidan"],["courtney"],["hannah","dad"],["mom"]]
        ask(q3,answers,results,scores)
        print(line)
        q4 = "How much python do you know?" 
        answers = ["I have a Phd","How much can you learn in a month?","Intro CS","Snakes?"]
        results = [["dad"],["aidan","courtney"],["hannah"],["mom"]]
        ask(q4,answers,results,scores)
        print(line)
        q5 = "What is your favorite kind of book?" 
        answers = ["TV","Romance","YA","Dogs"]
        results = [["courtney"],["aidan"],["dad","hannah"],["mom"]]
        ask(q5,answers,results,scores)
        print(line)
        q6 = "What's your favorite drink?"
        answers = ["Cosmo","Margs","Fireball Shots","Wine"]
        results = [["mom"],["dad","hannah"],["aidan"],["courtney"]]
        ask(q6,answers,results,scores)
    else:
        print("Alright. Maybe next time.")
        exit()

    print("\n"+"=-="*20)
    print(scores)
    maxscore = 0
    winner = ""
    for person in scores:
        if scores[person] > maxscore:
            maxscore = scores[person]
            winner = person
    print("Congrats! You are most like:", winner)

def getYN(q):
    """ask yes/no question, return True if they answer positive"""
    pos = ["y","yes","si"]
    neg = ["n","no","nyet"]
    while True:
        answer = input(q).rstrip('.,!').lower()
        if answer in pos:
            return True
        elif answer in neg:
            return False
        else:
            print("Don't think that's an answer? Try yes or no!")

def ask(question,answers,results,scores):
    """ask question with answers, update scores"""
    ans = menu(question,answers)
    people = results[ans]
    for who in people:
        scores[who] += 1

def menu(question, answers):
    """create menu of answers, make sure we get a valid input"""
    print(question)
    for i in range(len(answers)):
        print("%d) %s" % (i+1, answers[i]))
    while True:
        num = input(" ----> ")
        if num.isdigit():
            num = int(num)
            if num >= 1 and num <= len(answers):
                return num-1
            else:
                print("Please enter a number from 1-%d!" % (len(answers)))

main()
