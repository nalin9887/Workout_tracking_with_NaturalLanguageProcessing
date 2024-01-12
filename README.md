# Workout Tracker

Welcome to the Workout Tracker project! This Python-based tool allows you to effortlessly keep track of your workouts and fitness progress. By integrating the Nutritionix API for exercise data extraction and the Sheety API for storing workout records in a Google Sheet, you can efficiently monitor your fitness journey.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before you get started with the Workout Tracker, you'll need a few things:

- **Python**: Ensure that Python is installed on your system. If not, you can download and install it from [Python's official website](https://www.python.org/).

- **Required Libraries**: Make sure you have the necessary Python libraries installed, particularly the `requests` library. You can install it using pip:
    ```bash
    pip install requests
    ```

- **API Credentials**: To make use of the Nutritionix and Sheety APIs, you'll need to obtain API credentials. Sign up for these services and replace the placeholders in the script with your actual API keys.

## Features
- **Natural Language Processing**: Input your workout details using plain language, and the script will intelligently recognize the exercises you performed.

- **Nutritionix Integration**: The Nutritionix API is utilized to accurately extract exercise data from your input.

- **Google Sheets Integration**: Your workout data is seamlessly logged into a Google Sheet with the help of the Sheety API.

## Installation
1. **Clone the Repository**: Start by cloning this repository to your local machine using the following command:
    ```bash
    git clone https://github.com/YourUsername/WorkoutTracker.git
    ```

2. **Navigate to the Project Directory**: Move into the project directory:
    ```bash
    cd WorkoutTracker
    ```

3. **API Configuration**: Open the script and provide your Nutritionix and Sheety API credentials as instructed in the Configuration section of the script. Replace the placeholder values with your actual API keys.

4. **Run the Script**: Execute the script:
    ```bash
    python workout_tracker.py
    ```

5. **Input Workout Data**: Follow the on-screen prompts to input your workout details. The script will automatically recognize the exercises and log the data in a Google Sheet.

## Configuration
In the script, you will find placeholders for API credentials. Replace these placeholders with your actual API keys.

For example, in the script, you should have something like this:
```python
APP_ID = "your_nutritionix_app_id"
API_KEY = "your_nutritionix_api_key"
# ...

sheety_headers = {
    "Authorization": "Bearer YOUR_SHEETY_TOKEN",
    "Content-Type": "application/json",
}
