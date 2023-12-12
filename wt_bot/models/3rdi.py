from sqlalchemy import Integer, String, Column, Boolean, BigInteger, DateTime, Float, ARRAY
from wt_bot.db.base_class import Base

class PatientHistory(Base):  # (RdiBase):

   __tablename__ = "PatientHistory"
   Id = Column(BigInteger, primary_key=True, autoincrement=True)
   patientID = Column(String)
   caresummary = Column(String)
   created_at = Column(DateTime)
   tokens = Column(Integer)


# class Conversation(Base):  # (RdiBase):

#     __tablename__ = "Conversation"

#     Id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     consultationID = Column(String)
#     appointmentID = Column(String)
#     sessionID = Column(String)
#     conversationAudio = Column(String)
#     conversationText = Column(String)
#     inferenceTime = Column(Float)
#     floraTrigger = Column(Boolean)
#     history = Column(String)
#     summary = Column(String)


# class Support(Base):  # (RdiBase):

#     __tablename__ = "Support"

#     Id = Column(BigInteger, primary_key=True, autoincrement=True)
#     sessionID = Column(String)
#     endpoint = Column(String)
#     openAITime = Column(Float)
#     promptTokens = Column(Integer)
#     completionTokens = Column(Integer)


# class Questions(Base):  # (RdiBase):

#     __tablename__ = "Questions"

#     Id = Column(BigInteger, primary_key=True, autoincrement=True)
#     sessionID = Column(String)
#     question = Column(String)
#     reason = Column(String)
#     differentials = Column(ARRAY(String))
#     confidence = Column(Float)
#     relevant = Column(Boolean)
#     irrelevant = Column(Boolean)


# class Investigations(Base):  # (RdiBase):

#     __tablename__ = "Investigations"

#     id = Column(BigInteger, primary_key=True, autoincrement=True)
#     sessionID = Column(String)
#     investigation = Column(String)
#     confidence = Column(Float)
#     relevant = Column(Boolean)
#     irrelevant = Column(Boolean)


# class Diagnosis(Base):  # (RdiBase):

#     __tablename__ = "Diagnosis"

#     id = Column(BigInteger, primary_key=True, autoincrement=True)
#     sessionID = Column(String)
#     differential = Column(String)
#     confidence = Column(Float)
#     relevant = Column(Boolean)
#     irrelevant = Column(Boolean)


# class PatientHistory(Base):  # (RdiBase):

#     __tablename__ = "PatientHistory"

#     Id = Column(BigInteger, primary_key=True, autoincrement=True)
#     patientID = Column(String)
#     caresummary = Column(String)
#     created_at = Column(DateTime)
#     tokens = Column(Integer)


# class PatientHealth(PatientBase):

#     # __tablename__ = "Patient"

#     pass
