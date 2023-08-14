from database.models import Question, UserAnswer
from database import db

# funksiya dobavleniya voprosa - 7 parametrov
def add_questions(main_text, variant_1, variant_2, variant_3, variant_4, correct_answer, level):
    new_question = Question(main_text=main_text, variant_1=variant_1, variant_2=variant_2, variant_3=variant_3, variant_4=variant_4, correct_answer=correct_answer, level=level)
    db.session.add(new_question)
    db.session.commit()

    return True

# vivesti 20 voprosov
def get_questions_db(level):
    questions = Question.query.filter_by(level=level).all()
    return questions[:21]

# proverka otveta polzovatelya
def check_user_answer_db(question_id, user_answer):
    question = Question.query.filter_by(id=question_id).first()
    if question.correct_answer == user_answer:
        return True
    return False
