from django.contrib import admin
from django.urls import path , include


from .views import      PromoListView   \
                    ,   PromoDetailView \
                    ,   PromoCreateView \
                    ,   PromoUpdateView \
                    ,   PromoDeleteView

app_name = "promociones"

urlpatterns = [
    path("", PromoListView.as_view(), name="all"),
    path("create/", PromoCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", PromoDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", PromoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", PromoDeleteView.as_view(), name="delete")

]