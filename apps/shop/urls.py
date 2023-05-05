from django.urls import path
from apps.shop import views


urlpatterns = [
    path("", views.ProductView.as_view()),
    path("filter/", views.FilterProductView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path("add-rating/", views.AddStarRating.as_view(), name="add_rating"),
    path("json-filter/", views.JsonFilterProductView.as_view(), name="json_filter"),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    ]
