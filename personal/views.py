from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'personal/index.html')

class NotFoundView(View):
    def get(self, request):
        return render(request, 'personal/notfound.html', status=404)
