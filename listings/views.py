from django.shortcuts import render, get_object_or_404

def index(request):
    #listings = Listing.objects.all()
    return render(request, "listings/listings.html") #, {"listings": listings})

def listing(request):
    # try:
    #     listing = get_object_or_404(Listing, pk="listing_id")
    #     return render(request, "listings/listing.html", {"listing" : listing})
    # except Exception:
    #     return render(request, "listings/listings.html")
    return render(request, "listings/listing.html")


def search(request):
    return render(request, "listings/search.html")

