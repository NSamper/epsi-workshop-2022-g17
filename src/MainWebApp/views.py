from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone as tz

from MainWebApp.models import Feedbacks


# Create your views here.
def index(request):
    if request.user.is_authenticated:

        return render(request, 'MainWebApp/index.html')

    else:

        return redirect(to="login")


def login(request):
    return redirect(to=index)


@login_required
def mySpace(request):
    try:
        feedback = Feedbacks.objects.filter(personKey__username_id=request.user.id, date__lte=tz.now()).order_by(
            'date').first()

    except:
        return HttpResponse(status=500)

    context = {
        'feedback': feedback,
    }

    return render(request, 'MainWebApp/generic.html', context=context)