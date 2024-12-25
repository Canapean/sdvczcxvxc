from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.http import HttpRequest


class SearchView(View):

    def get(self, request: HttpRequest, *args, **kwargs):

        query = request.GET.get('query', None)

        if query is not None:
            result = self.search(query)
            return render(request, 'search/product_list.html', {'result': result})

        return redirect('store:list')

    def search(self, *args, **kwargs):
        from store.models import Product
        from django.db.models import Q, F

        return Product.objects.filter(title=args[0])



