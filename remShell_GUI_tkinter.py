import tkinter as tk
import customtkinter
from tkinter import scrolledtext
import json
import remShell_paramiko as prmiko
from tkinter import filedialog
import subprocess
import copy

class Main:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.rowconfigure(1,weight=1)
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1)
    
    # Root Window
    def root_window(self,name,geometry):
        self.name = name
        self.geometry = geometry
        self.root.title(self.name)
        self.root.geometry(self.geometry)
        # Root Window configure
        self.root.configure(background=Color.root_window_bg)
        # Root Window loop
        self.root.minsize(600,500)
        self.root.mainloop()

# Color Setting
class Color:
    root_window_bg = "#262b35",
    root_bg="#2e3440",
    root_fg="#e5e9f0",
    bg="#3b4252",
    fg="#eceff4",
    accent1="#8fbcbb",
    accent2="#81a1c1"

# Button
class Button():
    def __init__(self,frame,text,row,column,command,width=50,height=30,columnspan=1,rowspan=1, sticky="w"):
        self.button1 = customtkinter.CTkButton(
            frame.frame,
            text=text, 
            bg_color=Color.bg, 
            fg_color=Color.accent2,
            width=width,
            command=command,
            text_color=Color.root_bg,
            hover_color=Color.accent1,
            height=height
        )
        self.button1.grid(column=column,row=row,padx=10,pady=10,columnspan=columnspan,rowspan=rowspan,sticky=sticky)

# Scrolled Text Box
class TextBox():
    def __init__(self, frame, column=0, row=0, rowspan=1, columnspan=1, sticky="nesw", width=40):
        self.text_box = scrolledtext.ScrolledText(
            frame.frame,
            fg=Color.fg,
            bg=Color.bg, 
            width=width,
            height="5", 
            highlightbackground=Color.bg,
            highlightcolor=Color.accent1,
            highlightthickness=2,
            bd=0,
            font=("Noto Bold",11)
        )

        self.text_box.grid(
            padx=6, 
            pady=6, 
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky
        )

# Label
class Label():
    def __init__(self, frame, text, column, row, font_size):
        self.Label = tk.Label(
            frame.frame,
            text=text,
            bg=Color.root_bg,
            anchor="w", 
            fg=Color.fg, 
            padx=10, 
            font=("Noto Regular",font_size),
            pady=10,
        )
        self.Label.grid(column=column, row=row, sticky="w")

# Frame label
class Frame_label():
    def __init__(self, frame, row, column, columnspan=1, rowspan=1):
        self.frame = tk.Frame(frame.frame, bg=Color.root_bg, height=1, width=1)
        self.frame.grid(row=row, column=column,sticky="w", padx=2, pady=2,columnspan=columnspan,rowspan=rowspan)

class Frame():
    def __init__(self,class_Main,row, column, sticky, columnspan, rowspan):
        self.row = row
        self.column = column 
        self.sticky = sticky
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.frame = customtkinter.CTkFrame(
            class_Main.root, 
            bg_color=Color.root_window_bg,
            fg_color=Color.root_bg,
            corner_radius=10,
            highlightthickness=0, 
            highlightbackground=Color.root_bg,
            highlightcolor=Color.root_bg
        )
    def gr(self):
        self.frame.grid(
            row=self.row, 
            columnspan=self.columnspan,
            rowspan=self.rowspan,
            column=self.column, 
            sticky=self.sticky, 
            padx=10, pady=7, 
        )

# List box
class Listbox():
    def __init__(self, frame, row, column, sticky, rowspan, columnspan):
        self.list_box=tk.Listbox(
            frame.frame,
            height=5,
            bg=Color.bg,
            fg=Color.fg,
            bd=0,
            highlightthickness=2,
            highlightbackground=Color.accent2,
            highlightcolor=Color.accent1,
            font=("Noto Regular", 12),
            width=20
        )
        self.list_box.grid(row=row,column=column,sticky=sticky, rowspan=rowspan, columnspan=columnspan, padx=10, pady=10)
    def insert(self,text):
        self.list_box.insert("end", text)

