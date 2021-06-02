from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # 모델 객체들의 정렬 기준 설정 // ['-updated']: updated 내림차순으로 정렬
        ordering = ['-updated']

    # 글 작성자와 글 작성일 반환
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    # 객체 상세 페이지 URL 반환
    def get_absolute_url(self):
        # 'photo:photo_detail': 상세 페이지 뷰 이름
        # args로 URL 만들 때 필요한 pk값들을 전달함
        return reverse('photo:photo_detail', args=[str(self.id)])