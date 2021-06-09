from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# 함수형 뷰로 photo_list 뷰 만들기
# 함수형 뷰는 모든 기능을 직접 처리해야 함(상속 받지 못해서)
# 함수형 뷰는 Decorator 사용
@login_required()
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

# 클래스형 뷰는 Mixin을 첫 번째로 상속받도록
# 제네릭 뷰로 PhotoUploadView 만들기
class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    # 업로드 후 이동할 페이지 호출을 위한 메서드
    # form_valid 메서드를 오버라이드해서 작성자 설정 기능 추가
    def form_valid(self, form):
        # 작성자 = 현재 로그인 한 사용자
        form.instance.author_id = self.request.user.id

        # 이상 없을 시, DB 저장
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        # 이상 있을 시, 작성된 내용 그대로 작성 페이지에 표시
        else:
            return self.render_to_response({'form':form})

# 제네릭 뷰로 PhotoDeleteView 만들기
class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

# 제네릭 뷰로 PhotoUpdateView 만들기
class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo/detail.html'