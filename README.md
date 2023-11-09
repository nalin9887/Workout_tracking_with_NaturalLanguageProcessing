Workout Tracker Banner

Workout Tracker
Welcome to the Workout Tracker project! This Python-based tool allows you to effortlessly keep track of your workouts and fitness progress. By integrating the Nutritionix API for exercise data extraction and the Sheety API for storing workout records in a Google Sheet, you can efficiently monitor your fitness journey.

GitHub License
GitHub Stars
GitHub Forks
GitHub Issues

Table of Contents
Prerequisites
Features
Installation
Usage
Configuration
Screenshots
Contributing
License
Prerequisites
Before you get started with the Workout Tracker, you'll need a few things:

Python: Ensure that Python is installed on your system. If not, you can download and install it from Python's official website.

Required Libraries: Make sure you have the necessary Python libraries installed, particularly the requests library. You can install it using pip:

undefined
Copy code
pip install requests
API Credentials: To make use of the Nutritionix and Sheety APIs, you'll need to obtain API credentials. Sign up for these services and replace the placeholders in the script with your actual API keys.

Features
Natural Language Processing: Input your workout details using plain language, and the script will intelligently recognize the exercises you performed.

Nutritionix Integration: The Nutritionix API is utilized to accurately extract exercise data from your input.

Google Sheets Integration: Your workout data is seamlessly logged into a Google Sheet with the help of the Sheety API.

Installation
Clone the Repository: Start by cloning this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/YourUsername/WorkoutTracker.git
Navigate to the Project Directory: Move into the project directory:

bash
Copy code
cd WorkoutTracker
API Configuration: Open the script and provide your Nutritionix and Sheety API credentials as instructed in the Configuration section of the script. Replace the placeholder values with your actual API keys.

Run the Script: Execute the script:

undefined
Copy code
python workout_tracker.py
Input Workout Data: Follow the on-screen prompts to input your workout details. The script will automatically recognize the exercises and log the data in a Google Sheet.

Configuration
In the script, you will find placeholders for API credentials. Replace these placeholders with your actual API keys.

For example, in the script, you should have something like this:

makefile
Copy code
APP_ID = "your_nutritionix_app_id"
API_KEY = "your_nutritionix_api_key"
# ...

sheety_headers = {
    "Authorization": "Bearer YOUR_SHEETY_TOKEN",
    "Content-Type": "application/json",
}
Replace "your_nutritionix_app_id", "your_nutritionix_api_key", and "YOUR_SHEETY_TOKEN" with your actual API credentials.

Screenshots
Workout Tracker Screenshot

[Optional: Include screenshots or visuals of your Workout Tracker in action.]

Contributing
Contributions to this project are welcome! To contribute, please check the CONTRIBUTING.md file for guidelines and information on how to get involved.

License
This project is licensed under the MIT License. For more details, please refer to the LICENSE file.

Acknowledgments
This project was made possible with the help of various resources and references:

TIL Python Basics Day 38 - Workout Tracking Using Google Sheets
GitHub Topics: Nutritionix API
Google Sheets - Python API, Read & Write Data - YouTube
How to Read and Write In Google Spreadsheet Using Python and Sheety API? - Workfall
How to Connect Python to Google Sheets | Coupler.io Blog
Replace YourUsername/WorkoutTracker with your actual GitHub repository URL and update source URLs with real references used in your project.
