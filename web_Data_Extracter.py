import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "https://ramdevstore.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all categories (update the selector based on actual structure)
categories = soup.select('li.nav-item a')  # Updated selector

# Extract categories and corresponding products
category_list = []
for category in categories:
    category_name = category.text.strip()
    category_url = category['href']
    category_list.append({'name': category_name, 'url': category_url})

# Function to fetch products from a category page
def fetch_products(category_url):
    category_response = requests.get(category_url)
    category_soup = BeautifulSoup(category_response.content, 'html.parser')
    products = category_soup.select('div.product-item')  # Updated selector
    product_list = []
    for product in products:
        product_name = product.select_one('h2.product-title').text.strip()  # Updated selector
        product_weight = product.select_one('span.product-weight').text.strip()  # Updated selector
        product_price = product.select_one('span.product-price').text.strip()  # Updated selector
        product_list.append({
            'name': product_name,
            'weight': product_weight,
            'price': product_price
        })
    return product_list

# Fetch products for each category
for category in category_list:
    category_url = category['url']
    products = fetch_products(category_url)
    category['products'] = products

# Print the results
for category in category_list:
    print(f"Category: {category['name']}")
    for product in category['products']:
        print(f"  Product: {product['name']}, Weight: {product['weight']}, Price: {product['price']}")
