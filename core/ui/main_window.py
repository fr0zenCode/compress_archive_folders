import ctypes
import os
import tkinter as tk
from tkinter import filedialog

import PIL.Image
from PIL import ImageTk

from .tooltip import Tooltip
from .ui_widgets import (
    setup_main_action_button_widget,
    setup_main_label,
    setup_browse_file_button,
    setup_file_path_entry,
    setup_yes_or_no_type_checkbox
)
from ..archiver import zip_files, unzip_file
from ..config import MAIN_WINDOW_SIZE, APP_NAME
from ..picture_utils import small_file_system_icon, main_app_small_icon


class ArchiveApp:

    def __init__(self, root):

        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry(MAIN_WINDOW_SIZE)
        self.root.resizable(False, False)

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Slava's Archive Machine Random String")

        photo = PIL.ImageTk.PhotoImage(main_app_small_icon)
        root.iconphoto(False, photo)

        self.setup_ui()



    def setup_ui(self):


        #---------------------------- СОЗДАНИЕ ОБЪЕКТА ИЗОБРАЖЕНИЯ ----------------------------#
        self.small_file_system_icon_image = ImageTk.PhotoImage(small_file_system_icon)


        #---------------------------- СЕКЦИЯ АРХИВАЦИИ ----------------------------#
        self.archivate_lbl = setup_main_label(
            root=self.root,
            text="Выберите директорию для архивирования*:",
            row=0,
            column=0,
            sticky="w"
        )
        Tooltip(
            self.archivate_lbl,
            "Все папки, находящиеся в выбранной папке, не имеющие расширение .zip, будут заархивированы."
        )

        self.archive_dir_entry = setup_file_path_entry(root=self.root, row=1, column=0, sticky="w")

        self.delete_origin_file_after_zip_var = tk.BooleanVar()
        self.delete_origin_file_after_zip_checkbox = setup_yes_or_no_type_checkbox(
            root=self.root,
            text="Удалить исходный файл после архивации",
            onvalue=True,
            offvalue=False,
            variable=self.delete_origin_file_after_zip_var,
            row=2,
            column=0,
            sticky="w"
        )
        self.browse_dir_for_archive_button = setup_browse_file_button(
            root=self.root,
            command=self.browse_directory,
            row=1,
            column=1,
            sticky="w",
            image=self.small_file_system_icon_image
        )

        self.archive_button = setup_main_action_button_widget(
            root=self.root,
            text="Архивировать",
            command=lambda: self.archive_selected_folder(bool(self.delete_origin_file_after_zip_var)),
            row=3,
            column=0,
            sticky="w"
        )


        #---------------------------- СЕКЦИЯ ДЕ-АРХИВАЦИИ ----------------------------#
        self.unarchive_label = setup_main_label(
            root=self.root,
            text="Выберите файл для де-архивации*:",
            row=4,
            column=0,
            sticky="w"
        )
        Tooltip(self.unarchive_label, "Выбранный файл будет разархивирован.")

        self.unzip_file_entry = setup_file_path_entry(root=self.root, row=5, column=0, sticky="w")
        self.browse_file_for_unarchive_button = setup_browse_file_button(
            root=self.root,
            command=self.browse_zip_file,
            row=5,
            column=1,
            sticky="w",
            image=self.small_file_system_icon_image
        )

        self.delete_origin_file_after_unzip_var = tk.BooleanVar()
        self.delete_origin_file_after_unzip_checkbox = setup_yes_or_no_type_checkbox(
            root=self.root,
            text="Удалить исходный файл после разархивации",
            onvalue=True,
            offvalue=False,
            variable=self.delete_origin_file_after_unzip_var,
            row=6,
            column=0,
            sticky="w"
        )

        self.unarchive_button = setup_main_action_button_widget(
            root=self.root,
            text="Разархивировать",
            command=lambda: self.unzip_selected_file(bool(self.delete_origin_file_after_unzip_var)),
            row=7,
            column=0,
            sticky="w"
        )


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
            unzip_file(
                zip_path,
                save_unzip_file_path=os.path.dirname(zip_path),
                delete_origin_zip_file=delete_origin_zip_file
            )
