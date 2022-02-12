from question_model import Question
from data import Question_data
from quiz import Quiz

question_bank = []
for question in Question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.more_questions():
    quiz.next_question()
print("\n")
print("Ukończyłeś Quiz!")