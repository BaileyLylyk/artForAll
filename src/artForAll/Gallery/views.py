from django.shortcuts import render
from .models import GalleryPost

# Create your views here.
def gallery_detail_view(request):
    obj = GalleryPost.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'artist': obj.artist,
    #     'featured': obj.featured
    # }
    context = {
        'object': obj
    } 
    return render(request, "gallery/detail.html", context)

def gallery_view (request):
    qs = GalleryPost.objects.all()
    context = {
        'objects' : qs
     }
    return render(request, "gallery.html", context)

