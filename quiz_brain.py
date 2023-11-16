class Brain():
    
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.questions = len(self.question_list)
        self.score = 0
        
    def still_has_questions(self):
        if self.question_no < self.questions:
            return True
        else:
            return False
        
        
    def next_question(self):
        self.answer = input(f"{self.question_no + 1}. {self.question_list[self.question_no].question}  (True/False) ").title()
        
        if self.answer == self.question_list[self.question_no].answer:
            self.score += 1
            print(f"your answer was {self.answer} this is correct your score is ({self.score}/{self.questions})")
            
            self.question_no += 1
            
            if self.still_has_questions():
                self.next_question()
            else:
                print(f"your final score is ({self.score}/{self.questions})")
        
        else:
            print(f"your answer was {self.answer} this is false your score is ({self.score}/{self.questions})")
            
            self.question_no += 1
            
            if self.still_has_questions():
                self.next_question()
            else:
                print(f"your final score is ({self.score}/{self.questions})")
        
