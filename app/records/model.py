from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, backref
from app.database import SessionDB, Base


# Record Model
class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True, autoincrement=True)
    neutrality = Column(Float, nullable=False)
    happiness = Column(Float, nullable=False)
    sadness = Column(Float, nullable=False)
    anger = Column(Float, nullable=False)
    fear = Column(Float, nullable=False)
    file_path = Column(String(100), nullable=False)
    date_created = Column(DateTime, nullable=False)
    date_deleted = Column(DateTime, nullable=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, user_id, neutrality, happiness, sadness, anger, fear, file_path):
        self.user_id = user_id
        self.neutrality = neutrality
        self.happiness = happiness
        self.sadness = sadness
        self.anger = anger
        self.fear = fear
        self.file_path = file_path

    # Return object data in easily serializeable format
    @property
    def serialize(self):
        emotion = {
            'neutrality': self.neutrality,
            'happiness': self.happiness,
            'sadness': self.sadness,
            'anger': self.anger,
            'fear': self.fear
        }

        user_emotion = max(emotion.iterkeys(), key=(lambda key: emotion[key]))

        return {
            'id': self.id,
            'emotion': emotion,
            'user_emotion': user_emotion,
            'file_path': self.file_path,
            'date_created': self.date_created
        }