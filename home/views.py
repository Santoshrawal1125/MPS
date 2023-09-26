from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View


class Base(View):
    views = {}


class HomeView(Base):

    def get(self, request):
        self.views['sellings'] = TopSelling.objects.all
        self.views['news'] = Product.objects.filter(labels='new')
        self.views['features'] = Product.objects.filter(labels='hot')
        self.views['ads'] = Ad.objects.all
        return render(request, 'index-2.html', self.views)


class About(Base):

    def get(self, request):
        self.views['members'] = Member.objects.all
        return render(request, 'about-us.html', self.views)


class BlogView(Base):

    def get(self, request):
        self.views['blogs'] = Blog.objects.all
        return render(request, 'blog.html', self.views)


class BlogDetails(Base):

    def get(self, request, id):
        self.views['blogs'] = Blog.objects.filter(id=id)
        return render(request, 'blog-details.html', self.views)


class Cart(Base):

    def get(self, request):
        return render(request, 'cart.html', self.views)


class Checkout(Base):

    def get(self, request):
        return render(request, 'checkout.html', self.views)


class ContactView(Base):

    def get(self, request):
        return render(request, 'contact-us.html', self.views)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            data = Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            data.save()

        return render(request, 'contact-us.html', self.views)


class Error(Base):

    def get(self, request):
        return render(request, 'error404.html', self.views)


class Shop(Base):

    def get(self, request):
        self.views['products'] = Product.objects.all
        return render(request, 'shop.html', self.views)


class LoginRegister(Base):

    def get(self, request):
        return render(request, 'login-register.html', self.views)
