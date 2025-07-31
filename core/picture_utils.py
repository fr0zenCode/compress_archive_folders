import os

from PIL import Image

from core.config import BASE_DIR, SMALL_BUTTON_PICTURE_SIZE

small_file_system_icon = Image.open(os.path.join(BASE_DIR, "media", "images", "file_directory_icon.png"))
small_file_system_icon = small_file_system_icon.resize(SMALL_BUTTON_PICTURE_SIZE)

main_app_small_icon = Image.open(os.path.join(BASE_DIR, "media", "images", "small_app_icon.png"))
