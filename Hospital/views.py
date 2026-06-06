
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    return render(request, 'base.html')


def patient_list(request):
    patients = Patient.objects.all()
    return render(
        request,
        'patient_list.html',
        {'patients': patients}
    )


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('patient_list')

    else:
        form = PatientForm()

    return render(
        request,
        'patient_form.html',
        {'form': form}
    )


def doctor_list(request):
    doctors = Doctor.objects.all()

    return render(
        request,
        'doctor_list.html',
        {'doctors': doctors}
    )


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    else:
        form = DoctorForm()

    return render(
        request,
        'doctor_form.html',
        {'form': form}
    )


def appointment_list(request):
    appointments = Appointment.objects.all()

    return render(
        request,
        'appointment_list.html',
        {'appointments': appointments}
    )


def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:
        form = AppointmentForm()

    return render(
        request,
        'appointment_form.html',
        {'form': form}
    )