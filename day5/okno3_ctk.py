import customtkinter as ctk
from tkinter import messagebox


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class KalkulatorPodatku(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Prosty program księgowy")
        self.geometry("520x420")
        self.resizable(False, False)

        self.wynik_var = ctk.StringVar(
            value="Wprowadź zarobki i kliknij „Oblicz”."
        )

        self.utworz_interfejs()
        self.bind("<Return>", lambda event: self.wykonaj_obliczenia())

    @staticmethod
    def oblicz_podatek(zarobki: float) -> float:
        if zarobki <= 10_000:
            return 0.0

        podatek = min(zarobki - 10_000, 30_000) * 0.20

        if zarobki > 40_000:
            podatek += min(zarobki - 40_000, 60_000) * 0.40

        if zarobki > 100_000:
            podatek += (zarobki - 100_000) * 0.90

        return podatek

    def utworz_interfejs(self) -> None:
        self.grid_columnconfigure(0, weight=1)

        kontener = ctk.CTkFrame(self, corner_radius=16)
        kontener.grid(row=0, column=0, padx=24, pady=24, sticky="nsew")
        kontener.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            kontener,
            text="Kalkulator podatku",
            font=ctk.CTkFont(size=24, weight="bold")
        ).grid(row=0, column=0, padx=24, pady=(24, 10))

        ctk.CTkLabel(
            kontener,
            text="Zarobki brutto:",
            font=ctk.CTkFont(size=14)
        ).grid(row=1, column=0, padx=24, pady=(10, 6), sticky="w")

        self.pole_zarobki = ctk.CTkEntry(
            kontener,
            width=300,
            height=40,
            justify="center",
            placeholder_text="np. 12500,50",
            font=ctk.CTkFont(size=15)
        )
        self.pole_zarobki.grid(row=2, column=0, padx=24, pady=(0, 16))
        self.pole_zarobki.focus()

        ramka_przyciskow = ctk.CTkFrame(kontener, fg_color="transparent")
        ramka_przyciskow.grid(row=3, column=0, pady=(0, 18))

        ctk.CTkButton(
            ramka_przyciskow,
            text="Oblicz",
            command=self.wykonaj_obliczenia,
            width=130,
            height=38
        ).pack(side="left", padx=6)

        ctk.CTkButton(
            ramka_przyciskow,
            text="Wyczyść",
            command=self.wyczysc,
            width=130,
            height=38,
            fg_color="gray40",
            hover_color="gray30"
        ).pack(side="left", padx=6)

        self.wynik_label = ctk.CTkLabel(
            kontener,
            textvariable=self.wynik_var,
            justify="left",
            anchor="w",
            corner_radius=12,
            fg_color=("gray86", "gray20"),
            font=ctk.CTkFont(size=15),
            width=420,
            height=120
        )
        self.wynik_label.grid(
            row=4,
            column=0,
            padx=24,
            pady=(0, 24),
            sticky="ew"
        )

    def wykonaj_obliczenia(self) -> None:
        try:
            zarobki = float(self.pole_zarobki.get().replace(",", "."))

            if zarobki < 0:
                raise ValueError

            podatek = self.oblicz_podatek(zarobki)
            kwota_netto = zarobki - podatek

            self.wynik_var.set(
                f"Zarobki brutto: {zarobki:,.2f} zł\n"
                f"Podatek: {podatek:,.2f} zł\n"
                f"Kwota po podatku: {kwota_netto:,.2f} zł"
            )
        except ValueError:
            messagebox.showerror(
                "Błąd",
                "Wprowadź poprawną, nieujemną kwotę zarobków."
            )

    def wyczysc(self) -> None:
        self.pole_zarobki.delete(0, "end")
        self.wynik_var.set("Wprowadź zarobki i kliknij „Oblicz”.")
        self.pole_zarobki.focus()


if __name__ == "__main__":
    aplikacja = KalkulatorPodatku()
    aplikacja.mainloop()
