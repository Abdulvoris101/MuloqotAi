from sqlalchemy.orm import class_mapper, relationship

from db.setup import Base, session
from sqlalchemy import Column, Integer, String, UUID, BigInteger, Boolean, DateTime, ForeignKey
import uuid


class Limit(Base):
    __tablename__ = 'limit'

    id = Column(UUID(as_uuid=True), primary_key=True)
    monthlyLimitImage = Column(Integer)
    monthlyLimitGpt3 = Column(Integer)
    monthlyLimitGpt4 = Column(Integer)
    monthlyLimitTranslation = Column(Integer)
    limitOutputTokens = Column(Integer)
    limitInputTokens = Column(Integer)
    plans = relationship('Plan', backref='Plan.limitId', lazy='dynamic')

    @classmethod
    def update(cls, instance, column, value):
        setattr(instance, column, value)
        session.commit()

    @classmethod
    def delete(cls, chatId):
        limit = cls.get(chatId)
        session.delete(limit)

    @classmethod
    def get(cls, id):
        return session.query(Limit).filter_by(id=id).first()


class Plan(Base):
    __tablename__ = 'plan'

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String)
    description = Column(String, nullable=True)
    amountForMonth = Column(BigInteger)
    isFree = Column(Boolean)
    isGroup = Column(Boolean)
    limitId = Column(UUID, ForeignKey(Limit.id), nullable=True)

    def __init__(
            self, title,
            amountForMonth, isFree, 
            limitId, isGroup):
        
        self.id = uuid.uuid4()
        self.title = title
        self.amountForMonth = amountForMonth
        self.isFree = isFree
        self.limitId = limitId
        self.isGroup = isGroup

        super().__init__()

    def save(self):
        session.add(self)
        session.commit()

        return self
    
    @classmethod
    def update(cls, instance, column, value):
        setattr(instance, column, value)
        session.commit()

    @classmethod
    def delete(cls, planId):
        chat = session.query(Plan).filter_by(id=planId).first()
        session.delete(chat)


class Subscription(Base):
    __tablename__ = 'subscription'
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    planId = Column(UUID(as_uuid=True))
    currentPeriodStart = Column(DateTime)
    currentPeriodEnd = Column(DateTime, nullable=True)
    is_paid = Column(Boolean, default=False)
    chatId = Column(BigInteger)
    isCanceled = Column(Boolean, default=False)
    canceledAt = Column(DateTime, nullable=True)

    def __init__(self, planId, currentPeriodStart,
                 currentPeriodEnd, is_paid, chatId):

        self.id = uuid.uuid4()
        self.planId = planId
        self.currentPeriodStart = currentPeriodStart
        self.currentPeriodEnd = currentPeriodEnd
        self.is_paid = is_paid
        self.chatId = chatId

        super().__init__()

    def save(self):
        session.add(self)
        session.commit()

        return self


class FreeApiKey(Base):
    __tablename__ = 'freeapikey'
    
    id = Column(Integer, primary_key=True)
    apiKey = Column(String)
    isExpired = Column(Boolean, default=False)
    requests = Column(Integer, default=1)
    

class Configuration(Base):
    __tablename__ = "configuration"
    
    id = Column(Integer, primary_key=True)
    apikeyPosition = Column(Integer, default=0)
    isBeta = Column(Boolean, default=False)
    
    def __init__(self, apikeyPosition):
        self.apikeyPosition = apikeyPosition

        super().__init__()

    def save(self):
        session.add(self)
        session.commit()

        return self


class ChatQuota(Base):
    __tablename__ = 'chat_quota'

    id = Column(Integer, primary_key=True)
    chatId = Column(BigInteger, ForeignKey('chat.chatId'))
    additionalGpt3Requests = Column(BigInteger, default=0)
    additionalGpt4Requests = Column(BigInteger, default=0)
    additionalImageRequests = Column(BigInteger, default=0)

    def __init__(self, chatId, additionalGpt3Requests=0, additionalImageRequests=0,
                 additionalGpt4Requests: int = 0):
        self.chatId = chatId
        self.additionalGpt4Requests = additionalGpt4Requests
        self.additionalGpt3Requests = additionalGpt3Requests
        self.additionalImageRequests = additionalImageRequests

    def save(self):
        session.add(self)
        session.commit()

    def to_dict(self):
        """Converts SQL Alchemy model instance to dictionary."""
        return {c.key: getattr(self, c.key) for c in class_mapper(self.__class__).mapped_table.c}

    @classmethod
    def update(cls, instance, column, value):
        setattr(instance, column, value)
        session.commit()

    @classmethod
    def delete(cls, chatId):
        chatQuota = cls.get(chatId)
        session.delete(chatQuota)

    @classmethod
    def get(cls, chatId):
        chatQuota = session.query(ChatQuota).filter_by(chatId=chatId).first()
        return chatQuota

    @classmethod
    def getOrCreate(cls, chatId):
        chatQuota = cls.get(chatId)

        if chatQuota is None:
            ChatQuota(
                chatId=chatId, additionalGpt3Requests=0,
                additionalGpt4Requests=0,
                additionalImageRequests=0).save()

        return cls.get(chatId)



