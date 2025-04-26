### authenticate
<hr>

```authenticate```

- 사용자 인증을 수행(아이디/비밀번호가 맞는지 확인)
- 유저 인증 처리(비밀번호 확인 포함)

<br>

```login```

- 인증된 사용자를 현재 세션에 로그인 처리함
- ```login(request, user)```
  - 사용자 정보를 세션에 저장하여 ```request.user``` 가 로그인된 사용자로 인식되게 만듬
  - 내부적으로 Django의 세션 프레임워크를 사용하여 ```sessionid```쿠키를 설정함
  - 이로써 다음 요청부터는 ```request.user.is_authenticated==True``` 로 동작함
  - 세션에 사용자 등록(로그인 처리)
    - ```request.user``` : 현재 로그인된 사용자 객체 
<br>

```logout```

- 사용자의 인증 세션을 종료(로그아웃)하는 함수
- 주로 ```django.contrib.auth``` 모듈에 포함되어 있음
- ```logout(request)```는 현재 요청과 연결된 사용자의 세션 데이터를 삭제
- 로그아웃 처리가 끝나면 일반적으로 ```redirect```를 통해 로그인 화면 또는 홈페이지로 이동
- ```request.user```는 이후에 ```Anonymous```객체로 바뀜
- 세션에서 사용자 제거(로그아웃 처리)

### 주의사항

- ```logout```은 클라이언트의 세션 쿠키를 무효화하지만, 실제로 세션 객체는 서버에 남아 있을 수 있음(세션 만료 설정에 따라)
- 로그아웃 시 관련 로그를 남기거나 추가 처리가 필요하다면, ```logout_view()```안에 추가하면 됨
  - Django에서는 세션 정보를 서버(DB, 캐시 등)에 저장해 놓음
  - 클라이언트(브라우저)는 세션 ID만 들고 있고, 실제 데이터는 서버가 관리함
  - ```logout(request)```를 하면 클라이언트 세션 쿠키는 삭제되지만, <strong>서버에 저장된 세션 데이터(django_session 테이블 등에 있는)는 바로 지워지지 않을 수 있다는 의미</strong>
  - Django 세션은 보통 세션 만료 설정에 따라 일정 시간 이후 자동 삭제됨 -> ```logout(request)```를 했다고 바로 서버 DB에서 세션이 지워지는 게 아님, 그냥 쓸모없는 데이터로 남아있다가 자동으로 삭제되는 것임
  - 보안이 중요한 서비스라면
    - 로그아웃할 때 세션을 강제로 삭제하거나

```python
from django.contrib.auth import logout
import logging

logger = logging.getLogger(__name__)

def logout_view(request):
    logger.info(f"User {request.user} logged out.")  # 로그 기록
    logout(request)
    return redirect('login')
```

    - 로그를 남겨서 "언제 누가 로그아웃했는지" 기록하는 처리가 필요할 수 있음

```python
def logout_view(request):
    if request.user.is_authenticated:
        request.session.flush()  # 서버 세션도 통째로 삭제
    logout(request)
    return redirect('login')
```
