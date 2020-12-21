from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import EntryCreationForm
from .models import Entry, Language


def home(request):
    form = EntryCreationForm(instance=Entry.objects.first())
    if request.is_ajax():
        term = request.GET.get('term')
        languages = Language.objects.all().filter(title__icontains=term)
        return JsonResponse(list(languages.values()), safe=False)
    if request.method == 'POST':
        form = EntryCreationForm(request.POST, instance=Entry.objects.first())
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'core/home.html', {'form': form})