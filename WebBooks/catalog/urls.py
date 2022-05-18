from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borroweb'),
    path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]
