import tkinter as tk

BG_PRIMARY = "#212b44"
BG_PRIMARY_LIGHT = "#19212f"
BG_SECONDARY = "#151b2a"

TEXT_PRIMARY = "#ffffff"


class Label(tk.Label):
    def __init__(self, *args, fontSize=18, **kwargs):

        props = {
            'bg': BG_PRIMARY,
            'fg': TEXT_PRIMARY
        }

        super().__init__(*args, **props, **kwargs)

        self.config(font=("Helvetica", fontSize))


class Button(tk.Button):
    def __init__(self, *args, **kwargs):

        props = {
            'bg': BG_SECONDARY,
            'fg': TEXT_PRIMARY,
            'activebackground': BG_PRIMARY_LIGHT,
            'activeforeground': TEXT_PRIMARY,
            'borderwidth': 1,
            'highlightthickness': 1
        }

        super().__init__(*args, **props, **kwargs)


class Checkbutton(tk.Checkbutton):
    def __init__(self, *args, **kwargs):

        props = {
            'onvalue': 1,
            'offvalue': 0,
            'selectcolor': BG_PRIMARY_LIGHT,
            'bg': BG_PRIMARY,
            'fg': TEXT_PRIMARY,
            'activebackground': BG_PRIMARY,
            'activeforeground': TEXT_PRIMARY,
            'highlightthickness': 0
        }

        super().__init__(*args, **props, **kwargs)
