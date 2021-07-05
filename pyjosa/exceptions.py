class NotHangleException(Exception):
    def __init__(self):
        super().__init__("마지막 글자가 한글이 아닙니다.")

class JosaTypeException(Exception):
    def __init__(self):
        super().__init__("메서드의 인자로 주어진 조사가 올바르지 않습니다.")

class JongsungInstantiationException(Exception):
    def __init__(self):
        super().__init__("종성 클래스는 인스턴스화 할 필요가 없습니다.")