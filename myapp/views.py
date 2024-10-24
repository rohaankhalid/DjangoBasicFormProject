from django.shortcuts import render
from .forms import MyForm

# Create your views here.

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    
    else:
        form = MyForm()
    return render(request, 'myapp/form_page.html', {'form': form})