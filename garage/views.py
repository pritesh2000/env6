from django.shortcuts import render
from .models import Category, Subcategory, Service
from .forms import CategoryForm, SubcategoryForm, ServiceForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
# Create your views here.

def index(request):
    return render(request, 'index.html')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "garage/category/add_category.html"
    success_url = '/admin'

class SubcategoryCreateView(CreateView):
    model = Subcategory
    template_name = "garage/subcategory/add_subcategory.html"
    success_url = '/admin'
    form_class = SubcategoryForm



# ------------------SERVICE CRUD-----------------------

class ServiceCreateView(CreateView):
    model = Service
    template_name = "garage/service/add_service.html"
    success_url = '/admin'
    form_class = ServiceForm

class ServiceListView(ListView):
    model = Service
    services = Service.objects.all()
    context_object_name = 'services'
    template_name = "garage/service/list_service.html"
    ordering=['id']

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = "garage/service/delete_service.html"
    success_url = '/garage/listservice'

class ServiceUpdateView(UpdateView):
    model = Service
    template_name = "garage/service/update_service.html"
    success_url = '/garage/listservice'

class ServiceDetailView(DetailView):
    model = Service
    service = Service.objects.all()
    context_object_name = 'service'
    template_name = "garage/service/detail_service.html"

