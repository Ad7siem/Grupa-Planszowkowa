from tkinter import *
from tkinter import ttk
from sheet import OpenSheet

# Create function to update Board Game
def edit_board_game():
    global w_EBG
    global id_board_games
    w_EBG = Tk()
    w_EBG.title('Aktualizacja')
    w_EBG.geometry('340x350')
    w_EBG.iconbitmap('Logo klub.ico')
    w_EBG.config(bg='#3e3e3e')

    IBG_Frame = LabelFrame(w_EBG, bg='#3e3e3e')
    IBG_Frame.pack(side=TOP, padx=10, pady=(20,5))

    EB_Frame = Frame(w_EBG, bg='#3e3e3e')
    EB_Frame.pack(side=TOP, padx=10, pady=5)

    BGE_Frame = LabelFrame(w_EBG, bg='#3e3e3e')
    BGE_Frame.pack(side=TOP, padx=10, pady=5, ipady=5)

    SB_Frame = Frame(w_EBG, bg='#3e3e3e')
    SB_Frame.pack(side=TOP, padx=10, pady=5)


    # Create Text Box
    id_board_games = Entry(IBG_Frame, width=20, bg='#696969', fg='#d3d3d3')
    id_board_games.pack(side=RIGHT, padx=10, pady=10)

    # Create Text Box Labels
    id_board_games_label = Label(IBG_Frame, text='Id:', bg='#3e3e3e', fg='#d3d3d3')
    id_board_games_label.pack(side=LEFT, padx=10, pady=10)

    # Create Edit Button
    edit_btn = Button(EB_Frame, text='Wybierz', width=20, bg='#696969', fg='#d3d3d3', activebackground='#4a4a4a', activeforeground='white', command=edit)
    edit_btn.pack(padx=10, pady=10)
    save_btn = Button(SB_Frame, text='Zapisz zmiany', bg='#696969', fg='#d3d3d3', activebackground='#4a4a4a', activeforeground='white', width=20, command=update_button)
    save_btn.pack(padx=10, pady=10)

    # Create Global Variables for next box names
    global name_board_games_edit
    global type_board_games_edit
    global min_player_edit
    global max_player_edit
    global time_games_edit
    global owner_edit

    # Create Text Boxes
    name_board_games = Entry(BGE_Frame, width=30, bg='#696969', fg='#d3d3d3')
    name_board_games.grid(row=0, column=1, padx=10, pady=(10,0))
    type_board_games = Entry(BGE_Frame, width=30, bg='#696969', fg='#d3d3d3')
    type_board_games.grid(row=1, column=1)
    min_player = Entry(BGE_Frame, width=30, bg='#696969', fg='#d3d3d3')
    min_player.grid(row=2, column=1)
    max_player = Entry(BGE_Frame, width=30, bg='#696969', fg='#d3d3d3')
    max_player.grid(row=3, column=1)
    time_games = Entry(BGE_Frame, width=30, bg='#696969', fg='#d3d3d3')
    time_games.grid(row=4, column=1)
    owner = Entry(BGE_Frame, width=30, bg='#696969', fg='#d3d3d3')
    owner.grid(row=5, column=1)


    # Create Text Box Labels
    name_board_games_label = Label(BGE_Frame, text='Nazwa Gry:', padx=(10), bg='#3e3e3e', fg='#d3d3d3')
    name_board_games_label.grid(row=0, column=0, pady=(5,0))
    type_board_games_label = Label(BGE_Frame, text='Typ:', bg='#3e3e3e', fg='#d3d3d3')
    type_board_games_label.grid(row=1, column=0)
    min_player_label = Label(BGE_Frame, text='Min. graczy', bg='#3e3e3e', fg='#d3d3d3')
    min_player_label.grid(row=2, column=0)
    max_player_label = Label(BGE_Frame, text='Max. graczy', bg='#3e3e3e', fg='#d3d3d3')
    max_player_label.grid(row=3, column=0)
    time_games_label = Label(BGE_Frame, text='Czas gry', bg='#3e3e3e', fg='#d3d3d3')
    time_games_label.grid(row=4, column=0)
    owner_label = Label(BGE_Frame, text='Właściciel:', bg='#3e3e3e', fg='#d3d3d3')
    owner_label.grid(row=5, column=0)
    

# Create function in Button Edit Board Games
def edit():
    worksheet = OpenSheet()

    records = []
    records = worksheet.row_values(int(id_board_games.get()) + 1)
    name_board_games_edit.insert(0, records[1])
    type_board_games_edit.insert(0, records[2])
    min_player_edit.insert(0, records[3])
    max_player_edit.insert(0, records[4])
    time_games_edit.insert(0, records[5])
    owner_edit.insert(0, records[6])
 

 # Create function to Save Update Board Games
def update_button():
    worksheet = OpenSheet()
    worksheet.update(f'A{int(id_board_games.get())+1}:K{int(id_board_games.get())+1}', [[int(id_board_games.get()), name_board_games_edit.get(), type_board_games_edit.get(), int(min_player_edit.get()), int(max_player_edit.get()), int(time_games_edit.get()), owner_edit.get()]])

    # Close window
    w_EBG.destroy()