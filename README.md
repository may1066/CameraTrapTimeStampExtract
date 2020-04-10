_Note: This will only work on certain camera trap's footage, and was developed for a specific project_

# Setup
Install tesseract from here: https://tesseract-ocr.github.io/tessdoc/Home.html

Currrently, due to early development the path to the tesseract.exe file needs to be manually updated in camera_time_detect.py.
Replace the path on line 13 (`pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'`) with the path to your installation directory. Leave the r intact at the start of the string.

eg.
`pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'`
changes to
`pytesseract.pytesseract.tesseract_cmd = r'my_path_to_tesseract.exe'`

Make sure that any backslashes (\\) are either doubled or changed to forward slashes. (/)

You can set up the python enviroment using pip and the requirements.txt file. If you don't have python installed look at www.python.org and follow the instructions.
From a terminal(cmd or powershell should both work on Windows) navigate to the folder containing this repository and run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`


# Usage Example

Either run from the command line using:
 `python camera_time_detect.py "my_directory_containing_videos_path" "my_csv_path"`
 You can add an optional -d flag to indicate that you want to output as a human readable date stamp instead of a timestamp.
  `python camera_time_detect.py "my_directory_containing_videos_path" "my_csv_path" -d`


Or use as a library by using:
`import camera_time_detect`
 `write_to_csv("my_csv_path", run_dir("my_dir_path"))`

