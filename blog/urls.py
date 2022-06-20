from django.contrib import admin
from django.urls import path
from posts.views import index, post_detail, post_create, post_update, post_delete, post_search
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from users.views import register, user_login, profile_update, delete_profile, profile

urlpatterns = [
    path('', index, name = "index"),
    path('admin/', admin.site.urls),
    path('post/<int:id>', post_detail, name = "post_detail"),
    path('post/create', post_create, name = "post_create"),
    path('post/search', post_search, name = "post_search"),
    path('post/update/<int:id>', post_update, name = "post_update"),
    path('post/delete/<int:id>', post_delete, name = "post_delete"),
    path('user/<int:id>', profile, name = "profile"),
    path('user/update/<int:id>', profile_update, name = "profile_update"),
    path('user/delete/<int:id>', delete_profile, name = "delete_profile"),
    path('register/', register, name = "register"),
    path('login/', user_login, name = "login"),
    path('logout', LogoutView.as_view(next_page = 'index'), name = "logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)