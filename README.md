### books/models.py
<hr>

```python
@classmethod
def get_all_books(cls)->QuerySet['Book']:
    return cls.objects.all()
```

- ```@classmethod```
    - ```get_all_books``` 메서드를 클래스 메서드로 만듬
    - 클래스 메서드는 클래스 자체에 바인딩되며, 클래스의 인스턴스가 아닌 클래스를 통해 호출됨
    - 첫 번째 매개변수로 클래스 자체를 받는 ```cls``` 를 사용함
- ```def get_all_books(cls)```
    - ```get_all_books``` 라는 이름의 메서드를 정의
    - 이 메서드는 ```Book``` 객체를 가져오는 역할
    - ```cls``` 매개변수는 이 메서드가 호출될 때 해당 클래스(Book)를 자동으로 받음
    - ```->QuerySet['Book']``` 은 타입 힌트
        - 이 메서드가 반환할 것으로 예상되는 값의 타입을 나타냄
- ```return cls.objects.all()```
    - Django 모델은 자동으로 ```objects``` 라는 매니저를 생성
    - 이 메니저는 DB와 상호작용하는 메서드들을 제공
    - ```all()``` 해당 모델의 모든 레코드를 DB에서 가져옴

### objects filter keywords
<hr>

```python
__exact
```

- <b>대소문자 구분 - 정확히 일치해야만 함</b>
- 사용법
    - ```<keyword>__exact=<문자열>``` -> author__exact="J.K.Rowling"

<br>

```python
__iexact
```

- <b>대소문자를 구분하지 않는 정확한 일치</b>를 의미
- 사용법
    - ```<keyword>__iexact=<문자열>``` -> author__iexact="J.K.Rowling"

<br>

```python
__contains
```

- <b>대소문자 구분 - 포함 여부</b>
- 사용법
    - ```<keyword>__conains=<문자열>``` -> title__contains="magic"

<br>

```python
__icontains
```

- <b>대소문자를 구분하지 않고</b> 주어진 문자열이 포함되어 있는지를 검사
- 사용법
    - ```<keyword>__icontains=<문자열>``` -> title__icontains="magic"

