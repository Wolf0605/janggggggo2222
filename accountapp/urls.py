from django.urls import path


def hello_world(args):
    pass

app_name = 'accountapp'

urlpatterns = [
    path('hello_world',hello_world,name='hello_world')
]