# Pyjosa - 파이썬 한글 조사 처리 모듈

![PyPI](https://img.shields.io/pypi/v/pyjosa?style=plastic)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyjosa)
![GitHub](https://img.shields.io/github/license/kimsehwan96/pyjosa) ![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/kimsehwan96/pyjosa/Publish%20Python%20%F0%9F%90%8D%20distributions%20%F0%9F%93%A6%20to%20PyPI/release) ![PyPI - Downloads](https://img.shields.io/pypi/dm/pyjosa) 

## Pyjosa?

`Pyjosa`는 파이썬 한글 조사 처리 모듈입니다. 한글의 `은/는`, `이/가`와 같은 조사를 자동으로 처리해줍니다.

단어의 마지막 글자에 종성이 있는지 없는지에 따라서 조사가 결정됩니다. 

예를들어 `세환``이/가` 에서는 `세환`이라는 단어가 종성이 있기 때문에 `이`라는 종성이 붙어야 합니다.

이러한 종성에 따른 조사처리의 부담을 덜어주고자 시작한 프로젝트입니다.

## 기능

총 두가지의 인터페이스를 제공합니다. 

첫번째는, 조사를 붙이고자 하는 단어를 입력하고, 붙이고 싶은 조사를 입력하면, 올바른 조사를 리턴합니다.

두번째는, 조사를 붙이고자 하는 단어를 입력하고, 붙이고 싶은 조사를 입력하면, 조사를 붙인 문자열을 리턴합니다.

## 예제


```python
from pyjosa.josa import Josa

print(Josa.get_josa("철수", "은")) # 는
print(Josa.get_josa("오리", "을")) # 를
print(Josa.get_josa("닭", "는")) # 은
print(Josa.get_josa("산", "으로")) # 으로
print(Josa.get_josa("명예", "과")) # 와
print(Josa.get_josa("물", "나")) # 이나
# 사람 이름 + 이가/가 를 구분하기 위해서는 조사부분에 '이가'를 입력합니다.
print(Josa.get_josa("예나", "이가")) # 가
print(Josa.get_josa("세환", "이가")) # 이가

print(Josa.get_full_string("철수", "은")) # 철수는
print(Josa.get_full_string("오리", "을")) # 오리를
print(Josa.get_full_string("닭", "는")) # 닭은
print(Josa.get_full_string("산", "으로")) # 산으로
print(Josa.get_full_string("명예", "과")) # 명예와
print(Josa.get_full_string("물", "나")) # 물이나
# 사람 이름 + 이가/가 를 구분하기 위해서는 조사부분에 '이가'를 입력합니다.
print(Josa.get_full_string("예나", "이가")) # 예나가
print(Josa.get_full_string("세환", "이가")) # 세환이가
```

## 깃허브 주소

https://github.com/kimsehwan96/pyjosa

## 기여 방법

아직 미정입니다.