# Entry class
class Entry():
    def __init__(self,frame, text, row, column, columnspan, rowspan, show, width=150):
        self.entry = customtkinter.CTkEntry(
            frame.frame, 
            placeholder_text=text,
            fg_color=Color.bg,
            text_color=Color.fg,
            show=show,
            text_font = ("Noto Regular",10),
            height=25,
            width=width
        )
        self.entry.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=1, pady=1, sticky="w")

# Radio Button
class RadioButton():
    def __init__(self, frame, text, variable, value, row, column, command=None):
        self.radio_button = customtkinter.CTkRadioButton(
            master = frame,
            text=text,
            text_color=Color.fg,
            command=command,
            fg_color=Color.accent1,
            variable=variable,
            border_width_checked=3,
            border_width_unchecked=3,
            height=13,
            width=13,
            corner_radius=10,
            value=value
        )
        self.radio_button.grid(row=row, column=column, padx=0, pady=0, sticky="w")

class Button_custom(Button):
    def __init__(self,frame,text,row,column,command,width,height,columnspan,rowspan,sticky,fg_color):
        super().__init__(frame,text,row,column,command,width,height,columnspan,rowspan,sticky)
        self.button1.configure(fg_color=fg_color)

class Switch():
    def __init__(self,frame,text,variable,column,row,rowspan=0,columnspan=1,offvalue=None,onvalue=None,command=None,):
        self.switch = customtkinter.CTkSwitch(
            master=frame,
            text=text,
            command=command,
            variable=variable,
            onvalue=onvalue,
            offvalue=offvalue,
            fg_color=Color.bg,
            text_color=Color.fg,
        )
        self.switch.grid(column=column,row=row,rowspan=rowspan,columnspan=columnspan,padx=5,pady=5,sticky="w")

### Menu bar

# unhide entry key

def unhide():
    entry_key.entry.grid(column=3,columnspan=3,sticky="w",row=4,padx=15)
    entry_key.entry.config(width=240)
    button_keybrowse.button1.grid(column=2,sticky="", columnspan=2, row=4,padx=20)
    entry_type_key.entry.grid(column=5,columnspan=1,sticky="e",row=4,padx=2)
def hide():
    entry_key.entry.grid_forget()
    entry_type_key.entry.grid_forget()
    button_keybrowse.button1.grid_forget()

# create Menu bar

def Menubar():
    my_menu = tk.Menu(App.root, bg=Color.root_bg, fg=Color.root_fg, bd=0,activebackground=Color.accent1)
    App.root.config(menu=my_menu)
    file_menu = tk.Menu(my_menu,bg=Color.root_bg, fg=Color.root_fg, bd=0)
    edit_menu = tk.Menu(my_menu,bg=Color.root_bg, fg=Color.root_fg, bd=0)

    my_menu.add_cascade(label="File",menu=file_menu)
    my_menu.add_cascade(label="Edit",menu=edit_menu)

    # File menu
    open_config= file_menu.add_command(label="Open configuration", command=open_conf, activebackground=Color.accent1)
    save_as_config = file_menu.add_command(label="Save as ...", command=save_as, activebackground=Color.accent1)
    # Edit menu
    password_based = edit_menu.add_radiobutton(label="Password based authentication", activebackground=Color.accent1, var = based_auth, value="password based",command=hide)
    password_based = edit_menu.add_radiobutton(label="Key based authentication", activebackground=Color.accent1, selectcolor="", var = based_auth, value="key based",command=unhide)

    file_menu.add_separator()

    quit_command = file_menu.add_command(label="Exit", command=App.root.quit, activebackground=Color.accent1)

# Menubar command
# save as configuration
def save_as():
    filetypes = (
        ("text files",".txt"),
        ("All files",".")
    )
    path = filedialog.asksaveasfilename(
        title = "open a file",
        filetypes = filetypes
    )
    save_conf(path=path)

# save configuration
def save_conf(path):
    dict_config_copy = copy.deepcopy(dict_config)
    for i in dict_config:
        dict_config_copy[i].pop("password",None)
    save_string = json.dumps(dict_config_copy,indent=4,sort_keys=True) + "\n<<<slice>>>\n" + text_box_command.text_box.get("1.0","end")
    save_path = open(path,"w")
    save_path.write(save_string)
    save_path.close()

