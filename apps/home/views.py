from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.property.models import Property


@login_required
def frontpage(request):
    newest_property = Property.objects.all()[0:8]
    return render(request, 'home/frontPage.html', {'newest_property': newest_property})

