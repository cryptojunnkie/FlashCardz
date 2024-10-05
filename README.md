# CompTIA Security+ Study Guide

## Overview
   This application is designed to help users study for the CompTIA Security+ certification exam. It utilizes interactive 
   flashcards to provide educational content on key topics such as the CIA triad (Confidentiality, Integrity, Availability), 
   cybersecurity 
   objectives, and non-repudiation.

## Features
- **Flashcard Study Material**: Navigate through flashcards with essential information related to cybersecurity.
- **Audio Playback**: Listen to the flashcard content being read aloud, aiding in auditory learning.
- **Customizable User Interface**: Select your preferred background color for a more personalized user experience.
- **HTML Content Support**: Flashcards support basic HTML for formatting text and enhancing readability.

## Technologies Used
- **Streamlit**: A framework for building interactive web applications in Python.
- **gTTS (Google Text-to-Speech)**: A Python library that converts text into spoken audio.

## Installation
   To run this application locally, follow these steps:

### Prerequisites
   1. Install Python (version 3.7 or higher).
   2. Install Streamlit and gTTS using pip:

## Paste the code below in order to install the modules required to run the app properly:
   pip install streamlit gtts

## 2. Navigate to the Project Directory
   Change into the project directory:

## Copy code:
   cd FlashCardz

## 3. Install Prerequisites
   Make sure you have Python installed (version 3.7 or higher). Then, install Streamlit and gTTS using pip:

## Copy code:
   pip install streamlit gtts

## 4. Running the Application
   Run the Streamlit app:
## Copy code:
   streamlit run streamlit_app.py

## 5. Open the Application
   Upon running you should be redirected automatically to the localhost URL running to see the app running. Otherwise open the        provided local URL (usually http://localhost:8501) in your web browser to access the application. You will be able to view in 
   the terminal the correct URL being used to run the app on. The controls of how to select this URL will be displayed in 
   terminal. So follow those instructions. Since I am using VS Code in my terminal the command to go to the URL posted is >> 
   ctrl+left click of mouse on the URL.<<

## Usage
   Select the background color for the flashcards using the color picker in the sidebar.
   Click the "Read Aloud" button for any flashcard to listen to its content.
   Navigate through the flashcards to learn key concepts relevant to the Security+ certification.

## Feel free to modify the flashcard content in the code to fit your study needs.

### Making Changes and Uploading to GitHub
   After making any desired changes to the code, you can upload your modifications back to GitHub by following these steps:

## Check the Status: See which files have changed:
## Copy code:
   git status

## Stage the Changes: 
   Add the modified files to the staging area. You can add all changed files using:
## Copy code:
   git add .

## Alternatively, specify a single file:
## Copy code:
   git add path/to/streamlit_app.py

## Commit Your Changes: Create a commit with a descriptive message:
## Copy code:
   git commit -m "Your descriptive commit message goes inbetween the quotes here!"

## Push Changes to GitHub: Upload your changes to the main branch of your repository:
## Copy code:
   git push origin main

## Replace main with the correct branch name if you are working with a different branch.

## Contributing
   Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request or 
   submit an issue.

## License
   This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
   CompTIA: For providing the certification and materials that inspired this study guide.
   Streamlit: For creating an easy-to-use framework for building web applications.
gTTS: For enabling text-to-speech capabilities in Python.
