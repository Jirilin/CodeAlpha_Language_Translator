import tkinter as tk
from googletrans import Translator
# Create the main window.
root = tk.Tk()
root.title("MB Translator")
root.geometry("500x500")
# Create the text input field.
text_input = tk.Entry(root)
text_input.pack()
# Create the language selection menu.
language_menu = tk.OptionMenu(root, tk.StringVar(), "English", "Spanish", "French", "German", "Italian")
language_menu.pack()
# Create the translate button.
translate_button = tk.Button(root, text="Translate", command="translate_text")
translate_button.pack()
# Create the output label.
output_label = tk.Label(root, text="")
output_label.pack()
# Define the translate_text function.
def translate_text():
  # Get the text from the text input field.
  text = text_input.get()
  # Get the selected language from the language selection menu.
  language = language_menu.get()
  # Translate the text.
  translator = Translator()
  translation = translator.translate(text, dest=language)
  # Display the translated text in the output label.
  output_label.config(text=translation.text)
# Run the main loop.
root.mainloop()