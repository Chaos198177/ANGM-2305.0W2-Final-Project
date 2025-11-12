from PIL import Image
import glob
import os
import moviepy.editor as mpy


def main():
    images = input("Welcome to the Python Photo Manipulation Editor! Are you uploading an image or series of images? ").casefold()
    if images == 'image'.casefold():
        file_path_single = input("Please upload your image here! Please ensure to include the full filepath from the main directory! ")
        type_single = input("What type of format would you like to convert your image to? Please select from the following options: \nPNG \nJPEG"
    "\nHEIC \n \n").casefold()
        if type_single != 'PNG'.casefold() or 'JPEG'.casefold() or 'HEIC'.casefold():
            print("Sorry! That format is not accepted! Please try again with the provided options!")
        #print(images)
        #print(file_path_single)
        #print(type_single)
    elif images == 'images'.casefold():
        file_path_multiple = input("Please upload your images here! Please ensure to include the full filepath from the main directory! ")
        type_multiple = input("What type of format would you like to convert your images to? Please select from the following options: \nPNG \nJPEG" \
        "\nHEIC \nGIF \nMOV \nMP4 \n \n").casefold()
        if type_multiple != 'PNG'.casefold() or 'JPEG'.casefold() or 'JPG'.casefold() or 'HEIC'.casefold() or 'GIF'.casefold() or 'MOV'.casefold() or 'MP4'.casefold():
            print("Sorry! That format is not accepted! Please try again with the provided options!")
        #print(images)
        #print(file_path_multiple)
        #print(type_multiple)
    else:
        print("Sorry! That format is not accepted! Please try again!")
    
    


if __name__ == "__main__":
    main()