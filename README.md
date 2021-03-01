# Pyjosa

- 입력받은 한글 문자에 종성이 있을경우, 없을 경우를 구분하여 `을/를`, `이/가`와 같은 조사를 자동으로 붙여주는 패키지

- `PyPI`를 통해 배포 할 예정.

## 설치

`python3 -m pip install pyjosa`

## 사용법

```python3
from pyjosa.josa import Josa

s = '오리'
s2 = '철수'
    
print(f'{s}{Josa.get_josa(s, "이")}') # 오리가 
print(f'{s2}{Josa.get_josa(s2, "을")}') # 철수를
```

## Core Concept

- 추후 작성 예정

## release

- 추후 작성 예정

## Contribute

- 추후 작성 예정



