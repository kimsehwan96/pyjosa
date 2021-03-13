# 간단한 사용 방법

```python
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