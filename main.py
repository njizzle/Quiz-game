from data import *
from question_model import Question
from quiz_brain import *

# print(question_data)

question_bank = []

for q in question_data:
    question = q['text']
    answer = q['answer']
    
    new_question = Question(question, answer)
    
    question_bank.append(new_question)

quiz = Brain(question_bank)

quiz.next_question()
    
    

