from ddgs import DDGS
import requests

with DDGS() as ddgs:
    images = ddgs.images("Artificial Intelligence", max_results=5)

    for i, image in enumerate(images, start=1):
        url = image["image"]

        try:
            img = requests.get(url).content
            with open(f"image_{i}.jpg", "wb") as f:
                f.write(img)
            print(f"Downloaded image_{i}.jpg")
        except Exception:
            print("Failed to download an image.")