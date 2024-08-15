# main.py
from search import search_images
from download import download_images

def main():
    query = "Laptop ASUS M3500QC"
    soup = search_images(query)
    download_images(soup)

if __name__ == "__main__":
    main()
