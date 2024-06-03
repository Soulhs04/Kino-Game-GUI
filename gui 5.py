import tkinter as tk
import random

class KinoGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Kino Game")

        # Ο πίνακας με τους αριθμούς
        self.numbers_frame = tk.Frame(self.master)
        self.numbers_frame.pack()

        self.numbers = [str(i) for i in range(1, 81)]
        self.buttons = []
        for i in range(10):
            row = []
            for j in range(8):
                index = i * 8 + j
                if index < 80:
                    btn = tk.Button(self.numbers_frame, text=self.numbers[index], width=4, height=2, state=tk.DISABLED)
                    btn.grid(row=i, column=j, padx=2, pady=2)
                    row.append(btn)
            self.buttons.append(row)

        # Παράθυρο για εισαγωγή τυχερών αριθμών
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=10)

        self.entry_label = tk.Label(self.input_frame, text="Εισάγετε τυχαίους αριθμούς (1-80): ")
        self.entry_label.pack(side=tk.LEFT)

        self.num_entry = tk.Entry(self.input_frame, width=20)
        self.num_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.input_frame, text="Προσθήκη", command=self.add_numbers)
        self.add_button.pack(side=tk.LEFT)

        # Κουμπί για έναρξη / έξοδο παιχνιδιού
        self.start_button = tk.Button(self.master, text="Έναρξη Παιχνιδιού", command=self.start_game)
        self.start_button.pack(pady=10)

    def add_numbers(self):
        numbers = self.num_entry.get().split()
        for num in numbers:
            if num.isdigit() and 1 <= int(num) <= 80:
                index = int(num) - 1
                row = index // 8
                col = index % 8
                self.buttons[row][col].config(bg='green')
            else:
                print(f"Μη έγκυρος αριθμός: {num}")

    #### Προβολη αποτελεσματων
    def start_game(self):
        lucky_numbers = random.sample(range(1, 81), 20)  
        for num in lucky_numbers:
            index = num - 1
            row = index // 8
            col = index % 8
            self.buttons[row][col].config(bg='green')


def main():
    root = tk.Tk()
    kino_game = KinoGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
