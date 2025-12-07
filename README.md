# Photo Manipulation Program

## Demo
Demo Video: <https://youtu.be/-bZnyzBN09M>

## GitHub Repository
GitHub Repo: <https://github.com/Chaos198177/ANGM-2305.0W2-Final-Project.git>

## Description
### This program will take an image or series of images based on the user's input and convert it into any available format based on the user's wishes. It will then store it in the original folder under a new, recognizable name. 
#### Some research that I had to do in advance were the following:
- How to accept a file path from a user's input. It was challenging to figure out at first, but after much trial and error, I managed to get it. This lines up with converting an entire folder of images.
- How to implement cowsay into the user input. I did not want a simple, boring-looking program. While cowsay does not have the capability to accept user inputs, I was able to work around it and display the program's message in cowsay and accept the user input in another line beginning in ">"
- How to implement a progress bar for "MP4" conversions. I used tqdm to achieve this. It uses len and a counter.
- How to save the output file as the original name, but under a different extension. This was particularly tricky for folders, but I worked it out! This does NOT overwrite the original file(s)!
- How to skip files that couldn't be accessed and not run into an error and stop the entire process. This was done using Exception. 
- How to load all files for a GIF, including partial images, instead of running into an unwanted error. ImageFile.LOAD_TRUNCATED_IMAGES = True does this for me by forcing Pillow to load all files, and then uses try/except to skip corrupted files.
### What would I do to improve this program?
- Add more conversion options
- Add more user interaction (fun little games while waiting for the conversion to finish, perhaps)
- Add a random generator for the cowsay messages, specifically for user input
- Add the option to choose the FPS for MP4 and GIF
Overall, I'm pretty happy with this program! I like photography, and this program is fun for all ages! I hope you enjoy it!