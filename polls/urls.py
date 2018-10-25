from django.urls import path

from .views import index_view, detail_view, result_view, vote_view

app_name = 'polls'
urlpatterns = [
    path('', index_view, name='polls'),
    path('<int:question_id>/', detail_view, name='detail'),
    path('<int:question_id>/result/', result_view, name='result'),
    path('<int:question_id>/vote/', vote_view, name='vote'),
]
