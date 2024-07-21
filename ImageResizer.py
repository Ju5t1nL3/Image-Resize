"""
This program uses the Pillow Image module to resize any image.
"""

from PIL import Image

with Image.open("GitHub-logo.jpg") as im:
    print(f"Size: {im.size[0]} x {im.size[1]}")
    while True:
        try:
            length = int(input("What would like the new length to be? "))
            break
        except ValueError:
            print("Only integers are accepted. Try again.")
    while True:
        try:
            height = int(input("What would like the new height to be? "))
            break
        except ValueError:
            print("Only integers are accepted. Try again.")

    print(f"New Size: {length} x {height}")
    resized_im = im.resize((length,height))
    resized_im.save("Resized_image.jpg")
