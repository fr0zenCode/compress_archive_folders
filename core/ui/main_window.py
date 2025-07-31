import os
import tkinter as tk
from tkinter import filedialog, ttk

from PIL import ImageTk

from .tooltip import Tooltip
from ..archiver import zip_files, unzip_file
from ..config import (
    ENTRIES_WIDTH_PERCENTS,
    SMALL_BUTTON_WIDTH,
    ACTION_BUTTON_WIDTH,
    PADDING_USUAL,
    PADDING_FIRST_ELEMENT,
    PADDING_LAST_ELEMENT,
    MAIN_WINDOW_SIZE,
    APP_NAME
)
from ..picture_utils import small_file_system_icon


class ArchiveApp:

    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry(MAIN_WINDOW_SIZE)
        self.root.resizable(False, False)
        self.setup_ui()



    def setup_ui(self):
        padding_usual = PADDING_USUAL
        padding_first_element = PADDING_FIRST_ELEMENT
        padding_last_element = PADDING_LAST_ELEMENT


        #---------------------------- СЕКЦИЯ КАРТИНОК ----------------------------#
        self.small_file_system_icon_image = ImageTk.PhotoImage(small_file_system_icon)


        #---------------------------- СЕКЦИЯ АРХИВАЦИИ ----------------------------#
        self.archivate_lbl = ttk.Label(self.root, text="Выберите директорию для архивирования*:")
        self.archivate_lbl.grid(row=0, column=0, sticky="w", **padding_first_element)
        Tooltip(
            self.archivate_lbl,
            "Все папки, находящиеся в выбраннной папке, не имеющие расширение .zip будут заархивированы."
        )

        self.archive_dir_entry = ttk.Entry(self.root, width=ENTRIES_WIDTH_PERCENTS)
        self.archive_dir_entry.grid(row=1, column=0, sticky="w", **padding_usual)

        self.delete_origin_file_after_zip = tk.BooleanVar()
        self.c1 = ttk.Checkbutton(self.root, text="Удалить исходный файл после архивации", onvalue=True, offvalue=False, variable=self.delete_origin_file_after_zip)
        self.c1.grid(row=2, column=0, sticky="w", **padding_usual)

        self.browse_dir_button = ttk.Button(
            self.root,
            width=SMALL_BUTTON_WIDTH,
            image=self.small_file_system_icon_image,
            command=self.browse_directory
        )
        self.browse_dir_button.grid(row=1, column=1, sticky="w")

        archive_button = ttk.Button(
            self.root,
            text="Архивировать",
            width=ACTION_BUTTON_WIDTH,
            command=(lambda: self.archive_selected_folder(self.delete_origin_file_after_zip))
        )
        archive_button.grid(row=3, column=0, sticky="w", **padding_last_element)


        #---------------------------- СЕКЦИЯ ДЕ-АРХИВАЦИИ ----------------------------#
        tk.Label(self.root, text="Выберите файл для де-архивации*:").grid(
            row=4,
            column=0,
            sticky="w",
            **padding_usual
        )

        self.unzip_file_entry = ttk.Entry(self.root, width=ENTRIES_WIDTH_PERCENTS)
        self.unzip_file_entry.grid(row=5, column=0, sticky="w", **padding_usual)

        self.browse_file_button = ttk.Button(
            self.root,
            width=SMALL_BUTTON_WIDTH,
            image=self.small_file_system_icon_image,
            command=self.browse_zip_file
        )
        self.browse_file_button.grid(row=5, column=1, sticky="w")

        self.delete_origin_file_after_unzip = tk.BooleanVar()
        self.c1 = ttk.Checkbutton(self.root, text="Удалить исходный файл после де-архивации", onvalue=True, offvalue=False,
                                  variable=self.delete_origin_file_after_unzip)
        self.c1.grid(row=6, column=0, sticky="w", **padding_usual)


        unzip_button = ttk.Button(
            self.root,
            text="Разархивировать",
            width=ACTION_BUTTON_WIDTH,
            command=(lambda: self.unzip_selected_file(self.delete_origin_file_after_unzip))
        )
        unzip_button.grid(row=7, column=0, sticky="w", **padding_usual)


    def browse_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.archive_dir_entry.delete(0, tk.END)
            self.archive_dir_entry.insert(0, folder)

    def browse_zip_file(self):
        file = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
        if file:
            self.unzip_file_entry.delete(0, tk.END)
            self.unzip_file_entry.insert(0, file)

    def archive_selected_folder(self, delete_origin_non_zip_file: bool):
        path = self.archive_dir_entry.get()
        if path:
            zip_files(path, delete_origin_non_zip_file=delete_origin_non_zip_file)

    def unzip_selected_file(self, delete_origin_zip_file: bool):
        zip_path = self.unzip_file_entry.get()
        if zip_path:
            unzip_file(zip_path, save_unzip_file_path=os.path.dirname(zip_path), delete_origin_zip_file=delete_origin_zip_file)
