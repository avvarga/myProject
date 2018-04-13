from django.shortcuts import render,redirect
from django.contrib import messages
from models import *
import bcrypt

# Create your views here.
def index(request):
    # request.session.clear()
    return render (request,'myApp/index.html')

def login(request):
    errors = User.objects.valid_login(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect ('/')
    else:
        request.session['user'] = User.objects.get(username=request.POST['username']).name
        request.session['id'] = User.objects.get(username=request.POST['username']).id
        return redirect ('/dashboard')  

def register(request):
    errors = User.objects.valid_registration(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect ('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(name = request.POST['name'], username = request.POST['username'], password = password)
        request.session['user'] = User.objects.last().name
        return redirect ('/dashboard')
        
def dashboard (request):
    context = {
        'items': User.objects.get(name = request.session['user']).wish_items.all(),
        'others': Item.objects.exclude(wishlist__name = request.session['user']).all()
        }
    return render (request, 'myApp/dashboard.html', context)

def logout (request):
    request.session.clear()
    return redirect ('/')

def show (request,id):
    context = {
        'items': Item.objects.get(id=id).wishlist.all(),
        'product': Item.objects.get(id=id)
        }
    return render (request, 'myApp/items.html', context)

def delete (request,id):
    return redirect ('/dashboard')

def remove (request,id):
    this_user = User.objects.get(name = request.session['user'])
    this_item = Item.objects.get(id=id)
    this_item.wishlist.remove(this_user)    
    return redirect ('/dashboard')

def add(request,id):
    this_user = User.objects.get(name = request.session['user'])
    this_item = Item.objects.get(id=id)
    this_item.wishlist.add(this_user)
    return redirect ('/dashboard')

def create (request):
    return render (request,'myApp/create.html')

def new_item (request):
    errors = Item.objects.valid_item(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect ('/wish_items/create')
    else:
        item = request.POST['item']
        result = Item.objects.filter(name = item)
        if len(result) > 0:
            result_value = result.values('id')[0]['id']
            print result_value
            return redirect ('/wish_items/'+ str(result_value) +'/add')
        else:
            creator = User.objects.get( name = request.session['user'])
            Item.objects.create(name = item, user = creator)
            this_item = Item.objects.last()
            this_item.wishlist.add(creator)
            return redirect ('/dashboard')  

 



