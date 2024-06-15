import os
import cv2
import numpy as np
import face_recognition
import tkinter as tk
from tkinter import Tk,Entry,Button,INSERT
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
from IPython.display import display, Image
from PIL import Image as PILImage
from io import BytesIO
import instaloader

# Function to load images and their corresponding labels from a directory
def load_images_from_folder(folder):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            labels.append(os.path.splitext(filename)[0])  # Extracting the filename as label
    return images, labels

# Load known images
known_images, known_labels = load_images_from_folder("/workspaces/Mini-Project-1/known")

# Create a function to recognize faces in an unknown image
def recognize_faces(unknown_image_path):
    # Load the unknown image
    unknown_image = cv2.imread(unknown_image_path)
    # Encoding known faces (same as your existing code)
    # ...
    known_face_encodings = []
    for image in known_images:
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_img)
        if len(face_encodings) > 0:
            known_face_encodings.append(face_encodings[0])

    # Resize the unknown image (same as your existing code)
    # ...
    unknown_image_resized = cv2.resize(unknown_image, (0, 0), fx=0.5, fy=0.5)

    # Recognize faces (same as your existing code)
    # ...
    rgb_unknown_image_resized = cv2.cvtColor(unknown_image_resized, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_unknown_image_resized)
    unknown_face_encodings = face_recognition.face_encodings(rgb_unknown_image_resized, face_locations)    

    # Display the result (same as your existing code)
    # ...
#-------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
    for unknown_face_encoding in unknown_face_encodings:
        # Compare the face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
        name = "/workspaces/Mini-Project-1/unknown"

    # If a match is found, find the index of the matching known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_labels[first_match_index]

        # Draw a box around the face and label it
        top, right, bottom, left = face_locations[0]
        cv2.rectangle(unknown_image_resized, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(unknown_image_resized, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the resized image
    window_name = "My Image"
    # image = cv2.imread(unknown_image_resized)
    cv2.imshow(window_name,unknown_image_resized)
    cv2.waitKey()

    def download_image(url):
        response = requests.get(url)
        img = PILImage.open(BytesIO(response.content))
        return img

    def get_infobox_with_image(person_name):
        url = f"https://en.wikipedia.org/wiki/{person_name}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            infobox = soup.find('table', class_='infobox')
            if infobox:
                # Parse the infobox table and format it into a dictionary
                infobox_dict = {}
                img_url = None
                for row in infobox.find_all('tr'):
                    cells = row.find_all(['th', 'td'])
                    if len(cells) == 2:
                        key = cells[0].get_text().strip()
                        value = cells[1].get_text().strip()
                        # Check if the value contains an image
                        if cells[1].find('img'):
                            img_url = "https:" + cells[1].find('img')['src']
                            infobox_dict[key] = (value, img_url)
                        else:
                            infobox_dict[key] = value

                # Print the infobox in a table format
                print("Infobox:")
                for key, value in infobox_dict.items():
                    if isinstance(value, tuple):
                        print(f"| {key:<30} | {value[0]:<50} |")
                    else:
                        print(f"| {key:<30} | {value:<50} |")

                print("\n")

                # Display the main portrait image
                if img_url:
                    print("Main Portrait Image:")
                    response = requests.get(img_url)
                    img = PILImage.open(BytesIO(response.content))
                    img.show()
                else:
                    print("Main portrait image not found in the infobox.")
            else:
                print("Infobox not found on Wikipedia page.")
        else:
            print("Failed to retrieve Wikipedia page.")

    def main():
        person_name = name
        get_infobox_with_image(person_name)

    if __name__ == "__main__":
        main()

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        recognize_faces(file_path)

#===============================================================
# #Instagram Code
def Instagram_Code():
    print(entry.get()) 
    # instagram program
    L=instaloader.Instaloader()
    # a=input("Enter your Instagram ID: ")
    profile=instaloader.Profile.from_username(L.context,entry.get())
    print("Username",profile.full_name)
    print(f"Bio of {entry.get()} is: {profile.biography}")
    print(f"Number of Posts Uploaded: {profile.mediacount}")
    if not profile.is_private:
        print("Followers:",profile.followers)
        print("Following:",profile.followees)
    else:
        print("Profile is private")
    profile_pic_url=profile.profile_pic_url
    print("Profile Photo",)
    # URL of the image
    url = profile_pic_url

    # Fetch the image data from the URL
    response = requests.get(url)

    # Create an Image object from the response content
    img = PILImage.open(BytesIO(response.content))

    # Display the image
    img.show()

#==============================================================
# Create a simple GUI using tkinter
root = tk.Tk()
root.title("Face Recognition App")
root.geometry("620x300+200+200")
root.configure(bg="lightblue")

# Label for image selection
label_Select_Image = tk.Label(root, text="Select an image to recognize faces:", font=("calibre", 10, "bold"))
label_Select_Image.grid(row=0, column=0)

# Button for browsing
button1 = tk.Button(root, text="Browse", command=open_file_dialog)
button1.grid(row=0, column=1)

# Label and Entry for Instagram ID
name_label = tk.Label(root, text="Enter Instagram ID to get the Info of it", font=("calibre", 10, "bold"))
name_label.grid(row=1, column=0)
entry = tk.Entry(root, bg="white", width=40, borderwidth=5, relief="groove", font=("calibre", 10, "normal"))
entry.grid(row=1, column=1)

# Search button
button = tk.Button(root, text='Search', command=Instagram_Code, highlightthickness=6,highlightbackground="lightblue")
button.grid(row=2, column=1)

root.mainloop()