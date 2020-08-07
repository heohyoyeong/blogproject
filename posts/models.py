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


