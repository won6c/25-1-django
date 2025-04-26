### qa/models.py
<hr>

```python
from django.contrib.auth.models import User
```

- <b>Django</b>의 내장 사용자 인증 모델(User)을 가져오는 코드
    - <b><span style="color:ORANGE">Django의 내장 User 모델을 가져옴</span></b> : Django는 사용자 인증 시스템을 제공하며, User 모델은 이를 관리하는 기본 모델
    - <b><span style="color:ORANGE">사용자 정보 관리</span></b> : ```User``` 모델을 사용하여 로그인, 회원가입, 권한 관리 등을 수행할 수 있음
    - <b><span style="color:ORANGE">데이터베이스의 ```auth_user``` 테이블과 연결</span></b> : Django가 기본적으로 생성하는 ```auth_user``` 테이블과 연결되어 사용자 정보를 저장

```python
class Question(models.Model):
```

- Question class가 Django의 <b><span style="color:orange">models.Model클래스를 상속</span></b> 받음
- models.Model 클래스는 <b><span style="color:orange">데이터베이스 테이블과 매핑되는 파이썬 클래스를 만들기 위한 기본 클래스</span></b>
- 즉, <b><span style="color:orange">Question class는 데이터베이스의 테이블 구조를 정의하는 것<span></b>

```python
author = models.ForeignKey(User, on_delete=models.CASCADE)
```

- Django의 내장 User 모델과의 ```Foreign Key``` 관계를 설정
    - ```ForeignKey(User)``` : author 필드가 User 모델의 인스턴스와 연결됨을 나타냄<br> -> 각 Question 인스턴스는 하나의 User 인스턴스를 참조
- ```on_delete=models.CASCADE``` : <b><span style="color:orange">참조하고 있는 User 인스턴스가 데이터베이스에서 삭제될 경우, 해당 User가 작성한 모든 Question 인스턴스도 함께 삭제되도록 설정</span></b>

```python
question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
```

- ```related_name="answers"```
    - Question 모델에서 이 Answer 모델로의 역참조 이름을 ```answers```로 나타냄
    - 이를 통해 question 객체에서 ```question.answers.all()```과 같은 방식으로 해당 질문에 달린 모든 답변을 쉽게 조회 가능

### qa/admin.py
<hr>

```python
admin.site.register(Question)
admin.site.register(Answer)
```

- ```admin.site``` : Django의 관리자 사이트와 관련된 기능을 제공하는 전역 객체
    - ```.register(Question)``` : ```register()``` 메서드는 특정 모델 클래스를 Django 관리자 사이트에 등록하는 역할
    - ```Question``` <b><span style="color:orange">모델 클래스를 관리자 사이트에 등록</span></b>하여, 관리자 인터페이스에서 ```Question```모델의 데이터를 <b>생성, 조회, 수정, 삭제할 수 있는 기능을 활성화</b>

### config/settings.py
<hr>

