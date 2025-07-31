import tkinter as tk
from tkinter import ttk
from typing import Callable, Any

import PIL

from core.config import (
    ACTION_BUTTON_WIDTH,
    PADDING_USUAL,
    BIGGER_FONT,
    PADDING_FIRST_ELEMENT,
    SMALL_BUTTON_WIDTH,
    ENTRIES_WIDTH_PERCENTS
)


def setup_main_action_button_widget(
        root: tk.Tk,
        text: str,
        command: Callable,
        row: int,
        column: int,
        sticky: str
) -> ttk.Button:

    button = ttk.Button(root, text=text, width=ACTION_BUTTON_WIDTH, command=command)
    button.grid(row=row, column=column, sticky=sticky, **PADDING_USUAL)

    return button


def setup_main_label(root: tk.Tk, text: str, row: int, column: int, sticky: str) -> ttk.Label:
    lbl = ttk.Label(root, font=BIGGER_FONT, text=text)
    lbl.grid(row=row, column=column, sticky=sticky, **PADDING_FIRST_ELEMENT)
    return lbl


def setup_browse_file_button(
        root: tk.Tk,
        command: Callable,
        row: int,
        column: int,
        sticky: str,
        image: PIL.ImageTk
) -> ttk.Button:
    browse_file_button = ttk.Button(root, width=SMALL_BUTTON_WIDTH, image=image, command=command)
    browse_file_button.grid(row=row, column=column, sticky=sticky)
    return browse_file_button


def setup_file_path_entry(root: tk.Tk, row: int, column: int, sticky: str) -> ttk.Entry:
    file_path_entry = ttk.Entry(root, width=ENTRIES_WIDTH_PERCENTS)
    file_path_entry.grid(row=row, column=column, sticky=sticky, **PADDING_USUAL)
    return file_path_entry


def setup_yes_or_no_type_checkbox(
        root: tk.Tk,
        text: str,
        onvalue: Any,
        offvalue: Any,
        variable: Any,
        row: int,
        column: int,
        sticky: str
) -> ttk.Checkbutton:
    checkbox = ttk.Checkbutton(root, text=text, onvalue=onvalue, offvalue=offvalue, variable=variable)
    checkbox.grid(row=row, column=column, sticky=sticky, **PADDING_USUAL)
    return checkbox
