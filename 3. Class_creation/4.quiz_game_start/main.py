# importing class and data modules.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Accessing data from list.
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    # Holds all the data in created object.
    new_question = Question(question_text, question_answer)

    # Holding the Object data in an empty list.
    question_bank.append(new_question)

# For asking questions ---> Object creation.
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print(f"You've completed the quiz, Your final score was: {quiz.score}/{quiz.question_number}")
