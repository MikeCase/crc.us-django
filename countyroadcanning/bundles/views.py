from django.shortcuts import render
from .models import Bundle

# Create your views here.
def bundle_page(request, bundle_id):
    item = Bundle.objects.get(id = bundle_id)
    return render(request, 'bundles/bundle_page.html', {'bundle': item})

def bundles(request):
    item = Bundle.objects.all()
    return render(request, 'bundles/index.html', {'bundles': item})