# open file configuration
def open_conf():
    filetypes = (
        ("text files",".txt"),
        ("All files",".")
    )
    path = filedialog.askopenfilename(
        title = "open a file",
        filetypes = filetypes
    )
    file_conf_raw = open(path)
    file_conf = file_conf_raw.read().split("\n<<<slice>>>\n")
    file_conf_dict = json.loads(file_conf[0])
    dict_config.update(file_conf_dict)
    text_box_command.text_box.insert("end",file_conf[1])
    for i in dict_config:
        list_box.insert(i)

###

## Function for Button Command
#
def delete_config():
    value_list_box = list_box.list_box.get("anchor")
    del dict_config[value_list_box]
    list_box.list_box.delete("anchor")

# Update or add the configuration
def update():
    # Get entry widget value
    value_name = entry_name.entry.get()
    value_hostname = entry_hostname.entry.get()
    value_username = entry_username.entry.get()
    value_password = entry_password.entry.get()
    # Update to the dictionary configuration
    dict_config[value_name] = { "name":value_name,
                                "hostname":value_hostname,
                                "username":value_username,
                                "password":value_password,}
    if based_auth.get() == "key based":
        dict_config[value_name].update({"key":entry_key.entry.get(),
                                        "key_type":entry_type_key.entry.get()})
    list_config = list_box.list_box.get(0,"end")
    if value_name in list_config:
        pass
    else:
        list_box.list_box.insert("end",value_name)

# Print selected configuration to entry widget
def show_entry():
    entry_name.entry.delete(0,"end")
    entry_hostname.entry.delete(0,"end")
    entry_username.entry.delete(0,"end")
    entry_password.entry.delete(0,"end")
    entry_key.entry.delete(0,"end")
    entry_value = entry_hostname.entry.get()
    key_list_box = list_box.list_box.get("anchor") 
    entry_name.entry.insert(0,dict_config[key_list_box]["name"])
    entry_hostname.entry.insert(0,dict_config[key_list_box]["hostname"])
    entry_username.entry.insert(0,dict_config[key_list_box]["username"])
    entry_password.entry.insert(0,dict_config[key_list_box]["password"])
    if based_auth.get() == "key based":
        entry_key.entry.insert(0,dict_config[key_list_box]["key"])
 
 # Show the configuration file with json
def show_config():
    config_window = customtkinter.CTk()
    config_window.configure(bg="gray20", )
    config_window.geometry("700x500")
    config_window.rowconfigure(0,weight=1)
    config_window.columnconfigure(0,weight=1)
    text_config = scrolledtext.ScrolledText(config_window, bg="white", fg="black")
    text_config.grid(sticky="nesw")
    dict_config_copy = copy.deepcopy(dict_config)
    for i in dict_config_copy:
        dict_config_copy[i].pop("password", None)
    text_config.insert(tk.INSERT,json.dumps(dict_config_copy, indent=3, sort_keys=True))
    config_window.mainloop()

# Execute command with paramiko
def execute_password_based(value):
    if(value == "execute all target"):
        input_command = text_box_command.text_box.get("1.0","end")
        for i in dict_config:
            hostname = dict_config[i]["hostname"]
            username = dict_config[i]["username"]
            password = dict_config[i]["password"]
            target = prmiko.SSHClient(host=hostname,user=username)
            target.connect_password_based(password=password)
            target.exec(sudo_boolean.get(), True, input_command)
            text_box_output.text_box.insert("end",
                            f"{'='*33}\n==  Name {i}\n{'='*25}\n\n")
            output = target.result[0].replace("\n","\n")
            for i in output:
                if i == "\n":
                    break
                output = output.replace(i,"")
            text_box_output.text_box.insert("end",f"{output}\n\n")
    elif(value == "execute selected target"):
        input_command = text_box_command.text_box.get("1.0","end")
        name = entry_name.entry.get()
        hostname = entry_hostname.entry.get()
        username = entry_username.entry.get()
        password = entry_password.entry.get()
        target = prmiko.SSHClient(host=hostname,user=username)
        target.connect_password_based(password=password)
        target.exec(sudo_boolean.get(), True, input_command)
        text_box_output.text_box.insert("end",
                        f"{'='*33}\n==  Name {name}\n{'='*25}\n\n")
        for i in output:
            if i == "\n":
                break
            output = output.replace(i,"")
        text_box_output.text_box.insert("end",f"{output}\n\n")

