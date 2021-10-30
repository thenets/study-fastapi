# Model
import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# Create user model from BaseModel
class User(Base):
    __tablename__ = "users"

    id: Column(Integer, primary_key=True, index=True)
    username: Column(String, unique=True, index=True)
    password: Column(String)
    tweets: relationship("Tweet", back_populates="user")


# Create timeline model from BaseModel
class Timeline(Base):
    __tablename__ = "timelines"

    id: Column(Integer, primary_key=True, index=True)
    title: Column(String)
    description: Column(String)
    creator_user_id: Column(Integer, ForeignKey("users.id"))

# Create tweet model from BaseModel
class Tweet(Base):
    __tablename__ = "tweets"

    id: Column(Integer, primary_key=True, index=True)
    tweet_text: Column(String)
    creator_user_id: Column(Integer, ForeignKey("users.id"))
    tweet_timeline_id: Column(Integer, ForeignKey("timelines.id"))
    created_at: Column(String, default=datetime.datetime.now())
    updated_at: Column(String, default=datetime.datetime.now())
