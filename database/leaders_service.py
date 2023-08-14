from database import db
from database.models import Leaders, UserAnswer

# Zapis rezultata tekushevo testa
def user_end_test_db(user_id, correct_answers, level):
    exact_user_score = Leaders.query.fiter_by(user_id=user_id, level=level).first()

    # proverit yest li chto-to vnutri bazi
    if exact_user_score:
        # k starim ochkam dobavit tekushiy
        exact_user_score.score += correct_answers
        db.session.commit()

    # a yesli net
    else:
        # sozdayom zapis v baze dannix
        new_leader_date = Leaders(user_id=user_id, level=level, score=correct_answers)
        db.session.add(new_leader_date)
        db.session.commit()

    return True

# Vivod liderov iz konkretnix urovney
def get_top_5_leaders(level):
    exact_level_leaders = Leaders.query.filter_by(level=level).oreder_by(Leaders.score.desc()).all()

    return exact_level_leaders[:6]

# Zapis kajdogo otveta polzovatelya
def add_user_answer_db(user_id, q_id, user_answer, correctness):
    new_answer = UserAnswer(user_id=user_id, question_id=q_id, user_answer=user_answer, correctness=correctness)

    db.session.add(new_answer)
    db.session.commit()

    return True
