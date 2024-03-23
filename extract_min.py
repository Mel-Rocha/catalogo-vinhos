import requests
from bs4 import BeautifulSoup, NavigableString

url = 'https://www.cartadeivinicdv.com/collections/la-nostra-selezione/products/tristan-hyest-borde-de-marne?variant=37853465411733'
response = requests.get(url)
response_content = response.text

soup = BeautifulSoup(response_content, 'html.parser')

# Find the strong tags containing the keys
strongs = soup.find_all('strong')

result = {}

def extract_min():
    # Extract the keys and values from these strong tags
    for strong in strongs:
        key = strong.get_text(strip=True)
        # Only process the keys we are interested in
        if key in ["NOTE DI DEGUSTAZIONE", "PRODUTTORE"]:
            # Get the next sibling of the strong tag
            next_sibling = strong.next_sibling
            # If the next sibling is a NavigableString (i.e., text), use it as the value
            if isinstance(next_sibling, NavigableString):
                value = next_sibling.strip()
            # If the next sibling is another tag, get the text inside it
            elif next_sibling is not None:
                value = next_sibling.get_text(strip=True)
            else:
                value = None
            result[key] = value

    # Print the keys and values
    for key, value in result.items():
        print(f'{key}: {value}')

