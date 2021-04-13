import argparse
import os
from PIL import Image

PATH = os.getcwd()

def remove_data(filename):
    with Image.open(PATH + filename) as img:
        out = Image.new(img.mode, img.size)
        out.putdata(img.getdata())
        out.save(PATH + filename)


def main():
    parser = argparse.ArgumentParser(description='Remove EXIF data from images')
    parser.add_argument('image', type=argparse.FileType('r'), nargs='+')
    args = parser.parse_args()

    for image in args.image:
        remove_data(image)


if __name__ == '__main__':
    main()
