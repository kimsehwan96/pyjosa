# 유용한 사용 방법

```python
from pyjosa.josa import Josa

subject = '철수'
obj = '산'

full_string = f'{Josa.get_full_string(subject, "은")} {Josa.get_full_string(obj, "를")} 간다'

print(full_string) # 철수는 산을 오른다
```

```python
from pyjosa.josa import Josa

subjects = ['철수', '세환', '길동']
obj = ['산', '바다', '집']

for i, v in enumerate(subjects):
    print(f'{Josa.get_full_string(v, "은")} {Josa.get_full_string(obj[i], "를")} 간다')

```