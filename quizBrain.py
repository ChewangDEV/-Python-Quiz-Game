class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.questions_number = 0
        self.question_list = q_list



    def question_left(self):
        return self.questions_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.questions_number]
        self.questions_number += 1

        print(f"\n{self.questions_number}. {current_question.text}")

        letters = ["A", "B", "C", "D"] # gives each option a letter.

        for i in range(len(current_question.options)):
            print(f"{letters[i]}. {current_question.options[i]}") # print in column

        user_choice = input("Answer (A/B/C/D): ").upper()

        if user_choice in letters:
            selected_answer = current_question.options[letters.index(user_choice)] # give which index it is in by converting
            self.check_ans(selected_answer, current_question.ans)
        else:
            print("Invalid choice. Please choose A, B, C, or D.")

    def check_ans(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            self.score += 1
            print("\n" * 2)
        else:
            print("\n" * 2)