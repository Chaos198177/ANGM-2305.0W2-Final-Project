from PIL import Image
import glob
import os
import moviepy.editor as mpy
from tqdm import tqdm

def main():
    images = input("Welcome to the Python Photo Manipulation Editor! "
        "Are you uploading an image or series of images? ").casefold()

    if images == 'image':
        file_path_single = input("Please upload your image here! Include the full filepath with backslashes (case sensitive)! ")
        if os.path.exists(file_path_single):
            type_single = input("What type of format would you like to convert your image to?\n"
                "PNG\nJPEG\nHEIC\n\n").casefold()

            if type_single in ('png', 'jpeg', 'jpg', 'heic'):
                convert_image(file_path_single, output_format=type_single)
            else:
                print("Sorry! That format is not accepted!")
        else:
            print("The specified file path does NOT exist!")

    elif images == 'images':
        file_path_multiple = input("Please upload your images directory here! Include the full filepath with backslashes (case sensitive)! ")
        if os.path.exists(file_path_multiple):
            type_multiple = input("What type of format would you like to convert your images to?\n"
                "PNG\nJPEG\nHEIC\nGIF\nMOV\nMP4\n\n").casefold()

            if type_multiple == 'gif':
                output_gif_path = os.path.join(file_path_multiple, 'output.gif')
                convert_images_to_gif(file_path_multiple, output_gif_path)

            elif type_multiple in ('mov', 'mp4'):
                output_video_path = os.path.join(file_path_multiple, f'output.{type_multiple}')
                convert_images_to_video(file_path_multiple, output_video_path)

            elif type_multiple in ('png', 'jpeg', 'jpg', 'heic'):
                print("Each image will be converted to specified format! :).")
                convert_images_in_folder(file_path_multiple, type_multiple)

            else:
                print("Sorry! That format is not accepted! Please try again with the available options!")

        else:
            print("The specified file path does NOT exist! Please try again!")
    else:
        print("Sorry! That format is NOT accepted!")


def convert_image(file_path, output_format):
    try:
        img = Image.open(file_path)
        base, _ = os.path.splitext(file_path)
        output_path = f"{base}.{output_format.lower()}"
        img.save(output_path, output_format.upper())
        print(f"Image converted and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def convert_images_to_gif(image_folder, output_path, duration=500):
    img_files = glob.glob(os.path.join(image_folder, '*'))
    img_files.sort()
    images = [Image.open(img) for img in img_files]
    images[0].save(output_path,save_all=True,append_images=images[1:],duration=duration,loop=0)
    print(f"GIF created and saved as {output_path}")


def convert_images_to_video(image_folder, output_path, fps=24):
    img_files = glob.glob(os.path.join(image_folder, '*'))
    img_files.sort()
    clip = mpy.ImageSequenceClip(img_files, fps=fps)
    clip.write_videofile(output_path)
    print(f"Video created and saved as {output_path}")


def convert_images_in_folder(image_folder, output_format):
    try:
        img_files= glob.glob(os.path.join(image_folder, '*'))
        img_files.sort()
        if not img_files:
            print("No images were found! Please try again!")
            return
        output_dir = os.path.join(image_folder, f"converted_{output_format.lower()}")
        os.makedirs(output_dir, exist_ok=True)
        converted_count = 0
        for file_path in tqdm(img_files, desc="Converting images", unit="image"):
            try:
                img = Image.open(file_path)
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                output_path = os.path.join(output_dir, f"{base_name}.{output_format.lower()}")
                img.save(output_path, output_format.upper())
                converted_count += 1
            except Exception as e:
                continue
        print(f"Successfully converted {converted_count} of {len(img_files)} images to {output_format.upper()} format.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
