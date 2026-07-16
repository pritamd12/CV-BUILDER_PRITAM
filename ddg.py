from ddgs import DDGS

with DDGS() as ddgs:

    images = ddgs.images(
        "Artificial Intelligence",
        max_results=5
    )

    for image in images:
        print(image["image"])