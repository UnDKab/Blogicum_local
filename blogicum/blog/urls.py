from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path(
        'posts/<int:post_id>/',
        views.PostDetailView.as_view(),
        name='post_detail'),

    path('posts/<int:post_id>/delete/',
         views.PostDeleteView.as_view(),
         name='delete_post'),

    path(
        'posts/<int:post_id>/edit/',
        views.PostEditView.as_view(),
        name='edit_post'),

    path(
        'posts/create/',
        views.PostCreateView.as_view(),
        name='create_post'),

    path('posts/<int:post_id>/comment/',
         views.CommentCreateView.as_view(), name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.comment_edit_view, name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.comment_delete_view, name='delete_comment'),

    path('category/<slug:category_slug>/', views.CategoryPostsView.as_view(),
         name='category_posts'),
    path('profile/edit/',
         views.EditProfileView.as_view(),
         name='edit_profile'),
    path('profile/<str:username>/',
         views.ProfileView.as_view(),
         name='profile')
]
