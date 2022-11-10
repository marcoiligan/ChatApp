from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from base.views import lobby, room, getToken, createUser, getMember, deleteMember

urlpatterns = [
    path('', lobby, name="lobby"),
    path('room/', room, name="room"),

    path('get_token/', getToken, name="get_token"),
    path('create_member/', createUser, name="create_member"),
    path('get_member/', getMember, name="get_member"),
    path('delete_member/', deleteMember, name="delete_member"),
]