import datetime
import webbrowser
import cv2
import threading

def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(f"Good Morning {name}!")
    elif hour >= 12 and hour < 18:
        print(f"Good Afternoon {name}!")
    else:
        print(f"Good Evening {name}!")

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    day_of_the_week = Day_dict.get(day, "Invalid day")
    print("BOT: The day is " + day_of_the_week)

def username(name):
    print(f"BOT: How can I help you, {name}?")

def takeCommand(name):
    query = input(f"{name}: ")
    return query.lower()

def tellDate():
    today = datetime.datetime.today().strftime("%B %d, %Y")
    print(f"BOT: Today's date is {today}")

def addition(name):
    print("BOT: How many values?")
    n = int(input(f"{name}: "))
    values = [int(input(f"BOT: Enter value {i + 1}: ")) for i in range(n)]
    total = sum(values)
    print(f"BOT: The sum of {n} numbers is {total}")

def multiplication(name):
    print("BOT: How many values?")
    n = int(input(f"{name}: "))
    values = [int(input(f"BOT: Enter value {i + 1}: ")) for i in range(n)]
    total = 1
    for val in values:
        total *= val
    print(f"BOT: The product of {n} numbers is {total}")

def subtraction(name):
    print("BOT: Difference of two numbers")
    values = [int(input(f"BOT: Enter value {i + 1}: ")) for i in range(2)]
    total = abs(values[0] - values[1])
    print(f"BOT: The difference of two numbers is {total}")

def division(name):
    print("BOT: Division of two numbers")
    values = [int(input(f"BOT: Enter value {i + 1}: ")) for i in range(2)]
    quotient = values[0] / values[1]
    remainder = values[0] % values[1]
    print(f"BOT: The quotient is {quotient}")
    print(f"BOT: The remainder is {remainder}")

def int_division(name):
    print("BOT: Integer division of two numbers")
    values = [int(input(f"BOT: Enter value {i + 1}: ")) for i in range(2)]
    total = values[0] // values[1]
    print(f"BOT: The integer division result is {total}")

def google():
    webbrowser.open('https://google.com')

def open_camera_thread(cap, stop_event):
    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow('Image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def open_camera(name):
    cap = cv2.VideoCapture(0)
    stop_event = threading.Event()
    camera_thread = threading.Thread(target=open_camera_thread, args=(cap, stop_event))
    camera_thread.start()
   
    while True:
        print("BOT: Do you want to close the camera? Type 'yes' or 'no'")
        s = input(f"{name}: ").lower()
        if "yes" in s:
            stop_event.set()
            camera_thread.join()
            break

if __name__ == '__main__':
    name = input("What is your name? : ")
    wishMe(name)
    username(name)
   
    while True:
        command = takeCommand(name)
        if "day" in command:
            tellDay()
        elif "hi" in command or "hey" in command:
            print(f"BOT: Hello {name}")
            print(f"BOT: How are you {name}")
        elif "fine" in command:
            print("BOT: That's good.")
        elif "exit" in command:
            print("BOT: Exiting...")
            break
        elif "time" in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"BOT: {name}, the time is {strTime}")
        elif "who are you" in command:
            print("BOT: I am your chatbot.")
        elif "date" in command:
            tellDate()
        elif "addition" in command or "add" in command:
            print(f"BOT: Sure {name}")
            addition(name)
        elif "subtraction" in command or "subtract" in command or "difference" in command:
            print(f"BOT: Sure {name}")
            subtraction(name)
        elif "multiplication" in command or "multiply" in command or "product" in command:
            print(f"BOT: Sure {name}")
            multiplication(name)
        elif "division" in command or "divide" in command:
            print(f"BOT: Sure {name}")
            division(name)
            if "int" in command or "integer" in command:
                print(f"BOT: Sure {name}")
                int_division(name)
        elif "google" in command:
            google()
        elif "camera" in command:
            open_camera(name)
        else:
            print(f"BOT: I'm not sure how to respond to '{command}'. Try asking for something else, {name}, or type 'exit' to quit.")
