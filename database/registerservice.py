from database.models import User
from database import db

# funktsiya registratsii polzovatelya
def register_user_db(name, phone_number):
    # proverka polzovatelya na nalichie v baze
    checker = User.query.filter_by(phone_number=phone_number).first()

    # yesli yest polzovatel
    if checker:
        return checker.id

    # dobavlenie dannix v bazu
    new_user = User(name=name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()

    return new_user.id