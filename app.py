from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string


def image_to_sound(path_to_image):
    """
    Function for converting an  image to sound
    """
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="en")
        sound.save("https://1drv.ms/u/s!Ah3irGsS8cnzgl7T9hPAEYnidXx6?e=Duqw9e")
        return True
    except Exception as bug:
        print("The bug thrown while excuting the code\n", bug)
        return


if __name__ == "__main__":
    image_to_sound("https://1drv.ms/i/s!Ah3irGsS8cnzgmDSwMcNyFgLYBkc?e=d0j6pn")
    input()
