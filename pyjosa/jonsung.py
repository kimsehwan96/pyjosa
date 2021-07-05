#-*- coding: utf-8 -*-
import re
from pyjosa.exceptions import NotHangleException, JongsungInstantiationException


class Jongsung:
    """
    글자가 한글인지 체크 및 종성이 있는지 체크하는 클래스
    """
    # Class attribute
    _START_HANGLE = 44032
    _J_IDX = 28

    # we will not instantiate this class because it's not really needed.
    def __init__(self):
        raise JongsungInstantiationException

    @staticmethod
    def is_hangle(string: str) -> bool:
        """
        입력받은 문자열의 마지막 글자가 한글인지 체크하는 정적 메서드
        :param string: 처리하고자 하는 단어(문자열)
        :return: 마지막 글자가 한글일경우 True, 한글이 아닐경우 False
        """
        last_char = string[-1]
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', last_char) is None:
            return False
        return True

    @classmethod
    def has_jongsung(cls, string: str) -> bool:
        """
        입력받은 문자열의 마지막 글자가 한글인 경우, 해당 글자가 종성이 있는지 없는지 확인하는
        클래스 메서드
        :param string: 입력받은 문자열
        :return: 종성이 있을경우 True
        """
        if not cls.is_hangle(string):
            raise NotHangleException
        last_char = string[-1]
        if (ord(last_char) - cls._START_HANGLE) % cls._J_IDX > 0:
            return True
        return False
