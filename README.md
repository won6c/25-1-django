### myapp/views.py
<hr>

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
```

- ```from rest_framework.decorators import api_view```
    - DRF(Django Rest Framework)에서 제공하는 데코레이터인 ```api_view```를 가져옴
    - 이 데코레이터는 함수 기반 뷰를 RESTfilAPI 엔드포인트로 변환하는 데 사용됨
- ```from rest_framework.response import Response```
    - Django의 ```HttpResponse``` 대신 DRF의 ```Response```를 사용하여 API 응답을 생성
- ```from rest_framework import status```
    - 다양한 HTTP 상태 코드를 상수로 정의하고 있어 API 응답의 상태를 명확하게 지정하는 데 사용됨

```python
@api_view(['GET'])
```

- ```['GET']```은 API 엔드포인트가 오직 HTTP GET 요청만 처리하도록 지정
- 다른 HTTP 메서드(POST, PUT, DELETE 등)로 요청이 들어오면 DRF는 405 Method Not Allowed 응답을 반환

```python
@api_view(['POST'])
```

- ```['POST']```은 API 엔드포인트가 오직 HTTP POST 요청만 처리하도록 지정
- 다른 HTTP 메서드(GET, PUT, DELETE 등)로 요청이 들어오면 DRF는 405 Method Not Allowed 응답을 반환

### config/settings.py

```python
INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- 앱의 이름 대신 ```rest_framework```를 추가함
    - 앱 이름 대신 ```rest_framework```를 추가한 이유는 <strong>Django REST Framework(DRF) 자체가 하나의 <span style="color:red">독립적인 Django 앱</span>이기 떄문</strong>

## HTTP 요청 메시지의 구조

```
1. 요청 라인(Request Line)
2. 헤더(Headers)
3. 빈 줄(CRLF, 개행)
4. 메시지 바디(Body, 선택적)
```

### 1. 요청 라인(Request Line)

```
<메서드> <요청> <HTTP 버전>

GET /index.html HTTP/1.1
```

- ```GET```, ```POST```, ```PUT```, ```DELETE```
    - HTTP 메서드 ( 동작 종류 )
- ```/index.html```
    - 요청 대상 자원의 경로(URI)
- ```HTTP/1.1```
    - 사용하는 HTTP 프로토콜 버전

### 2. 헤더(Headers)
- 요청에 대한 추가 정보를 담는 부분
- 형식 : ```헤더이름:값```

```
Host: www.example.com
User-Agent: Mozila/5.0
Content-Type:application/x-www-form-urlencoded
Content-Length:34
```

- ```Host```
    - 요청 대상 서버(도메인)
- ```User-Agent```
    - 클라이언트 정보(브라우저, OS 등)
- ```Content-Type```
    - 바디에 담긴 테이터 형식
- ```Content-Length```
    - 바디의 길이(바이트 수)

### 3. 빈 줄(CRLF)
- 헤더와 바디 사이를 구분하는 <b>빈 줄 하나(\r\n)</b>
- 이 줄이 없으면 서버는 "헤더가 끝났는지"를 알 수 없음

### 4. 메시지 바디(Body)
- 주로 ```POST```, ```PUT``` 요청에서 사용
- 클라이언트가 서버에 전달하려는 데이터가 담겨 있음

```username=kimcs&password=1234```

- 이 데이터는 ```Content-Type``` 헤더에 따라 형식이 달라짐

- <b>Content-Type</b>
    - ```application/x-www-form-urlencoded```
        - <i>key=value&key2=value2(폼)</i>
    - ```application/json```
        - <i>{"key":"value"}</i>
    - ```multipart/form-data```
        - <i>파일 업로드 용</i>

#### 5. 추가 사항
- ```GET```요청은 바디가 거의 없고, 데이터는 URL 쿼리 스트링에 포함됨
- ```POST``` 요청은 바디에 데이터를 담고 보냄

## HTTP 응답 메시지 구조

