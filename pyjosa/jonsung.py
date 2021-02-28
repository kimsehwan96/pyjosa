#-*- coding: utf-8 -*-
import re

J_LIST = [] # 종성 리스트  추가

def is_hangle(string: str) -> bool:
    last_char = string[-1]
    if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', last_char) is None:
        return False
    return True




def has_jungsung(string: str)  -> bool:
    last_char = string[-1]
    encoded_last_char = last_char.encode('utf8')
    #유니코드 계산을 통해 종성을 분리한다.
    #종성이 있을경우 True, 없을경우 False를 반환하도록 작성한다.
    pass