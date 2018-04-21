from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path( '', TemplateView.as_view(template_name = 'contoh_static/home.html'), name = 'contoh_static_view_home' ),
]
