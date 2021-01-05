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

    def amazon(search):
        FINAL_AMAZON_URL = AMAZONE_URL.format(
            requests.compat.quote_plus(search))
        response = requests.get(FINAL_AMAZON_URL)
        soup = BeautifulSoup(response.text, features="html.parser")
        search_title = soup.find_all(
            'span', {'class': 'a-size-medium a-color-base a-text-normal'})
        search_price = soup.find_all(
            'span', {'class': 'a-price-whole'})
        search_link = soup.find_all(
            'a', {'class': 'a-link-normal a-text-normal'})
        search_photo = soup.find_all('img', {'class': 's-image'})
        amazon_title = search_title[0].text
        amazon_price = search_price[0].text
        amazon_url = f"https://www.amazon.in{search_link[0].get('href')}"
        amazon_photo = search_photo[0].get('src')
        return {'amazon_title': amazon_title,
                'amazon_price': amazon_price,
                'amazon_url': amazon_url,
                'amazon_photo': amazon_photo}

    def flipkart(search):
        FINAL_FLIPKART_URL = FLIPKART_URL.format(
            requests.compat.quote_plus(search))
        response = requests.get(FINAL_FLIPKART_URL)
        soup = BeautifulSoup(response.text, features="html.parser")
        search_title = soup.find_all(
            'div', {'class': '_4rR01T'})
        search_price = soup.find_all(
            'div', {'class': '_30jeq3 _1_WHN1'})
        search_link = soup.find_all(
            'a', {'class': '_1fQZEK'})
        flipkart_title = search_title[0].text
        flipkart_price = search_price[0].text
        flipkart_url = f"https://www.flipkart.com{search_link[0].get('href')}"
        return {'flipkart_title': flipkart_title,
                'flipkart_price': flipkart_price,
                'flipkart_url': flipkart_url}
    context = {
        'search': search,
    }
    context.update(amazon(search))
    context.update(flipkart(search))
    print(context)
    return render(request, 'home/new_search.html', context)
