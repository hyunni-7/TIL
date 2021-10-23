# 🔥 Django Notes

*   Sanghyun Park



##### Content

>   1.   가상환경 구축
>   2.   Django Project 생성 및 App 등록
>   3.   



## 001. 가상환경 구축



##### 001.1. 가상환경 생성

```bash
$ python -m venv venv
```



##### 001.2. Django 라이브러리 설치

```bash
$ pip install django
```





## 002. Django Project 생성 및 App 등록



##### 002.1. Project 생성

```bash
# project의 이름으로 Python이나 Django에서 사용 중인 키워드 사용 불가, hyphen 사용 불가
$ django-admin startproject comp_prac .
```



##### 002.2. App 생성

```bash
$ python manage.py startapp articles  # 복수형 권장
$ python manage.py startapp accounts
```



##### 002.3. App 등록

*   App을 **먼저 생성한 후**, settings.py에 등록해야 정상적으로 동작

```python
INSTALLED_APPS = [
    # my apps
    'articles',
    'accounts',
    
    # 3rd-party apps
    
    # Django default apps
]
```



>   **참고.** 서버 실행
>
>   ```bash
>   $ python manage.py runserver
>   ```



>   **참고.** 환경 설정
>
>   ```python
>   LANGUAGE_CODE = 'ko-kr'  # 언어 설정, USE_I18N 값이 True이어야 적용 가능
>   
>   TIME_ZONE = 'Asia/Seoul'  # DB 타임존 설정, USE_TZ 값이 True이어야 에러가 발생하지 않음
>   
>   USE_I18N = True
>   
>   USE_L10N = True  # 날짜/시간 지역 서식 적용 여부
>   
>   USE_TZ = True
>   ```

