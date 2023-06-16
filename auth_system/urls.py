from django.urls import path
from .views import main_page, main_page_pl, py, py_pl, programs, programs_pl, other, other_pl, info, info_pl, Register, Login, logoutuser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page, name="main-page"),
    path('jp', main_page_pl, name="strona glowna"),
    path('programs', programs, name="Programs"),
    path('programsPL', programs_pl, name="Programy"),
    path('py', py, name="Prev Years"),
    path('pyPL', py_pl, name="Zeszle lata"),
    path('info', info, name="info"),
    path('infoPL', info_pl, name="ipl"),
    path('other', other, name="other"),
    path('otherPL', other_pl, name="inne"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)