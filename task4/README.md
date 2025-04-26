### main/views.py
<hr>

```python
from django.contrib.auth import authenticate, login
```

- ```authenitcate```
    - 제공된 자격 증명(일반적으로 사용자 이름과 비밀번호)을 사용하여 Django의 인증 백엔드(autehnticate backends)를 통해 사용자를 인증하려고 시도
    - 인증에 성공하면 해당 ```User``` 객체를 반환
    - 인증에 실해파면 ```None``` 을 반환
    - ```authenticate()``` 함수는 직접 데이터베이스를 조회하는 대신, 설정된 인증 백엔드들에게 자격 증명을 전달하여 인증을 시도하도록 위임
- ```login```
    - 이미 인증된 ```User``` 객체를 사용하여 현재 요청에 대한 사용자 세션을 설정
    - 사용자를 실제 <b>로그인</b>시키는 역할
    - Django의 세션 프레임워크를 사용하여 사용자 ID를 세션에 저장하고, 이후의 요청에서 해당 사용자가 로그인 상태임을 인식할 수 있도록 함
    - 필수 인자로 ```request```, ```User``` 를 받음
    - 함수 호출 후 ```request.user``` 속성을 통해 현재 로그인한 사용자의 정보를 뷰 함수 내에서 접근할 수 있음

```python
username=request.POST['username']
password = request.POST['password']
```

- ```username```, ```password``` 필드가 POST 데이터에 반드시 존재해야 함
- 만약 해당 필드가 존재하지 않으면 KeyError가 발생함

```python
title=request.POST.get('title')
content = request.POST.get('content')
```

- ```content``` 필드가 존재하지 않으면 None을 반환하거나 기본값을 설정할 수 있음
    - ```content = request.POST.get('content', '기본값')```

### templates/attack.html
<hr>

```javascript
<script>
    document.forms[0].submit()//자동으로 전송 ( 사용자 몰래 )
</script>
```

- 페이지가 로그되자마자 현재 페이지의 첫 번째 폼(```document.forms[0]```)을 자동으로 제출

### main/admin.py
<hr>

```python
from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','author','created_at')
    search_fields = ('title', 'content', 'author__username')
```

- ```@admin.reigster(Post)```
    - ```PostAdmin``` 클래스를 ```Post``` 모델과 연결하여 Django 관리자 사이트에 등록하는 역할
    - ```admin.site.register(Post, PostAdmin)``` 과 동일한 효과를 얻을 수 있음
- ```list_display = ('id', 'title', 'author', 'created_at')```
    - ```PostAdmin``` 클래스의 속성
    - 관리자 목록 페이지에 표시할 필드들을 튜플 형태로 정의
- ```search_fields = ('title', 'content', 'author__username')```
    - 관리자 목록 페이지 상단에 검색 기능을 활성화하고, 검색을 수행할 필드들을 튜플 형태로 정의
    - ```author__username```
        - ```Post``` 모델의 ```author``` 필드는 ```User``` 모델과의 ForeignKey 관계를 가지고 있음
        - ```__``` 표기법을 사용하여 연결된 ```User``` 모델의 ```username``` 필드를 검색 대상으로 포함
        - 이를 통해 작성자의 사용자 이름으로도 게시글을 검색할 수 있음음