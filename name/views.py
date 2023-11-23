from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Name


class NameListView(View):
    """Вывод данных из модели Name """

    def get(self, request):
        names = Name.objects.all()
        name_list = [{'id': name.id, 'name': name.name} for name in names]
        context = {
            'name_list': name_list,
        }
        return render(request,'name/main.html', context)


class AddNameView(View):
    """Добавление новых имён в Name"""

    def get(self, request):
        return render(request, 'name/index.html')

    def post(self, request):
        names = {}
        for key, value in request.POST.items():
            if key.startswith('name') and value:
                names[key] = value
        Name.objects.create(name=names)
        messages.success(request, 'Данные успешно добавлены.')
        return redirect('/')
