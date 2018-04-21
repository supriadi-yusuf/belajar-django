from django.shortcuts import render
from .models import Publisher

#lokasi_template = "publishing/templates/html"
lokasi_template = "html"

# Create your views here.
def index(request):
    param={
       'judul': 'publikasi di Web',
       'isi': 'Halaman ini berisi publikasi ilmiah.'
              'Penulisnya adalah para ahli di bidangnya masing-masing.'
    }
    return render( request, lokasi_template + '/index.html', param)

def list_publisher(request):
    publishers = Publisher.objects.all()
    param = {
        'publisher_list': publishers
    }

    return render( request, lokasi_template + '/publisher_list.html', param)

def publisher_details(request, id):
    publisher = Publisher.objects.get(pk=id)
    param = {'publisher': publisher}
    return render( request, lokasi_template + '/publisher_details.html', param)
