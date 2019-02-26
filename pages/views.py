from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-listdate').filter(ispublished=True)[:3]
    return render(request, "pages/index.html", {"listings": listings})

def about(request):
    realtors = Realtor.objects.order_by("-hiredate")
    mvp = Realtor.objects.get(ismvp=True)
    context = {
        "realtors": realtors,
        "mvp": mvp,
    }
    return render(request, "pages/about.html", context)