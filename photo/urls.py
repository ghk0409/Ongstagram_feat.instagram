from django.urls import path
from .views import *
# Detail 뷰를 views.py로 옮기기 때문에 필요없는 임포트 지우기
# from django.views.generic.detail import DetailView # 여기서 Detail 뷰 추가
# from .models import Photo

# 네임스페이스(namespace) 설정
# [app_name:URL패턴 이름] 형태로 URL 템플릿 태그 사용 가능
app_name = 'photo'

urlpatterns = [
    # 함수형 뷰는 함수 이름으로 호출, 클래스형 뷰는 클래스명.as_view()로 호출
    path('', photo_list, name='photo_list'),
    # views.py가 아닌 여기에 inline 코드로 뷰 만들기
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'), # model=Photo, template_name='photo/detail.html'
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]