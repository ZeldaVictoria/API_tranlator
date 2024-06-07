from tkinter import filedialog
from package import app
import deepl
import csv

# ---------------- VARIABLES ------------------------
language_option_array =  ["German", "English"]
clear_label = ""


# ---------------- API ------------------------
api_key = "API Key" # Replace with your API key
api_translator = deepl.Translator(api_key)


# ---------------- TRANSLATION ------------------------
# ---------------- Function to handle translation and update the target label with source text
def translate_text(gui):
    lang_validation = validate_languages(gui)
    source_lang_text = gui.input_widget.get("1.0", "end-1c") 
    set_languages_tuple = set_languges(gui)
    if len(source_lang_text) != 0 and lang_validation == True: #check input_widget has value
        translated_text = api_translator.translate_text(source_lang_text, source_lang = set_languages_tuple[0], target_lang = set_languages_tuple[1])
        gui.output_widget.config(text = translated_text)
        gui.information_widget.config(text = clear_label)
   
    else:
        gui.information_widget.config(text = clear_label)
        gui.information_widget.config(text = "- No text to translate \n- No different source and target language", fg = "#ED1652")

# ---------------- Function to check which languages are selected
def validate_languages(gui):
    if gui.source_language_combobox.get() == language_option_array[0] and gui.target_language_combobox.get() == language_option_array[1]:
        return True
    elif gui.source_language_combobox.get() == language_option_array[1] and gui.target_language_combobox.get() == language_option_array[0]:
        return True
    else:
        return False

# ---------------- Function to set source and target languages for API
def set_languges (gui):
    source_lang_array = ["DE", "EN"]
    target_lang_array = ["DE", "EN-US"]
    if gui.source_language_combobox.get() == language_option_array[0] and gui.target_language_combobox.get() == language_option_array[1]:
        set_source_lang = source_lang_array[0]
        set_target_lang = target_lang_array[1]
        return set_source_lang, set_target_lang #returns a tuple
    
    elif gui.source_language_combobox.get() == language_option_array[1] and gui.target_language_combobox.get() == language_option_array[0]:
        set_source_lang = source_lang_array[1]
        set_target_lang = target_lang_array[0]
        return set_source_lang, set_target_lang #returns a tuple


# ---------------- CSV CREATION ------------------------        
# ---------------- Function for CSV creation 
def create_csv(gui):
    widget_values = validate_widgets(gui)
    if widget_values == True:
        source_text_array = create_source_array(gui)
        target_text_array = create_target_array(gui)
        source_lang = set_languges (gui)[0]
        write_csv(gui, source_text_array, target_text_array, source_lang)
    else:
        gui.information_widget.config(text = clear_label)
        gui.information_widget.config(text = "Widgets are empty", fg = "#ED1652")
    
# ---------------- Function validates input and output widgets
def validate_widgets(gui):
    source_textbox_value = gui.input_widget.get("1.0", "end-1c")
    target_textbox_value = gui.output_widget.cget("text")
    if len(source_textbox_value) != 0 and len(target_textbox_value) != 0: 
        return True
    else:
        return False

# ---------------- Function to write array to csv
def write_csv(gui, pSource_array, pTarget_array, pSource_lang):
    csv_fields = ["KEY", "de"]
    filepath = open_filexplorer()
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file, delimiter = ";")
        writer.writerow(csv_fields)
        for i in range(len(pTarget_array)):
            if pSource_lang == "DE":
                writer.writerow([pSource_array[i], pTarget_array[i]])
                
            elif pSource_lang == "EN":
                writer.writerow([pSource_array[i], pTarget_array[i]])
                

# ---------------- Function to create array from input field
def create_source_array(gui):
    source_textbox_value = gui.input_widget.get("1.0", "end-1c")
    return source_textbox_value.split("\n")

# ---------------- Function to create array from output field
def create_target_array(gui):
    target_textbox_value = gui.output_widget.cget("text")
    return target_textbox_value.split("\n")

# ---------------- Function to open the file explorer to choose the save file location
def open_filexplorer(): 
    filepath = filedialog.asksaveasfilename(confirmoverwrite = True, initialfile = "test",title = "Select file", defaultextension=".csv", filetypes=(("csv file", "*.csv"),("All Files", "*.*") ))
    return filepath