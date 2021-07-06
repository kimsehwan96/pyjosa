import timeit
from pyjosa.josa import Josa

word_list = ['오리', '예나', '세환', '철수', '길동', '우주']

start_time = timeit.default_timer()  # 시작 시간 체크

for i in range(100000):
    for word in word_list:
        a = Josa.get_full_string(word, '은')
        b = Josa.get_full_string(word, '이가')
        c = Josa.get_full_string(word, '와')
        d = Josa.get_full_string(word, '를')

terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))

pyjosa_time1 = terminate_time - start_time

import re

JOSA_PAIRD = {
    u"(이)가": (u"이", u"가"),
    u"(와)과": (u"과", u"와"),
    u"(을)를": (u"을", u"를"),
    u"(은)는": (u"은", u"는"),
    u"(으)로": (u"으로", u"로"),
    u"(아)야": (u"아", u"야"),
    u"(이)여": (u"이여", u"여"),
    u"(이)라": (u"이라", u"라"),
}

JOSA_REGEX = re.compile(u"\(이\)가|\(와\)과|\(을\)를|\(은\)는|\(아\)야|\(이\)여|\(으\)로|\(이\)라")


def choose_josa(prev_char, josa_key, josa_pair):
    """
    조사 선택
    :param prev_char 앞 글자
    :param josa_key 조사 키
    :param josas 조사 리스트
    """
    char_code = ord(prev_char)

    # 한글 코드 영역(가 ~ 힣) 아닌 경우
    if char_code < 0xac00 or char_code > 0xD7A3:
        return josa_pair[1]

    local_code = char_code - 0xac00  # '가' 이후 로컬 코드
    jong_code = local_code % 28

    # 종성이 없는 경우
    if jong_code == 0:
        return josa_pair[1]

    # 종성이 있는 경우
    if josa_key == u"(으)로":
        if jong_code == 8:  # ㄹ 종성인 경우
            return josa_pair[1]

    return josa_pair[0]


def replace_josa(src):
    tokens = []
    base_index = 0
    for mo in JOSA_REGEX.finditer(src):
        prev_token = src[base_index:mo.start()]
        prev_char = prev_token[-1]
        tokens.append(prev_token)

        josa_key = mo.group()
        tokens.append(choose_josa(prev_char, josa_key, JOSA_PAIRD[josa_key]))

        base_index = mo.end()

    tokens.append(src[base_index:])
    return ''.join(tokens)


word_list = ['오리', '예나', '세환', '철수', '길동', '우주']

start_time = timeit.default_timer()  # 시작 시간 체크

for i in range(100000):
    for word in word_list:
        a = replace_josa(f"{word}(은)는")
        b = replace_josa(f"{word}(이)가")
        c = replace_josa(f"{word}(와)과")
        d = replace_josa(f"{word}(을)를")

terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))

pyjosa_time2 = terminate_time - start_time

print(pyjosa_time1, pyjosa_time2)

"""
4.704572초 걸렸습니다.  : https://github.com/kimsehwan96/pyjosa
5.381061초 걸렸습니다.  : https://github.com/myevan/pyjosa
"""