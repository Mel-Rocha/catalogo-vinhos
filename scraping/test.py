from extract_min import extract_min
from extract_max import extract_max


def main():
    url = 'https://www.cartadeivinicdv.com/products/andre-clouet-un-jour-de-1911-grand-cru-brut?variant=37853625417877'
    # Call the functions
    extract_max(url)
    extract_min(url)


if __name__ == "__main__":
    main()
