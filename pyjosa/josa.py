from pyjosa.jonsung import Jongsung
from pyjosa.exceptions import JosaTypeException

class Josa:

    @staticmethod
    def get_josa(string: str, josa: str) -> str:
        """
        조사를 반환하는 정적 메서드
        :param string: 입력받는 한글 단어
        :param josa: 체크하고자 하는 조사
        :return: 종성 여부에 따라 적절한 조사 반환
        """

        if (josa == '을') or (josa == '를'):
            return '을' if Jongsung.has_jongsung(string) else '를'
        elif (josa == '은') or (josa == '는'):
            return '은' if Jongsung.has_jongsung(string) else '는'
        elif (josa == '이') or (josa == '가'):
            return '이' if Jongsung.has_jongsung(string) else '가'
        elif (josa == '과') or (josa == '와'):
            return '과' if Jongsung.has_jongsung(string) else '와'
        elif (josa == '이나') or (josa == '나'):
            return '이나' if Jongsung.has_jongsung(string) else '나'
        elif (josa == '으로') or (josa == '로'):
            return '으로' if Jongsung.has_jongsung(string) else '로'
        elif (josa == '아') or (josa == '야'):
            return '아' if Jongsung.has_jongsung(string) else '야'
        elif (josa == '이랑') or (josa == '랑'):
            return '이랑' if Jongsung.has_jongsung(string) else '랑'
        elif (josa == '이며') or (josa == '며'):
            return '이며' if Jongsung.has_jongsung(string) else '며'
        elif (josa == '이다') or (josa == '다'):
            return '이다' if Jongsung.has_jongsung(string) else '다'
        elif josa == '이가':
            return '이가' if Jongsung.has_jongsung(string) else '가'
        else:
            raise JosaTypeException

    @classmethod
    def get_full_string(cls, string: str, josa: str) -> str:
        """
        단어 뒤에 조사를 붙여서 반환하는 정적 메서드
        :param string: 입력받는 한글 단어
        :param josa: 체크하고자 하는 조사
        :return: 단어와 조사를 붙인 문자열을 반환
        """
        return string + cls.get_josa(string, josa)


# TODO : Refactor pyjosa's architecture with oop.
# TODO : need to remove duplicated codes with 'if ... elif...' (refactor)
