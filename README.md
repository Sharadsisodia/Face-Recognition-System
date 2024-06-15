# Mini-Project-1
<h1>Project Name: Face Recognition and Instagram User Identification (FRI-UI)</h1>
<br>
Author- Sharad Sisodia 
<br>
<h2>About Project: </h2>
<br>
A face recognition system analyses and compares one’s facial features against database of known faces to identify the person. This project
aims to improve on the existing face recognition technology by implementing Open-Source Intelligence (OSINT). Our goal is to make
identifying people more informative and accurate. Typically, facial recognition systems don't give a lot of specific details about the person whose face they detect. By integrating OSINT, our system ensures that this gap is filled. We used publicly available data sources like Wikipedia to make it possible. We have made this project in Python and utilised its libraries like OpenCV, PIL etc.
Apart from this, this project also provides the detail of instagram user by just entering the instagram id of the user.
<br>
<h2>Working of project:</h2>
<br>
<h4>Image Loading:</h4> It loads images from a specified folder and labels them based on the filename.<br>
<h4>Face Recognition:</h4> It encodes faces from known images and compares them with faces in an unknown image to recognize them.<br>
<h4>GUI with Tkinter:</h4> Although not fully implemented in the provided code, it seems intended to create a user interface for selecting files and displaying results.<br>
<h4>Web Scraping:</h4> It scrapes Wikipedia for information about a person using requests and BeautifulSoup.<br>
<h4>Displaying Images:</h4> It uses IPython.display and PIL to display images within a Jupyter notebook environment.<br>
<h4>Instagram Downloading:</h4> The instaloader module is imported, suggesting functionality to download images from Instagram, although this is not implemented in the provided code.<br>
<h5>The main function recognize_faces takes an unknown image path, resizes the image, detects faces, encodes them, compares them with known faces, and if a match is found, draws a rectangle around the face and labels it with the name of the recognized person. Then it displays the image with rectangles and labels.</h5><br>
<br>
The code also includes functions for downloading an image from a URL and scraping Wikipedia for an infobox related to a person’s name. However, these functions are not fully implemented in the provided snippet.