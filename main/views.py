from django.shortcuts import render,redirect
from main.models import *
from main.forms import *
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index (request):
    queryset = request.GET.get('search')
    products=Product.objects.filter(visible=True)
    title='Productos registrados en el Sistema'

    if queryset:
        products=Product.objects.filter(
            Q(name__icontains=queryset) |
            Q(brand__name__icontains=queryset) |
            Q(department__name__icontains=queryset)
        )& Product.objects.filter(visible=True)
        return render(request,'index.html',{
            'title':title,
            'products':products
        })

    return render(request,'index.html',{
        'title':title,
        'products':products
    })

#Brands
def create_brand(request):

    if request.method=='POST':
        form = FormBrand(request.POST)

        if form.is_valid():
            data_form = form.cleaned_data

            name = data_form.get('name')
            brand = Brand(name=name)
            brand.save()
            
            messages.success(request,f'Marca {brand.name} creada correctamente')
            return redirect(show_brands)
    else:
        form = FormBrand()

    return render(request,'brands/create_brand.html',{
        'form':form,
        'title':'Crear Marca'
    })

def delete_brand(request,id):
    brand = Brand.objects.get(pk=id)
    brand.delete()
    messages.success(request,'Borrado exitosamente')
    return redirect(show_brands)

def show_brands(request):
    brands = Brand.objects.all()

    return render(request,'brands/show_brands.html',{
        'brands':brands,
        'title':'Marcas Registradas en el Sistema'
    })

#Department
def create_department(request):

    if request.method=='POST':
        form = FormDepartment(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            name = data_form.get('name')
            department = Department(name=name)
            department.save()

            messages.success(request,f'Departamento {department.name} creado correctamente')
            return redirect(show_department)
    else:
        form = FormDepartment()
    
    return render(request,'departments/create_department.html',{
        'title':'Agregar Departamento',
        'form':form
    })

def delete_department(request,id):

    department = Department.objects.get(pk=id)
    department.delete()
    messages.success(request,'Borrado exitosamente')
    return redirect(show_department)

def show_department(request):
    departments = Department.objects.all()
     
    return render(request,'departments/show_department.html',{
        'title':'Departamentos registrados en el Sistema',
        'departments':departments
    })

#Products
def create_product(request):

    if request.method=='POST':
        form=FormProduct(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            name = data_form.get('name')
            amount = data_form.get('amount')
            brand = data_form.get('brand')  
            department = data_form.get('department')
            visible = data_form.get('visible')

            product = Product(
                name=name,
                amount=amount,
                brand=brand,
                department=department,
                visible=visible,
            )
            product.save()

            messages.success(request,f'Producto {product.name} creado correctamente')
            return redirect(index)
    else:
        form=FormProduct()

    return render(request,'products/product_form.html',{
        'title':'Crear Producto',
        'form':form
    })

def update_product(request,id):
    product = Product.objects.get(id=id)
    form = FormProduct(instance=product)

    if request.method =='POST':
        form=FormProduct(request.POST,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,f'Producto {product.name} editado correctamente')
            return redirect(index)
   

    title = (f'Editar producto {product.name}')
    

    return render(request,'products/product_form.html',{
        'title':title,
        'form':form
    })

def delete_product(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request,'Borrado exitosamente')
    return redirect(index)
