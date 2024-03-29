from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductGallery, Review
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django .http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories,
            is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=single_product).exists

    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(
                user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    # Get the reviews
    reviews = Review.objects.filter(product_id=single_product.id, status=True)

    product_gallery = ProductGallery.objects.filter(
        product_id=single_product.id)

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        "product_gallery": product_gallery,
        'reviews': reviews,
        'orderproduct': orderproduct,

    }
    return render(request, 'store/product_detail.html', context)


# for search

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by(
                '-created_date').filter(description__icontains=keyword, product_name__icontains=keyword)
    context = {
        'products': products,
    }

    return render(request, 'store/store.html', context)


# for review prodcut

def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = Review.objects.get(
                user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(
                request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Review()
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(
                    request, 'Your Review submitted!.')
                return redirect(url)
