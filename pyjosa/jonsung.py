#-*- coding: utf-8 -*-
import re
from pyjosa.exceptions import NotHangleException, JongsungInstantiationException


class Jongsung:
    # we will not instantiate this class because it's not really needed.
    def __init__(self):
        raise JongsungInstantiationException
    START_HANGLE = 44032
    J_IDX = 28

    @staticmethod
    def is_hangle(string: str) -> bool:
        last_char = string[-1]
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', last_char) is None:
            return False
        return True

    @classmethod
    def has_jongsung(cls, string: str) -> bool:
        if not cls.is_hangle(string):
            raise NotHangleException

        last_char = string[-1]
        if (ord(last_char) - cls.START_HANGLE) % cls.J_IDX > 0:
            return True
        return False
