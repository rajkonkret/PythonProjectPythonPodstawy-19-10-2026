import tkinter as tk
from tkinter import filedialog


def wybierz_plik():
    plik = filedialog.askopenfilename(title="Wybierz plik")

    if plik:
        print("Wybrano plik:", plik)
        # Wybrano plik: //10.247.54.135/Users/CSComarch/Downloads/DYSK Sieciowy/streamlit_23-09-2026/daty-01.xlsx


root = tk.Tk()
root.withdraw()  # zamyka głowne okno

wybierz_plik()
