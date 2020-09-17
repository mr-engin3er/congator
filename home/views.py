import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Search


# Create your views here.
AMAZONE_URL = 'https://www.amazon.in/s?k={}'
FLIPKART_URL = 'https://www.flipkart.com/search?q={}'


def index(request):
    return render(request, 'home/index.html')


def new_search(request):
    search = request.POST.get('search')
    # Search.objects.create(search=search)
    FINAL_AMAZON_URL = AMAZONE_URL.format(requests.compat.quote_plus(search))
    res = requests.get(FINAL_AMAZON_URL)
    soup = BeautifulSoup(res.text, features="html.parser")
    search_title = soup.find_all(
        'span', {'class': 'a-size-medium a-color-base a-text-normal'})
    search_price = soup.find_all(
        'span', {'class': 'a-price-whole'})
    search_link = soup.find_all(
        'a', {'class': 'a-link-normal a-text-normal'})
    print(search_title[0].text)
    print(search_price[0].text)
    print(f"https://www.amazon.in{search_link[0].get('href')}")
    context = {
        'search': search,
    }
    return render(request, 'home/new_search.html', context)
