class QuizBrain:
    def __init__(self, q_list):
      self.question_num = 0
      self.question_list = q_list

    def question_answer(self):
        your_score = 0
        for item in self.question_list:
            self.question_num += 1
            user_answer = input("Q.{}: {} True/False? ".format(self.question_num, item.text))
            if (user_answer == item.answer):
                print("You are right")
                your_score += 1
            else:
                print("You are wrong")
            print("The correct answer was {}".format(item.answer))
            print(f"Your current score is {your_score}/{self.question_num}")

            

        

