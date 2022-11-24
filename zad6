from PIL import Image
from pathlib import Path


def convert_to_png(p: Path):
    with Image.open(p) as img:
        img.save(p.with_suffix('.png'))


def main():
    path = Path(r'C:\Users\Monika\Desktop\5.jpg')
    convert_to_png(path)


if __name__ == '__main__':
    main()
