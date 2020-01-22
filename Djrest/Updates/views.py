from django.shortcuts import render, get_object_or_404()
from django.http import HttpResponse, JsonResponse, Http404

from .models import Update


# Create your views here.
def json_example_view(request):
    data = {
        'name': 'Imran',
        'age': 24,
        'occupation': 'service holder!',
        'expertise': 'can pass enormous amount of time on home entertainment!'
    }
    return JsonResponse(data)


def details_update_page(request, integer_field):
    print(integer_field.__class__)
    try:
        obj = Update.objects.get(integer_field=str(integer_field))
    except Update.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    template_name = 'Updates/details_update_page.html'
    context = {
        "object": obj
    }
    return render(request, template_name, context)

# * This method does the same job as the above, but in a simpler way

def details_update_page_version2(request, integer_field):
    print(integer_field.__class__)
    obj = get_object_or_404(Update, integer_field = integer_field)
    template_name = 'Updates/details_update_page.html'
    context = {
        "object": obj
    }
    return render(request, template_name, context)
