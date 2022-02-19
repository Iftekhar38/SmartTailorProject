from django.shortcuts import render, redirect
from STApp.models import GalaryModel
import folium
import geocoder
from django.contrib.auth.decorators import login_required
from STApp.forms import addProductForm, signUpForm
from django.http import HttpResponseRedirect
from django.contrib.messages import success

# Create your views here.

def index(request):
    return render(request, 'STApp/index.html')

def galary(request):
    data = GalaryModel.objects.all()
    return render(request, 'STApp/galary.html', {'data':data})

def about(request):
    return render(request, 'STApp/about.html')

def contact(request):
    location = geocoder.osm('Saharsa')
    lat = location.lat
    lng = location.lng
    country = location.country
    #Create Map object
    m = folium.Map(location = [25.8801170,86.5925780], zoom_start=12)
    folium.Marker([25.8801170,86.5925780],tooltip = 'click for more', popup="Saharsa").add_to(m)
    #get HTML Repersenation of map object
    folium.Marker([lat,lng],tooltip = 'click for more', popup=country).add_to(m)
    m =  m._repr_html_()
    context = {
        'm':m,
    }
    return render(request, 'STApp/contact.html', context)
# def login(request):
    #return render(request, 'STApp/login.html')



@login_required
def addProduct(request):
        form = addProductForm()
        if request.method =='POST':
            form = addProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=True)
                success(request, 'Product Successfully Added')
        return render(request, 'STApp/addproduct.html', {'form':form})

def signUp(request):
    form =  signUpForm()
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('accounts/login')
    return render(request, 'STApp/signup.html', {'form':form})

def logout(request):
    return render(request, 'STApp/logout.html')
@login_required
def viewProduct(request):
    data =  GalaryModel.objects.all()
    return render(request, 'STApp/viewproduct.html', {'products': data})

def updateproduct(request, id):
    product = GalaryModel.objects.get(id = id)
    form = addProductForm(request.POST, request.FILES, instance = product)
    if request.method == 'POST':
        form = addProductForm(request.POST,request.FILES, instance = product)
        # form = addProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save(commit=True)
            success(request, 'Product Successfully Updated')
            #return redirect('/')
    return render(request, 'STApp/update.html', {'form': form})
        
def deleteproduct(request, id):
     product = GalaryModel.objects.get(id=id)
     product.delete()
     success(request, 'Product is Deleted')
     return redirect('viewproduct')