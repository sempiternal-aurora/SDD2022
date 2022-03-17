import tkinter as tk

grid = []
current_player = 0 #noughts = 0, crosses = 1

def initialise_grid(x_size, y_size):
    #creates a 2D grid as a list of lists bounded by specified x and y values
    global grid
    for i in range(y_size):
        x_grid = []
        for j in range(x_size):
            x_grid.append(" ")
        grid.append(x_grid)

def user_input_validation(x_coordinate,y_coordinate):
    #Validates whether the user input is within 0-2
    if x_coordinate > 2 or y_coordinate > 2:
        return False
    else:
        return True

def user_inputs(grid):
    user_input = input("Where do you want to go (x,y)")
    x_coordinate = int(user_input[0])
    y_coordinate = int(user_input[2])
    isvalid = user_input_validation(x_coordinate,y_coordinate)
    while isvalid is False:
        print("That is not a valid input")
        user_input = input("Where do you want to go (x,y)")
        x_coordinate = int(user_input[0])
        y_coordinate = int(user_input[2])
        isvalid = user_input_validation(x_coordinate,y_coordinate)
        """
        if user_input == "x" or user_input == "o":
            print("Pick an empty spot")
        else:
            grid[user_input] = "x"
        """
    return y_coordinate, x_coordinate

def display_grid(playing_grid):
    for i in playing_grid:
        print(i)

def check_win_condition(grid):
    #checks horizontals, than verticals, than diagonals for win conditions
    is_win = 0
    continuity = True
    for i in grid:
        if i[0] != 0:
            continuity == True
            for j in i:
                if j != i[0]:
                    continuity == False
            if continuity == True:
                is_win = i[0]
    for i in range(0, 3):
        if grid[0][i] != 0:
            continuity == True
            for j in range(0,3):
                if grid[j][i] != grid[0][i]:
                    continuity == False
            if continuity == True:
                is_win == grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
        is_win == grid[1][1]
    return is_win

def alternate_turn():
    global current_player
    current_player += 1
    current_player = current_player % 2

def play_tictactoe():
    current_player = 0
    grid = initialise_grid(3, 3)
    is_won = False
    while is_won == False:
        display_grid(grid)
        if current_player == 0:
            print("\nNoughts player")
        else:
            print("\nCrosses player")
        row_index, column_index = user_inputs(grid)
        grid[row_index][column_index] = current_player + 1
        win_state = check_win_condition(grid)
        if win_state > 0:
            is_won = True
        current_player = alternate_turn(current_player)
    if win_state == 1:
        print("Noughts WIN!\n")
    elif win_state == 2:
        print("Crosses WIN!\n")

class App_Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tic Tac Toe")
        self.geometry("405x720")
        main_window_frame = tk.Frame(self)
        main_window_frame.pack()

        self.frames = {}
        for f in (Main_Page, Game_Page):
            frame = f(main_window_frame, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nesw")

        self.show_frame(Main_Page)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class Main_Page(tk.Frame):
    def __init__(self, parent, container):
        #initialises the main page, which opens first, allowing the user to start playing a game
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Main Menu")
        play_game_button = tk.Button(self, text="Start Game", command = lambda: container.show_frame(Game_Page))
        label.grid(row=0, column=0)
        play_game_button.grid(row=1, column=0)

class Game_Page(tk.Frame):
    def __init__(self, parent, container):
        #initialises the game page, with the Tic tac toe grid.
        tk.Frame.__init__(self, parent)
        exit_button = tk.Button(self, text="Exit Game", command= lambda: container.show_frame(Main_Page))
        exit_button.grid(row=0, column=0, columnspan=3)

        #creates a grid of buttons
        self.grid_buttons = []
        self.grid_button_text = []
        for row in range(0, 3):
            self.grid_buttons.append([])
            self.grid_button_text.append([])
            for column in range(0, 3):
                button_text = tk.StringVar()
                button_text.set(" ")
                button = tk.Button(self, textvariable=button_text, command = lambda r=row, c=column, text=button_text: self.button_pressed(text, r, c))
                self.grid_button_text.append(button_text)
                self.grid_buttons[row].append(button)
                self.grid_buttons[row][column].grid(row=(row+1), column=column)

        self.current_turn_label = tk.StringVar()
        self.current_turn_label.set("Noughts' Turn")
        turn_label = tk.Label(self, textvariable=self.current_turn_label)
        turn_label.grid(row=4, column=0, columnspan=3)

    def button_pressed(self, button_text, row, column):
        #runs the checks for whether a win condition is met, or if the input is valid
        self.update_button(button_text, row, column)
        is_win = check_win_condition(grid)
        self.alternate_turn()
    
    def update_button(self, text, row, column):
        global grid
        if grid[row][column] == " ":
            if current_player == 1:
                grid[row][column] = "X"
            else:
                grid[row][column] = "O"           
        text.set(grid[row][column])

    def alternate_turn(self):
        global current_player
        alternate_turn()
        if current_player == 1:
            self.current_turn_label.set("Crosses' Turn")
        else:
            self.current_turn_label.set("Noughts' Turn")


def main():
    initialise_grid(3,3)
    my_app = App_Window()
    my_app.mainloop()
    """
    play_tictactoe()
    while True:
        play_game = input("do you want to play another game? (y/n) ")
        if play_game == "y":
            play_tictactoe()
        else:
            break
    """

if __name__ == "__main__":
    main()