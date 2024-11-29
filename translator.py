import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator


class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Translator")
        self.root.geometry("1080x400")
        self.root.configure(bg="white")

        self.create_widgets()

    def translate_text(self):
        source_text = self.input_text.get("1.0", tk.END).strip()
        source_lang = self.source_lang_combo.get()
        target_lang = self.target_lang_combo.get()

        if source_text and source_lang and target_lang:
            try:
                translation = GoogleTranslator(
                    source=source_lang.lower(),
                    target=target_lang.lower()
                ).translate(source_text)
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, translation)
            except Exception as e:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, f"Error: {str(e)}")

    def swap_languages(self):
        # Swap source and target languages
        source_lang = self.source_lang_combo.get()
        target_lang = self.target_lang_combo.get()
        self.source_lang_combo.set(target_lang)
        self.target_lang_combo.set(source_lang)

        # Swap input and output text
        source_text = self.input_text.get("1.0", tk.END).strip()
        target_text = self.output_text.get("1.0", tk.END).strip()
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, target_text)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, source_text)

    def create_widgets(self):

        title_label = tk.Label(
            self.root,
            text="Google Translate",
            font=("Helvetica", 18, "bold"),
        )
        title_label.pack(pady=10)
        # Language Selection Frame
        lang_frame = tk.Frame(self.root, bg="white")
        lang_frame.pack(pady=10)

        # Source Language Dropdown
        self.source_lang_combo = ttk.Combobox(
            lang_frame, values=GoogleTranslator().get_supported_languages(),height=10, width=20, font=("SST", 10)
        )
        self.source_lang_combo.grid(row=0, column=0, padx=10)
        self.source_lang_combo.set("english")  # Default source language

        # Target Language Dropdown
        self.target_lang_combo = ttk.Combobox(
            lang_frame, values=GoogleTranslator().get_supported_languages(),height=10, width=20, font=("SST", 10)
        )
        self.target_lang_combo.grid(row=0, column=2, padx=10)
        self.target_lang_combo.set("french")  # Default target language

        # Arrow Button for Language Swap
        swap_button = tk.Button(
            lang_frame,
            text="⇄",
            font=("SST", 16),
            bg="white",
            fg="blue",
            relief="flat",
            command=self.swap_languages,
        )
        swap_button.grid(row=0, column=1, padx=10)

        # Main Translation Frame
        translate_frame = tk.Frame(self.root, bg="white")
        translate_frame.pack(pady=20)

        # Input Section
        tk.Label(translate_frame, text="ENGLISH", font=("Anek", 12, "bold"), bg="white").grid(
            row=0, column=0, padx=7, pady=5
        )
        self.input_text = tk.Text(translate_frame, height=6, width=40, font=("Anek", 12), bd=2, relief="solid")
        self.input_text.grid(row=1, column=0, padx=10, pady=10)

        # Output Section
        tk.Label(translate_frame, text="SELECT  LANGUAGE", font=("Anek", 12, "bold"), bg="white").grid(
            row=0, column=2, padx=7, pady=5
        )
        self.output_text = tk.Text(translate_frame, height=6, width=40, font=("Anek", 12), bd=2, relief="solid")
        self.output_text.grid(row=1, column=2, padx=10, pady=10)

        # Translate Button
        translate_button = tk.Button(
            translate_frame,
            text="Translate",
            font=("Helvetica", 12, "bold"),
            bg="red",
            fg="white",
            command=self.translate_text,
        )
        translate_button.grid(row=1, column=1, padx=10, pady=10)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
