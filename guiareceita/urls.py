from django.urls import path, re_path
from guiareceita import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("viagem/", views.ViagemView.as_view(), name="viagem"),
    path("viagem/inserir/", views.ViagemInsert.as_view(), name="inserir_viager"),
    re_path(r'^viagem/atualizar/(?P<pk>\d+)/$', views.ViagemUpdate.as_view(), name="atualizar_viagem"),
    path("classificacao_viagem/", views.ClassificacaoViagemView.as_view(), name="classificacao_viagem"),
]
