from django.db.models import Q
from django.http import request, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import ReviewForm, RatingForm
from .models import Category, Rating, Product


def index(request):
    context = {'title': 'E Shop'}
    return render(request, 'shop/index.html', context)


def shop(request):
    context = {
        'title': 'E Shop - Каталог',
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'shop/shop.html', context)
#
# class ProductView(ListView):
#     model = Product
#     queryset = Product.objects.all()
#     paginate_by = 3
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     slug_field = "url"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['star_form'] = RatingForm()
#         context['form'] = ReviewForm()
#         return context
#
#
# class AddReview(View):
#     def post(self, request, pk):
#         form = ReviewForm(request.POST)
#         product = Product.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             if request.POST.get("parent", None):
#                 form.parent_id = int(request.POST.get("parent"))
#             form.product = product
#             form.save()
#         return redirect(Product.get_absolute_url())
#
#
# class FilterProductView(ListView):
#     paginate_by = 2
#
#     def get_queryset(self):
#         queryset = Product.objects.filter(
#             Q(year__in=self.request.GET.getlist('year'))
#         ).distinct()
#         return queryset
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['year'] = ''.join([f'year={x}&' for x in request.GET.getlist('year')])
#         return context
#
#
# class JsonFilterProductView(ListView):
#     def get_queryset(self):
#         queryset = Product.objects.filter(
#             Q(year__in=self.request.GET.getlist('year'))
#         ).distinct().value('title', 'url', 'poster')
#         return queryset
#
#     def get(self, request, *args, **kwargs):
#         queryset= list(self.get_queryset())
#         return JsonResponse({'products': queryset}, safe=False)
#
#
# class AddStarRating(View):
#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X-FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip
#
#     def post(self, request):
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             Rating.objects.update_or_create(
#                 ip=self.get_client_ip(request),
#                 movie_id=int(request.POST.get('product')),
#                 defaults={'star_id': int(request.POST.get('star'))})
#             return HttpResponse(status=201)
#         else:
#             return HttpResponse(status=400)
#
#
# class Search(ListView):
#     paginate_by = 3
#
#     def get_queryset(self):
#         return Product.objects.filter(title__icontains=self.request.GET.get("q"))
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['q'] = f'q={self.request.GET.get("q")}&'
#         return context
