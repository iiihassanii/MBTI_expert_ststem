#!/usr/bin/python3
from random import choice
from experta import *

def questions_I_E():
    questions = [("At a party do you", "interact with many, including strangers", "interact with a few, known  to you"),
    ("At parties do you", "Stay late, with increasing energy", "Leave early, with decreasing energy"),
    ("In your social groups do you", "Keep abreast of others happenings", "Get behind on the news"),
    ("Are you usually rather", "Quick to agree to a time", "Reluctant to agree to a time"),
    ("In company do you", "Start conversations", "Wait to be approached"),
    ("Does new interaction with others", "Stimulate and energize you", "Tax your reserves"),
    ("Do you prefer", "Many friends with brief contact", "A few friends with longer contact"),
    ("Do you", "Speak easily and at length with strangers", "Find little to say to strangers"),
    ("When the phone rings do you", "Quickly get to it first", "Hope someone else will answer"),
    ("At networking functions you are", "Easy to approach", "A little reserved")]

    counter_a, counter_b = 0, 0
    for question in questions:
        question_string = f"{question[0]}:\n\tA. {question[1]}\n\tB. {question[2]}\n[a/b]:  "
        answer = input(question_string).lower()
        while answer not in ("a", "b"):
            print("\n\n \t\t********Please choose A or B********")
            answer = input(question_string).lower()
        if answer == "a":
            counter_a += 1
        else:
            counter_b += 1


    if counter_a > counter_b:
        return 'E'
    else:
        return 'I'

def questions_S_N():
    questions = [("Are you usually more", "Fair minded", "Kind hearted"),
    ("Is it more natural to be", "Fair to others", "Nice to others"),
    ("Are you more naturally", "Impartial", "Compassionate"),
    ("Are you inclined to be more", "Cool headed", "Warm hearted"),
    ("Are you usually more", "Tough minded", "Tender hearted"),
    ("Which is more satisfying", "To discuss an issue throughly", "To arrive at agreement on an issue"),
    ("Are you more comfortable when you are", "Objective", "Personal"),
    ("Are you typically more a person of", "Clear reason", "Strong feeling"),
    ("In judging are you usually more", "Neutral", "Charitable"),
    ("Are you usually more", "Unbiased", "compassionate")]

    counter_a, counter_b = 0, 0
    for question in questions:
        question_string = f"{question[0]}:\n\tA. {question[1]}\n\tB. {question[2]}\n[a/b]:  "
        answer = input(question_string).lower()
        while answer not in ("a", "b"):
            print("\n\n \t\t********Please choose A or B********")
            answer = input(question_string).lower()
        if answer == "a":
            counter_a += 1
        else:
            counter_b += 1


    if counter_a > counter_b:
        return 'S'
    else:
        return 'N'


def questions_T_F():
    questions =  [("Do you prefer to work", "To deadlines", "Just whenever"),
    ("Are you usually more", "Punctual", "Leisurely"),
    ("Do you usually", "Settle things", "Keep options open"),
    ("Are you more comfortable", "Setting a schedule", "Putting things off"),
    ("Are you more prone to keep things", "well organized", "Open-ended"),
    ("Are you more comfortable with work", "Contracted", "Done on a casual basis"),
    ("Are you more comfortable with", "Final statements", "Tentative statements"),
    ("Is it preferable mostly to", "Make sure things are arranged", "Just let things happen"),
    ("Do you prefer?", "Getting something done", "Having the option to go back"),
    ("Is it more like you to", "Make snap judgements", "Delay making judgements")]

    counter_a, counter_b = 0, 0
    for question in questions:
        question_string = f"{question[0]}:\n\tA. {question[1]}\n\tB. {question[2]}\n[a/b]:  "
        answer = input(question_string).lower()
        while answer not in ("a", "b"):
            print("\n\n \t\t********Please choose A or B********")
            answer = input(question_string).lower()
        if answer == "a":
            counter_a += 1
        else:
            counter_b += 1


    if counter_a > counter_b:
        return 'T'
    else:
        return 'F'


def questions_J_P():
    questions = [("Do you tend to choose", "Rather carefully", "Somewhat impulsively"),
    ("Does it bother you more having things", "Incomplete", "Completed"),
    ("Are you usually rather", "Quick to agree to a time", "Reluctant to agree to a time"),
    ("Are you more comfortable with", "Written agreements", "Handshake agreements"),
    ("Do you put more value on the", "Definite", "Variable"),
    ("Do you prefer things to be", "Neat and orderly", "Optional"),
    ("Are you more comfortable", "After a decision", "Before a decision"),
    ("Is it your way more to", "Get things settled", "Put off settlement"),
    ("Do you prefer to?", "Set things up perfectly", "Allow things to come together"),
    ("Do you tend to be more", "Deliberate than spontaneous", "Spontaneous than deliberate")]


    counter_a, counter_b = 0, 0
    for question in questions:
        question_string = f"{question[0]}:\n\tA. {question[1]}\n\tB. {question[2]}\n[a/b]:  "
        answer = input(question_string).lower()
        while answer not in ("a", "b"):
            print("\n\n \t\t********Please choose A or B********")
            answer = input(question_string).lower()
        if answer == "a":
            counter_a += 1
        else:
            counter_b += 1


    if counter_a > counter_b:
        return 'J'
    else:
        return 'P'


    

