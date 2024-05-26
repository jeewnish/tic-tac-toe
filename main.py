import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('normal', 40), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.restart_button = tk.Button(self.root, text='Restart', command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3)

    def on_button_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')

    def restart_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal')


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
