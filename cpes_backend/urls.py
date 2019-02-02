from django.contrib import admin
from django.urls import path
from GulleApp.views import (Login, Logout, Signup, no_access, professors_list)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', professors_list, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('messages/',messages ,name='messages'),

    path('noaccess/',no_access ,name='no-access'),


    # path('like/<int:user_id>/', like, name='like'),
    # path('liked/',liked ,name='liked'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)