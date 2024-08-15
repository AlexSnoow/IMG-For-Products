# download.py
import requests
from PIL import Image
from io import BytesIO
import os
import re

def modify_image_url(url, min_width=800, min_height=600):
    modified_url = re.sub(r'w=\d+', f'w={min_width}', url)
    modified_url = re.sub(r'h=\d+', f'h={min_height}', modified_url)
    return modified_url

def download_images(soup, folder_name='images', min_width=800, min_height=600):
    images = soup.find_all('img', class_='mimg')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    downloaded = 0
    for img in images:
        img_url = img.get('src') or img.get('data-src')
        
        if img_url and img_url.startswith('http'):
            print(f"Original image URL: {img_url}")
            img_url = modify_image_url(img_url, min_width, min_height)
            print(f"Modified image URL: {img_url}")

            response = requests.get(img_url, stream=True)
            response.raw.decode_content = True
            
            try:
                image = Image.open(BytesIO(response.content))
                width, height = image.size
                print(f"Image width: {width}px, height: {height}px")

                if width >= min_width:
                    downloaded += 1
                    with open(f'{folder_name}/image_{downloaded}.jpg', 'wb') as handler:
                        handler.write(response.content)
                    print(f"Image {downloaded} downloaded with width {width}px")
                    
                if downloaded == 4:  # Останавливаем после загрузки 4 изображений
                    break

            except Exception as e:
                print(f"Failed to process image: {e}")
        else:
            print(f"Skipping image with invalid URL: {img_url}")
