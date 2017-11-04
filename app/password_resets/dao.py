from sqlalchemy.exc import InvalidRequestError

from app.database import SessionDB
from model import PasswordReset


def get(user_id):
    db_session = SessionDB
    try:
        db_session.rollback()
        result = db_session.query(PasswordReset).filter(PasswordReset.user_id == user_id).first()
        db_session.close()
    except InvalidRequestError:
        db_session.rollback()
        db_session.close()
    return result


def get_by_code(code):
    db_session = SessionDB
    try:
        db_session.rollback()
        result = db_session.query(PasswordReset).filter(PasswordReset.code == code).first()
        db_session.close()
    except InvalidRequestError:
        db_session.rollback()
        db_session.close()
    return result


def save(password_reset):
    db_session = SessionDB()
    db_session.add(password_reset)
    db_session.commit()
    db_session.close()
    return True


def update(user_id, code):
    db_session = SessionDB()
    pr = db_session.query(PasswordReset).filter(PasswordReset.user_id == user_id).first()

    if pr is not None:
        pr.code = code
        db_session.commit()
        db_session.close()
        return True
    else:
        return False


def delete(password_reset):
    db_session = SessionDB()
    db_session.delete(password_reset)
    db_session.commit()
    db_session.close()
    return True
