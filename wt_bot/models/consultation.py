from sqlalchemy import Integer, String, Column, Boolean, BigInteger, DateTime, Text, ForeignKey
from wt_bot.db.session import Base

class ApgarConsultation(Base):

    __tablename__ = "apgar_consultation"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey("apgar_users.id", ondelete="CASCADE"), nullable=False)
    apgar_conversation= Column(Text, nullable=False)
    user_conversation = Column(Text, nullable=False)
    evaluation = Column(Integer, nullable=False)
    ccl_id = Column(String(36), ForeignKey("PatientHistory.patientID", ondelete="CASCADE"), nullable=True)

