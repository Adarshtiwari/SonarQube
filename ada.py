import requests
from bs4 import BeautifulSoup

def search_product_and_get_brands(product_name):
    # Create the search URL based on the product name
    search_url = f"https://www.example.com/search?q={product_name}"  # Replace with the appropriate website URL

    # Send a GET request to the search URL
    response = requests.get(search_url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract brand information from the parsed HTML
        brand_names = []
        brand_elements = soup.find_all('span', {'class': 'brand'})  # Replace with the appropriate HTML element for the brand name

        for brand_element in brand_elements:
            brand_name = brand_element.text.strip()
            brand_names.append(brand_name)

        return brand_names

    return []

product_name = "YOUR_PRODUCT_NAME"
brands = search_product_and_get_brands(product_name)
if brands:
    print("Matching Brand Names:")
    for brand in brands:
        print(brand)


# https://autocomplete.clearbit.com/v1/companies/suggest?query
else:
    print("No matching brands found for the product name.")
