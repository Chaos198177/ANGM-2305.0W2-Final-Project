from PIL import Image
import glob
import os
import moviepy.editor as mpy
import fileinput


def main():
    images = input("Welcome to the Python Photo Manipulation Editor! " \
    "Are you uploading an image or series of images? ").casefold()
    if images == 'image'.casefold():
        file_path_single = input("Please upload your image here! Please ensure to include the full filepath from the main directory! Make sure to use backslashes (case sensitive)! ")
        if os.path.exists(file_path_single):
            type_single = input("What type of format would you like to convert your image to? Please select from the following options: \nPNG \nJPEG"
    "\nHEIC \n \n").casefold()
            if type_single != 'PNG'.casefold() and type_single != 'JPEG'.casefold() and type_single != 'JPG'.casefold() and type_single != 'HEIC'.casefold():
                print("Sorry! That format is not accepted! Please try again with the provided options!")
        else:
            print("The specified file path does NOT exist. Please try again!")
    elif images == 'images'.casefold():
        file_path_multiple = input("Please upload your images here! Please ensure to include the full filepath from the main directory Make sure to use backslashes (case sensitive)! ")
        if os.path.exists(file_path_multiple):
            type_multiple = input("What type of format would you like to convert your images to? Please select from the following options: \nPNG \nJPEG" 
        "\nHEIC \nGIF \nMOV \nMP4 \n \n").casefold()
            if type_multiple != 'PNG'.casefold() and type_multiple != 'JPEG'.casefold() and type_multiple != 'JPG'.casefold() and type_multiple != 'HEIC'.casefold() \
                and type_multiple != 'GIF'.casefold() and type_multiple != 'MOV'.casefold() and type_multiple != 'MP4'.casefold():
                print("Sorry! That format is not accepted! Please try again with the provided options!")
        else:
            print("The specified file path does NOT exist. Please try again!")
    else:
        print("Sorry! That format is not accepted! Please try again!")
    
    


if __name__ == "__main__":
    main()