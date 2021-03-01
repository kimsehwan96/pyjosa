from pyjosa.jonsung import has_jongsung

class Josa:
    def __init__(self):
        pass

    @staticmethod
    def get_josa(string, josa):
        if (josa == '을') or (josa =='를'):
            return '을' if has_jongsung(string) else '를'
        elif (josa == '은') or (josa =='는'):
            return '는' if has_jongsung(string) else '은'
        elif (josa == '이') or (josa =='가'):
            return '이' if has_jongsung(string) else '가'
        else:
            raise Exception("아직 구현중임")



    @staticmethod
    def get_full_string(string, josa):
        pass

# TODO: make main function as class's static method? or not a class's static method just a function.


if __name__ =="__main__":
    s = '오리'
    s2 = '철수'
    
    print(f'{s}{Josa.get_josa(s, "이")}') # 오리가 
    print(f'{s2}{Josa.get_josa(s2, "을")}') # 철수를
    # 사용법이 너무 어려워 보이는데?
    # 더 나은 사용법 제공을 위해 고민하기.