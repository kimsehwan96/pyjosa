#-*- coding: utf-8 -*-
import re
from pyjosa.exceptions import NotHangleException

START_HANGLE = 44032
J_IDX = 28

def is_hangle(string: str) -> bool:
    last_char = string[-1]
    if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', last_char) is None:
        return False
    return True

def has_jongsung(string: str)  -> bool:
    if not is_hangle(string):
        raise NotHangleException

    last_char = string[-1]
    if (ord(last_char) - START_HANGLE) % J_IDX > 0:
        return True
    return  False


# TODO: can we make above functions as Decorator?