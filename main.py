import requests
from pathlib import Path
import os


def main():
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    base_path = Path(__file__).absolute().parent
    output_dir = base_path / "images"
    filename = output_dir / "hubble.jpeg"
    os.makedirs(output_dir, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response.content)
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP ошибка: {err}")
        exit()


if __name__ == "__main__":
    main()
