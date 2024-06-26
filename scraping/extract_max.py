import requests
from bs4 import BeautifulSoup


def extract_max(url):
    response = requests.get(url)
    response_content = response.text

    soup = BeautifulSoup(response_content, 'html.parser')

    # Find the divs containing the information
    divs = soup.find_all('div', {'data-mce-fragment': '1'})

    result = {}

    # Extract the keys and values from these divs
    for i in range(len(divs)):
        if divs[i].strong is not None:
            key = divs[i].strong.get_text(strip=True)
            # If the key is "CANTINA", skip this iteration
            if key == "CANTINA":
                continue
            # If the key is one of the special keys, look for the value in the next div
            if key in ["TEMPERATURA DI SERVIZIO", "NAZIONE"]:
                if i+1 < len(divs):
                    value = divs[i+1].get_text(strip=True)
            else:
                value = divs[i].get_text(strip=True).replace(key, '').strip()
            result[key] = value

    # Print the keys and values
    for key, value in result.items():
        print(f'{key}: {value}')

    return result