def execute_key_based(value):
    if(value == "execute all target"):
        for i in dict_config:
            name     = dict_config[i]["name"]
            hostname = dict_config[i]["hostname"]
            username = dict_config[i]["username"]
            password = dict_config[i]["password"]
            keyfile  = dict_config[i]["key"]
            keytype  = dict_config[i]["key_type"]
            command  = text_box_command.text_box.get("1.0","end")
            ssh_client = prmiko.SSHClient(hostname,username)
            ssh_client.connect_key_based(keyfile=keyfile,password=password,type=keytype)
            ssh_client.exec(sudo_boolean.get(),True,command)
            output = ssh_client.result[0]
            text_box_output.text_box.insert("end",
                            f"{'='*33}\n==  Name {name}\n{'='*25}\n\n")
            for i in output:
                if i == "\n":
                    break
                output = output.replace(i,"")
            text_box_output.text_box.insert("end",f"{output}\n\n")

    elif(value == "execute selected target"):
        name = entry_name.entry.get()
        hostname = dict_config[name]["hostname"]
        username = dict_config[name]["username"]
        password = dict_config[name]["password"]
        keyfile  = dict_config[name]["key"]
        keytype  = dict_config[name]["key_type"]
        command  = text_box_command.text_box.get("1.0","end")
        ssh_client = prmiko.SSHClient(hostname,username)
        ssh_client.connect_key_based(keyfile=keyfile,password=password,type=keytype)
        ssh_client.exec(sudo_boolean.get(),True,command)
        output = ssh_client.result[0]
        text_box_output.text_box.insert("end",
                        f"{'='*33}\n==  Name {name}\n{'='*25}\n\n")
        for i in output:
            if i == "\n":
                break
            output = output.replace(i,"")
        text_box_output.text_box.insert("end",f"{output}\n\n")

def browse_key_func():
    path = filedialog.askopenfilename(title = "open a file",)
    entry_key.entry.delete(0,"end")
    entry_key.entry.insert(0,path)

# Clear 
def clear_output():
    text_box_output.text_box.delete("1.0","end")

def clear_command():
    text_box_command.text_box.delete("1.0","end")

#
##

