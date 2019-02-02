from django.contrib import admin
from django.urls import path
from GulleApp.views import (Login, Logout, Signup, home, )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('messages/',messages ,name='messages'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)