# TODO : Asking the Questions 
# TODO : Checking the answer 
# TODO : Checking if at the end of the quiz 

class QuizBrain: 

    def __init__(self, q_list): 
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list) 
        
    
    def next_question(self):
        current_question = self.question_list[self.question_number] 
        self.question_number += 1
        answer_from_user = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")           
        if self.check_answer(answer_from_user, current_question.answer): 
            self.score += 1
            print(f"You got it Right!") 
        else:
            print("Wrong Answer!", end="\n")  
            print(f"The correct answer was : '{current_question.answer}'")   
        
        print(f"=> Your score is: {self.score}/{self.question_number}\n\n") 
            


    def check_answer(self, user_answer, correct_answer): 
        return user_answer.lower() == correct_answer.lower()

