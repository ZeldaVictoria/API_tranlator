import json


filepath = "config.json"

with open(filepath, "r") as file:
    data = json.load(file)


class Style:
    def __init__(self):
        self.header_bg = data["header"]["background-color"]
        self.header_fg = data["header"]["font-color"]
        self.header_ftyle =data["header"]["font-style"]
        self.header_fsize =data["header"]["font-size"]

        self.input_widget_bg = data["input-widget"]["background-color"]
        self.input_widget_fg = data["input-widget"]["font-color"]
        self.input_widget_fstyle = data["input-widget"]["font-style"]
        self.input_widget_fsize = data["input-widget"]["font-size"]
        self.input_widget_wx = data["input-widget"]["window-width"]
        self.input_widget_wy = data["input-widget"]["window-height"]

        self.output_widget_bg = data["output-widget"]["background-color"]
        self.output_widget_fg = data["output-widget"]["font-color"]
        self.output_widget_fstyle = data["output-widget"]["font-style"]
        self.output_widget_fsize = data["output-widget"]["font-size"]
        self.output_widget_wx = data["output-widget"]["window-width"]
        self.output_widget_wy = data["output-widget"]["window-height"]

        self.information_widget_bg = data["information-widget"]["background-color"]
        self.information_widget_fg = data["information-widget"]["font-color"]
        self.information_widget_fstyle = data["information-widget"]["font-style"]
        self.information_widget_fsize = data["information-widget"]["font-size"]
        self.information_widget_wx = data["information-widget"]["window-width"]
        self.information_widget_wy = data["information-widget"]["window-height"]

        self.translate_btn_bg = data["translation-button"]["background-color"]
        self.translate_btn_fg = data["translation-button"]["font-color"]
        self.translate_btn_fstyle = data["translation-button"]["font-style"]
        self.translate_btn_fsize = data["translation-button"]["font-size"]
        self.translate_btn_wx = data["translation-button"]["button-width"]
        self.translate_btn_wy = data["translation-button"]["button-height"]

        self.csv_btn_bg = data["csv-button"]["background-color"]
        self.csv_btn_fg = data["csv-button"]["font-color"]
        self.csv_btn_fstyle = data["csv-button"]["font-style"]
        self.csv_btn_fsize = data["csv-button"]["font-size"]
        self.csv_btn_wx = data["csv-button"]["button-width"]
        self.csv_btn_wy = data["csv-button"]["button-height"]