if __name__ == "__main__":

    # Dictionary configuration
    dict_config = {}

    # Main
    App = Main()

    # Main Frame
    frame_right = Frame(App,row=0,column=1,sticky="nesw",columnspan=1, rowspan=1)
    frame_input = Frame(App,row=0,column=0,sticky="nesw", columnspan=1, rowspan=1)
    frame_right.frame.columnconfigure(0,weight=1)

    frame_input.gr()
    frame_right.gr()

    frame_bottom = Frame(App,row=1,column=0,sticky="nsew", columnspan=2, rowspan=1)

    frame_bottom.frame.columnconfigure(4, weight=1)
    frame_bottom.frame.columnconfigure(7, weight=2)
    frame_bottom.frame.rowconfigure(2 ,weight=1)

    frame_bottom.gr()

    # Frame label top
    frame_label_left = Frame_label(frame=frame_right, row=0, column=0)
    frame_label_name = Frame_label(frame=frame_input, row=0, column=0)
    frame_label_hostname = Frame_label(frame=frame_input, row=1, column=0)
    frame_label_username = Frame_label(frame=frame_input, row=0, column=3)
    frame_label_password = Frame_label(frame=frame_input, row=1, column=3)

    # Frame label bottom
    frame_label_command = Frame_label(frame=frame_bottom, row=0, column=0, rowspan=2)
    frame_label_output = Frame_label(frame=frame_bottom, row=0, column=5, rowspan=2)

    # label in bottom frame
    label_command = Label(frame_label_command, text="Command", row=0, column=0, font_size=12)
    label_output = Label(frame_label_output, text="Output", row=0, column=0, font_size=12)

    # label in top frame
    label_name = Label(frame_label_name, text=" Name", row=0, column=0, font_size=11)
    label_hostname = Label(frame_label_hostname, text=" Hostname", row=0, column=0, font_size=11)
    label_username = Label(frame_label_username, text=" Username", row=0, column=0, font_size=11)
    label_password= Label(frame_label_password, text=" Password", row=0, column=0, font_size=11)

    # List box
    list_box = Listbox(frame_right, row=0, column=0, rowspan=3, columnspan=2, sticky="nesw")
    for i in dict_config:
        list_box.insert(dict_config[i]["name"])

    # scrolled text box
    text_box_command = TextBox(frame=frame_bottom, column=0, row=2, rowspan=1, columnspan=5, sticky="nesw", width=35)
    text_box_output = TextBox(frame=frame_bottom, column=5, row=2, rowspan=1, columnspan=3, sticky="nesw",width=35)

    # button frame rigth
    button_select = Button(frame=frame_right, text="Select", row=0, column=2, command=show_entry)
    button_delete = Button(frame=frame_right, text="Delete", row=1, column=2, command=delete_config)
    button_show = Button(frame=frame_right, text=" Show ", row=2, column=2, command=show_config)

    # button frame left
    button_update = Button(frame=frame_input, text="Update Configuration",row=4, column=0,width=150, height=30,
                        columnspan=3, command=update)
    # button for browse the key file
    button_keybrowse= Button(frame=frame_input, text="Browse", row=4, column=2, command=browse_key_func, width=60, sticky="", columnspan=2)
    button_keybrowse.button1.grid_forget()

   # button bottom frame
    selected = tk.StringVar()
    selected.set("execute all target")
    # function for selecting password based or key based, use by button_exec
    def execute_auth_based(value):
        if based_auth.get() == "password based":
            execute_password_based(value)
        elif based_auth.get() == "key based":
            execute_key_based(value)
    button_exec = Button_custom(frame=frame_bottom, text="Exec", row=0, column=2,
                        width=55,height=30,command=lambda: execute_auth_based(selected.get()),sticky='w', fg_color=Color.accent2,
                        columnspan=1,rowspan=2)
    button_clear_output = Button_custom(frame=frame_bottom, text="Clear", row=0, column=6,
                        width=30,height=30,command=clear_output,columnspan=1,rowspan=2,sticky="w",
                        fg_color="#d08770")

    button_clear_command = Button_custom(frame=frame_bottom, text="Clear", row=0, column=1,
                        width=30,height=30,command=clear_command,columnspan=1,rowspan=2,sticky="e",
                        fg_color="#d08770")

    # Radio button
    radio_alltarget = RadioButton(frame_bottom.frame,text="All Target",variable=selected,
                            value="execute all target", row=0, column=3)
    radio_selectedtarget = RadioButton(frame_bottom.frame,text="Selected Target",variable=selected,
                            value="execute selected target", row=1, column=3)

    #Entry
    entry_name = Entry(frame_input, text="Configuration name",show="" ,column=2, row=0, columnspan=1, rowspan=1)
    entry_hostname = Entry(frame_input, text="Hostname/Address",show="" ,column=2, row=1, columnspan=1, rowspan=1)
    entry_username = Entry(frame_input, text="Username",show="" ,column=4, row=0, columnspan=1, rowspan=1)
    entry_password = Entry(frame_input, text="Password",show="*", column=4, row=1, columnspan=1, rowspan=1)
    entry_key = Entry(frame_input, text="Key file path location",show="", column=2, row=1, columnspan=2, rowspan=1)
    entry_key.entry.grid_forget()
    entry_type_key = Entry(frame_input, text="Type",show="", column=2, row=1, columnspan=2, rowspan=1, width=80)
    entry_type_key.entry.insert(0,"rsa")
    entry_type_key.entry.grid_forget()

    # Switch
    sudo_boolean = tk.BooleanVar()
    sudo_boolean.set(True)
    switch_sudo = Switch(frame=frame_bottom.frame,text="Sudo",variable=sudo_boolean,column=4,
                        row=0,rowspan=2,onvalue=True,offvalue=False)

    # Menu bar
    # Menu bar radiobutton variable
    based_auth = tk.StringVar()
    based_auth.set("password based")

    menu_bar = Menubar()

    # Configuration main window
    App.root_window("Remote Shell","950x600")

