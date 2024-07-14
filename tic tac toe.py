import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x400")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font='Arial 20 bold', height=3, width=6,
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.check_winner() is False:
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col]["bg"] = "red"  # Set button color to red
            if self.check_winner():
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def show_winner(self):
        winner = f"Player {self.current_player} wins!"
        messagebox.showinfo("Tic-Tac-Toe", winner)
        self.reset_board()

    def show_draw(self):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
                button["bg"] = "SystemButtonFace"  # Reset button color to default
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
