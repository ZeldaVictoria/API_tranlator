import tkinter as tk 
from tkinter import ttk
from package import libraries
from package import config



class App_GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Translation Tool")
        self.geometry("1600x800")
        self.resizable(False, False)
        # ---------------- HEADER ------------------------
        self.header = tk.Label(self, 
                               text = "Python Translator", 
                               background = config.Style().header_bg,
                               foreground = config.Style().header_fg,
                               font = (config.Style().header_ftyle, config.Style().header_fsize))
        self.header.place(relx=0.5, rely=0.1, anchor = "center")

        
        # ---------------- INPUT / SOURCE LANGUAGE SIDE ------------------------
        self.source_side_header = tk.Label(self, 
                                           text = "Input source language", 
                                           font = ("default, 12"))
        self.source_side_header.place(relx=0.2, rely = 0.25, anchor = "center")
        
        # ---------------- Drop Down Menu
        self.source_language_combobox = ttk.Combobox(self, width = 30, state = "readonly", values = libraries.language_option_array)
        self.source_language_combobox.set("Select an option")
        self.source_language_combobox.place(relx=0.2, rely = 0.3, anchor = "center")
        
        # ---------------- inputbox
        self.input_widget = tk.Text(self, 
                                     width = config.Style().input_widget_wx, 
                                     height = config.Style().input_widget_wy, 
                                     bg = config.Style().input_widget_bg, 
                                     fg = config.Style().input_widget_fg,
                                     font = (config.Style().input_widget_fstyle, config.Style().input_widget_fsize))
        self.input_widget.place(relx=0.2, rely = 0.6, anchor = "center")


        # ---------------- OUTPUT / TARGET LANGUAGE SIDE ------------------------
        self.target_side_header = tk.Label(self, 
                                           text = "Input target language", 
                                           font = ("default, 12"))
        self.target_side_header.place(relx=0.8, rely = 0.25, anchor = "center")
        
        # ---------------- Drop Down Menu
        self.target_language_combobox = ttk.Combobox(self, width = 30, state = "readonly", values = libraries.language_option_array)
        self.target_language_combobox.set("Select an option")
        self.target_language_combobox.place(relx=0.8, rely = 0.3, anchor = "center")
        
        # ---------------- outputbox
        self.output_widget = tk.Label(self, 
                                     width = config.Style().output_widget_wx, 
                                     height = config.Style().output_widget_wy, 
                                     bg = config.Style().output_widget_bg, 
                                     fg = config.Style().output_widget_fg,
                                     font = (config.Style().output_widget_fstyle, config.Style().output_widget_fsize),
                                     text = "", 
                                     wraplength=400, 
                                     anchor="nw", 
                                     justify="left")
        self.output_widget.place(relx=0.8, rely = 0.6, anchor = "center")


        # ---------------- INFORMATION LABEL ------------------------
        self.information_widget = tk.Label(self, 
                                          text = "", 
                                          justify="center", 
                                          width = config.Style().information_widget_wx, 
                                          height = config.Style().information_widget_wy, 
                                          bg = config.Style().information_widget_bg, 
                                          fg = config.Style().information_widget_fg,
                                          font = (config.Style().information_widget_fstyle, config.Style().information_widget_fsize))
        self.information_widget.place(relx=0.5, rely = 0.9, anchor = "center")


        # ---------------- START TRANSLATION BUTTON  ------------------------
        self.start_translate_button = tk.Button(self, 
                                                text = "translate", 
                                                bg = config.Style().translate_btn_bg, 
                                                fg = config.Style().translate_btn_fg, 
                                                width = config.Style().translate_btn_wx,
                                                height = config.Style().translate_btn_wy,
                                                font = (config.Style().translate_btn_fstyle, config.Style().translate_btn_fsize))
        self.start_translate_button["command"] = lambda: libraries.translate_text(self)
        self.start_translate_button.place(relx = 0.5, rely= 0.5, anchor = "center")

        # ---------------- CREATE CSV BUTTON  ------------------------
        self.create_csv_button = tk.Button(self, 
                                           text = "create\nCSV", 
                                           bg = config.Style().csv_btn_bg, 
                                           fg = config.Style().csv_btn_fg,
                                           width = config.Style().csv_btn_wx,
                                           height = config.Style().csv_btn_wy,
                                           font = (config.Style().csv_btn_fstyle, config.Style().csv_btn_fsize))
        self.create_csv_button["command"] = lambda: libraries.create_csv(self)
        self.create_csv_button.place(relx = 0.5, rely= 0.7, anchor = "center")