from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = {
    path('lists/', CreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)