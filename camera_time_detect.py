# author: Alice Lynch
# version 0.0

import cv2
import pytesseract
import arrow
import glob
from tqdm import tqdm

import sys, os

#Update below line to the path to your installation of tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

"""
Reads a single video and outputs the onscreen timestamp of the first frame (either as a number or in date format)
"""
def read_in_video(path, output="timestamp"):
    vidcap = cv2.VideoCapture(path)
    success, image = vidcap.read()
    if success:
        image = image[1035:1080, 850:1950]
        cv2.imwrite("first_frame.jpg", image)
        datetime = pytesseract.image_to_string(image)[:18]
        date = arrow.get(datetime, 'MM/DD/YYYY HH:mmA')
        if output=="timestamp":
            return date.timestamp
        else:
            return date.format()

"""
Returns a dictionary containing the timestamps of the first frame of all MP4 files in a directory.
"""
def run_dir(dir_path, output="timestamp"):
    videos = glob.glob(f"{dir_path}/*.MP4")
    time_stamps = {}
   # for video in videos:
    for i in tqdm(range(len(videos))):
        video = videos[i]
        try:
            timestamp = read_in_video(video, output=output)
            time_stamps[video[len(dir_path) + 1:]] = timestamp
        except arrow.parser.ParserMatchError as e:
            time_stamps[video[len(dir_path)+1:]] = "Error"
    return time_stamps

"""
Writes a dictionary containing "filename":"timestamp" to a csv file, with headers.
No return value.
"""
def write_to_csv(csv_path, dict):
    with open(csv_path,'w+') as f:
        f.write("Filename, Timestamp \n")
        for item in dict:
            f.write(f"{item}, {dict[item]} \n")


if __name__ == "__main__":
    if not(len(sys.argv)>=3 and len(sys.argv)<=4):
        print("Incorrect command line usage \nPlease input 'python camera_time_detect.py \"my_directory_path\" \"my_csv_path\"' \nYou can add an optional -d flag to indicate that you want to output as a human readable date stamp instead of a timestamp." )
    else:
        if len(sys.argv) == 4:
            if sys.argv[3] == "-d":
                timestamp="date"
            else:
                print("Error, unrecognised flag: " + sys.argv[3])
                sys.exit()
        else:
            timestamp = "timestamp"
        if not os.path.exists(sys.argv[1]):
            print(f"Video directory path \"{sys.argv[1]}\" does not exist")
        elif not os.path.isdir(sys.argv[1]):
            print(f"Video directory path \"{sys.argv[1]}\" is not a directory")
        elif os.path.exists(sys.argv[2]):
            answer = input(f"csv output path \"{sys.argv[2]}\" already exists, do you want to overwrite? y/n")
            if answer == "y":
                write_to_csv(sys.argv[2], run_dir(sys.argv[1],timestamp))
        else:
            write_to_csv(sys.argv[2], run_dir(sys.argv[1],timestamp))
