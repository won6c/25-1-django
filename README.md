### config/settings.py
<hr>

```python
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

- Django 프로젝트의 설정 파일(settings.py)에서 미디어 파일을 처리하기 위한 설정을 정의하는 부분
- ```MEDIA_URL = '/media/'```
    - ```MEDIA_URL``` : Django의 설정변수
    - 웹 브라우저에서 미디어 파일에 접근할 때 사용되는 기본 URL 접두사를 정의

### request_test/models.py
<hr>

```python
from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

- ```file = models.FIleField(upload_to='uploads/')```
    - ```UploadedFile``` 모델의 ```file``` 필드를 정의
    - ```models.FileField``` : 파일을 저장하는 데 사용되는 필드 타입
    - ```upload_to='uploads/'``` : 업로드 된 파일이 저장될 서버의 하위 디렉토리를 지정, Django는 자동으로 이 디렉토리를 생성함(권한이 있다면)

### request_test/templates/upload_file.html
<hr>

```python
<h2>📤파일 업로드</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <label>제목 : </label><br>
    <input type="text" name="title"><br><br>

    <label>파일 선택 : </label><br>
    <input type="file" name="file"><br><br>

    <button type="submit">업로드</button>
</form>

{% if uploaded_file_url %}
    <h3>업로드 결과</h3>
    <p><strong>제목:</strong>{{title}}</p>
    <p><a href="{{ uploaded_file_url }}">업로드된 파일 보기</a></p>
{% endif %}
```

- ```<form method='post' enctype='multipart/form-data'>```
    - ```enctype='multipart/form-data'``` : 폼 데이터의 인코딩 방식을 지정, 파일을 업로드할 때는 반드시 이 속성을 사용해야 함

### config/urls.py
<hr>

```python
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- ```from django.conf.urls.static import static```
    - Django에서 개발환경에서 정적 파일(static files)과 미디어 파일(media files)을 제공하기 위한 URL 패턴을 자동으로 생성해주는 도우미 함수
    - ```static``` : 웹 애플리케이션의 레이아웃이나 동작을 정의하는 데 사용되는 변하지 않는 파일들 - CSS, JS 등
    - ```media``` : 사용자가 애플리케이션에 업로드하는 파일들 - 이미지, 문서, 동영상 등등
- ```urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)```
    - ```static``` 함수를 사용하여 정적 파일과 미디어 파일을 직접 제공
    - ```settings.MEDIA_URL```로 시작하는 URL 요청이 들어오면 ```settings.MEDIA_ROOT```에 있는 파일을 찾아서 제공하도록 Django의 URL 패턴에 추가하는 역할

### request 주요 속성과 기능
<hr>

```request.method```

- 요청 방식(문자열)
- ```GET```, ```POST```, ```PUT```, ```DELETE```

<br><br>

```request.GET```

- ```GET``` 방식으로 전달된 쿼리 파라미터(딕셔너리처럼 사용)

<br><br>

```request.POST```

- ```POST``` 방식으로 전달된 <strong>폼 데이터</strong>

<br><br>

```request.FILES```

- 업로드된 파일 정보

<br><br>

```request.user```

- 현재 로그인한 사용자 객체(```User``` 또는 ```Anonymous```)
- ```is_authenticated``` 로 로그인 여부 확인 가능

<br><br>

```request.session```

- 서버 측 세션 데이터(로그인 상태 유지, 장바구니 등)

<br><br>

```request.COOKIES```

- 클라이언트가 보낸 쿠키 정보

<br><br>

```reqeust.META```

- HTTP 헤더 및 환경 변수 딕셔너리
- ```User-Agent```, ```IP```, ```Router```

<br><br>

```request.path```

- 요청된 URL 경로 (쿼리스트링 제외)

<br><br>

```reqeust.build_absolute_uri()```

- 현재 URL의 절대 경로 반환(도메인 포함)

<br><br

- Django 템플릿에서는 context라는 딕셔너리 전체를 넘기지 않습니다.
- render(request, template_name, context)를 호출하면 context 딕셔너리의 키(key) 들이 템플릿에 각각 변수로 등록됩니다.
- 그래서 {{context.user}}가 아닌 {{user}}를 사용한다.
