# Chatbot Application

This is a simple Python-based chatbot application that performs various tasks such as greeting the user, providing the current date and time, performing arithmetic operations, and more. The chatbot also includes functionality to open the default web browser to Google's homepage and to access the system's camera.

## Features

- Greets the user based on the current time of day
- Provides the current day of the week
- Displays the current date
- Performs arithmetic operations: addition, subtraction, multiplication, division, and integer division
- Opens the default web browser to Google
- Accesses the system's camera and displays the feed
- Responds to basic conversational inputs

## Requirements

- Python 3.x
- OpenCV (cv2)
- Threading module

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sms32/CHATBOT-PYTHON
cd chatbot
```

2. Install the required libraries:

```python
pip install opencv-python
```

## Usage
1. Run the chatbot application:
   
```python
python chatbot.py
```

2.  The chatbot will ask for your name and greet you based on the current time of day.

3.  You can interact with the chatbot by typing commands. Here are some examples of commands you can use:
     ·  "day" - The chatbot will tell you the current day of the week.

     ·  "date" - The chatbot will tell you the current date.
   
     ·  "time" - The chatbot will tell you the current time.
   
     ·  "addition" or "add" - The chatbot will ask for values and perform addition.
   
     ·  "subtraction" or "subtract" or "difference" - The chatbot will ask for values and perform subtraction.
   
   
     ·  "multiplication" or "multiply" or "product" - The chatbot will ask for values and perform multiplication.
   
     ·  "division" or "divide" - The chatbot will ask for values and perform division.
   
     ·  "int division" or "integer division" - The chatbot will perform integer division.
   
     ·  "google" - The chatbot will open Google's homepage in the default web browser.
   
     ·  "camera" - The chatbot will access the system's camera and display the feed.
   
     ·  "exit" - The chatbot will exit the application.

4. The chatbot will respond to basic conversational inputs like "hi", "hey", "who are you", and "how are you".

## Code Explanation
- 'wishMe(name)'
   Greets the user based on the current time of day.

- 'tellDay()'
   Tells the user the current day of the week.

- 'username(name)'
   Prints a message asking how the chatbot can help the user.

- 'takeCommand(name)'
   Takes input from the user and returns it in lowercase.

- 'tellDate()'
Tells the user the current date.

- 'addition(name)'
   Asks the user for values and performs addition.

- 'multiplication(name)'
   Asks the user for values and performs multiplication.

- 'subtraction(name)'
   Asks the user for values and performs subtraction.

- 'division(name)'
   Asks the user for values and performs division.

- 'int_division(name)'
   Asks the user for values and performs integer division.

- 'google()'
   Opens Google's homepage in the default web browser.

- 'open_camera_thread(cap, stop_event)'
   Opens the system's camera and displays the feed in a separate thread.

- 'open_camera(name)'
   Handles the camera feed and allows the user to close the camera feed.

- 'Main Function'
   The main function initializes the chatbot, greets the user, and enters a loop to take and respond to user commands.

## Contributing
Feel free to fork this repository and contribute by submitting a pull request. Any contributions, such as bug fixes, enhancements, or new features, are welcome!


## SAMPLE

<img src="https://github.com/sms32/CHATBOT-PYTHON/assets/153702953/51f902f1-b778-4362-8b57-d18910a2efe7" alt="ARDUINO UNO"  width="50%">
<br>
<br>
<img src="https://github.com/sms32/CHATBOT-PYTHON/assets/153702953/85ddb439-91ea-482e-a82d-8eebda88a3ca" alt="ARDUINO UNO"  width="50%">
<br>
<br>
<img src="https://github.com/sms32/CHATBOT-PYTHON/assets/153702953/9b1fc0d7-48c8-4fe8-a618-4a340e181ff6" alt="ARDUINO UNO"  width="50%">


