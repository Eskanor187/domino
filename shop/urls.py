from django.urls import *

urlpatterns = [
	path('<slug:category_slug>/', prodycts_by_category, name='by-category')
]