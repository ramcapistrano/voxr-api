from sqlalchemy.exc import InvalidRequestError
from model import User
from app.database import SessionDB


def get(user_id):
    db_session = SessionDB
    try:
        db_session.rollback()
        result = db_session.query(User).filter(User.id == user_id).first()
        db_session.close()
    except InvalidRequestError:
        db_session.rollback()
        db_session.close()
    return result


def save(user):
    db_session = SessionDB()
    db_session.add(user)
    db_session.commit()
    db_session.close()
    return True


def update(user):
    db_session = SessionDB()
    updated_user = (
        db_session.query(User)
        .filter(User.id == user.id)
        .first()
    )
    updated_user.first_name = user.first_name
    updated_user.last_name = user.last_name
    db_session.commit()
    db_session.close()
    return True
