from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.property.models import Property

# View for the frontpage, where the chatbot will be displayed
@login_required
def frontpage(request):
    # Get the newest 8 properties
    newest_property = Property.objects.all()[0:8]
    return render(request, 'home/frontPage.html', {'newest_property': newest_property})

# View for the property list page
def property_list(request):
    # Get the currently logged-in user
    user = request.user

    # Ensure the user is authenticated (if needed)
    if user.is_authenticated:
        # Exclude properties posted by the logged-in user
        newest_property = Property.objects.exclude(user=user).order_by('-created_at')
    else:
        # If not logged in, show all properties
        newest_property = Property.objects.all().order_by('-created_at')

     return render(request, 'home/frontPage.html', {'newest_property': newest_property})
