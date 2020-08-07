from django.db import models

class Post(models.Model):
    author = models.CharField('작성자',max_length=20)  # 1줄짜리 입력칸이 CharField
    contents = models.TextField('글내용',max_length=1000) # TextField는 여러줄에 걸친 입력상자
    # author와 contents를 다른 함수를 준 이유는 modelform이 html의 입력상자를 자동으로 생성해주기때문에
    # 사용용도에 알맞은 필드를 입력

    def __str__(self):
        return self.contents

class Datt(models.Model):
    author_text=models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.CharField('사용자', max_length=20)
    contents = models.CharField('글내용', max_length=50)

    def __str__(self):
        return self.contents

class User(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    username = models.CharField(max_length=64,verbose_name = '사용자명')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')

    def __str__(self): # 이 함수 추가
        return self.username  # User object 대신 나타낼 문자
    #저장되는 시점의 시간을 자동으로 삽입해준다.


    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_user'
