from PIL import Image, ImageOps
import sys
import os

if len(sys.argv) == 3:
    _, ext = os.path.splitext(sys.argv[-1])
    _, ext2 = os.path.splitext(sys.argv[1])
    try:
        if ext == ext2:
            # Open two images to work with
            shirt = Image.open("shirt.png")
            background = Image.open(sys.argv[1])

            # Fit and paste background image with mask image with mask image size
            background = ImageOps.fit(background, shirt.size)
            background.paste(shirt, shirt)

            # Save the result as a different file
            background.save(sys.argv[-1])

            # Close the images
            shirt.close()
            background.close()

        elif ext == ".png" or ext2 == "jpg"  or "jpeg" and ext != ext2:
            sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")
    except FileNotFoundError:
        sys.exit("Input does not exist")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
