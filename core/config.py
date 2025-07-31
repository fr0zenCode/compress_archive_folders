import os
from typing import Final

BASE_DIR: Final[str] = os.path.dirname(os.path.dirname(__file__))

MAIN_WINDOW_SIZE: Final[str] = "600x400"
APP_NAME: Final[str] = "Slava's Archive Machine"

MAIN_FONT: Final[tuple] = ("Arial", 9)
BIGGER_FONT: Final[tuple] = ("Arial", 11)

# окно-подсказка, которое появляется при наведении на текстовые лейблы
TOOLTIP_X_PADDING: Final[int] = 50
TOOLTIP_Y_PADDING: Final[int] = -20

# поля ввода, где будут отображаться пути до выбранных папок/файлов
ENTRIES_WIDTH_PERCENTS: Final[int] = 80

# маленькая кнопка со значком файла, для перехода в файловую систему Windows для выбора нужного файла/папки
SMALL_BUTTON_WIDTH: Final[int] = 5
SMALL_BUTTON_PICTURE_SIZE: Final[tuple] = (20, 20)

# кнопки "Архивировать" и "Разархивировать"
ACTION_BUTTON_WIDTH: Final[int] = 30

# отступы элемента, к которому применяется, от окружающих элементов
PADDING_USUAL: Final[dict] = {"padx": 10, "pady": 5}
PADDING_FIRST_ELEMENT: Final[dict] = {"padx": 10, "pady": (30, 5)}
PADDING_LAST_ELEMENT: Final[dict] = {'padx': 10, 'pady': (5, 50)}

# ЦВЕТА
WHITE: Final[str] = "white"
