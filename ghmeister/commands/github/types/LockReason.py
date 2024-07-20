from enum import Enum


class LockReason(str, Enum):
    off_topic = 'off-topic'
    too_heated = 'too heated'
    resolved = 'resolved'
    spam = 'spam'
