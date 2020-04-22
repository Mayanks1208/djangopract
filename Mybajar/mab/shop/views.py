from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):

    #for 33 video........................................


    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # return render(request, 'shop/index.html', params)

#with some change in video 33 now 34...............................................


    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at Tracker")

def search(request):
    return HttpResponse("We are at search")

def prodView(request):
    return HttpResponse("We are at Productview")

def checkout(request):
    return HttpResponse("We are at checkout")






#
# <!--{% extends 'shop/basic.html' %}-->
# <!--{% block css %}-->
# <!--          .col-md-3-->
# <!--          {-->
# <!--          display: inline-block;-->
# <!--          margin-left:-4px;-->
# <!--          }-->
#
# <!--          .carousel-indicators .active {-->
# <!--          background-color: blue;-->
# <!--            }-->
#
# <!--          .col-md-3 img{-->
#
# <!--          width: 227px;-->
# <!--          max-height: 242px;-->
# <!--          }-->
#
# <!--          body .carousel-indicator li{-->
# <!--          background-color: blue;-->
# <!--          }-->
#
# <!--          body .carousel-indicators{-->
# <!--          bottom: 0;-->
# <!--          }-->
#
# <!--          body .carousel-control-prev-icon,-->
# <!--          body .carousel-control-next-icon{-->
# <!--          background-color: blue;-->
# <!--          }-->
#
# <!--          .carousel-control-prev,-->
# <!--          .carousel-control-next{-->
# <!--          top: auto;-->
# <!--bottom: auto;-->
# <!--          }-->
# <!--           body .no-padding{-->
# <!--           padding-left: 0,-->
# <!--           padding-right: 0;-->
# <!--           }-->
# <!-- {% endblock %}-->
#
# <!--{% block body %}-->
# <!--{% load static %}-->
# <!--<div class="container">-->
#
# <!--    &lt;!&ndash;Slideshow starts here &ndash;&gt;-->
# <!--    {% for product, range, nSlides in allProds %}-->
# <!--    <h5 class="my-4">Flash Sale On {{product.0.category}} - Recommended Items</h5>-->
# <!--<div id="demo{{forloop.counter}}" class="carousel slide my-3" data-ride="carousel">-->
# <!--    <ul class="carousel-indicators">-->
# <!--      <li data-target="#demo{{forloop.counter}}" data-slide-to="0" class="active"></li>-->
#
# <!--       {% for i in range %}-->
# <!--      <li data-target="#demo{{forloop.parentloop.counter}}" data-slide-to="{{i}}" ></li>-->
# <!--      {% endfor %}-->
# <!--    </ul>-->
#
#
# <!--    <div class="container carousel-inner no-padding">-->
#
# <!--      <div class="carousel-item active">-->
# <!--        <div class="col-xs-3 col-sm-3 col-md-3">-->
# <!--          <div class="card" style="width: 18rem;">-->
# <!--            <img src='/media/{{product.0.image}}' class="card-img-top" alt="...">-->
# <!--            <div class="card-body">-->
# <!--                <h5 class="card-title">{{product.0.product_name}}</h5>-->
# <!--                <p class="card-text">{{product.0.desc}}</p>-->
# <!--                <button id="pr{{product.0.id}}" class="btn btn-primary cart">Add To Cart</button-->
# <!--            </div>-->
# <!--          </div>-->
# <!--       </div>-->
#
#
# <!--        {% for i in product|slice:"1:"%}-->
# <!--        <div class="col-xs-3 col-sm-3 col-md-3">-->
# <!--          <div class="card" style="width: 18rem;">-->
# <!--            <img src='/media/{{i.image}}' class="card-img-top" alt="...">-->
# <!--            <div class="card-body">-->
# <!--              <h5 class="card-title">{{i.product_name}}</h5>-->
# <!--              <p class="card-text">{{i.desc}}</p>-->
# <!--              <button id="pr{{i.id}}" class="btn btn-primary cart">Add To Cart</button>-->
# <!--            </div>-->
# <!--          </div>-->
# <!--        </div>-->
# <!--        {% if forloop.counter|divisibleby:3 and forloop.counter > 0 and not forloop.last %}-->
# <!--      </div><div class="carousel-item">-->
# <!--        {% endif %}-->
#
# <!--        {% endfor %}-->
# <!--    </div>-->
# <!--</div>-->
# <!--</div>-->
#
# <!--    &lt;!&ndash; left and right controls for the slide &ndash;&gt;-->
# <!--    <a class="carousel-control-prev" href="#demo{{forloop.counter}}" data-slide="prev">-->
# <!--        <span class="carousel-control-prev-icon"></span>-->
# <!--    </a>-->
# <!--    <a class="carousel-control-next" href="#demo{{forloop.counter}}" data-slide="next">-->
# <!--        <span class="carousel-control-next-icon"></span>-->
# <!--    </a>-->
# <!--    {% endfor %}-->
# <!--</div>-->
# <!-- {% endblock %}-->
#
# <!--{% block js %}-->
# <!--<script>-->
# <!--console.log('working');-->
# <!--if(localStorage.getItem('cart') == null){-->
# <!--var cart = {};-->
# <!--}-->
# <!--else-->
# <!--{-->
# <!--cart = JSON.parse(localStorage.getItem('cart'));-->
# <!--}-->
# <!--$('.cart').click(function(){-->
# <!--console.log('clicked');-->
# <!--var idstr = this.id.toString();-->
# <!--console.log(idstr);-->
# <!--if (cart[idstr] !=undefined){-->
# <!--cart[idstr] = cart[idstr] + 1;-->
# <!--}-->
# <!--else-->
# <!--{-->
# <!--cart[idstr] = 1;-->
# <!--}-->
# <!--console.log(cart);-->
# <!--localStorage.setItem('cart', JSON.stringify(cart));-->
# <!--});-->
# <!--</script>-->
# <!--{% endblock %}-->
