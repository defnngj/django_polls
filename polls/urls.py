from django.conf.urls import url
from . import views_interface


app_name = 'polls'
urlpatterns = [
    # polls interface
    # ex : /polls/questions/
    url(r'^questions/$', views_interface.questions, name='questions'),
    # ex : /polls/question_option/
    url(r'^question_option/$', views_interface.question_option, name='question_option'),
    # ex : /polls/question_result/
    url(r'^question_result/$', views_interface.question_result, name='question_result'),
    # ex : /polls/question_vote/
    url(r'^question_vote/$', views_interface.question_vote, name='question_vote'),
]
