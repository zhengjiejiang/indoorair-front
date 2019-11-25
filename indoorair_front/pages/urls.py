from django.urls import path

from . import views

urlpatterns = [
# ---- homepage -----

    path('', views.index_page, name='index_page'),
    path('contact', views.contact_page, name='contact_page'),
# ---- gateway-----

    path('register', views.register_page, name='register_page'),
    path('register/ok', views.register_ok_page, name ='register_ok_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.login_page, name='logout_page'),
# ---- dashboard -----

    path('dashboard', views.dashboard_page, name='dashboard_page'),
# ---- instrument -----

    # path('instrument/create', views.i_create_page, name='i_create_page'),
    path('instruments', views.i_list_page, name='i_list_page'),
    path('instrument/<int:id>', views.i_retrieve_page, name='i_retrieve_page'),
    path('instrument/<int:id>/update', views.i_update_page, name='i_update_page'),


# ---- report -----

    path('reports', views.report_list_page, name='report_list_page'),
    path('report/1', views.report_01_page, name='report_01_page'),
# ---- sensor -----

    path('sensor/<int:id>', views.sensor_retrieve_page, name='sensor_retrieve_page'),
# ---- user profile -----

    path('profile', views.profile_retrieve_page, name='profile_retrieve_page'),
    path('profile/update', views.profile_update_page, name='profile_update_page'),

]


# path   网站的前缀
