"""Конфигурация URL-адреса yatube
Список urlpatterns направляет URL-адреса к представлениям.
 Для получения дополнительной информации, пожалуйста, смотрите:
 https://docs.djangoproject.com/en/2.2/topics/http/urls/
Примеры:
Представления функций
 1. Добавьте импорт: из представлений импорта my_app
 2. Добавьте URL-адрес в urlpatterns: path(", views.home, name='home')
Представления на основе классов
 1. Добавьте импорт: из other_app.views импортируйте домой
 2. Добавьте URL-адрес в urlpatterns: path(", Home.as_view(), name='home')
Включая другой URLconf
 1. Импортируйте функцию include(): из django.urls импортируйте include, путь
 2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
