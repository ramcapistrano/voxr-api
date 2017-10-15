from sqlalchemy.exc import InvalidRequestError
from sqlalchemy import and_
from model import Record
from app.database import SessionDB
import datetime


def get(user_id, record_id):
    db_session = SessionDB
    try:
        db_session.rollback()
        result = db_session.query(Record).filter(and_(Record.user_id == user_id), (Record.id == record_id)).first()
        db_session.close()
    except InvalidRequestError:
        db_session.rollback()
        db_session.close()
    return result


def get_all(user_id):
    db_session = SessionDB
    try:
        db_session.rollback()
        results = db_session.query(Record).filter(and_(Record.user_id == user_id), (Record.date_deleted.is_(None))).all()
        records = []
        for result in results:
            records.append(result.serialize)
        db_session.close()
    except InvalidRequestError:
        db_session.rollback()
        db_session.close()
    return records


def save(record):
    db_session = SessionDB()
    db_session.add(record)
    db_session.commit()
    db_session.close()
    return True


def update(user_id, record_id):
    db_session = SessionDB()
    record = db_session.query(Record).filter(and_(Record.user_id == user_id), (Record.id == record_id),
                                             (Record.date_deleted.is_(None))).first()
    if record is not None:
        record.date_deleted = datetime.datetime.now()
        db_session.commit()
        db_session.close()
        return True
    else:
        return False
