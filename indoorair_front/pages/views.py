from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import status, response, views






# ---- homepage -----


def index_page(request):
    return render(request, 'pages/homepage/index.html', {

    })

def contact_page(request):
    return render(request, 'pages/homepage/contact.html', {

    })

# def api_version(request):
#     return JsonResponse({'version': 'Melody'})


#----gateway----
def register_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "pages/gateway/register.html", {})


def register_ok_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "pages/gateway/register_success.html", {})


def login_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "pages/gateway/login.html", {})



def logout_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "pages/gateway/logout.html", {})





#---dashboard---

def dashboard_page(request):
    return render(request, "pages/dashboard/dashboard.html", {
        'user': request.user,
    })




# ---instrument ---
def i_list_page(request):
    return render(request, "pages/instrument/list.html", {})

def i_create_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "pages/instrument/create.html", {})


def i_retrieve_page(request, id):
    return render(request, "pages/instrument/retrieve.html", {
        "instrument_id": int(id),
    })


def i_update_page(request, id):
    return render(request, "pages/instrument/update.html", {
        "instrument_id": int(id),
    })





#---report---


def report_list_page(request):
    return render(request,"pages/report/list.html",{})


def report_01_page(request):
    return render(request,"pages/report/01.html",{})


def sensor_retrieve_page(request, id):
    return render(request, "pages/sensor/retrieve.html", {
        "sensor_id": int(id),
    })

#---sensor---

def sensor_retrieve_page(request, id):
    return render(request, "pages/sensor/retrieve.html", {
        'id': id,
    })
#---user profile---


def profile_retrieve_page(request):
    return render(request, "pages/userprofile/retrieve.html", {})



def profile_update_page(request):
    return render(request, "pages/userprofile/update.html", {})
