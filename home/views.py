from django.shortcuts import render, redirect
from .models import *
# Create your views here.
# from django.views import View
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User
import pdb


class Base(View):
    views = {}


class HomeView(Base):

    def get(self, request):
        self.views['sellings'] = TopSelling.objects.all
        self.views['news'] = Product.objects.filter(labels='new')
        self.views['features'] = Product.objects.filter(labels='hot')
        self.views['ads'] = Ad.objects.all
        return render(request, 'index-2.html', self.views)


class CategoryView(Base):
    def get(self, request, slug):
        cat_id = Category.objects.get(slug=slug).id
        self.views['cat_products'] = Product.objects.filter(category_id=cat_id)
        self.views['categories'] = Category.objects.all()
        return render(request, 'category.html', self.views)


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


class MyAccount(Base):

    def get(self, request):
        return render(request, 'my-account.html', self.views)


class Shop(Base):

    def get(self, request):
        self.views['products'] = Product.objects.all()
        self.views['categories'] = Category.objects.all()
        return render(request, 'shop.html', self.views)


class ProductDetails(Base):

    def get(self, request, slug):
        self.views['products_detail'] = Product.objects.filter(slug=slug)
        return render(request, 'product-details.html', self.views)


class SearchView(Base):
    def get(self, request):
        if request.method == 'GET':
            query = request.GET['query']
            if query != "":
                self.views['search_products'] = Product.objects.filter(name__icontains=query)
            else:
                redirect('/')

        self.views['categories'] = Category.objects.all()
        return render(request, 'search.html', self.views)


def signup(request):
    if request.method == "POST":
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "The username is already taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "The email is already used")
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                data.save()

        else:
            messages.error(request, "The passwords do not match")
            return redirect('/signup')
    return render(request, 'signup.html')


class CartView(Base):

    def get(self, request):
        username = request.user.username
        self.views['my_cart'] = Cart.objects.filter(username=username)
        return render(request, 'cart.html', self.views)


def add_to_cart(request, slug):
    username = request.user.username
    if Cart.objects.filter(username=username, slug=slug, checkout=False):
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = Cart.objects.get(slug=slug).quantity
        quantity = quantity + 1

        if discounted_price > 0:
            total = discounted_price * quantity
        else:
            total = price * quantity

        Cart.objects.filter(username=username, slug=slug, checkout=False).update(
            quantity=quantity,
            total=total
        )
        return redirect('/cart')
    else:

        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = 1

        if discounted_price > 0:
            total = discounted_price
        else:
            total = price
        data = Cart.objects.create(
            username=username,
            slug=slug,
            quantity=quantity,
            total=total,
            items=Product.objects.filter(slug=slug)[0]

        )
        data.save()
        return redirect('/cart')


def delete_cart(request, slug):
    username = request.user.username
    if Cart.objects.filter(slug=slug, username=username, checkout=False):
        Cart.objects.filter(slug=slug, username=username, checkout=False).delete()

    return redirect('/cart')


def reduce_cart(request, slug):
    username = request.user.username
    if Cart.objects.filter(username=username, slug=slug, checkout=False):
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = Cart.objects.get(slug=slug).quantity
        if quantity > 1:
            quantity = quantity - 1

            if discounted_price > 0:
                total = discounted_price * quantity
            else:
                total = price * quantity

            Cart.objects.filter(username=username, slug=slug, checkout=False).update(
                quantity=quantity,
                total=total
            )
        return redirect('/cart')
