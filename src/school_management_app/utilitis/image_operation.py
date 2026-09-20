from PIL import Image
from io import BytesIO


def image_to_binary(file_path, max_size=1024 * 1024):
    image = Image.open(file_path)

    image.thumbnail((1600, 1600))

    if image.mode in ("RGBA", "LA", "P"):
        image = image.convert("RGB")

    quality = 90

    while quality >= 30:
        buffer = BytesIO()

        image.save(
            buffer,
            format="JPEG",
            quality=quality,
            optimize=True
        )

        data = buffer.getvalue()
        if len(data) <= max_size:
            return data

        quality -= 5

    return data