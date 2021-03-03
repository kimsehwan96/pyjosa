# Pyjosa

- 입력받은 한글 문자에 종성이 있을경우, 없을 경우를 구분하여 `을/를`, `이/가`와 같은 조사를 자동으로 붙여주는 패키지

- `PyPI`를 통해 배포 할 예정.

## 설치

`python3 -m pip install pyjosa`

## 사용법

```python3
from pyjosa.josa import Josa

print(Josa.get_josa("철수", "은")) # 는
print(Josa.get_josa("오리", "을")) # 를
print(Josa.get_josa("닭", "는")) # 은
print(Josa.get_josa("산", "으로")) # 으로
print(Josa.get_josa("명예", "과")) # 와
print(Josa.get_josa("물", "나")) # 이나

print(Josa.get_full_string("철수", "은")) # 철수는
print(Josa.get_full_string("오리", "을")) # 오리를
print(Josa.get_full_string("닭", "는")) # 닭은
print(Josa.get_full_string("산", "으로")) # 산으로
print(Josa.get_full_string("명예", "과")) # 명예와
print(Josa.get_full_string("물", "나")) # 물이나

```

## Core Concept

- 추후 작성 예정

## release

- 추후 작성 예정

## Contribute

- 추후 작성 예정