```
1. 상태 라인(Status Line)
2. 헤더(Headers)
3. 빈 줄(CRLF)
4. 메시지 바디(Body, 선택적)
```

### 1. 상태 라인(Status Line)

```
HTTP/1.1 200 OK
```

- ```HTTP/1.1```
    - HTTP 프로토콜 버전
- ```200```
    - 상태 코드(성공, 실패 등 숫자로 표현)
- ```OK```
    - 상태 메시지(상태 코드에 대한 설명)

- <stong>주요 상태 코드</stong>
    - ```200 OK``` - 요청 성공
    - ```301 Moved Permanetly``` - 리다이렉션
    - ```400 Bad Request``` - 클라이언트 오류
    - ```401 Unauthorized``` - 인증 실패
    - ```403 Forbidden``` - 권한 없음
    - ```404 Not Found``` - 리소스 없음
    - ```500 Internal Server Error``` - 서버 내부 오류

### 2. 헤더(Headers)

```
Content-Type : test/htmll charset=UTF-8
Content-Length : 1234
Set-Cookie:sessionid = abc123
```

- 응답에 대한 부가 정보
- <strong>클라이언트가 응답을 어떻게 해석할 지 알려줌</strong>
- ```Content-Type```
    - 응답 본문의 형식(```text/hrml```, ```application/json``` 등)
- ```Content-Length```
    - 본문의 길이(바이트 수)
- ```Set-Cookie```
    - 클라이언트에 쿠키 저장 요청
- ```Cache-Control```
    - 캐시 관련 정책

### 3. 빈 줄(\r\n)
- 헤더와 본문을 구분하는 구분석
- 반드시 한 줄 빈 줄 이썽야 서버가 헤더의 끝을 인식

### 4. 메시지 바디(Body, 선택적)
- 실제 콘텐츠가 담기는 곳(HTML, JSON, 이미지, 파일 등)
- ```Content-Type```에 따라 클라이언트가 이를 해석

## Django HTTP 응답

### 1. 기본 HTML 응답

```python
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("<h1>Hello, Django!</h1>")
```

- ```HttpResponse```
    - 기본적인 문자열(html포함)을 반환
    - ```Content-Type:text/html``` 자동 설정

### 2. 템플릿 렌더링 응답

```python
from django.shortcuts import render

def greeting_view(request):
    context = {'name':'홍길동'}
    return render(request, 'myapp/greeting.html', context)
```

- ```greeting.html``` 템플릿을 렌더링해서 반환
- 내부적으로 ```HttpResponse```로 반환됨 -> ```text/html```

### 3. JSON 응답

```python
from django.http import JsonResponse

def api_data(request):
    data = {'status':'ok', 'message':'요청 성공'}
    return JsonResponse(data)
```

- ```Content-Type:application/json``` 자동 설정
- ```dict``` 또는 ```list``` 형태만 반환 가능

### 4. 파일 다운로드 응답

```python
from django.http import FileResponse

def download_file(request):
    filepath = 'static/files/example.pdf'
    return FileResponse(open(filepath, 'rb', as_attachment=True, filename='example.pdf'))
```

- 브라우저에서 파일 다운로드 창이 열림
- ```as_attachment=True```가 핵심
    - 웹 서버가 클라이언트에게 응답을 보낼 때, 해당 응답의 내용을 웹 페이지에 내장하여 보여주는 대신, 파일로 다운로드하도록 지시하는 옵션
- ```application/octet-stream``` 또는 ```바이너리```

### 5. 상태 코드 변경 응답

```python
from django.http improt HttpResponseNotFound

def not_found_view(request):
    return HttpResponseNotFound("<h1>404 - 페이지를 찾을 수 없습니다</h1>") 
    #return HttpResponse("권한 없음", status=403)
```

- 에러 응답
    - ```HttpResponseNotFound```, ```HttpResponseForbidden``` 등
- Content-Type으로는 다양함함
