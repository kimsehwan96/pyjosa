# Pyjosa

![PyPI](https://img.shields.io/pypi/v/pyjosa?style=plastic)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyjosa)
![GitHub](https://img.shields.io/github/license/kimsehwan96/pyjosa) ![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/kimsehwan96/pyjosa/Publish%20Python%20%F0%9F%90%8D%20distributions%20%F0%9F%93%A6%20to%20PyPI/release) 

![PyPI - Downloads](https://img.shields.io/pypi/dm/pyjosa) 

입력받은 한글 문자에 종성이 있을경우, 없을 경우를 구분하여 `을/를`, `이/가`와 같은 조사를 자동으로 붙여주는 패키지

`PyPI`에 배포 하였음. 현재 버전 ![PyPI](https://img.shields.io/pypi/v/pyjosa?style=plastic)

## 공식 도큐먼트

https://kimsehwan96.github.io/pyjosa/

## 설치

`python3 -m pip install pyjosa`

혹은

`pip install pyjosa`

## 사용법

```python3
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
print(Josa.get_josa("예나", "이가")) # 예나가
print(Josa.get_josa("세환", "이가")) # 세환이가

```

## Core Concept


## Release


## Contribute





