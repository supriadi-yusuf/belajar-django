""" publishing_view url Configuration
"""

from django.urls import path, re_path
from .views import PublishingListView, PublishingDetailView
from django.views.generic import TemplateView

urlpatterns = [
    path( 'list', PublishingListView.as_view(), name = 'publisherview_list'),
    re_path( r'^detail/(?P<pk>\d+)/$', PublishingDetailView.as_view(), name = 'publisherview_detail'),
    path( 'tentang-kami', TemplateView.as_view(template_name = 'publishing/tentang_kami.html'), name = 'publisherview_tentang-kami')
]
