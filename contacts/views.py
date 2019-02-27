from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == "POST":
        listingid = request.POST["listingid"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        userid = request.POST["userid"]
        realtoremail = request.POST["realtoremail"]

        if request.user.is_authenticated:
            userid = request.user.id
            hascontacted = Contact.objects.all().filter(listingid=listingid, userid=userid)
            if hascontacted:
                messages.error(request, "You have already made an inquery on this listing")
                return redirect("/listings/" + listingid)

        contact = Contact(listing=listing, listingid=listingid, name=name, email=email, phone=phone, message=message, userid=userid )
        contact.save()

        send_mail(
            "Propery Listing Inquiry",  # title
            "There has been an inquiry for " + listing,  # body
            "newrotoc@gmail.com",  # from
            [realtoremail, ],  # to
            fail_silently=False,
        )

        messages.success(request, "Your request has been submitted, a realtor will get back to you soon")
        return redirect("/listings/" + listingid)
