import tkinter as tk
from tkinter import ttk
from poker import calculate_equity
import random

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Tools")
        self.root.geometry("400x300")

        # create a notebook widget from tkinter
        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill='both')

        # create frames for each tab
        tab1 = tk.Frame(notebook, bg="lightblue")
        tab2 = tk.Frame(notebook, bg="lightgreen")

        # add tabs to the notebook
        notebook.add(tab1, text="Random")
        notebook.add(tab2, text="Equity")

        # add rng widgets to the first tab
        self.rng = tk.Label(tab1, font=("arial",70,"bold"), fg="#ee666d")
        self.rng.place(relx=0.4,y=40)
        # it binds the mouse click to action
        self.root.bind("<Button-1>", self.on_button_click)

        # add an Entry widget for player 1's hand to the second tab
        self.holding1 = tk.Entry(tab2, justify="left", width=20, font=("poppins", 14, "bold"), bg="white", border=0, fg="black")
        self.holding1.place(x=50, y=60)
        self.holding1.insert(0, "Player 1's hand")

        # add an Entry widget for player 2's hand to the second tab
        self.holding2 = tk.Entry(tab2, justify="left", width=20, font=("poppins", 14, "bold"), bg="white", border=0, fg="black")
        self.holding2.place(x=50, y=120)
        self.holding2.insert(0, "Player 2's hand")

        # add an Entry widget for the board to the second tab
        self.board = tk.Entry(tab2, justify="left", width=20, font=("poppins", 14, "bold"), bg="white", border=0, fg="black")
        self.board.place(x=50, y=180)
        self.board.insert(0, "Run Out: None")

        # placeholder for results
        self.player1_result =tk.Label(tab2,text="Equity" ,font=("arial",14,"bold"), fg="#FFFFFF")
        self.player1_result.place(x=280, y=60)
        self.player2_result =tk.Label(tab2,text="Equity" ,font=("arial",14,"bold"), fg="#FFFFFF")
        self.player2_result.place(x=280, y=120)

        # add a button to print the input values
        button = tk.Button(tab2, text="Calculate", borderwidth=1, cursor="hand2", bg="#FFFFFF", command=self.button_click)
        button.place(x=150, y=220, width=100, height=30)

        # starting clock for auto update
        self.schedule_periodic_call()

    def button_click(self):
        holding1_input = self.holding1.get()
        holding2_input = self.holding2.get()
        board_input = self.board.get()        
        
        player1_hand = [holding1_input[i:i+2] for i in range(0, len(holding1_input), 2)]        
        player2_hand = [holding2_input[i:i+2] for i in range(0, len(holding2_input), 2)] 
        board = [board_input[i:i+2] for i in range(0, len(board_input), 2)]

        # setting to empty for preflop calcs
        if board_input == "Run Out: None":
            board = []

        # for testing
        #print(f"Holding 1: {player1_hand}")
        #print(f"Holding 2: {player2_hand}")
        #print(f"Board: {board}")
        
        # fill the data into their placeholders, and format them
        player1_equity, player2_equity = calculate_equity(player1_hand, player2_hand, board)
        self.player1_result.config(text=f"{player1_equity * 100:.2f}%")
        self.player2_result.config(text=f"{player2_equity * 100:.2f}%")
        if player1_equity > player2_equity:
            self.player1_result.config(fg="green")
            self.player2_result.config(fg="red")
        else:
            self.player1_result.config(fg="red")
            self.player2_result.config(fg="green")

    def on_button_click(self, event=None):
        random_Nr = random.randint(0,100)
        self.rng.config(text=random_Nr)

    def schedule_periodic_call(self):
        self.on_button_click() 
        self.root.after(10000, self.schedule_periodic_call)

# create the main window
root = tk.Tk()
app = App(root)

# run the application
root.mainloop()
