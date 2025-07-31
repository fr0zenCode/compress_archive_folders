import tkinter as tk

from core.ui.main_window import ArchiveApp


def main():
    root = tk.Tk()
    app = ArchiveApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