```python
INSTALLED_APPS = [
    'qa',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- ```INSTALLED_APPS``` : Django 설정파일(settimgs.py)에 있는 리스트 변수
    - Django 프로젝트에서 활성화할 애플리케이션들의 이름을 담고 있음
    - ```qa``` : 프로젝트 내에서 직접 개발한 애플리케이션의 이름    

### qa/views.py
<hr>

```python
from django.shortcuts import render, get_object_or_404, redirect
```

- ```render```
    - <b>주어진 템플릿을 지정된 컨텍스트 데이터와 결합하여 HTML 응답을 생성하는 함수</b>
    - 일반적으로 웹 페이지를 보여줄 때 사용
    - 템플릿 파일(.html)을 찾고, 파이썬 변수(컨텍스트)의 값을 템플릿에 넣어 최종 HTML 코드를 생성하여 클라이언트에게 보냄
    - 인자로는 주로 ```request```객체, 탬플릿 파일 경로(문자열), 그리고 템플릿에 전달할 데이터(딕셔너리)를 받음
- ```get_object_or_404```
    <b> 주어진 모델과 검색 조건(pk=id)을 사용하여 데이터베이스에서 해당 객체를 조회하는 함수</b>
    - <b><span style="color:orange">조건에 맞는 객체가 존재하면 해당 객체를 반환</span></b>
    - <b><span style="color:orange">조건에 맞는 객체가 존재하지 않으면 자동으로 Http404 예외를 발생시킴</span></b>
    - 객체가 없는 경우에 대한 예외 처리를 직접 작성하는 대신 이 함수를 사용하면 코드를 간결하고 가독성 있게 만들 수 있음
- ```redirect```
    - HTTP 리다이렉션 응답을 생성하는 함수
    - 클라이언트의 브라우저에게 특정 URL로 다시 요청하도록 지시

```python
from django.contrib.auth.decorators import login_required
```

- 데코레이터(Decorator)
    - 함수나 클래스의 기능을 변경하거나 확장하는 데 사용되는 특별한 종류의 함수
    - <b><span style="color:orange">원래 함수를 감싸서 추가적인 기능을 덧붙이는 역할을 함</span></b>
- <span style="color:yellow">```@login_required```</span>
    - 해당 뷰에 접근하려는 사용자가 로그인했는지 확인
    - 로그인하지 않은 사용자라면 설정된 로그인 페이지로 리다이렉션 시킴
    - 로그인한 사용자라면 정상적으로 뷰 함수를 실행

```python
def question_list(request):
    questions = Question.objects.order_by("-created_at")
    return render(request, 'qa/question_list.html',{"questions":questions
```

- ```Question.objects```
    - Django의 <b><span style="color:orange">ORM(Object-Relational Mapper)</span></b>을 통해 ```Question```모델과 관련된 데이터베이스 queryset을 가져옴
    - queryset에는 데이터베이스에서 가져온 객체들의 컬렉션을 나타냄
- ```.order_by("-created_at")```
    - queryset에 포함된 질문 객체들을 ```creted_at``` 필드를 기준으로 정렬하는 메서드
    - ```-``` : 내림차순으로 정렬을 의미 -> 가장 최근에 생성된 질문부터 표시됨

```python
def question_detail(request, pk):
    question = get_object_or_404(Question, pk = pk)

    if request.method=="POST":
        content = request.POST.get('content')
        if content and request.user.is_authenticated:
            Answer.objects.create(
                question = question,
                content = content,
                author = request.user,
                created_at = timezone.now()
            )
            return redirect('question_detail',pk=pk)
    return render(request, 'qa/question_detail.html',{"question":question})
```

- ```def question_detail(request, pk):```
    - ```pk```
        - URL을 통해 전달되는 값
        - Question 객체를 식별하는 기본 키( prime key )
        - Django는 URL 패턴에서 이 pk 값을 추출하여 뷰 함수의 인자로 전달
- ```return redirect('question_detail',pk=pk)```
    - ```question_detail```
        - URL 패턴의 이름
    - ```pk=pk```
        - 리다이렉션할 URL에 필요한 인자를 전달
        - pk값을 다시 전달하여 답변이 성공적으로 등록된 후에도 같은 질문 상세 페이지를 보여주도록 함

### qa/urls.py
<hr>

```python
from django.urls import path
from . import views

urlpatterns = [
    path('',views.question_list, name="question_list"),
    path('question/<int:pk>',views.question_detail, name='question_detail'),
    path('ask/',views.ask_question, name='ask_question')
]
```

- ```question/<int:pk>```
    - ```/question/``` 뒤에 정수형(int)변수 ```pk```가 오는 URL과 매칭된
    - <span style="color:red">```<int:pk>```</span> : Django의 경로 변환기, <b><span style="color:orange">URL의 해당 부분을 정수로 변환하여 뷰 함수의 인자로 전달</span></b>

```python
from django.contrib.auth import views as auth_views
urlpatterns+=[
    path("login/",auth_views.LoginView.as_view(template_name="qa/login.html"),name='login'),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
]
```

- ```from django.contrib.auth import views as auth_views```
    - Django의 ```django.contrib/auth``` 애플리케이션에서 ```views```모듈을 가져옴
    - ```as auth_views``` : ```views```모듈에 ```auth_views```라는 별칭을 부여
- ```auth_views.LoginView.as_view(template_name="qa/login.html")```
    - ```auth_views.LoginView``` : Django가 제공하는 내장 클래스 기반 뷰, 사용자 로그인 기능을 처리
    - ```.as_view()``` : 클래스 기반 뷰를 호출 가능한 뷰 함수로 변환
    - ```template_name="qa/login.html"``` : 로그인 폼을 랜더링하는 데 사용할 템플릿 파일의 경로를 지정

### qa/templates/login.html
<hr>

```html
{% extends "qa/base.html" %}
{% block content %}
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">Login</button>
    </form>
{% endblock content %}
```

- ```{% extends "qa/base.html%}```
    - Django 템플릿 상속을 나타내는 탬플릿 태그
- ```{% block content %}```
    - 템플릿 블록을 정의하는 템플릿 태그
    - ```content```라는 이름을 가진 블록을 시작
    - 현재 템플릿의 이 ```{% block content %}```와 ```{% end content %}``` 사이의 내용은 부모 템플릿의 ```content``` 라는 이름으로 정의되어 있음
- ```{{form.as_p}}```
    - ```form```
        - 뷰 함수에서 템플릿으로 전달된 폼(form) 객체를 나타냄
        - Django의 폼은 폼 필드, 유효성 감사 규칙 등을 포함
    - ```.as_p```
        - 폼 객체의 각 필드를 ```<p>```태그로 감싸서 HTML 형태로 랜더링하는 필터
        - 폼 필드의 레이아웃을 간ㄷ나하게 처리할 수 있도록 해줌
        - 폼 필드의 레이블과 입력 요소 등이 자동으로 생성되어 표시됨

### qa/templates/base.html
<hr>

```html
<!DOCTYPE html>
<head>
    <title>
        QnA Site
    </title>
</head>
<body>
    <h1><a href="/">QnA</a></h1>
    {% if user.is_authenticated %}
        <form action="{% url 'logout' %}" method="post" style="display:inline;">
            {% csrf_token %}
            <button type="submit">Logout</button>
        </form>
    {% else %}
        <p><a href="/login/">Login</a></p>
    {% endif %}
    <hr>
    {% block content%}{% end block %}
</body>
```

- ```{% if user.is_authenticated %}```
    - Django 템플릿 언어의 조건문
    - ```user``` 객체가 인증된 사용자(로그인한 사용자)인지 확인
- ```<form action="{% url 'logout' %}" method="post" style="display:inline;">```
    - ```action="{% url 'logout' %}"```
        - 폼 데이터가 제출될 URL을 지정
        - ```{% url 'logout' %}``` 는 urls.py에 정의된 ```name```이 'logout'인 URL 패턴을 동적으로 가져오는 Django 템플릿 태그
        - 절대로 ```<a href="/logout/">Logout</a>``` 형태로 하면 안됨
