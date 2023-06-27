from django.urls import path

from .import views

from.forms import FormUser1

urlpatterns = [
    path('',views.index, name='index'),
    path('pag2/',views.pag2, name='pagina2'),
    path('livraria/',views.livraria, name='livraria'),
    path('<int:livro_id>/',views.detalhe, name='detalhe'),
    path('editora/', views.editora, name="editora"),
    path('cidades/', views.cidade, name="cidades"),
    path('form1/', views.form1, name='form1'),
    path('registo/',views.RegistoUser, name='registo'),
]
