# 지원되는 조사

1. 을 / 를
2. 은 / 는
3. 이 / 가
4. 과 / 와
5. 이나 / 나
6. 으로 / 로
7. 아 / 야
8. 이랑 / 랑
9. 이며 / 며
10. 이다 / 다
11. 이가 / 가

## 각 케이스별 사용 방법

word는 조사를 붙이고자 하는 문자열입니다. 

예시 :

```python3
from pyjosa.josa import Josa

word = '예나'

print(Josa.get_josa(word, '이가')) # 가
```

### 을/를
   - `Josa.get_josa(word, '을')`
   - `Josa.get_josa(word, '를')`
### 은/는
   - `Josa.get_josa(word, '은')`
   - `Josa.get_josa(word, '는')`
### 이/가
   - `Josa.get_josa(word, '이')`
   - `Josa.get_josa(word, '가')`
### 과/와
   - `Josa.get_josa(word, '과')`
   - `Josa.get_josa(word, '와')`
### 이나/나
   - `Josa.get_josa(word, '이나')`
   - `Josa.get_josa(word, '나')`
### 으로/로
   - `Josa.get_josa(word, '으로')`
   - `Josa.get_josa(word, '로')`
### 아/야
   - `Josa.get_josa(word, '아')`
   - `Josa.get_josa(word, '야')`
### 이랑/랑
   - `Josa.get_josa(word, '이랑')`
   - `Josa.get_josa(word, '랑')`
### 이며/며
   - `Josa.get_josa(word, '이며')`
   - `Josa.get_josa(word, '며')`
### 이다/다
   - `Josa.get_josa(word, '이다')`
   - `Josa.get_josa(word, '다')`
### 이가/가
   - `Josa.get_josa(word, '이가')`

    