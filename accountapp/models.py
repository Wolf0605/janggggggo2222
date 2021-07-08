from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
    # 마이그래이션을 통해서 db 를 만들고 model 을 통해서 db 의 한줄을 HelloWorld 로 추가 #}