from art import logo
from data import easy_questions, hard_questions, extra_hard_questions
from quizBrain import QuizBrain
from question_model import Question

question_bank = []
questions = []
print(logo)

print("Choose your difficulty:")
print("1. Easy")
print("2. Hard")
print("3. Extra Hard")

difficulty = input("Enter your choice: ").lower()
if difficulty == "1" or difficulty == "easy":
    questions = easy_questions

elif difficulty == "2" or difficulty == "hard":
    questions = hard_questions

elif difficulty == "3" or difficulty == "extra hard":
    questions = extra_hard_questions

else:
    print("Invalid choice")

for question in questions:
    question_text = question["question"]
    question_answer = question["answer"]
    question_options = question["options"]
    new_question = Question(question_text, question_answer, question_options)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.question_left():
    quiz.next_question()

print(f"You have done well!")
print(f"Your final score is: {quiz.score}/{quiz.questions_number}")

