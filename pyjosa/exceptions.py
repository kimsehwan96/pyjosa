class NotHangleException(Exception):
    def __init__(self):
        super().__init__("마지막 글자가 한글이 아닙니다.")
