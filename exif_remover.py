import argparse
from PIL import Image


def remove_data(filename):
    print(f'Removing EXIF data from {filename}...')
    with Image.open(filename) as img:
        out = Image.new(img.mode, img.size)
        out.putdata(img.getdata())
        out.save(filename)
    print(f'Successfully removed EXIF data from {filename}')


def main():
    parser = argparse.ArgumentParser(description='Remove EXIF data from image')
    parser.add_argument('image', nargs='+')
    args = parser.parse_args()

    for image in args.image:
        remove_data(image)


if __name__ == '__main__':
    main()
