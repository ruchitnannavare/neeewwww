from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar
import sqlite3
from sqlite3 import Error
import json
import functionsendtext
from requests import ConnectionError
from socket import SO_ERROR
import datetime
import os.path
favicon = "favicon.ico"
admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
admissions_standard_dict = {admissions_standard_list[0]: "eleven_science", admissions_standard_list[1]: "twelve_science"}
admissions_standard_dict_invert = {"eleven_science": admissions_standard_list[0], "twelve_science": admissions_standard_list[1]}
def custom_text():
    custom_root = Toplevel()
    custom_root.title("markOS™")
    custom_root.geometry("350x360")
    custom_root.iconbitmap(favicon)
    custom_root.resizable(0, 0)
    custom_root.attributes('-topmost', 'true')
    custom_root.configure(background="#d3d3d3")

    send_custom_text_label = Label(custom_root, text="Select one method.", bg="#d3d3d3", fg="#585858", font=(("Helvetica"), 10))
    send_custom_text_label.pack(anchor=W, padx=10, pady=(10, 15))

    option_frame_1 = Frame(custom_root, bg="#bababa", height=100, width=340)
    option_frame_1.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_1.propagate(False)
    empty_label = Label(option_frame_1, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_one_label = Label(option_frame_1, text="Send To One", font=("Helvetica", 18, "italic"), fg="#585858", bg="#bababa")
    send_one_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_one_instruction = Label(option_frame_1, text="Send custom text to one student.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    send_one_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    # Function for one
    def send_one():
        one_proceed_button.configure(state=DISABLED)
        send_one_toplevel = Toplevel()
        send_one_toplevel.iconbitmap(favicon)
        send_one_toplevel.title("markOS™")
        send_one_toplevel.configure(bg="#bababa")
        custom_root.attributes('-topmost', 'false')
        send_one_toplevel.attributes('-topmost', 'true')
        send_one_toplevel.geometry("310x135")
        send_one_prompt_label = Label(send_one_toplevel,
                                      text="Enter the students mID and the text you want to send.",
                                      bg="#bababa",
                                      fg="#585858",
                                      font=("Helvetica", 9))
        send_one_prompt_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        student_roll_label = Label(send_one_toplevel, text="Student mID:", font=7, bg="#bababa")
        student_roll_label.grid(row=1, column=0, pady=(15, 5), padx=10, sticky=W)

        student_roll_input = Entry(send_one_toplevel, borderwidth=0, width=25)
        student_roll_input.grid(row=1, column=1, sticky=W, padx=10, pady=(15, 5))
        def enter_text_one():
            unique_id = str(student_roll_input.get()).upper()
            unique_id = unique_id[:4]
            with open("C:/Users/Ruchit/PycharmProjects/markOS/student_key_data.json", "r") as file:
                try:
                    dictionary = json.load(file)
                    found_list = dictionary[unique_id]
                    permission = True
                except KeyError:
                    error_message = messagebox.showerror("Student Not found!",
                                                         "The mID unique key you entered isn't assigned to anyone yet.")
                    if error_message == "ok":
                        pass
                    student_roll_input.delete(0, END)
                    permission = False
            if permission == True:
                def printgiven(id):
                    print(id)
                    connection_name = "admission_" + str(found_list[0]) + ".db"
                    print(connection_name)
                    connection = sqlite3.connect(connection_name)
                    cursor = connection.cursor()
                    xcude = admissions_standard_dict[str(found_list[1])]
                    print(xcude)
                    toprint = f"select * FROM {xcude} WHERE rollno=?"
                    print(toprint)
                    try:
                        cursor.execute(toprint, (id,))
                        row = cursor.fetchone()
                        print(row)
                        print(1)
                    except Error as e:
                        print(e)
                        row = e

                    return row
                    connection.close()
                    cursor.close()

                data_tuple = printgiven(unique_id)
                print(found_list)
                send_one_toplevel.destroy()
                text_toplevel = Toplevel()
                text_toplevel.iconbitmap(favicon)
                text_toplevel.title("Send Text")
                text_toplevel.attributes('-topmost', 'true')
                text_toplevel.geometry("300x337")
                text_toplevel.configure(bg="#bababa")
                text_toplevel.resizable(0, 0)

                to_text_label = Label(text_toplevel, text=f"This message is associated to", fg="#585858", bg="#bababa", font=("Helvetica", 10))
                to_text_label.grid(row=0, column=0, columnspan=3, pady=(10, 0), padx=10, sticky=W)

                to_text_label_0 = Label(text_toplevel,
                                        text=f"{str(str(data_tuple[1]).lower()).capitalize()} {str(str(data_tuple[2]).lower()).capitalize()} studying in {found_list[1]}.",
                                        fg="#585858", bg="#bababa", font=("Helvetica", 10))
                to_text_label_0.grid(row=1, column=0, columnspan=3, pady=(0, 15), padx=10, sticky=W)

                text_message_label = Label(text_toplevel, text="Type your message below:", font=("Times", 9), bg="#bababa")
                text_message_label.grid(row=2, column=0, pady=(15, 0), padx=(10, 0), sticky=W)

                text_box = ScrolledText(text_toplevel, width=32, height=10)
                text_box.grid(row=3, column=0, columnspan=3, sticky=W, padx=10)

                send_to_option_label = Label(text_toplevel, text="Send To:", bg="#bababa", font=("Times", 9))
                send_to_option_label.grid(row=4, column=0, padx=10, pady=(10, 2), sticky=W)

                text_box_empty_frame = Frame(text_toplevel, bg="#bababa")
                text_box_empty_frame.grid(row=5, column=0, columnspan=3, padx=5, pady=3)
                class The_connecting_buttons:
                    def __init__(self, text, column, command):
                        self.text = text
                        self.column = column
                        self.command = command

                    def describe(self):
                        new_button = Button(text_box_empty_frame,
                                            text=self.text,
                                            font=("Helvetica", 10),
                                            width=10,
                                            borderwidth=0,
                                            bg="#45b4e7",
                                            fg="white",
                                            activeforeground="white",
                                            activebackground="#1ca0dd",
                                            command=self.command
                                            )
                        new_button.grid(row=0, column=self.column, padx=5, pady=3)
                def send_to_parent_only():
                    text_toplevel.attributes('-topmost', 'true')
                    try:
                        functionsendtext.custom_text(data_tuple[13], text_box.get("1.0", END))
                        show_success_message = messagebox.showinfo("Sent Successful!", "Message has been successfully sent!")
                        if show_success_message == "ok":
                            pass
                    except ConnectionError as e:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)
                    except SO_ERROR:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)

                def send_to_student_only():
                    text_toplevel.attributes('-topmost', 'true')
                    try:
                        functionsendtext.custom_text(data_tuple[14], text_box.get("1.0", END))
                        show_success_message = messagebox.showinfo("Sent Successful!", "Message has been successfully sent!")
                        if show_success_message == "ok":
                            pass
                    except ConnectionError as e:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)
                    except SO_ERROR:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)

                def send_to_both():
                    send_to_parent_only()
                    send_to_student_only()

                send_parent = The_connecting_buttons(f"{str(str(data_tuple[3]).lower()).capitalize()}", 0, send_to_parent_only)
                send_parent.describe()
                send_student = The_connecting_buttons("Student", 1, send_to_student_only)
                send_student.describe()
                send_both = The_connecting_buttons("Both", 2, send_to_both)
                send_both.describe()



        send_one_next_button = Button(send_one_toplevel,
                                      text="Next >",
                                      font=("Helvetica", 10),
                                      width=12,
                                      borderwidth=0,
                                      bg="#45b4e7",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#1ca0dd",
                                      command=enter_text_one)
        send_one_next_button.grid(row=2, columnspan=2, column=0, pady=15)

    one_proceed_button = Button(option_frame_1,
                                text="Send One",
                                font=("Helvetica", 10),
                                width=12,
                                borderwidth=0,
                                bg="#45b4e7",
                                fg="white",
                                activeforeground="white",
                                activebackground="#1ca0dd",
                                command=send_one)
    one_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))
    option_frame_2 = Frame(custom_root, bg="#bababa", height=100, width=340)
    option_frame_2.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_2.propagate(False)
    empty_label = Label(option_frame_2, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_batch_label = Label(option_frame_2, text="Send In Batch", font=("Helvetica", 18, "italic"), fg="#585858", bg="#bababa")
    send_batch_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_batch_instruction = Label(option_frame_2, text="Send custom text whole class.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    send_batch_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def send_all():
        custom_root.attributes('-topmost', 'false')
        send_all_toplevel = Toplevel()
        send_all_toplevel.geometry("255x180")
        send_all_toplevel.resizable(0, 0)
        send_all_toplevel.title("Send Text")
        send_all_toplevel.iconbitmap(favicon)
        send_all_toplevel.configure(background="#d3d3d3")
        standard_list = ["11 SCIENCE", "12 SCIENCE"]
        standard_dict = {standard_list[0]: "eleven_science", standard_list[1]: "twelve_science"}
        sub_list = ["Chemistry"]
        sub_dict = {"Chemistry": "chem"}
        academic_year_list = []
        for year in range(0, 79):
            year_string = "20" + str(20 + year) + "-" + str(21 + year)
            academic_year_list.append(year_string)

        prompt_label = Label(send_all_toplevel,
                             text="Send text to all students of the class.",
                             font=("Helvetica", 10),
                             bg="#d3d3d3",
                             fg="#585858")
        prompt_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=(10, 17))

        standard_label = Label(send_all_toplevel,
                               text="Standard:",
                               bg="#d3d3d3")
        standard_label.grid(row=1, column=0, sticky=W, padx=16, pady=5)

        standard = StringVar()
        standard.set(standard_list[0])

        standard_scroll = OptionMenu(send_all_toplevel,
                                     standard,
                                     *standard_list)
        standard_scroll.grid(row=1, column=1, sticky=EW, padx=16)

        absolute_year = datetime.date.today().year
        absolute_year = str(absolute_year)
        absolute_year_0 = absolute_year[2:]
        absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
        admissions_year = StringVar()
        admissions_year.set(absolute_year_variable)
        admissions_year_label = Label(send_all_toplevel,
                                      text="Academic Year:",
                                      bg="#d3d3d3")
        admissions_year_label.grid(row=2, column=0, sticky=W, padx=16, pady=5)

        admissions_year_scroll = OptionMenu(send_all_toplevel,
                                            admissions_year,
                                            *academic_year_list)
        admissions_year_scroll.grid(row=2, column=1, sticky=EW, padx=16, pady=5)

        def enter_text_all():
            send_all_next_button.configure(state=DISABLED)
            connection_name = "admission_" + str(admissions_year.get()) + ".db"
            xcude = standard_dict[str(standard.get())]
            if os.path.isfile(connection_name) == True:
                def get_chatids(database, table):

                    connection = sqlite3.connect(database)
                    cursor = connection.cursor()
                    try:

                        command = "select g_cid,s_cid from {}".format(table)
                        cursor.execute(command)
                        values = cursor.fetchall()
                        print("Done")
                    except Error as e:
                        show_warning = messagebox.showwarning("Data not found!",
                                                              "Data for the standard you entered doesnt exist yet!")
                        if show_warning == "ok":
                            pass
                    return values

                sender_list = get_chatids(connection_name, xcude)


                send_all_toplevel.destroy()
                text_toplevel = Toplevel()
                text_toplevel.iconbitmap(favicon)
                text_toplevel.title("Send Text")
                text_toplevel.attributes('-topmost', 'true')
                text_toplevel.geometry("300x370")
                text_toplevel.configure(bg="#bababa")
                text_toplevel.resizable(0, 0)

                to_text_label = Label(text_toplevel, text=f"This message is associated to", fg="#585858", bg="#bababa",
                                      font=("Helvetica", 10))
                to_text_label.grid(row=0, column=0, columnspan=3, pady=(10, 0), padx=10, sticky=W)

                to_text_label_0 = Label(text_toplevel,
                                        text=f"All students of {standard.get()} .",
                                        fg="#585858", bg="#bababa", font=("Helvetica", 10))
                to_text_label_0.grid(row=1, column=0, columnspan=3, pady=0, padx=10, sticky=W)

                to_text_label_1 = Label(text_toplevel,
                                        text=f"studying in academic year {admissions_year.get()}.",
                                        fg="#585858", bg="#bababa", font=("Helvetica", 10))
                to_text_label_1.grid(row=2, column=0, columnspan=3, pady=(0, 15), padx=10, sticky=W)

                text_message_label = Label(text_toplevel, text="Type your message below:", font=("Times", 9), bg="#bababa")
                text_message_label.grid(row=3, column=0, pady=(15, 0), padx=(10, 0), sticky=W)

                text_box = ScrolledText(text_toplevel, width=32, height=10)
                text_box.grid(row=4, column=0, columnspan=3, sticky=W, padx=10)

                send_to_option_label = Label(text_toplevel, text="Send To:", bg="#bababa", font=("Times", 9))
                send_to_option_label.grid(row=5, column=0, padx=10, pady=(10, 2), sticky=W)

                text_box_empty_frame = Frame(text_toplevel, bg="#bababa")
                text_box_empty_frame.grid(row=6, column=0, columnspan=3, padx=5, pady=3)


                class TheConnectingButtons:
                    def __init__(self, text, column, command):
                        self.text = text
                        self.column = column
                        self.command = command

                    def describe(self):
                        new_button = Button(text_box_empty_frame,
                                            text=self.text,
                                            font=("Helvetica", 10),
                                            width=10,
                                            borderwidth=0,
                                            bg="#45b4e7",
                                            fg="white",
                                            activeforeground="white",
                                            activebackground="#1ca0dd",
                                            command=self.command
                                            )
                        new_button.grid(row=0, column=self.column, padx=5, pady=3)

                """progress = Progressbar(text_toplevel, orient=HORIZONTAL, length=100, mode='indeterminate')
                progress.grid(row=5, columnspan=3, column=0, padx=10, pady=5)"""

                def send_to_parent_only(parent_cid):
                    text_toplevel.attributes('-topmost', 'true')
                    try:
                        functionsendtext.custom_text(parent_cid, text_box.get("1.0", END))
                    except ConnectionError as e:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)
                    except SO_ERROR:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)

                def send_to_student_only(student_cid):
                    text_toplevel.attributes('-topmost', 'true')
                    try:
                        functionsendtext.custom_text(student_cid, text_box.get("1.0", END))

                    except ConnectionError as e:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)
                    except SO_ERROR:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)

                def send_to_all_parent():
                    text_toplevel.geometry("300x420")
                    progressbar_label = Label(text_toplevel, text="Sending In Progress:", font=("Times", 10), bg="#bababa")
                    progressbar_label.grid(row=7, column=0, columnspan=2, pady=(5, 0), padx=(10, 0), sticky=W)
                    progressbar = Progressbar(text_toplevel, length=280, maximum=len(sender_list), value=0, mode="determinate", orient=HORIZONTAL)
                    progressbar.grid(row=8, column=0, columnspan=3, pady=(5, 0), padx=10, sticky=EW)
                    progress_variable = 0
                    for student_data_tuple in sender_list:
                        send_to_parent_only(student_data_tuple[0])
                        progress_variable += 1
                        progressbar.configure(value=progress_variable)
                    show_success_message = messagebox.showinfo("Sent Successful!",
                                                               "Message has been successfully sent!")
                    if show_success_message == "ok":
                        pass

                def send_to_all_students():
                    text_toplevel.geometry("300x420")
                    progressbar_label = Label(text_toplevel, text="Sending In Progress:", font=("Times", 10),
                                              bg="#bababa")
                    progressbar_label.grid(row=7, column=0, columnspan=2, pady=(5, 0), padx=(10, 0), sticky=W)
                    progressbar = Progressbar(text_toplevel, length=280, maximum=len(sender_list), value=0,
                                              mode="determinate", orient=HORIZONTAL)
                    progressbar.grid(row=8, column=0, columnspan=3, pady=(5, 0), padx=10, sticky=EW)
                    progress_variable = 0
                    for student_data_tuple in sender_list:
                        send_to_student_only(student_data_tuple[1])
                        progress_variable += 1
                        progressbar.configure(value=progress_variable)
                    show_success_message = messagebox.showinfo("Sent Successful!",
                                                               "Message has been successfully sent!")
                    if show_success_message == "ok":
                        pass

                def send_to_both():
                    progressbar_label = Label(text_toplevel, text="Sending In Progress:", font=("Times", 10),
                                              bg="#bababa")
                    progressbar_label.grid(row=7, column=0, columnspan=2, pady=(5, 0), padx=(10, 0), sticky=W)
                    progressbar = Progressbar(text_toplevel, length=280, maximum=len(sender_list), value=0,
                                              mode="determinate", orient=HORIZONTAL)
                    progressbar.grid(row=8, column=0, columnspan=3, pady=(5, 0), padx=10, sticky=EW)
                    progress_variable = 0
                    for student_data_tuple in sender_list:
                        send_to_parent_only(student_data_tuple[0])
                        send_to_student_only(student_data_tuple[1])
                        progress_variable += 1
                        progressbar.configure(value=progress_variable)
                    show_success_message = messagebox.showinfo("Sent Successful!",
                                                               "Message has been successfully sent!")
                    if show_success_message == "ok":
                        pass
                send_parent = TheConnectingButtons(f"All Guardians", 0, send_to_all_parent)
                send_parent.describe()
                send_student = TheConnectingButtons("All Students", 1, send_to_all_students)
                send_student.describe()
                send_both = TheConnectingButtons("Both", 2, send_to_both)
                send_both.describe()



            else:
                show_warning = messagebox.showwarning("Data not found!", "Data for the year you entered doesnt exist yet!")
                if show_warning == "ok":
                    send_all_next_button.configure(state=ACTIVE)




        send_all_next_button = Button(send_all_toplevel,
                                      text="Next >",
                                      font=("Helvetica", 10),
                                      width=12,
                                      borderwidth=0,
                                      bg="#45b4e7",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#1ca0dd",
                                      command=enter_text_all)
        send_all_next_button.grid(row=3, columnspan=2, column=0, pady=15)


    all_proceed_button = Button(option_frame_2, text="Send All",
                                font=("Helvetica", 10),
                                width=12,
                                borderwidth=0,
                                bg="#45b4e7",
                                fg="white",
                                activeforeground="white",
                                activebackground="#1ca0dd",
                                command=send_all)
    all_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))

    option_frame_3 = Frame(custom_root, bg="#bababa", height=100, width=340)
    option_frame_3.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_3.propagate(False)
    empty_label = Label(option_frame_3, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_specify_label = Label(option_frame_3, text="Send To Specific", font=("Helvetica", 18, "italic"), fg="#585858",
                               bg="#bababa")
    send_specify_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_specify_instruction = Label(option_frame_3, text="Send custom text to specific students.", font=("Helvetica", 9),
                                     fg="#585858", bg="#bababa")
    send_specify_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def send_specify():
        custom_root.attributes('-topmost', 'false')
        send_specify_toplevel = Toplevel()
        send_specify_toplevel.geometry("255x180")
        send_specify_toplevel.resizable(0, 0)
        send_specify_toplevel.title("Send Text")
        send_specify_toplevel.iconbitmap(favicon)
        send_specify_toplevel.configure(background="#d3d3d3")
        standard_list = ["11 SCIENCE", "12 SCIENCE"]
        standard_dict = {standard_list[0]: "eleven_science", standard_list[1]: "twelve_science"}
        sub_list = ["Chemistry"]
        sub_dict = {"Chemistry": "chem"}
        academic_year_list = []
        for year in range(0, 79):
            year_string = "20" + str(20 + year) + "-" + str(21 + year)
            academic_year_list.append(year_string)

        prompt_label = Label(send_specify_toplevel,
                             text="Send text to all students of the class.",
                             font=("Helvetica", 10),
                             bg="#d3d3d3",
                             fg="#585858")
        prompt_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=(10, 17))

        standard_label = Label(send_specify_toplevel,
                               text="Standard:",
                               bg="#d3d3d3")
        standard_label.grid(row=1, column=0, sticky=W, padx=16, pady=5)

        standard = StringVar()
        standard.set(standard_list[0])

        standard_scroll = OptionMenu(send_specify_toplevel,
                                     standard,
                                     *standard_list)
        standard_scroll.grid(row=1, column=1, sticky=EW, padx=16)

        absolute_year = datetime.date.today().year
        absolute_year = str(absolute_year)
        absolute_year_0 = absolute_year[2:]
        absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
        admissions_year = StringVar()
        admissions_year.set(absolute_year_variable)
        admissions_year_label = Label(send_specify_toplevel,
                                      text="Academic Year:",
                                      bg="#d3d3d3")
        admissions_year_label.grid(row=2, column=0, sticky=W, padx=16, pady=5)

        admissions_year_scroll = OptionMenu(send_specify_toplevel,
                                            admissions_year,
                                            *academic_year_list)
        admissions_year_scroll.grid(row=2, column=1, sticky=EW, padx=16, pady=5)

        def enter_text_specific():
            send_all_next_button.configure(state=DISABLED)
            connection_name = "admission_" + str(admissions_year.get()) + ".db"
            xcude = standard_dict[str(standard.get())]
            if os.path.isfile(connection_name) == True:
                def get_chatids(database, table):

                    connection = sqlite3.connect(database)
                    cursor = connection.cursor()
                    try:

                        command = "select rollno,g_cid,s_cid,first,last from {}".format(table)
                        cursor.execute(command)
                        values = cursor.fetchall()
                        print("Done")
                    except Error as e:
                        print(e)
                        show_warning = messagebox.showwarning("Data not found!",
                                                              "Data for the standard you entered doesnt exist yet!")
                        if show_warning == "ok":
                            pass
                    return values

                sender_list = get_chatids(connection_name, xcude)

                send_specify_toplevel.destroy()
                text_layout_toplevel = Toplevel()

                text_box_input = ScrolledText(text_layout_toplevel, width=100, height=10)
                text_box_input.pack()

                output_frame = Frame(text_layout_toplevel, width=1130, height=300)
                output_frame.pack(expand=True, fill=BOTH)
                output_canvas = Canvas(output_frame, width=1130, scrollregion=(0, 0, 1000, 1000))
                h = Scrollbar(output_frame, orient=HORIZONTAL, bg="green")
                h.pack(side=BOTTOM, fill=X)
                h.config(command=output_canvas.xview)
                v = Scrollbar(output_frame, orient=VERTICAL)
                v.pack(side=RIGHT, fill=Y)
                v.config(command=output_canvas.yview)
                output_canvas.configure(xscrollcommand=h.set, yscrollcommand=v.set)
                output_canvas.pack(side=LEFT, expand=True, fill=BOTH)

                the_other_output_canvas = Canvas(output_canvas, width=1130)
                the_other_output_canvas.pack(side=LEFT)

                """def on_mousewheel(event):
                    output_canvas.xview_scroll(-1 * (event.delta / 120), "units")"""

                #output_canvas.bind_all("<MouseWheel>", on_mousewheel)
                output_canvas.bind('<MouseWheel>', lambda event: output_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
                bgcolo = "#585858"
                roll_number_label = Label(the_other_output_canvas, text="mID", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                roll_number_label.grid(row=0, column=0, ipadx=5)

                name_label = Label(the_other_output_canvas, text="First Name", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                name_label.grid(row=0, column=1, ipadx=5)

                last_name_label = Label(the_other_output_canvas, text="Last Name", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                last_name_label.grid(row=0, column=2, ipadx=5)

                send_command_label = Label(the_other_output_canvas, text="Send To:", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                send_command_label.grid(row=0, column=3, ipadx=5)

                class TheConnectingButtons:
                    def __init__(self, text, column, command, frame):
                        self.text = text
                        self.column = column
                        self.command = command
                        self.frame = frame

                    def describe(self):
                        global new_button
                        new_button = Button(self.frame,
                                            text=self.text,
                                            font=("Helvetica", 10),
                                            width=10,
                                            borderwidth=0,
                                            bg="#45b4e7",
                                            fg="white",
                                            activeforeground="white",
                                            activebackground="#1ca0dd",
                                            command=lambda: self.command)
                        new_button.grid(row=0, column=self.column, padx=5, pady=3)

                    def pressed(self):
                        new_button.configure(bg="#67e867", activebackground="#35e035")
                """progress = Progressbar(text_toplevel, orient=HORIZONTAL, length=100, mode='indeterminate')
                progress.grid(row=5, columnspan=3, column=0, padx=10, pady=5)"""

                def send_to_parent_only(parent_cid):
                    text_layout_toplevel.attributes('-topmost', 'true')
                    try:
                        functionsendtext.custom_text(parent_cid, text_box_input.get("1.0", END))
                    except ConnectionError as e:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)
                    except SO_ERROR:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)

                def send_to_student_only(student_cid):
                    text_layout_toplevel.attributes('-topmost', 'true')
                    try:
                        functionsendtext.custom_text(student_cid, text_box_input.get("1.0", END))

                    except ConnectionError as e:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)
                    except SO_ERROR:
                        show_warning = messagebox.showwarning("Not connected to the internet.",
                                                              "You are not connected to the internet! Try again later.")
                        if show_warning == "ok":
                            custom_root.destroy()
                            one_proceed_button.configure(state=ACTIVE)

                def send_both(parent, student):
                    send_to_parent_only(parent)
                    send_to_student_only(student)

                def send_to_parent_only_next(parent, parent_b):
                    send_to_parent_only(parent)
                    parent_b.configure(bg="#67e867", activebackground="#35e035")

                def send_to_student_only_next(student, student_b):
                    send_to_student_only(student)
                    student_b.configure(bg="#67e867", activebackground="#35e035")

                def send_both_next(parent, student, both_b):
                    send_both(parent, student)
                    both_b.configure(bg="#67e867", activebackground="#35e035")
                the_bogo_color = "#bababa"
                indexing_number = 1
                for data_tuple in reversed(sender_list):
                    create_roll_label = Label(the_other_output_canvas, text=data_tuple[0], bg=the_bogo_color, width=31, font=9)
                    create_roll_label.grid(row=indexing_number, column=0, pady=(0, 5))

                    create_name_label = Label(the_other_output_canvas, text=data_tuple[3], bg=the_bogo_color, width=31, font=9)
                    create_name_label.grid(row=indexing_number, column=1, pady=(0, 5))

                    create_last_name_label = Label(the_other_output_canvas, text=data_tuple[4], bg=the_bogo_color, width=31, font=9)
                    create_last_name_label.grid(row=indexing_number, column=2, pady=(0, 5))

                    create_button_frame = Frame(the_other_output_canvas, bg=the_bogo_color)
                    create_button_frame.grid(row=indexing_number, column=3, pady=(0, 5))




                    """parent_button = TheConnectingButtons("Parent", 0, send_to_parent_only(data_tuple[1]), create_button_frame)
                    parent_button.describe()
                    student_button = TheConnectingButtons("Student", 1, send_to_student_only(data_tuple[2]), create_button_frame)
                    student_button.describe()
                    both_button = TheConnectingButtons("Both", 2, send_both(data_tuple[1], data_tuple[2]), create_button_frame)
                    both_button.describe()
                    indexing_number += 1"""



                    parent_button = Button(create_button_frame,
                                           text="Parent",
                                           font=("Helvetica", 10),
                                           width=10,
                                           borderwidth=0,
                                           bg="#45b4e7",
                                           fg="white",
                                           activeforeground="white",
                                           activebackground="#1ca0dd")
                    parent_button.configure(command=lambda i=data_tuple[1], parent_b=parent_button:send_to_parent_only_next(i, parent_b))
                    parent_button.grid(row=0, column=1, padx=4)
                    student_button = Button(create_button_frame,
                                            text="Student",
                                            font=("Helvetica", 10),
                                            width=10,
                                            borderwidth=0,
                                            bg="#45b4e7",
                                            fg="white",
                                            activeforeground="white",
                                            activebackground="#1ca0dd")
                    student_button.configure(command=lambda i=data_tuple[2], student_b=student_button: send_to_student_only_next(i, student_b))
                    student_button.grid(row=0, column=2, padx=5)
                    both_button = Button(create_button_frame,
                                         text="Both",
                                         font=("Helvetica", 10),
                                         width=10,
                                         borderwidth=0,
                                         bg="#45b4e7",
                                         fg="white",
                                         activeforeground="white",
                                         activebackground="#1ca0dd")
                    both_button.configure(command=lambda i=data_tuple[1], j=data_tuple[2], both_b=both_button: send_both_next(i, j, both_b))

                    both_button.grid(row=0, column=3, padx=4)
                    indexing_number += 1

                scroll_lord = output_canvas.create_window(0, 0, window=the_other_output_canvas, anchor=NW)
                output_canvas.configure(scrollregion=output_canvas.bbox("all"))

        send_all_next_button = Button(send_specify_toplevel,
                                      text="Next >",
                                      font=("Helvetica", 10),
                                      width=12,
                                      borderwidth=0,
                                      bg="#45b4e7",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#1ca0dd",
                                      command=enter_text_specific)
        send_all_next_button.grid(row=3, columnspan=2, column=0, pady=15)

    specify_proceed_button = Button(option_frame_3, text="Send Specific",
                                    font=("Helvetica", 10),
                                    width=12,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=send_specify)
    specify_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))





