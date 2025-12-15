# File Organizer Web Application

## Description
This project is a Python-based File Organizer that helps users organize files in a selected directory. Files are categorized into folders such as Images, Documents, Videos, Music, Archives, and Others using a Flask web interface.

## Technologies Used
- Python
- Flask
- HTML
- os, shutil libraries

## Features
- Organizes files based on file extensions
- Automatically creates folders
- Web-based user interface
- Handles permission errors safely

## How to Run
1. Install Flask  
   pip install flask

2. Run the application  
   python app.py

3. Open browser and visit  
   http://127.0.0.1:5000/

4. Enter a user-level directory path (e.g., Downloads)

## Note
Do not use system root directories (C:\\) due to permission restrictions.
