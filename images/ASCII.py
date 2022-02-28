##################################
#   ASCII ART IMAGE GENERATOR    #
#--------------------------------#
# Functional ASCII art generator #
# to convert images into text    #
# files containing art to be     #
# used in other projects. Not to #
# be used as a dependency for    #
# other files.                   #
##################################

import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

#Resize the image
def resize(image, new_width = 100):
    width, height = image.size
    new_height = new_width * height / width
    return image.resize((int(new_width), int(new_height)))

#Convert image to greyscale
def to_greyscale(image):
    return image.convert("L")

#Convert image to ASCII characters
def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "";
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25];
    return ascii_str
    
#Main function
def main():
    #Attempt to open the image
    path = input("Enter the path to the image file: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image")
    
    image_width = int(input("Enter image size (default 100)"))

    #Resize the image
    image = resize(image, image_width)

    greyscale_image = to_greyscale(image)

    ascii_str = pixel_to_ascii(greyscale_image)

    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img);

main()