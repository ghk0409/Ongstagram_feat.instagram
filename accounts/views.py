from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    # 회원가입 정보가 서버로 전달될 경우 (POST 형식은 자료를 전달하는 상태)
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)

        if user_form.is_valid():
            # commit = False이기 때문에 아직 DB에 저장하지 않고 메모리 상에 객체만 만듦
            new_user = user_form.save(commit=False)
            # set_password를 통해 비밀번호를 암호화 시켜서 저장
            new_user.set_password(user_form.cleaned_data['password'])
            # 실제 DB 저장
            new_user.save()
            # 'register_done.html 템플릿으로 렌더링해서 결과를 보여줌
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    # POST 형식이 아닐 경우
    else:
        # 빈 RegisterForm 객체 초기화
        user_form = RegisterForm()
    # 빈 RegisterForm 객체로 register.html 템플릿 렌더링 결과 보여줌
    return render(request, 'registration/register.html', {'form':user_form})