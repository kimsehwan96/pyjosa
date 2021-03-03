from pyjosa.jonsung import has_jongsung


class Josa:

    @staticmethod
    def get_josa(string, josa) -> str:

        if (josa == '을') or (josa == '를'):
            return '을' if has_jongsung(string) else '를'
        elif (josa == '은') or (josa == '는'):
            return '은' if has_jongsung(string) else '는'
        elif (josa == '이') or (josa == '가'):
            return '이' if has_jongsung(string) else '가'
        elif (josa == '과') or (josa == '와'):
            return '과' if has_jongsung(string) else '와'
        elif (josa == '이나') or (josa == '나'):
            return '이나' if has_jongsung(string) else '나'
        elif (josa == '으로') or (josa == '로'):
            return '으로' if has_jongsung(string) else '로'
        else:
            raise Exception("올바르지 않은 조사.")

    @classmethod
    def get_full_string(string, josa) -> str:

        if (josa == '을') or (josa == '를'):
            return string + '을' if has_jongsung(string) else string + '를'
        elif (josa == '은') or (josa == '는'):
            return string + '은' if has_jongsung(string) else string + '는'
        elif (josa == '이') or (josa == '가'):
            return string + '이' if has_jongsung(string) else string + '가'
        elif (josa == '과') or (josa == '와'):
            return string + '과' if has_jongsung(string) else string + '와'
        elif (josa == '이나') or (josa == '나'):
            return string + '이나' if has_jongsung(string) else string + '나'
        elif (josa == '으로') or (josa == '로'):
            return string + '으로' if has_jongsung(string) else string + '로'
        else:
            raise Exception("올바르지 않은 조사.")
