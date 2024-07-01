# Mini-Project-1
# Face Recognition and Instagram User Identification (FRI-UI)

**Author**: Sharad Sisodia

## About Project

This project is a face recognition system that analyses and compares one's facial features against a database of known faces to identify the person. The aim is to enhance existing face recognition technology by integrating Open-Source Intelligence (OSINT), making the identification process more informative and accurate. The system uses publicly available data sources like Wikipedia and is developed in Python, utilizing libraries such as OpenCV and PIL. Additionally, it offers the capability to retrieve details of an Instagram user by entering their ID.

## Working of Project

### Image Loading
- Loads images from a specified folder and labels them based on the filename.

### Face Recognition
- Encodes faces from known images and compares them with faces in an unknown image to recognize them.

### GUI with Tkinter
- Intended to create a user interface for selecting files and displaying results (not fully implemented).

### Web Scraping
- Scrapes Wikipedia for information about a person using requests and BeautifulSoup.

### Displaying Images
- Uses IPython.display and PIL to display images within a Jupyter notebook environment.

### Instagram Downloading
- Imports the instaloader module to download images from Instagram (functionality not fully implemented).

The `recognize_faces` function takes an unknown image path, resizes the image, detects faces, encodes them, compares them with known faces, and if a match is found, draws a rectangle around the face and labels it with the name of the recognized person, then displays the image with rectangles and labels.

Additional functions for downloading an image from a URL and scraping Wikipedia for an infobox related to a person's name are included but not fully implemented.
