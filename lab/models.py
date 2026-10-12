from django.db import models


class Auth(models.Model):
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()

    # 기존 테이블 사용, Django에서 생성하지 않음 (lab_auth를 미리 준비해야 함)
    class Meta:
        db_table = "lab_auth"
        managed = False

    def __str__(self):
        return self.account