def send_scores():
    send_test_open = Toplevel()
    send_test_open.geometry("400x250")
    send_test_open.resizable(0, 0)
    send_test_open.title("Send Scores")
    send_test_open.iconbitmap(favicon)
    send_test_open.configure(background="#d3d3d3")
    new_test_standard_list = ["11 SCIENCE", "12 SCIENCE"]
    new_test_standard_dict = {new_test_standard_list[0]: "eleven_science", new_test_standard_list[1]: "twelve_science"}
    open_test_sub_list = ["Chemistry"]
    open_test_sub_dict = {"Chemistry": "chem"}
    academic_year_list = []
    for year in range(0, 79):
        year_string = "20" + str(20 + year) + "-" + str(21 + year)
        academic_year_list.append(year_string)

    test_open_prompt_label = Label(send_test_open, text="Prompt for opening an old test from your markOS database.",
                                   font=("Helvetica", 10),
                                   bg="#d3d3d3",
                                   fg="#585858")
    test_open_prompt_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=(10, 17))

    test_open_standard_label = Label(send_test_open,
                                     text="Standard:",
                                     bg="#d3d3d3")
    test_open_standard_label.grid(row=1, column=0, sticky=W, padx=16, pady=5)

    test_open_standard = StringVar()
    test_open_standard.set(new_test_standard_list[0])

    test_open_standard_scroll = OptionMenu(send_test_open,
                                           test_open_standard,
                                           *new_test_standard_list)
    test_open_standard_scroll.grid(row=1, column=1, sticky=EW, padx=16)

    absolute_year = datetime.date.today().year
    absolute_year = str(absolute_year)
    absolute_year_0 = absolute_year[2:]
    absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
    admissions_year = StringVar()
    admissions_year.set(absolute_year_variable)
    admissions_year_label = Label(send_test_open,
                                  text="Academic Year:",
                                  bg="#d3d3d3")
    admissions_year_label.grid(row=2, column=0, sticky=W, padx=16, pady=5)

    admissions_year_scroll = OptionMenu(send_test_open,
                                        admissions_year,
                                        *academic_year_list)
    admissions_year_scroll.grid(row=2, column=1, sticky=EW, padx=16, pady=5)

    subject_var = StringVar()
    subject_var.set(open_test_sub_list[0])

    subject_label = Label(send_test_open,
                          text="Subject:",
                          bg="#d3d3d3")
    subject_label.grid(row=3, column=0, sticky=W, padx=16, pady=5)

    subject_scroll = OptionMenu(send_test_open,
                                subject_var,
                                *open_test_sub_list)
    subject_scroll.grid(row=3, column=1, sticky=EW, padx=16, pady=5)

    def load_test():
        subject_name = subject_var.get()
        test_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[subject_var.get()] + "_" + str(new_test_standard_dict[test_open_standard.get()]) + ".db"
        if os.path.isfile(test_name) == True:
            test_open_prompt_label.configure(text="Please select the test to open.")
            send_test_open.geometry("380x240")
            admissions_year_label.destroy()
            admissions_year_scroll.destroy()
            test_open_standard_label.destroy()
            test_open_standard_scroll.destroy()
            subject_label.destroy()
            subject_scroll.destroy()
            connection = sqlite3.connect(test_name)
            cursor = connection.cursor()
            cursor.execute("select * from SQLite_master")
            test_name_table = []
            row = cursor.fetchall()
            rowlength = len(row)
            length = range(rowlength)
            for x in length:
                if ((x % 2) == 0):
                    test_name_table.append(row[x][1])
            test_name_label = Label(send_test_open,
                                    text="Test Name:",
                                    bg="#d3d3d3")
            test_name_label.grid(row=1, column=0, sticky=W, padx=16, pady=5)

            test_name_var = StringVar()
            test_name_var.set("Select the test you want to send.")
            test_name_scroll = OptionMenu(send_test_open,
                                          test_name_var,
                                          *test_name_table)
            test_name_scroll.grid(row=1, column=1, sticky=EW, padx=16, pady=5)



            def get_lst(database_name, test_name):
                connection = sqlite3.connect(database_name)
                cursor = connection.cursor()

                row = [("Rollno.", "First Name", "Last Name", "Marks Scored", "Maximun Marks", "Percentage Secured")]
                try:

                    command = "select rollno,first,last,marks_scored,max_marks,percentage from {}".format(test_name)
                    print(100)
                    cursor.execute(command)
                    rowss = cursor.fetchall()

                except Error as e:
                    print(e)
                try:
                    rows = row + rowss
                    return rows
                except UnboundLocalError:
                    show_warning = messagebox.showwarning("Error!", "Please select a test first.")
                    if show_warning == "ok":
                        pass

            def show_table():
                class Mytable:
                    def __init__(self, show_test_root):
                        for i in range(totalrows):
                            for j in range(totalcolumns):
                                self.e = Label(show_test_root, width=20, fg="black", font=("Arial", 11))
                                self.e.grid(row=i, column=j)
                                self.e.configure(text=str(lst[i][j]), borderwidth=1, relief="solid", bg="#d3d3d3", anchor=W)
                lst = get_lst(test_name, test_name_var.get())

                totalrows = len(lst)
                totalcolumns = len(lst[1])
                show_test_root = Toplevel()
                show_test_root.title(test_name_var.get())
                show_test_root.iconbitmap(favicon)
                show_test_root.resizable(0, 0)
                mt = Mytable(show_test_root)

            def send_scores(database_name, test_name):
                connection = sqlite3.connect(database_name)
                cursor = connection.cursor()

                row = [("Rollno.", "First Name", "Last Name", "Marks Scored", "Maximun Marks", "Percentage Secured")]
                try:

                    command = "select rollno,first,last,marks_scored,max_marks,percentage,g_cid,s_cid from {}".format(test_name)
                    print(100)
                    cursor.execute(command)
                    rowss = cursor.fetchall()
                    progressbar_label = Label(send_test_open, text="Sending In Progress:", font=("Times", 10),
                                              bg="#d3d3d3")
                    progressbar_label.grid(row=5, column=0, padx=16, pady=(30, 0), sticky=W)
                    progressbar = Progressbar(send_test_open, length=340, maximum=len(rowss), value=0,
                                              mode="determinate", orient=HORIZONTAL)
                    progressbar.grid(row=6, column=0, columnspan=2, padx=16, pady=(5, 0), sticky=EW)
                    progress_variable = 0
                    test_date = test_name[13:18]
                    for data_tuple in rowss:
                        print(data_tuple)
                        full_name = str(data_tuple[1]) + " " + str(data_tuple[2])
                        functionsendtext.send_them_scores(full_name,
                                                          data_tuple[3],
                                                          data_tuple[4],
                                                          subject_name,
                                                          test_date,
                                                          data_tuple[6],
                                                          data_tuple[7])
                        progress_variable += 1
                        progressbar.configure(value=progress_variable)
                except Error as e:
                    rows = e
                    print(e)


            open_old_test_old_test_button.configure(text="See Test", command=show_table)
            send_test_button = Button(send_test_open,
                                      text="Send Test Result",
                                      font=("Helvetica", 10),
                                      width=18,
                                      borderwidth=0,
                                      bg="#67e867",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#35e035",
                                      command=lambda :send_scores(test_name, test_name_var.get()))
            send_test_button.grid(row=4, column=1, sticky=W, padx=16, pady=(30, 0))
        else:
            show_error = messagebox.showerror("Data does not exist!", "No such test has been created!")
            if show_error == "ok":
                pass
    open_old_test_old_test_button = Button(send_test_open,
                                           text="Show Test",
                                           font=("Helvetica", 10),
                                           width=12,
                                           borderwidth=0,
                                           bg="#45b4e7",
                                           fg="white",
                                           activeforeground="white",
                                           activebackground="#1ca0dd",
                                           command=load_test)
    open_old_test_old_test_button.grid(row=4, column=0, sticky=EW, padx=16, pady=(30, 0))

