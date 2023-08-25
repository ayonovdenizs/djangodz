from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

# Create your views here.

def index(request):
    advertisements: list[Advertisement] = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, 'advertisement/index.html', context)


def advertisement_post(request):
    if request.method == "POST":
        print(request.user) # AnonymousUser если не войти в админку. после того как в неё вошли будет admin
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv_object = Advertisement(**form.cleaned_data)
            adv_object.author = request.user
            adv_object.save()

    form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement/advertisement-post.html', context)
