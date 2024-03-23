from extract_min import extract_min
from extract_max import extract_max


def main():
    url = 'https://www.cartadeivinicdv.com/collections/la-nostra-selezione/products/tristan-hyest-borde-de-marne?variant=37853465411733'
    # Call the functions
    extract_max(url)
    extract_min(url)


if __name__ == "__main__":
    main()
