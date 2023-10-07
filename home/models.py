from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class TopSelling(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


STOCK = (('in_stock', 'In Stock'), ('out of stock', 'Out of Stock'))
LABELS = (('', 'default'), ('new', 'new'), ('sale', 'sale'), ('hot', 'hot'))


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    data_sheet = models.TextField(blank=True)
    slug = models.CharField(max_length=500, unique=True)
    url = models.URLField(blank=True, max_length=500)
    stock = models.CharField(choices=STOCK, max_length=50)
    labels = models.CharField(choices=LABELS, max_length=50, blank=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    username = models.CharField(max_length=200)
    slug = models.CharField(max_length=300)
    quantity = models.IntegerField()
    total = models.IntegerField()
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Blog(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    body = models.TextField()
    full_body = models.TextField(blank=True)
    quote = models.TextField(blank=True)

    def __str__(self):
        return self.name


class WishList(models.Model):
    username = models.CharField(max_length=200)
    slug = models.CharField(max_length=300)
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class ProductReview(models.Model):
    username = models.CharField(max_length=200)
    comment = models.TextField()
    slug = models.CharField(max_length=500)
    star = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class BlogReview(models.Model):
    username = models.CharField(max_length=200)
    comment = models.TextField()
    id = models.CharField(max_length=500, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
