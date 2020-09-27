"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', views.course_list.as_view()),
    path('course/<int:pk>', views.course_detail.as_view()),
]

"""
from django.contrib import admin
from django.urls import path, include
from cbvApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
  ]


