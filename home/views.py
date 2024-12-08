from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

# 하드코딩된 로그인 정보
ADMIN_ID = "admin"
ADMIN_PASSWORD = "sky5"

class LoginView(TemplateView):
    template_name = "login.html"

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == ADMIN_ID and password == ADMIN_PASSWORD:
            # 세션에 로그인 상태 저장
            request.session["logged_in"] = True
            return redirect("/")  # 로그인 성공 시 홈으로 리다이렉트
        return render(request, self.template_name, {"error": "Invalid credentials"})

class HomeView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        # 로그인 여부 확인
        if not request.session.get("logged_in"):
            return redirect("/login/")  # 로그인 안 되어 있으면 로그인 페이지로 리다이렉트
        return super().dispatch(request, *args, **kwargs)

def logout_view(request):
    request.session.flush()  # 세션 초기화
    return redirect("/login/")