class Test_I_E(Fact):
   """Info about E (Extraversion) vs. I (Introversion)"""
   pass

class Test_S_N(Fact):
   """Info about S (Sensing) vs. N (Intuition)"""
   pass

class Test_T_F(Fact):
   """Info about T (Thinking) vs. F (Feeling)"""
   pass

class Test_J_P(Fact):
   """Info about J (Judging) vs. P (Perceiving)"""
   pass


class personalityResult(Fact):
    pass

class personalityTest(KnowledgeEngine):
    
    @Rule(Test_I_E(result='I'))
    def is_it_I(self):
        print("I", end='')

    @Rule(Test_I_E(result='E'))
    def is_it_E(self):
        print("E", end='')
        
    @Rule(Test_S_N(result='S'))
    def is_it_S(self):
        print("S", end='')

    @Rule(Test_S_N(result='N'))
    def is_it__N(self):
        print("N", end='')
    
    @Rule(Test_T_F(result='T'))
    def is_it_T(self):
        print("T", end='')

    @Rule(Test_T_F(result='F'))
    def is_it_F(self):
        print("F", end='')

    @Rule(Test_J_P(result='J'))
    def is_it_J(self):
        print("J")

    @Rule(Test_J_P(result='P'))
    def is_it_P(self):
        print("P")

    @Rule(personalityResult(result='INTJ'))
    def it_is_INTJ(self):
        print("=========>Architect<=========")
        print("Description")
        print("Imaginative and strategic thinkers, with a plan for everything")
    
    @Rule(personalityResult(result='INTP'))
    def it_is_INTP(self):
        print("=========>Logician<=========")
        print("Description")
        print("Innovative inventor; insatiable thirst for knowledge")
    
    @Rule(personalityResult(result='ENTJ'))
    def it_is_ENTJ(self):
        print("=========>Commander<=========")
        print("Description")
        print("Imaginative, strong willed, and always able to find a way")
    
    @Rule(personalityResult(result='ENTP'))
    def it_is_ENTP(self):
        print("=========>Debater<=========")
        print("Description")
        print("Smart and curious who cannot resist an intellectual challenge")
    
    @Rule(personalityResult(result='INFJ'))
    def it_is_INFJ(self):
        print("=========>Advocate<=========")
        print("Description")
        print("Quiet, inspiring, tireless idealist")
    
    @Rule(personalityResult(result='INFP'))
    def it_is_INFP(self):
        print("=========>Mediator<=========")
        print("Description")
        print("Poetic, kind and altruistic, eager to help a good cause")

    @Rule(personalityResult(result='ENFJ'))
    def it_is_ENFJ(self):
        print("=========>Protagonist<=========")
        print("Description")
        print("Charismatic and inspiring, able to mesmerize listeners")
    
    @Rule(personalityResult(result='ENFP'))
    def it_is_ENFP(self):
        print("=========>Campaigner<=========")
        print("Description")
        print("Enthusiastic, creative and free spirited; always finds a reason to smile")
    @Rule(personalityResult(result='ISTJ'))
    def it_is_ISTJ(self):
        print("=========>Logistician<=========")
        print("Description")
        print("Practical and fact-minded; reliable")
    
    @Rule(personalityResult(result='ISFJ'))
    def it_is_ISFJ(self):
        print("=========>Defender<=========")
        print("Description")
        print("Dedicated and warm protector; ready to defend their loved ones")

    @Rule(personalityResult(result='ESTJ'))
    def it_is_ESTJ(self):
        print("=========>Executive<=========")
        print("Description")
        print("Great at managing things or people, excellent administrators")

    @Rule(personalityResult(result='ESFJ'))
    def it_is_ESFJ(self):
        print("=========>Consul<=========")
        print("Description")
        print("Caring, social, popular with people; always eager to help")
    @Rule(personalityResult(result='ISTP'))
    def it_is_ISTP(self):
        print("=========>Virtuoso<=========")
        print("Description")
        print("Bold and practical experimenters")
    @Rule(personalityResult(result='ISFP'))
    def it_is_ISFP(self):
        print("=========>Adventurer<=========")
        print("Description")
        print("Flexible and charming artist; always looking for new experiences")
    @Rule(personalityResult(result='ESTP'))
    def it_is_ESTP(self):
        print("=========>Entrepreneur<=========")
        print("Description")
        print("Smart, energetic, and very perceptive; loves living on the edge")
    @Rule(personalityResult(result='ESFP'))
    def it_is_ESFP(self):
        print("=========>Entertainer<=========")
        print("Description")
        print("Spontaneous and enthusiastic; life of the party")



if __name__ == '__main__':
    engine = personalityTest()
    engine.reset()

    questions1 = questions_I_E()
    questions2 = questions_S_N()
    questions3 = questions_T_F()
    questions4 = questions_J_P()
    personality = str(questions1 + questions2 + questions3 + questions4)

    engine.declare(personalityResult(result=personality))
    engine.declare(Test_J_P(result=questions4))
    engine.declare(Test_T_F(result=questions3))
    engine.declare(Test_S_N(result=questions2))
    engine.declare(Test_I_E(result=questions1))
    

    engine.run()
