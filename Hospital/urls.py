from django.urls import path
from . import views

urlpatterns = [

    # Patient
    path('', views.home, name='base'),

    path(
        'patients/',
        views.patient_list,
        name='patient_list'
    ),

    path(
        'patients/add/',
        views.add_patient,
        name='add_patient'
    ),

    # Doctor

    path(
        'doctors/',
        views.doctor_list,
        name='doctor_list'
    ),

    path(
        'doctors/add/',
        views.add_doctor,
        name='add_doctor'
    ),

    # Appointment

    path(
        'appointments/',
        views.appointment_list,
        name='appointment_list'
    ),

    path(
        'appointments/add/',
        views.add_appointment,
        name='add_appointment'
    ),
]