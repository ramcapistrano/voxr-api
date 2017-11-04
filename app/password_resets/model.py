from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, backref
from app.database import SessionDB, Base


# PasswordReset Model
class PasswordReset(Base):
    __tablename__ = 'password_resets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(4), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, user_id, code):
        self.user_id = user_id
        self.code = code

    # Return object data in easily serializeable format
    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'code': self.code
        }
