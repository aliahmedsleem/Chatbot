import nltk
from nltk.chat.util import Chat, reflections
import time
import sys
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define the typing effect function with green color for chatbot responses
def type_like_human(text):
    if "Chatbot:" in text:
        text_parts = text.split("Chatbot: ")
        sys.stdout.write(text_parts[0])
        sys.stdout.flush()
        time.sleep(0.05)  # Faster typing for initial text
        sys.stdout.write("Chatbot: ")
        sys.stdout.flush()
        time.sleep(0.05)  # Slight delay after "Chatbot: "
        sys.stdout.write(Fore.GREEN)  # Start green color
        for char in text_parts[1]:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)  # Slower typing for the chatbot's response
        sys.stdout.write(Style.RESET_ALL)  # Reset color back to default
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Normal typing speed
    print()  # Print a newline after the text

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Ali Ahmed. You can call me Chatbot!",]
    ],
    [
        r"how are you?",
        ["I'm doing good, How about You?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. Bye :)"]
    ],
    [
        r"where are you",
        ["I'm here :)", "Inside this computer :)"]
    ],
    [
        r"where did you develop?",
        ["IKC",]
    ],
    [
        r"what is IKC?",
        ["IKC is an Iraqi college, based in Baghdad - Near Oil Sport Club",]
    ],
    [
        r"tell me more about IKC?",
        ["IKC college has the following departments: Law, Science of Quran, Sharia, Islamic methodology, Arabic language, History, Political science, Media, English, Computer tech engineering, Financial, Kindergarten, Business, Cybersecurity",]
    ],
]

chatbot = Chat(pairs, reflections)

def chatbot_response():
    type_like_human("Hi! I am your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            type_like_human("Chatbot: Bye! Take care.")
            break
        response = chatbot.respond(user_input)
        if response:
            type_like_human(f"Chatbot: {response}")
        else:
            type_like_human("Chatbot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot_response()
