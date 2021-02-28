#-*- coding: utf-8 -*-
import re

BASE_CODE = 44032

def is_hangle(string: str) -> bool:
    last_char = string[-1]
    if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', last_char) is None:
        return False
    return True

def has_jongsung(string: str)  -> bool:
    if not is_hangle(string):
        raise Exception("마지막 글자가 한글이 아닙니다.")

    last_char = string[-1]
    if (ord(last_char) - 44032) % 28 > 0:
        return True
    return  False


# TODO: can we make above functions as Decorator?