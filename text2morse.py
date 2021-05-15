import argparse

"""
    TEXT-TO-MORSE
    Text to Morse converter is a basic converter that converts a text into morse code
    
    DISCLAIMER
    This is not intended for production use. It is a very basic exercise made for learning Python
"""

morse_dict = {"a": ".-",
              "b": "-...",
              "c": "-.-.",
              "d": "-..",
              "e": ".",
              "f": "..-.",
              "g": "--.",
              "h": "....",
              "i": "..",
              "j": ".---",
              "k": "-.-",
              "l": ".-..",
              "m": "--",
              "n": "-.",
              "o": "---",
              "p": ".--.",
              "q": "--.-",
              "r": ".-.",
              "s": "...",
              "t": "-",
              "u": "..-",
              "v": "...-",
              "w": ".--",
              "x": "-..-",
              "y": "-.--",
              "z": "--..",
              " ": "/",
              "0": "-----",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
              ".": ".-.-.-",
              ",": "--..--",
              "?": "..--..",
              "'": ".----.",
              "!": "-.-.-----.",
              "/": "-..-.",
              "(": "-.--.",
              ")": "-.--.-",
              "&": ".-...",
              ":": "---...",
              ";": "-.-.-.",
              "=": "-...-",
              "+": ".-.-.-",
              "-": "-....-",
              "_": "..--.-",
              '"': ".-..-.",
              "$": "...-..-",
              "@": ".--.-."}


def convert_to_morse(text):
    """
    convert_to_morse is a function that converts the string parameter and returns the morse code into a string

    :param text:
    :return:
    """
    morse_stmt = ""
    for car in text:
        morse_stmt += morse_dict.get(car.lower())
        morse_stmt += " "

    return morse_stmt


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", help="Text to convert in morse")
    args = parser.parse_args()

    if args.text:
        print(convert_to_morse(args.text))
