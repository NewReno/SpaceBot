import requests
from pathlib import Path
import os

def fetch_spacex_last_launch(spacex_url):
    base_path = Path(__file__).absolute().parent
    output_dir = base_path / "images"
    os.makedirs(output_dir, exist_ok=True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    response = requests.get(spacex_url, headers=headers)
    response.raise_for_status()
    spacex_data = response.json()
    image_url = spacex_data['links']['flickr']['original']

    for i, img_url in enumerate(image_url):
        img_response = requests.get(img_url, headers=headers)
        img_response.raise_for_status()

        filename = f'{output_dir}/foto{i+1}.jpg'

        with open(filename, 'wb') as file:
            file.write(response.content)

def download_image(url):
    base_path = Path(__file__).absolute().parent
    output_dir = base_path / "images"
    filename = output_dir / "hubble.jpeg"
    os.makedirs(output_dir, exist_ok=True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    try:
        spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
        fetch_spacex_last_launch(spacex_url)
        url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
        download_image(url)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP ошибка: {err}")
        exit()


if __name__ == "__main__":
    main()