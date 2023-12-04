import PySimpleGUI as sg

# User's health
health = 10
cont = 0

# Define the layout for the PySimpleGUI window
layout = [
    [sg.Text("What is your name?"), sg.InputText(key="name")],
    [sg.Text("What is your age?"), sg.InputText(key="age")],
    [sg.Button("Start Game")],
]

secondlayout = [
    [sg.Text(f"Your Health {health}")],    
    [sg.Text("Please click the Continue button to continue the story.")],
    [sg.Button("Continue")],
    [sg.Multiline(size=(40, 10), key="output_text", autoscroll=True)]  # Text display area

]
def switch_to_second_layout():
    window.close
    window2 = sg.Window("Knighting Blade", secondlayout, finalize=True, icon="icon.png")  # Create a new window with the second layout
    return window2


# Create the window
window = sg.Window("Knighting Blade", layout, finalize=True, icon="icon.png")

def display_text(text):
    window["output_text"].print(text)

# Game loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Start Game" and cont == 0:
        cont = 1
        name = values["name"]
        age = values["age"]
        sg.popup(f"Hello, {name}. You are {age} years old. A little introduction. This is my first ever game. I implemented this using pysimplegui. At the end of the game, you will have the option to provide me with feedback. Please do so!")
        
        window = switch_to_second_layout()
        window["output_text"].print("It's medieval times, and you're relaxing at home, sharpening your blade when you hear a knock. This blade is your most prized possession, passed down from your father. This was before the war...before his death.")
        window["output_text"].print("You live in a small village, Caltadia, with your mother. When suddenly, a higher elf priest contacts you...")
        window["output_text"].print(f"Good day, fellow traveler. You, {name}, have been found by the great elves to be in possession of a mystical weapon known as the...")

    
    # You can add more event handling code for the game's progress here.

# Close the window
window.close()
