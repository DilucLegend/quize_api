from api import api_bp
from database import get_questions_db, check_user_answer_db, user_end_test_db

# url dlya polucheniya voprossov
@api_bp.route('/get-questions/<int:level>', methods=['GET'])
def get_question(level: int):
    result = get_questions_db(level)
    return {'status': 1, 'questions': result}

# url dlya proverki otveta polzovatelya
@api_bp.route('/check-answer/<int:question_id>/<int:user-answer>', methods=['POST'])
def check_user_answer(question_id: int, user_answer: int):
    result = check_user_answer_db(question_id, user_answer)

    if result:
        return {'status': 1, }
    else:
        return {'status': 0}
# url dlya zaversheniya i polucheniya rezultatov testa
@api_bp.route('/done/<int:user_id>/<int:correct_answer>/<int:level>', methods=['POST'])
def commit_user_answer(user_id: int, correct_answer: int, level: int):
    result = user_end_test_db(user_id, correct_answer, level)

    return {'status': 1, 'correct answers': correct_answer, 'position on top': result}