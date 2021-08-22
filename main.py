# I know Pillow has built in algorithms for rotating images
# but I just want to apply the algorithm I've done a few days ago on leetcode!
from typing import Tuple
from PIL import Image
from PIL.Image import Image as ImageObject
from math import floor


def swap(image: ImageObject, a: Tuple[int, int], b: Tuple[int, int]):
    tmp = image.getpixel(a)
    image.putpixel(a, image.getpixel(b))
    image.putpixel(b, tmp)


def main():
    image = Image.open("assets/angular.png")
    (n, _) = image.size
    rgb = image.convert("RGBA")

    # step 1 = transpose array
    for k in range(n - 1):
        rowJ = k
        colI = k
        while rowJ < n:
            swap(rgb, (colI, k), (k, rowJ))

            rowJ += 1
            colI += 1

    m: int = floor(n / 2)

    # step 2 = flip horizontally
    for i in range(n):
        a = 0
        b = n - 1
        while a < m:
            swap(rgb, (i, a), (i, b))
            a += 1
            b -= 1
    rgb.show()


if __name__ == "__main__":
    main()
