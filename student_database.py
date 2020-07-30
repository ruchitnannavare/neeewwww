from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os.path
import json
import datetime
import globalvariables
from tkinter.scrolledtext import ScrolledText
favicon = "favicon.ico"


def update_data_function():
    update_database_root = Toplevel()
    update_database_root.geometry("300x120")
    update_database_root.title("Update")
    update_database_root.iconbitmap(favicon)
    update_database_root.resizable(0, 0)
    update_database_root.configure(background="#d3d3d3")
    update_label = Label(update_database_root, text="Prompt for updating student information.", font=("Helvetica", 10), fg="#585858", bg="#d3d3d3")
    update_label.grid(row=0, column=0, columnspan=2, ipadx=10, pady=(10, 5))
    student_roll_label = Label(update_database_root, text="Enter student's unique ID:", anchor=W, bg="#d3d3d3")
    student_roll_label.grid(row=1, column=0, padx=5, pady=5)
    student_roll_input = Entry(update_database_root, borderwidth=0)
    student_roll_input.grid(row=1, column=1, padx=5, pady=5)
    admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
    admissions_standard_dict = {admissions_standard_list[0]: "eleven_science", admissions_standard_list[1]: "twelve_science"}
    admissions_standard_dict_invert = {"eleven_science": admissions_standard_list[0],
                                       "twelve_science": admissions_standard_list[1]}
    def update_data():
        update_data_buttom = Button(update_database_root,
                                    text="Enter",
                                    font=("Helvetica", 10),
                                    width=15,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=update_data,
                                    state=DISABLED)
        update_data_buttom.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))
        unique_id = str(student_roll_input.get()).upper()
        with open("student_key_data.json", "r") as file:
            try:
                dictionary = json.load(file)
                found_list = dictionary[unique_id]
                permission = True
            except KeyError:
                error_message = messagebox.showerror("Student Not found!", "The mID unique key you entered isn't assigned to anyone yet.")
                if error_message == "ok":
                    pass
                student_roll_input.delete(0, END)
                update_data_buttom.configure(state=ACTIVE)
                permission = False
        if permission == True:
            print(found_list)

            def printgiven(id):
                print(id)
                connection_name = "admission_" + str(found_list[0]) + ".db"
                print(connection_name)
                connection = sqlite3.connect(connection_name)
                cursor = connection.cursor()
                xcude = admissions_standard_dict[str(found_list[1])]
                print(xcude)
                toprint = f"select * FROM {xcude} where Rollno=?"
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
            print(data_tuple)
            admissions_root = Toplevel()
            admissions_root.geometry("496x545")
            admissions_root.resizable(0, 0)
            admissions_root.title("Update Data")
            admissions_root.iconbitmap(favicon)
            admissions_root.configure(background="#d3d3d3")
            admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
            admissions_branch_list = ["Harni", "Karelibaug"]
            admissions_year_list = []
            for year in range(0, 79):
                year_string = "20" + str(20 + year) + "-" + str(21 + year)
                admissions_year_list.append(year_string)
            admissions_parent_relation_list = ["Mother", "Father", "Guardian"]

            # Admission prompt
            admissions_label = Label(admissions_root,
                                     text="Prompt for updating student data, fill in the details.",
                                     anchor=W,
                                     bg="#d3d3d3",
                                     fg="#585858",
                                     font=("Helevetica", 10))
            admissions_label.grid(row=0, column=0, columnspan=2, ipadx=78, pady=(15, 15))
            # Student details
            # Students first name
            admissions_firstname_label = Label(admissions_root,
                                               text="Student's First Name:",
                                               bg="#d3d3d3")
            admissions_firstname_label.grid(row=1, column=0, padx=10, sticky=W)
            firstname_var = StringVar()
            firstname_var.set(data_tuple[1])
            admissions_firstname_input = Entry(admissions_root,
                                               width=30,
                                               font=11,
                                               bg="white",
                                               borderwidth=0,
                                               textvariable=firstname_var)
            admissions_firstname_input.grid(row=1, column=1, padx=15, sticky=W)
            # Student's last name
            admissions_lastname_label = Label(admissions_root,
                                              text="Student's Last Name:",
                                              bg="#d3d3d3")
            admissions_lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
            lastname_var = StringVar()
            lastname_var.set(data_tuple[2])
            admissions_lastname_input = Entry(admissions_root,
                                              width=30,
                                              font=11,
                                              bg="white",
                                              borderwidth=0,
                                              textvariable=lastname_var)
            admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

            # Relation dropdown menu
            guardian_relation = StringVar()
            guardian_relation.set(data_tuple[3])
            admissions_guardian_relation_label = Label(admissions_root,
                                                       text="Guardian Relation:",
                                                       bg="#d3d3d3")
            admissions_guardian_relation_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
            admissions_relation_label = OptionMenu(admissions_root, guardian_relation, *admissions_parent_relation_list)
            admissions_relation_label.grid(row=3, column=1, padx=14, pady=10, sticky=W)

            # Guardian name input
            admissions_guardian_name_label = Label(admissions_root,
                                                   text=f"{guardian_relation.get()} Full Name:",
                                                   bg="#d3d3d3")
            admissions_guardian_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
            guardianname_var = StringVar()
            guardianname_var.set(data_tuple[4])
            admissions_guardian_name_input = Entry(admissions_root,
                                                   width=30,
                                                   font=11,
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=guardianname_var)
            admissions_guardian_name_input.grid(row=4, column=1, padx=15, pady=10, sticky=W)

            # Student Address
            admissions_student_address_label = Label(admissions_root,
                                                     text="Student Address:",
                                                     bg="#d3d3d3")
            admissions_student_address_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
            address_var = StringVar()
            address_var.set(data_tuple[5])
            admissions_student_address_input = Entry(admissions_root,
                                                     width=30,
                                                     font=(11),
                                                     bg="white",
                                                     borderwidth=0,
                                                     textvariable=address_var)
            admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

            # Admission year frame
            admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
            admissions_year_frame.grid(row=6, column=0)

            admissions_year = StringVar()
            admissions_year.set(data_tuple[6])
            admissions_year_label = Label(admissions_year_frame,
                                          text="Academic Year:",
                                          bg="#d3d3d3")
            admissions_year_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

            admissions_year_scroll = OptionMenu(admissions_year_frame,
                                                admissions_year,
                                                *admissions_year_list, )
            admissions_year_scroll.grid(row=0, column=1, sticky=W)

            # Standard frame
            admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
            admissions_standard_frame.grid(row=6, column=1)
            admissions_standard_label = Label(admissions_standard_frame,
                                              text="                              Standard:",
                                              bg="#d3d3d3")
            admissions_standard_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

            admissions_standard = StringVar()
            admissions_standard.set(data_tuple[7])

            admissions_standard_scroll = OptionMenu(admissions_standard_frame,
                                                    admissions_standard,
                                                    *admissions_standard_list)
            admissions_standard_scroll.grid(row=0, column=1, sticky=W)

            # Branch Frame
            admissions_branch_label = Label(admissions_root,
                                            text="Branch:",
                                            bg="#d3d3d3")
            admissions_branch_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

            admissions_branch = StringVar()
            admissions_branch.set(data_tuple[8])

            admissions_branch_scroll = OptionMenu(admissions_root,
                                                  admissions_branch,
                                                  *admissions_branch_list)
            admissions_branch_scroll.grid(row=7, column=1, padx=14, pady=10, sticky=EW)

            # parents mobile number
            admissions_parent_number_label = Label(admissions_root,
                                                   text="Guardian Phone Number:",
                                                   bg="#d3d3d3")
            admissions_parent_number_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
            parent_var = IntVar()
            parent_var.set(data_tuple[9])
            admissions_parent_number_input = Entry(admissions_root,
                                                   width=30,
                                                   font=11,
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=parent_var)
            admissions_parent_number_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

            # Student phone Number
            admissions_student_number_label = Label(admissions_root,
                                                    text="Student Phone Number:",
                                                    bg="#d3d3d3")
            admissions_student_number_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
            student_var = IntVar()
            student_var.set(data_tuple[10])
            admissions_student_number_input = Entry(admissions_root,
                                                    width=30,
                                                    font=11,
                                                    bg="white",
                                                    borderwidth=0,
                                                    textvariable=student_var)
            admissions_student_number_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

            # Guardian email address
            admissions_guardian_email_label = Label(admissions_root,
                                                    text="Guardian Email Address:",
                                                    bg="#d3d3d3")
            admissions_guardian_email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
            parent_mail_var = StringVar()
            parent_mail_var.set(data_tuple[11])
            admissions_guardian_email_input = Entry(admissions_root,
                                                    width=30,
                                                    font=11,
                                                    bg="white",
                                                    borderwidth=0,
                                                    textvariable=parent_mail_var)
            admissions_guardian_email_input.grid(row=10, column=1, padx=15, pady=10, sticky=W)

            # Student email address
            admissions_student_email_label = Label(admissions_root,
                                                   text="Student Email Address:",
                                                   bg="#d3d3d3")
            admissions_student_email_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
            student_mail_var = StringVar()
            student_mail_var.set(data_tuple[12])
            admissions_student_email_input = Entry(admissions_root,
                                                   width=30,
                                                   font=(11),
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=student_mail_var)
            admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)

            # Functions for checking admission details
            def check_admission_details():
                input_list = [admissions_firstname_input, admissions_lastname_input, admissions_guardian_name_input,
                              admissions_student_address_input, admissions_parent_number_input, admissions_student_number_input,
                              admissions_guardian_email_input, admissions_student_email_input]
                input_label_list = [admissions_firstname_label, admissions_lastname_label, admissions_guardian_name_label,
                                    admissions_student_address_label, admissions_parent_number_label,
                                    admissions_student_number_label, admissions_guardian_email_label,
                                    admissions_student_email_label]
                for i in input_list:
                    if len(i.get()) == 0:
                        missing_text = input_label_list[input_list.index(i)].cget("text")
                        give_warning = messagebox.showerror("Blank is Empty", f"{missing_text} Can not be left empty!")
                        if give_warning == "ok":
                            i.delete(0, END)

            # Check Int and strings
            def check_int_str():
                variable_int_list = [admissions_student_number_input, admissions_parent_number_input]
                variable_int_list_label = [admissions_student_number_label, admissions_parent_number_label]
                for integer in variable_int_list:
                    try:
                        int(integer.get())
                    except ValueError:
                        integer_error_variable = variable_int_list_label[variable_int_list.index(integer)].cget("text")
                        integer_error = messagebox.showerror("Number Error",
                                                             f"{integer_error_variable} Can only contain numbers!")
                        if integer_error == "ok":
                            integer.delete(0, END)

                variable_str_list = [admissions_firstname_input, admissions_lastname_input, admissions_guardian_name_input]
                variable_str_list_label = [admissions_firstname_label, admissions_lastname_label,
                                           admissions_guardian_name_label]
                for string in variable_str_list:
                    string_list = list(string.get())
                    occurance = 0
                    for element in string_list:
                        for num in list(range(0, 10)):
                            if str(num) == element:
                                print(num)
                                string_error_variable = variable_str_list_label[variable_str_list.index(string)].cget("text")
                                string_error = messagebox.showerror("Character Error",
                                                                    f"{string_error_variable} Can only contain alphabetic characters.")
                                occurance += 1
                                if string_error == "ok":
                                    string.delete(0, END)
                        if occurance >= 1:
                            break

            # Submit button function
            def update_submit():
                global data_tuple_2
                check_admission_details()
                check_admission_details()
                check_int_str()
                admissions_confirmation = messagebox.askyesno("Confirm Update",
                                                              "All the details are filled in!\nClick YES to update your markOS database.",
                                                              master=admissions_root)
                data_tuple_2 = (str(admissions_firstname_input.get()).upper(),
                                str(admissions_lastname_input.get()).upper(),
                                str(guardian_relation.get().upper()),
                                str(admissions_guardian_name_input.get()).upper(),
                                str(admissions_student_address_input.get()).upper(),
                                str(admissions_year.get()),
                                str(admissions_standard.get()),
                                str(admissions_branch.get()).upper(),
                                int(admissions_parent_number_input.get()),
                                int(admissions_student_number_input.get()),
                                str(admissions_guardian_email_input.get()),
                                str(admissions_student_email_input.get()))
                print(data_tuple_2)
                if admissions_confirmation == True:
                    password_window = Toplevel()
                    password_window.attributes('-topmost', 'true')
                    password_window.geometry("200x130")
                    password_window.iconbitmap(favicon)
                    password_window.configure(background="#d3d3d3")
                    password_window.resizable(0, 0)
                    password_window_label = Label(password_window, width=25,
                                                  text="Please enter master password\nto edit your markOS database.",
                                                  bg="#d3d3d3")
                    password_window_label.pack(pady=(10, 0))
                    password_window_input = Entry(password_window, borderwidth=0, show="*", width=25, font=("Times", 9, "bold"))
                    password_window_input.pack(pady=(15, 0))

                    def update_successfull():
                        print(password_window_input.get())
                        if str(password_window_input.get()) == "1234":
                            admissions_root.attributes('-topmost', 'false')
                            password_window.attributes('-topmost', 'false')

                            admission_succesfull_message = messagebox.showinfo("Update Successful!",
                                                                               f"Update process has been succesfull.")


                            if admission_succesfull_message == "ok":
                                def update_given(Rollno, sfn, sln, gr, gfn, sa, ay, std, branch, gpn, spn, gea, sea):
                                    connection_name = "admission_" + str(found_list[0]) + ".db"
                                    print(connection_name)
                                    xcude = admissions_standard_dict[str(found_list[1])]
                                    print(xcude)
                                    connection = sqlite3.connect(connection_name)
                                    cursor = connection.cursor()

                                    updategiven = f"""update {xcude} set
                                                   first='%s',
                                                   last='%s',
                                                   gr='%s',
                                                   guardian='%s',
                                                   address='%s',
                                                   year='%s',
                                                   standard='%s',
                                                   branch='%s',
                                                   g_no='%s',
                                                   s_no='%s',
                                                   g_em='%s',
                                                   s_em='%s'
                                                   where rollno='%s' """
                                    args = (sfn, sln, gr, gfn, sa, ay, std, branch, gpn, spn, gea, sea, Rollno)

                                    try:
                                        cursor.execute(updategiven % args)
                                        connection.commit()
                                        out = "Done."

                                    except Error as e:
                                        connection.rollback()
                                        print(e)
                                        out = e
                                    return out
                                    connection.close()
                                    cursor.close()
                                admissions_root.destroy()
                                password_window.destroy()
                                update_given(str(unique_id)[:4],
                                             data_tuple_2[0],
                                             data_tuple_2[1],
                                             data_tuple_2[2],
                                             data_tuple_2[3],
                                             data_tuple_2[4],
                                             data_tuple_2[5],
                                             data_tuple_2[6],
                                             data_tuple_2[7],
                                             data_tuple_2[8],
                                             data_tuple_2[9],
                                             data_tuple_2[10],
                                             data_tuple_2[11])
                                update_database_root.destroy()
                        else:
                            messagewarning = messagebox.showwarning("Incorrect Password",
                                                                    "The Password you have entered is incorrect,\nplease try again.")
                            if messagewarning == "ok":
                                password_window_input.delete(0, END)

                    password_window_confirmation_button = Button(password_window,
                                                                 text="Enter Admission",
                                                                 font=("Helvetica", 9),
                                                                 width=15,
                                                                 borderwidth=0,
                                                                 bg="#67e867",
                                                                 fg="white",
                                                                 activeforeground="white",
                                                                 activebackground="#35e035",
                                                                 command=update_successfull)
                    password_window_confirmation_button.pack(pady=(15, 0))
                else:
                    admissions_root.destroy()

            # Submit button
            update_submit_button = Button(admissions_root,
                                          text="Submit Update",
                                          width=25,
                                          borderwidth=0,
                                          font=("Helvetica", 9),
                                          bg="#45b4e7",
                                          fg="white",
                                          activeforeground="white",
                                          activebackground="#1ca0dd",
                                          command=update_submit)
            update_submit_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)

    update_button = Button(update_database_root,
                           text="Enter",
                           font=("Helvetica", 10),
                           width=15,
                           borderwidth=0,
                           bg="#45b4e7",
                           fg="white",
                           activeforeground="white",
                           activebackground="#1ca0dd",
                           command=update_data)

    update_button.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))

def access_data_function():
    data_access_top = Toplevel()
    data_access_top.title("markOS™ Current Year Data.")
    data_access_top.geometry("350x260")
    data_access_top.iconbitmap(favicon)
    data_access_top.resizable(0, 0)
    data_access_top.attributes('-topmost', 'true')
    data_access_top.configure(background="#d3d3d3")

    send_custom_text_label = Label(data_access_top, text="Select one method to see current year data.", bg="#d3d3d3", fg="#585858", font=(("Helvetica"), 10))
    send_custom_text_label.pack(anchor=W, padx=10, pady=(10, 15))

    option_frame_1 = Frame(data_access_top, bg="#bababa", height=100, width=340)
    option_frame_1.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_1.propagate(False)
    empty_label = Label(option_frame_1, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_one_label = Label(option_frame_1, text="See One", font=("Helvetica", 18, "italic"), fg="#585858", bg="#bababa")
    send_one_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_one_instruction = Label(option_frame_1, text="See data of one student in particular.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    send_one_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def access_data_function_for_one():
        data_access_top.attributes('-topmost', 'false')
        access_data_root = Toplevel()
        access_data_root.attributes('-topmost', 'true')
        access_data_root.geometry("300x120")
        access_data_root.title("Student Data")
        access_data_root.iconbitmap(favicon)
        access_data_root.resizable(0, 0)
        access_data_root.configure(background="#d3d3d3")
        data_access_top.destroy()
        access_data_label = Label(access_data_root, text="Prompt for accessing student information.", font=("Helvetica", 10), fg="#585858", bg="#d3d3d3")
        access_data_label.grid(row=0, column=0, columnspan=2, ipadx=10, pady=(10, 5))
        student_roll_label = Label(access_data_root, text="Enter student's unique ID:", anchor=W, bg="#d3d3d3")
        student_roll_label.grid(row=1, column=0, padx=5, pady=5)
        student_roll_input = Entry(access_data_root, borderwidth=0)
        student_roll_input.grid(row=1, column=1, padx=5, pady=5)
        admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
        admissions_standard_dict = {"11 SCIENCE": "eleven_science", "12 SCIENCE": "twelve_science"}
        admissions_standard_dict_invert = {"eleven_science": admissions_standard_list[0],
                                           "twelve_science": admissions_standard_list[1]}
        def access_data():
            access_data_button.configure(state=DISABLED)
            unique_id = str(student_roll_input.get()).upper()
            with open("student_key_data.json", "r") as file:
                try:
                    dictionary = json.load(file)
                    found_list = dictionary[unique_id]
                    access_data_root.attributes('-topmost', 'false')
                    permission = True
                except KeyError:
                    access_data_root.attributes('-topmost', 'false')
                    error_message = messagebox.showerror("Student Not found!", "The mID unique key you entered isn't assigned to anyone yet.")
                    if error_message == "ok":
                        access_data_root.attributes('-topmost', 'true')
                    access_data_root.attributes('-topmost', 'true')
                    student_roll_input.delete(0, END)
                    access_data_button.configure(state=ACTIVE)
                    permission = False
            if permission == True:
                print(found_list)

                def printgiven(id):
                    print(id)
                    connection_name = "admission_" + str(found_list[0]) + ".db"
                    print(connection_name)
                    connection = sqlite3.connect(connection_name)
                    cursor = connection.cursor()
                    xcude = admissions_standard_dict[str(found_list[1])]
                    print(xcude)
                    toprint = f"select * FROM {xcude} where Rollno=?"
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
                print(data_tuple)
                admissions_root = Toplevel()
                admissions_root.geometry("496x545")
                admissions_root.resizable(0, 0)
                admissions_root.title("Current year student data")
                admissions_root.iconbitmap(favicon)
                admissions_root.configure(background="#d3d3d3")
                admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
                admissions_branch_list = ["Harni", "Karelibaug"]
                admissions_year_list = []
                for year in range(0, 79):
                    year_string = "20" + str(20 + year) + "-" + str(21 + year)
                    admissions_year_list.append(year_string)
                admissions_parent_relation_list = ["Mother", "Father", "Guardian"]

                # Admission prompt
                admissions_label = Label(admissions_root,
                                         text="Accessing current year student data.",
                                         anchor=W,
                                         bg="#d3d3d3",
                                         fg="#585858",
                                         font=("Helevetica", 10))
                admissions_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(15, 15), sticky=W)
                # Student details
                # Students first name
                admissions_firstname_label = Label(admissions_root,
                                                   text="Student's First Name:",
                                                   bg="#d3d3d3")
                admissions_firstname_label.grid(row=1, column=0, padx=10, sticky=W)
                firstname_var = StringVar()
                firstname_var.set(data_tuple[1])
                admissions_firstname_input = Entry(admissions_root,
                                                   width=30,
                                                   font=11,
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=firstname_var)
                admissions_firstname_input.grid(row=1, column=1, padx=15, sticky=W)
                # Student's last name
                admissions_lastname_label = Label(admissions_root,
                                                  text="Student's Last Name:",
                                                  bg="#d3d3d3")
                admissions_lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
                lastname_var = StringVar()
                lastname_var.set(data_tuple[2])
                admissions_lastname_input = Entry(admissions_root,
                                                  width=30,
                                                  font=11,
                                                  bg="white",
                                                  borderwidth=0,
                                                  textvariable=lastname_var)
                admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

                # Relation dropdown menu
                guardian_relation = StringVar()
                guardian_relation.set(data_tuple[3])
                admissions_guardian_relation_label = Label(admissions_root,
                                                           text="Guardian Relation:",
                                                           bg="#d3d3d3")
                admissions_guardian_relation_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
                admissions_relation_label = OptionMenu(admissions_root, guardian_relation, *admissions_parent_relation_list)
                admissions_relation_label.grid(row=3, column=1, padx=14, pady=10, sticky=W)

                # Guardian name input
                admissions_guardian_name_label = Label(admissions_root,
                                                       text=f"{guardian_relation.get()} Full Name:",
                                                       bg="#d3d3d3")
                admissions_guardian_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
                guardianname_var = StringVar()
                guardianname_var.set(data_tuple[4])
                admissions_guardian_name_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=guardianname_var)
                admissions_guardian_name_input.grid(row=4, column=1, padx=15, pady=10, sticky=W)

                # Student Address
                admissions_student_address_label = Label(admissions_root,
                                                         text="Student Address:",
                                                         bg="#d3d3d3")
                admissions_student_address_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
                address_var = StringVar()
                address_var.set(data_tuple[5])
                admissions_student_address_input = Entry(admissions_root,
                                                         width=30,
                                                         font=11,
                                                         bg="white",
                                                         borderwidth=0,
                                                         textvariable=address_var)
                admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

                # Admission year frame
                admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
                admissions_year_frame.grid(row=6, column=0)

                admissions_year = StringVar()
                admissions_year.set(found_list[0])
                admissions_year_label = Label(admissions_year_frame,
                                              text="Academic Year:",
                                              bg="#d3d3d3")
                admissions_year_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

                admissions_year_scroll = OptionMenu(admissions_year_frame,
                                                    admissions_year,
                                                    *admissions_year_list, )
                admissions_year_scroll.grid(row=0, column=1, sticky=W)

                # Standard frame
                admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
                admissions_standard_frame.grid(row=6, column=1)
                admissions_standard_label = Label(admissions_standard_frame,
                                                  text="                              Standard:",
                                                  bg="#d3d3d3")
                admissions_standard_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

                admissions_standard = StringVar()
                admissions_standard.set(found_list[1])

                admissions_standard_scroll = OptionMenu(admissions_standard_frame,
                                                        admissions_standard,
                                                        *admissions_standard_list)
                admissions_standard_scroll.grid(row=0, column=1, sticky=W)

                # Branch Frame
                admissions_branch_label = Label(admissions_root,
                                                text="Branch:",
                                                bg="#d3d3d3")
                admissions_branch_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

                admissions_branch = StringVar()
                admissions_branch.set(data_tuple[8])

                admissions_branch_scroll = OptionMenu(admissions_root,
                                                      admissions_branch,
                                                      *admissions_branch_list)
                admissions_branch_scroll.grid(row=7, column=1, padx=14, pady=10, sticky=EW)

                # parents mobile number
                admissions_parent_number_label = Label(admissions_root,
                                                       text="Guardian Phone Number:",
                                                       bg="#d3d3d3")
                admissions_parent_number_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
                parent_var = IntVar()
                parent_var.set(data_tuple[9])
                admissions_parent_number_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=parent_var)
                admissions_parent_number_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

                # Student phone Number
                admissions_student_number_label = Label(admissions_root,
                                                        text="Student Phone Number:",
                                                        bg="#d3d3d3")
                admissions_student_number_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
                student_var = IntVar()
                student_var.set(data_tuple[10])
                admissions_student_number_input = Entry(admissions_root,
                                                        width=30,
                                                        font=11,
                                                        bg="white",
                                                        borderwidth=0,
                                                        textvariable=student_var)
                admissions_student_number_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

                # Guardian email address
                admissions_guardian_email_label = Label(admissions_root,
                                                        text="Guardian Email Address:",
                                                        bg="#d3d3d3")
                admissions_guardian_email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
                parent_mail_var = StringVar()
                parent_mail_var.set(data_tuple[11])
                admissions_guardian_email_input = Entry(admissions_root,
                                                        width=30,
                                                        font=11,
                                                        bg="white",
                                                        borderwidth=0,
                                                        textvariable=parent_mail_var)
                admissions_guardian_email_input.grid(row=10, column=1, padx=15, pady=10, sticky=W)

                # Student email address
                admissions_student_email_label = Label(admissions_root,
                                                       text="Student Email Address:",
                                                       bg="#d3d3d3")
                admissions_student_email_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
                student_mail_var = StringVar()
                student_mail_var.set(data_tuple[12])
                admissions_student_email_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=student_mail_var)
                admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)


                # Submit button
                def okay_function():
                    access_data_root.destroy()
                    admissions_root.destroy()
                okay_button = Button(admissions_root,
                                     text="Close",
                                     width=25,
                                     borderwidth=0,
                                     font=("Helvetica", 9),
                                     bg="#ff6565",
                                     fg="white",
                                     activeforeground="white",
                                     activebackground="#ff4f4f",
                                     command=okay_function)
                okay_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)



        access_data_button = Button(access_data_root,
                                    text="Enter",
                                    font=("Helvetica", 10),
                                    width=15,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=access_data)
        access_data_button.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))

    one_proceed_button = Button(option_frame_1,
                                    text="See One",
                                    font=("Helvetica", 10),
                                    width=12,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=access_data_function_for_one)
    one_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))

    option_frame_2 = Frame(data_access_top, bg="#bababa", height=100, width=340)
    option_frame_2.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_2.propagate(False)
    empty_label = Label(option_frame_2, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    see_batch_label = Label(option_frame_2, text="See Batch", font=("Helvetica", 18, "italic"), fg="#585858", bg="#bababa")
    see_batch_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    see_batch_instruction = Label(option_frame_2, text="See data of whole class.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    see_batch_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def access_all():
        data_access_top.attributes('-topmost', 'false')
        access_all_toplevel = Toplevel()
        access_all_toplevel.geometry("255x180")
        access_all_toplevel.resizable(0, 0)
        access_all_toplevel.title("Send Text")
        access_all_toplevel.iconbitmap(favicon)
        access_all_toplevel.configure(background="#d3d3d3")
        standard_list = ["11 SCIENCE", "12 SCIENCE"]
        standard_dict = {standard_list[0]: "eleven_science", standard_list[1]: "twelve_science"}
        sub_list = ["Chemistry"]
        sub_dict = {"Chemistry": "chem"}
        academic_year_list = []
        for year in range(0, 79):
            year_string = "20" + str(20 + year) + "-" + str(21 + year)

        prompt_label = Label(access_all_toplevel,
                             text="Send text to all students of the class.",
                             font=("Helvetica", 10),
                             bg="#d3d3d3",
                             fg="#585858")
        prompt_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=(10, 17))

        standard_label = Label(access_all_toplevel,
                               text="Standard:",
                               bg="#d3d3d3")
        standard_label.grid(row=1, column=0, sticky=W, padx=16, pady=5)

        standard = StringVar()
        standard.set(standard_list[0])

        standard_scroll = OptionMenu(access_all_toplevel,
                                     standard,
                                     *standard_list)
        standard_scroll.grid(row=1, column=1, sticky=EW, padx=16)

        absolute_year = datetime.date.today().year
        if datetime.date.today().month >= globalvariables.new_academic_year_month_stopper:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
        else:
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(int(absolute_year) - 1) + "-" + str(int(absolute_year_0))
        academic_year_list.append(absolute_year_variable)
        admissions_year = StringVar()
        admissions_year.set(absolute_year_variable)
        admissions_year_label = Label(access_all_toplevel,
                                      text="Academic Year:",
                                      bg="#d3d3d3")
        admissions_year_label.grid(row=2, column=0, sticky=W, padx=16, pady=5)

        admissions_year_scroll = OptionMenu(access_all_toplevel,
                                            admissions_year,
                                            *academic_year_list)
        admissions_year_scroll.grid(row=2, column=1, sticky=EW, padx=16, pady=5)

        def access_batch_details():
            all_proceed_button.configure(state=DISABLED)
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

                access_all_toplevel.destroy()
                student_list_toplevel = Toplevel()
                student_list_toplevel.iconbitmap(favicon)
                student_list_toplevel.resizable(0, 10)

                output_frame = Frame(student_list_toplevel, width=948, height=300)
                output_frame.pack(expand=True, fill=BOTH)
                output_canvas = Canvas(output_frame, width=950, scrollregion=(0, 0, 10000, 10000))
                h = Scrollbar(output_frame, orient=HORIZONTAL, bg="green")
                h.pack(side=BOTTOM, fill=X)
                h.config(command=output_canvas.xview)
                v = Scrollbar(output_frame, orient=VERTICAL)
                v.pack(side=RIGHT, fill=Y)
                v.config(command=output_canvas.yview)
                output_canvas.configure(xscrollcommand=h.set, yscrollcommand=v.set)
                output_canvas.pack(side=LEFT, expand=True, fill=BOTH)

                the_other_output_canvas = Canvas(output_canvas, width=948)
                the_other_output_canvas.pack(side=LEFT)
                output_canvas.bind_all('<MouseWheel>', lambda event: output_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

                bgcolo = "#585858"
                roll_number_label = Label(the_other_output_canvas, text="mID", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                roll_number_label.grid(row=0, column=0, ipadx=5)

                name_label = Label(the_other_output_canvas, text="First Name", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                name_label.grid(row=0, column=1, ipadx=5)

                last_name_label = Label(the_other_output_canvas, text="Last Name", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                last_name_label.grid(row=0, column=2, ipadx=5)

                send_command_label = Label(the_other_output_canvas, text="Open", font=("Helvetica", 12), bg=bgcolo, width=10, fg="white")
                send_command_label.grid(row=0, column=3)

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

                def access_data(unique_id, open_b):
                    open_b.configure(bg="#67e867", activebackground="#35e035", text="Opened", state=DISABLED)
                    with open("student_key_data.json", "r") as file:
                        try:
                            dictionary = json.load(file)
                            found_list = dictionary[unique_id]
                            #access_data_root.attributes('-topmost', 'false')
                            permission = True
                        except KeyError:
                            #access_data_root.attributes('-topmost', 'false')
                            error_message = messagebox.showerror("Student Not found!",
                                                                 "The mID unique key you entered isn't assigned to anyone yet.")
                            if error_message == "ok":
                                #access_data_root.attributes('-topmost', 'true')
                                permission = False
                            #access_data_root.attributes('-topmost', 'true')
                    if permission == True:
                        print(found_list)

                        def printgiven(id):
                            print(id)
                            connection_name = "admission_" + str(found_list[0]) + ".db"
                            print(connection_name)
                            connection = sqlite3.connect(connection_name)
                            cursor = connection.cursor()
                            xcude = standard_dict[str(found_list[1])]
                            print(xcude)
                            toprint = f"select * FROM {xcude} where Rollno=?"
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
                        print(data_tuple)
                        admissions_root = Toplevel()
                        admissions_root.geometry("496x525")
                        admissions_root.resizable(0, 0)
                        admissions_root.title("Student Data")
                        admissions_root.iconbitmap(favicon)
                        admissions_root.configure(background="#d3d3d3")
                        admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
                        admissions_branch_list = ["Harni", "Karelibaug"]
                        admissions_year_list = []
                        for year in range(0, 79):
                            year_string = "20" + str(20 + year) + "-" + str(21 + year)
                            admissions_year_list.append(year_string)
                        admissions_parent_relation_list = ["Mother", "Father", "Guardian"]

                        # Admission prompt
                        admissions_label = Label(admissions_root,
                                                 text="Accessing current year student data.",
                                                 anchor=W,
                                                 bg="#d3d3d3",
                                                 fg="#585858",
                                                 font=("Helevetica", 10))
                        admissions_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(15, 15), sticky=W)
                        # Student details
                        # Students first name
                        admissions_firstname_label = Label(admissions_root,
                                                           text="Student's First Name:",
                                                           bg="#d3d3d3")
                        admissions_firstname_label.grid(row=1, column=0, padx=10, sticky=W)
                        firstname_var = StringVar()
                        firstname_var.set(data_tuple[1])
                        admissions_firstname_input = Entry(admissions_root,
                                                           width=30,
                                                           font=11,
                                                           bg="#d3d3d3",
                                                           borderwidth=0,
                                                           textvariable=firstname_var,
                                                           state="readonly")
                        admissions_firstname_input.grid(row=1, column=1, padx=15, sticky=W)
                        # Student's last name
                        admissions_lastname_label = Label(admissions_root,
                                                          text="Student's Last Name:",
                                                          bg="#d3d3d3")
                        admissions_lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
                        lastname_var = StringVar()
                        lastname_var.set(data_tuple[2])
                        admissions_lastname_input = Entry(admissions_root,
                                                          width=30,
                                                          font=11,
                                                          bg="#d3d3d3",
                                                          borderwidth=0,
                                                          textvariable=lastname_var,
                                                          state="readonly")
                        admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

                        # Relation dropdown menu
                        guardian_relation = StringVar()
                        guardian_relation.set(data_tuple[3])
                        admissions_guardian_relation_label = Label(admissions_root,
                                                                   text="Guardian Relation:",
                                                                   bg="#d3d3d3")
                        admissions_guardian_relation_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
                        admissions_relation_label = Entry(admissions_root,
                                                          font=11,
                                                          bg="#d3d3d3",
                                                          borderwidth=0,
                                                          textvariable=guardian_relation,
                                                          state="readonly")
                        admissions_relation_label.grid(row=3, column=1, padx=14, pady=10, sticky=W)

                        # Guardian name input
                        admissions_guardian_name_label = Label(admissions_root,
                                                               text=f"{guardian_relation.get()} Full Name:",
                                                               bg="#d3d3d3")
                        admissions_guardian_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
                        guardianname_var = StringVar()
                        guardianname_var.set(data_tuple[4])
                        admissions_guardian_name_input = Entry(admissions_root,
                                                               width=30,
                                                               font=11,
                                                               bg="#d3d3d3",
                                                               borderwidth=0,
                                                               textvariable=guardianname_var,
                                                               state="readonly")
                        admissions_guardian_name_input.grid(row=4, column=1, padx=15, pady=10, sticky=W)

                        # Student Address
                        admissions_student_address_label = Label(admissions_root,
                                                                 text="Student Address:",
                                                                 bg="#d3d3d3")
                        admissions_student_address_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
                        address_var = StringVar()
                        address_var.set(data_tuple[5])
                        admissions_student_address_input = Entry(admissions_root,
                                                                 width=30,
                                                                 font=11,
                                                                 bg="#d3d3d3",
                                                                 borderwidth=0,
                                                                 textvariable=address_var,
                                                                 state="readonly")
                        admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

                        # Admission year frame
                        admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
                        admissions_year_frame.grid(row=6, column=0)

                        admissions_year = StringVar()
                        admissions_year.set(found_list[0])
                        admissions_year_label = Label(admissions_year_frame,
                                                      text="Academic Year:",
                                                      bg="#d3d3d3")
                        admissions_year_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

                        admissions_year_scroll = Entry(admissions_year_frame,
                                                       width=10,
                                                       font=11,
                                                       bg="#d3d3d3",
                                                       borderwidth=0,
                                                       textvariable=admissions_year,
                                                       state="readonly")
                        admissions_year_scroll.grid(row=0, column=1, sticky=W)

                        # Standard frame
                        admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
                        admissions_standard_frame.grid(row=6, column=1)
                        admissions_standard_label = Label(admissions_standard_frame,
                                                          text="                              Standard:",
                                                          bg="#d3d3d3")
                        admissions_standard_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

                        admissions_standard = StringVar()
                        admissions_standard.set(found_list[1])

                        admissions_standard_scroll = Entry(admissions_standard_frame,
                                                           width=11,
                                                           font=11,
                                                           bg="#d3d3d3",
                                                           borderwidth=0,
                                                           textvariable=admissions_standard,
                                                           state="readonly")
                        admissions_standard_scroll.grid(row=0, column=1, sticky=W)

                        # Branch Frame
                        admissions_branch_label = Label(admissions_root,
                                                        text="Branch:",
                                                        bg="#d3d3d3")
                        admissions_branch_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

                        admissions_branch = StringVar()
                        admissions_branch.set(data_tuple[8])

                        admissions_branch_scroll = Entry(admissions_root,
                                                         font=11,
                                                         bg="#d3d3d3",
                                                         borderwidth=0,
                                                         textvariable=admissions_branch,
                                                         state="readonly")
                        admissions_branch_scroll.grid(row=7, column=1, padx=14, pady=10, sticky=W)

                        # parents mobile number
                        admissions_parent_number_label = Label(admissions_root,
                                                               text="Guardian Phone Number:",
                                                               bg="#d3d3d3")
                        admissions_parent_number_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
                        parent_var = IntVar()
                        parent_var.set(data_tuple[9])
                        admissions_parent_number_input = Entry(admissions_root,
                                                               width=30,
                                                               font=11,
                                                               bg="#d3d3d3",
                                                               borderwidth=0,
                                                               textvariable=parent_var,
                                                               state="readonly")
                        admissions_parent_number_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

                        # Student phone Number
                        admissions_student_number_label = Label(admissions_root,
                                                                text="Student Phone Number:",
                                                                bg="#d3d3d3")
                        admissions_student_number_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
                        student_var = IntVar()
                        student_var.set(data_tuple[10])
                        admissions_student_number_input = Entry(admissions_root,
                                                                width=30,
                                                                font=11,
                                                                bg="#d3d3d3",
                                                                borderwidth=0,
                                                                textvariable=student_var,
                                                                state="readonly")
                        admissions_student_number_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

                        # Guardian email address
                        admissions_guardian_email_label = Label(admissions_root,
                                                                text="Guardian Email Address:",
                                                                bg="#d3d3d3")
                        admissions_guardian_email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
                        parent_mail_var = StringVar()
                        parent_mail_var.set(data_tuple[11])
                        admissions_guardian_email_input = Entry(admissions_root,
                                                                width=30,
                                                                font=11,
                                                                bg="#d3d3d3",
                                                                borderwidth=0,
                                                                textvariable=parent_mail_var,
                                                                state="readonly")
                        admissions_guardian_email_input.grid(row=10, column=1, padx=15, pady=10, sticky=W)

                        # Student email address
                        admissions_student_email_label = Label(admissions_root,
                                                               text="Student Email Address:",
                                                               bg="#d3d3d3")
                        admissions_student_email_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
                        student_mail_var = StringVar()
                        student_mail_var.set(data_tuple[12])
                        admissions_student_email_input = Entry(admissions_root,
                                                               width=30,
                                                               font=11,
                                                               bg="#d3d3d3",
                                                               borderwidth=0,
                                                               textvariable=student_mail_var,
                                                               state="readonly")
                        admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)

                        # Submit button
                        def okay_function():
                            #access_data_root.destroy()
                            open_b.configure(bg="#67e867", activebackground="#35e035", text="Reopen", state=ACTIVE)
                            admissions_root.destroy()

                        okay_button = Button(admissions_root,
                                             text="Close",
                                             width=25,
                                             borderwidth=0,
                                             font=("Helvetica", 9),
                                             bg="#ff6565",
                                             fg="white",
                                             activeforeground="white",
                                             activebackground="#ff4f4f",
                                             command=okay_function)
                        okay_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)


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



                    open_button = Button(create_button_frame,
                                         text="Open",
                                         font=("Helvetica", 10),
                                         width=11,
                                         borderwidth=0,
                                         bg="#45b4e7",
                                         fg="white",
                                         activeforeground="white",
                                         activebackground="#1ca0dd")
                    open_button.configure(command=lambda i=data_tuple[0], open_b=open_button: access_data(i, open_b))
                    open_button.grid(row=0, column=1)

                    indexing_number += 1
                scroll_lord = output_canvas.create_window(0, 0, window=the_other_output_canvas, anchor=NW)
                output_canvas.configure(scrollregion=output_canvas.bbox("all"))

        access_batch_details_button = Button(access_all_toplevel,
                                             text="Next >",
                                             font=("Helvetica", 10),
                                             width=12,
                                             borderwidth=0,
                                             bg="#45b4e7",
                                             fg="white",
                                             activeforeground="white",
                                             activebackground="#1ca0dd",
                                             command=access_batch_details)
        access_batch_details_button.grid(row=3, columnspan=2, column=0, pady=15)



    all_proceed_button = Button(option_frame_2, text="See Batch",
                                font=("Helvetica", 10),
                                width=12,
                                borderwidth=0,
                                bg="#45b4e7",
                                fg="white",
                                activeforeground="white",
                                activebackground="#1ca0dd",
                                command=access_all)
    all_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))






# Archived data

def archive_function():
    data_access_top = Toplevel()
    data_access_top.title("markOS™ Archives")
    data_access_top.geometry("350x260")
    data_access_top.iconbitmap(favicon)
    data_access_top.resizable(0, 0)
    data_access_top.attributes('-topmost', 'true')
    data_access_top.configure(background="#d3d3d3")

    send_custom_text_label = Label(data_access_top, text="Select one method to see archives.", bg="#d3d3d3", fg="#585858", font=(("Helvetica"), 10))
    send_custom_text_label.pack(anchor=W, padx=10, pady=(10, 15))

    option_frame_1 = Frame(data_access_top, bg="#bababa", height=100, width=340)
    option_frame_1.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_1.propagate(False)
    empty_label = Label(option_frame_1, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_one_label = Label(option_frame_1, text="See One", font=("Helvetica", 18, "italic"), fg="#585858", bg="#bababa")
    send_one_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_one_instruction = Label(option_frame_1, text="See data of one student in particular.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    send_one_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def access_data_function_for_one():
        data_access_top.attributes('-topmost', 'false')
        access_data_root = Toplevel()
        access_data_root.attributes('-topmost', 'true')
        access_data_root.geometry("300x120")
        access_data_root.title("Student Data")
        access_data_root.iconbitmap(favicon)
        access_data_root.resizable(0, 0)
        access_data_root.configure(background="#d3d3d3")
        data_access_top.destroy()
        access_data_label = Label(access_data_root, text="Prompt for accessing student information.", font=("Helvetica", 10), fg="#585858", bg="#d3d3d3")
        access_data_label.grid(row=0, column=0, columnspan=2, ipadx=10, pady=(10, 5))
        student_roll_label = Label(access_data_root, text="Enter student's unique ID:", anchor=W, bg="#d3d3d3")
        student_roll_label.grid(row=1, column=0, padx=5, pady=5)
        student_roll_input = Entry(access_data_root, borderwidth=0)
        student_roll_input.grid(row=1, column=1, padx=5, pady=5)
        admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
        admissions_standard_dict = {"11 SCIENCE": "eleven_science", "12 SCIENCE": "twelve_science"}
        admissions_standard_dict_invert = {"eleven_science": admissions_standard_list[0],
                                           "twelve_science": admissions_standard_list[1]}
        def access_data():
            access_data_button.configure(state=DISABLED)
            unique_id = str(student_roll_input.get()).upper()
            with open("student_key_data.json", "r") as file:
                try:
                    dictionary = json.load(file)
                    found_list = dictionary[unique_id]
                    access_data_root.attributes('-topmost', 'false')
                    permission = True
                except KeyError:
                    access_data_root.attributes('-topmost', 'false')
                    error_message = messagebox.showerror("Student Not found!", "The mID unique key you entered isn't assigned to anyone yet.")
                    if error_message == "ok":
                        access_data_root.attributes('-topmost', 'true')
                    access_data_root.attributes('-topmost', 'true')
                    student_roll_input.delete(0, END)
                    access_data_button.configure(state=ACTIVE)
                    permission = False
            if permission == True:
                print(found_list)

                def printgiven(id):
                    print(id)
                    connection_name = "admission_" + str(found_list[0]) + ".db"
                    print(connection_name)
                    connection = sqlite3.connect(connection_name)
                    cursor = connection.cursor()
                    xcude = admissions_standard_dict[str(found_list[1])]
                    print(xcude)
                    toprint = f"select * FROM {xcude} where Rollno=?"
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
                print(data_tuple)
                admissions_root = Toplevel()
                admissions_root.geometry("496x559")
                admissions_root.resizable(0, 0)
                admissions_root.title("Student data from archives")
                admissions_root.iconbitmap(favicon)
                admissions_root.configure(background="#d3d3d3")
                admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
                admissions_branch_list = ["Harni", "Karelibaug"]
                admissions_year_list = []
                for year in range(0, 79):
                    year_string = "20" + str(20 + year) + "-" + str(21 + year)
                    admissions_year_list.append(year_string)
                admissions_parent_relation_list = ["Mother", "Father", "Guardian"]

                # Admission prompt
                admissions_label = Label(admissions_root,
                                         text="Accessing student data from archives.",
                                         anchor=W,
                                         bg="#d3d3d3",
                                         fg="#585858",
                                         font=("Helevetica", 10))
                admissions_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(15, 15), sticky=W)
                # Student details
                # Students first name
                admissions_firstname_label = Label(admissions_root,
                                                   text="Student's First Name:",
                                                   bg="#d3d3d3")
                admissions_firstname_label.grid(row=1, column=0, padx=10, sticky=W)
                firstname_var = StringVar()
                firstname_var.set(data_tuple[1])
                admissions_firstname_input = Entry(admissions_root,
                                                   width=30,
                                                   font=11,
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=firstname_var)
                admissions_firstname_input.grid(row=1, column=1, padx=15, sticky=W)
                # Student's last name
                admissions_lastname_label = Label(admissions_root,
                                                  text="Student's Last Name:",
                                                  bg="#d3d3d3")
                admissions_lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
                lastname_var = StringVar()
                lastname_var.set(data_tuple[2])
                admissions_lastname_input = Entry(admissions_root,
                                                  width=30,
                                                  font=11,
                                                  bg="white",
                                                  borderwidth=0,
                                                  textvariable=lastname_var)
                admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

                # Relation dropdown menu
                guardian_relation = StringVar()
                guardian_relation.set(data_tuple[3])
                admissions_guardian_relation_label = Label(admissions_root,
                                                           text="Guardian Relation:",
                                                           bg="#d3d3d3")
                admissions_guardian_relation_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
                admissions_relation_label = OptionMenu(admissions_root, guardian_relation, *admissions_parent_relation_list)
                admissions_relation_label.grid(row=3, column=1, padx=14, pady=10, sticky=W)

                # Guardian name input
                admissions_guardian_name_label = Label(admissions_root,
                                                       text=f"{guardian_relation.get()} Full Name:",
                                                       bg="#d3d3d3")
                admissions_guardian_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
                guardianname_var = StringVar()
                guardianname_var.set(data_tuple[4])
                admissions_guardian_name_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=guardianname_var)
                admissions_guardian_name_input.grid(row=4, column=1, padx=15, pady=10, sticky=W)

                # Student Address
                admissions_student_address_label = Label(admissions_root,
                                                         text="Student Address:",
                                                         bg="#d3d3d3")
                admissions_student_address_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
                address_var = StringVar()
                address_var.set(data_tuple[5])
                admissions_student_address_input = Entry(admissions_root,
                                                         width=30,
                                                         font=11,
                                                         bg="white",
                                                         borderwidth=0,
                                                         textvariable=address_var)
                admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

                # Admission year frame
                admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
                admissions_year_frame.grid(row=6, column=0)

                admissions_year = StringVar()
                admissions_year.set(data_tuple[6])
                admissions_year_label = Label(admissions_year_frame,
                                              text="Year of \nAdmission:",
                                              bg="#d3d3d3")
                admissions_year_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

                admissions_year_scroll = OptionMenu(admissions_year_frame,
                                                    admissions_year,
                                                    *admissions_year_list, )
                admissions_year_scroll.grid(row=0, column=1, sticky=W)

                # Standard frame
                admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
                admissions_standard_frame.grid(row=6, column=1)
                admissions_standard_label = Label(admissions_standard_frame,
                                                  text="           Admitted            \nin Standard:",
                                                  bg="#d3d3d3")
                admissions_standard_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

                admissions_standard = StringVar()
                admissions_standard.set(data_tuple[7])

                admissions_standard_scroll = OptionMenu(admissions_standard_frame,
                                                        admissions_standard,
                                                        *admissions_standard_list)
                admissions_standard_scroll.grid(row=0, column=1, sticky=W)

                # Branch Frame
                admissions_branch_label = Label(admissions_root,
                                                text="Branch:",
                                                bg="#d3d3d3")
                admissions_branch_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

                admissions_branch = StringVar()
                admissions_branch.set(data_tuple[8])

                admissions_branch_scroll = OptionMenu(admissions_root,
                                                      admissions_branch,
                                                      *admissions_branch_list)
                admissions_branch_scroll.grid(row=7, column=1, padx=14, pady=10, sticky=EW)

                # parents mobile number
                admissions_parent_number_label = Label(admissions_root,
                                                       text="Guardian Phone Number:",
                                                       bg="#d3d3d3")
                admissions_parent_number_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
                parent_var = IntVar()
                parent_var.set(data_tuple[9])
                admissions_parent_number_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=parent_var)
                admissions_parent_number_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

                # Student phone Number
                admissions_student_number_label = Label(admissions_root,
                                                        text="Student Phone Number:",
                                                        bg="#d3d3d3")
                admissions_student_number_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
                student_var = IntVar()
                student_var.set(data_tuple[10])
                admissions_student_number_input = Entry(admissions_root,
                                                        width=30,
                                                        font=11,
                                                        bg="white",
                                                        borderwidth=0,
                                                        textvariable=student_var)
                admissions_student_number_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

                # Guardian email address
                admissions_guardian_email_label = Label(admissions_root,
                                                        text="Guardian Email Address:",
                                                        bg="#d3d3d3")
                admissions_guardian_email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
                parent_mail_var = StringVar()
                parent_mail_var.set(data_tuple[11])
                admissions_guardian_email_input = Entry(admissions_root,
                                                        width=30,
                                                        font=11,
                                                        bg="white",
                                                        borderwidth=0,
                                                        textvariable=parent_mail_var)
                admissions_guardian_email_input.grid(row=10, column=1, padx=15, pady=10, sticky=W)

                # Student email address
                admissions_student_email_label = Label(admissions_root,
                                                       text="Student Email Address:",
                                                       bg="#d3d3d3")
                admissions_student_email_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
                student_mail_var = StringVar()
                student_mail_var.set(data_tuple[12])
                admissions_student_email_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=student_mail_var)
                admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)


                # Submit button
                def okay_function():
                    access_data_root.destroy()
                    admissions_root.destroy()
                okay_button = Button(admissions_root,
                                     text="Close",
                                     width=25,
                                     borderwidth=0,
                                     font=("Helvetica", 9),
                                     bg="#ff6565",
                                     fg="white",
                                     activeforeground="white",
                                     activebackground="#ff4f4f",
                                     command=okay_function)
                okay_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)



        access_data_button = Button(access_data_root,
                                    text="Enter",
                                    font=("Helvetica", 10),
                                    width=15,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=access_data)
        access_data_button.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))

    one_proceed_button = Button(option_frame_1,
                                    text="See One",
                                    font=("Helvetica", 10),
                                    width=12,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=access_data_function_for_one)
    one_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))

    option_frame_2 = Frame(data_access_top, bg="#bababa", height=100, width=340)
    option_frame_2.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_2.propagate(False)
    empty_label = Label(option_frame_2, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    see_batch_label = Label(option_frame_2, text="See Batch", font=("Helvetica", 18, "italic"), fg="#585858", bg="#bababa")
    see_batch_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    see_batch_instruction = Label(option_frame_2, text="See data of whole class.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    see_batch_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def access_all():
        data_access_top.attributes('-topmost', 'false')
        access_all_toplevel = Toplevel()
        access_all_toplevel.geometry("255x180")
        access_all_toplevel.resizable(0, 0)
        access_all_toplevel.title("Send Text")
        access_all_toplevel.iconbitmap(favicon)
        access_all_toplevel.configure(background="#d3d3d3")
        standard_list = ["11 SCIENCE", "12 SCIENCE"]
        standard_dict = {standard_list[0]: "eleven_science", standard_list[1]: "twelve_science"}
        sub_list = ["Chemistry"]
        sub_dict = {"Chemistry": "chem"}
        academic_year_list = []
        for year in range(0, 79):
            year_string = "20" + str(20 + year) + "-" + str(21 + year)
            academic_year_list.append(year_string)

        prompt_label = Label(access_all_toplevel,
                             text="Send text to all students of the class.",
                             font=("Helvetica", 10),
                             bg="#d3d3d3",
                             fg="#585858")
        prompt_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=(10, 17))

        standard_label = Label(access_all_toplevel,
                               text="Standard:",
                               bg="#d3d3d3")
        standard_label.grid(row=1, column=0, sticky=W, padx=16, pady=5)

        standard = StringVar()
        standard.set(standard_list[0])

        standard_scroll = OptionMenu(access_all_toplevel,
                                     standard,
                                     *standard_list)
        standard_scroll.grid(row=1, column=1, sticky=EW, padx=16)

        absolute_year = datetime.date.today().year
        if datetime.date.today().month >= 4:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
        else:
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(int(absolute_year) - 1) + "-" + str(int(absolute_year_0))
        academic_year_list.append(absolute_year_variable)
        admissions_year = StringVar()
        admissions_year.set(absolute_year_variable)
        admissions_year_label = Label(access_all_toplevel,
                                      text="Academic Year:",
                                      bg="#d3d3d3")
        admissions_year_label.grid(row=2, column=0, sticky=W, padx=16, pady=5)

        admissions_year_scroll = OptionMenu(access_all_toplevel,
                                            admissions_year,
                                            *academic_year_list)
        admissions_year_scroll.grid(row=2, column=1, sticky=EW, padx=16, pady=5)

        def access_batch_details():
            all_proceed_button.configure(state=DISABLED)
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

                access_all_toplevel.destroy()
                student_list_toplevel = Toplevel()
                student_list_toplevel.iconbitmap(favicon)
                student_list_toplevel.resizable(0, 10)

                output_frame = Frame(student_list_toplevel, width=948, height=300)
                output_frame.pack(expand=True, fill=BOTH)

                output_canvas = Canvas(output_frame, width=948, scrollregion=(0, 0, 10000, 10000))
                h = Scrollbar(output_frame, orient=HORIZONTAL, bg="green")
                h.pack(side=BOTTOM, fill=X)
                v = Scrollbar(output_frame, orient=VERTICAL)
                v.pack(side=RIGHT, fill=Y)
                output_canvas.configure(xscrollcommand=h.set, yscrollcommand=v.set)
                h.config(command=output_canvas.xview)
                v.config(command=output_canvas.yview)

                output_canvas.pack()

                bgcolo = "#585858"

                the_other_output_canvas = Canvas(output_canvas, width=948)
                the_other_output_canvas.pack(side=TOP, anchor=N, pady=0)

                output_canvas.bind_all('<MouseWheel>', lambda event: output_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

                roll_number_label = Label(the_other_output_canvas, text="mID", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                roll_number_label.grid(row=0, column=0, ipadx=5)

                name_label = Label(the_other_output_canvas, text="First Name", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                name_label.grid(row=0, column=1, ipadx=5)

                last_name_label = Label(the_other_output_canvas, text="Last Name", font=("Helvetica", 12), bg=bgcolo, width=30, fg="white")
                last_name_label.grid(row=0, column=2, ipadx=5)

                send_command_label = Label(the_other_output_canvas, text="Open", font=("Helvetica", 12), bg=bgcolo, width=10, fg="white")
                send_command_label.grid(row=0, column=3)

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

                def access_data(unique_id, open_b):
                    open_b.configure(bg="#67e867", activebackground="#35e035", text="Opened", state=DISABLED)
                    with open("student_key_data.json", "r") as file:
                        try:
                            dictionary = json.load(file)
                            found_list = dictionary[unique_id]
                            #access_data_root.attributes('-topmost', 'false')
                            permission = True
                        except KeyError:
                            #access_data_root.attributes('-topmost', 'false')
                            error_message = messagebox.showerror("Student Not found!",
                                                                 "The mID unique key you entered isn't assigned to anyone yet.")
                            if error_message == "ok":
                                #access_data_root.attributes('-topmost', 'true')
                                permission = False
                            #access_data_root.attributes('-topmost', 'true')
                    if permission == True:
                        print(found_list)

                        def printgiven(id):
                            print(id)
                            connection_name = "admission_" + str(found_list[0]) + ".db"
                            print(connection_name)
                            connection = sqlite3.connect(connection_name)
                            cursor = connection.cursor()
                            xcude = standard_dict[str(found_list[1])]
                            print(xcude)
                            toprint = f"select * FROM {xcude} where Rollno=?"
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
                        print(data_tuple)
                        admissions_root = Toplevel()
                        admissions_root.geometry("496x545")
                        admissions_root.resizable(0, 0)
                        admissions_root.title("Student data from archives")
                        admissions_root.iconbitmap(favicon)
                        admissions_root.configure(background="#d3d3d3")
                        admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
                        admissions_branch_list = ["Harni", "Karelibaug"]
                        admissions_year_list = []
                        for year in range(0, 79):
                            year_string = "20" + str(20 + year) + "-" + str(21 + year)
                            admissions_year_list.append(year_string)
                        admissions_parent_relation_list = ["Mother", "Father", "Guardian"]

                        # Admission prompt
                        admissions_label = Label(admissions_root,
                                                 text="Accessing student data from archives.",
                                                 anchor=W,
                                                 bg="#d3d3d3",
                                                 fg="#585858",
                                                 font=("Helevetica", 10))
                        admissions_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(15, 15), sticky=W)
                        # Student details
                        # Students first name
                        admissions_firstname_label = Label(admissions_root,
                                                           text="Student's First Name:",
                                                           bg="#d3d3d3")
                        admissions_firstname_label.grid(row=1, column=0, padx=10, sticky=W)
                        firstname_var = StringVar()
                        firstname_var.set(data_tuple[1])
                        admissions_firstname_input = Entry(admissions_root,
                                                           width=30,
                                                           font=11,
                                                           bg="#d3d3d3",
                                                           borderwidth=0,
                                                           textvariable=firstname_var,
                                                           state="readonly")
                        admissions_firstname_input.grid(row=1, column=1, padx=15, sticky=W)
                        # Student's last name
                        admissions_lastname_label = Label(admissions_root,
                                                          text="Student's Last Name:",
                                                          bg="#d3d3d3")
                        admissions_lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
                        lastname_var = StringVar()
                        lastname_var.set(data_tuple[2])
                        admissions_lastname_input = Entry(admissions_root,
                                                          width=30,
                                                          font=11,
                                                          bg="#d3d3d3",
                                                          borderwidth=0,
                                                          textvariable=lastname_var,
                                                          state="readonly")
                        admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

                        # Relation dropdown menu
                        guardian_relation = StringVar()
                        guardian_relation.set(data_tuple[3])
                        admissions_guardian_relation_label = Label(admissions_root,
                                                                   text="Guardian Relation:",
                                                                   bg="#d3d3d3")
                        admissions_guardian_relation_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
                        admissions_relation_label = Entry(admissions_root,
                                                          font=11,
                                                          bg="#d3d3d3",
                                                          borderwidth=0,
                                                          textvariable=guardian_relation,
                                                          state="readonly")
                        admissions_relation_label.grid(row=3, column=1, padx=14, pady=10, sticky=W)

                        # Guardian name input
                        admissions_guardian_name_label = Label(admissions_root,
                                                               text=f"{guardian_relation.get()} Full Name:",
                                                               bg="#d3d3d3")
                        admissions_guardian_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
                        guardianname_var = StringVar()
                        guardianname_var.set(data_tuple[4])
                        admissions_guardian_name_input = Entry(admissions_root,
                                                               width=30,
                                                               font=11,
                                                               bg="#d3d3d3",
                                                               borderwidth=0,
                                                               textvariable=guardianname_var,
                                                               state="readonly")
                        admissions_guardian_name_input.grid(row=4, column=1, padx=15, pady=10, sticky=W)

                        # Student Address
                        admissions_student_address_label = Label(admissions_root,
                                                                 text="Student Address:",
                                                                 bg="#d3d3d3")
                        admissions_student_address_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
                        address_var = StringVar()
                        address_var.set(data_tuple[5])
                        admissions_student_address_input = Entry(admissions_root,
                                                                 width=30,
                                                                 font=11,
                                                                 bg="#d3d3d3",
                                                                 borderwidth=0,
                                                                 textvariable=address_var,
                                                                 state="readonly")
                        admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

                        # Admission year frame
                        admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
                        admissions_year_frame.grid(row=6, column=0)

                        admissions_year = StringVar()
                        admissions_year.set(data_tuple[6])
                        admissions_year_label = Label(admissions_year_frame,
                                                      text="Year of \nAdmission:",
                                                      bg="#d3d3d3")
                        admissions_year_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

                        admissions_year_scroll = Entry(admissions_year_frame,
                                                       width=10,
                                                       font=11,
                                                       bg="#d3d3d3",
                                                       borderwidth=0,
                                                       textvariable=admissions_year,
                                                       state="readonly")
                        admissions_year_scroll.grid(row=0, column=1, sticky=W)

                        # Standard frame
                        admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
                        admissions_standard_frame.grid(row=6, column=1)
                        admissions_standard_label = Label(admissions_standard_frame,
                                                          text="                Admitted              \nin Standard:",
                                                          bg="#d3d3d3")
                        admissions_standard_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

                        admissions_standard = StringVar()
                        admissions_standard.set(data_tuple[7])

                        admissions_standard_scroll = Entry(admissions_standard_frame,
                                                           width=11,
                                                           font=11,
                                                           bg="#d3d3d3",
                                                           borderwidth=0,
                                                           textvariable=admissions_standard,
                                                           state="readonly")
                        admissions_standard_scroll.grid(row=0, column=1, sticky=W)

                        # Branch Frame
                        admissions_branch_label = Label(admissions_root,
                                                        text="Branch:",
                                                        bg="#d3d3d3")
                        admissions_branch_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

                        admissions_branch = StringVar()
                        admissions_branch.set(data_tuple[8])

                        admissions_branch_scroll = Entry(admissions_root,
                                                         font=11,
                                                         bg="#d3d3d3",
                                                         borderwidth=0,
                                                         textvariable=admissions_branch,
                                                         state="readonly")
                        admissions_branch_scroll.grid(row=7, column=1, padx=14, pady=10, sticky=W)

                        # parents mobile number
                        admissions_parent_number_label = Label(admissions_root,
                                                               text="Guardian Phone Number:",
                                                               bg="#d3d3d3")
                        admissions_parent_number_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
                        parent_var = IntVar()
                        parent_var.set(data_tuple[9])
                        admissions_parent_number_input = Entry(admissions_root,
                                                               width=30,
                                                               font=11,
                                                               bg="#d3d3d3",
                                                               borderwidth=0,
                                                               textvariable=parent_var,
                                                               state="readonly")
                        admissions_parent_number_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

                        # Student phone Number
                        admissions_student_number_label = Label(admissions_root,
                                                                text="Student Phone Number:",
                                                                bg="#d3d3d3")
                        admissions_student_number_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
                        student_var = IntVar()
                        student_var.set(data_tuple[10])
                        admissions_student_number_input = Entry(admissions_root,
                                                                width=30,
                                                                font=11,
                                                                bg="#d3d3d3",
                                                                borderwidth=0,
                                                                textvariable=student_var,
                                                                state="readonly")
                        admissions_student_number_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

                        # Guardian email address
                        admissions_guardian_email_label = Label(admissions_root,
                                                                text="Guardian Email Address:",
                                                                bg="#d3d3d3")
                        admissions_guardian_email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
                        parent_mail_var = StringVar()
                        parent_mail_var.set(data_tuple[11])
                        admissions_guardian_email_input = Entry(admissions_root,
                                                                width=30,
                                                                font=11,
                                                                bg="#d3d3d3",
                                                                borderwidth=0,
                                                                textvariable=parent_mail_var,
                                                                state="readonly")
                        admissions_guardian_email_input.grid(row=10, column=1, padx=15, pady=10, sticky=W)

                        # Student email address
                        admissions_student_email_label = Label(admissions_root,
                                                               text="Student Email Address:",
                                                               bg="#d3d3d3")
                        admissions_student_email_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
                        student_mail_var = StringVar()
                        student_mail_var.set(data_tuple[12])
                        admissions_student_email_input = Entry(admissions_root,
                                                               width=30,
                                                               font=11,
                                                               bg="#d3d3d3",
                                                               borderwidth=0,
                                                               textvariable=student_mail_var,
                                                               state="readonly")
                        admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)

                        # Submit button
                        def okay_function():
                            #access_data_root.destroy()
                            open_b.configure(bg="#67e867", activebackground="#35e035", text="Reopen", state=ACTIVE)
                            admissions_root.destroy()

                        okay_button = Button(admissions_root,
                                             text="Close",
                                             width=25,
                                             borderwidth=0,
                                             font=("Helvetica", 9),
                                             bg="#ff6565",
                                             fg="white",
                                             activeforeground="white",
                                             activebackground="#ff4f4f",
                                             command=okay_function)
                        okay_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)


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



                    open_button = Button(create_button_frame,
                                         text="Open",
                                         font=("Helvetica", 10),
                                         width=11,
                                         borderwidth=0,
                                         bg="#45b4e7",
                                         fg="white",
                                         activeforeground="white",
                                         activebackground="#1ca0dd")
                    open_button.configure(command=lambda i=data_tuple[0], open_b=open_button: access_data(i, open_b))
                    open_button.grid(row=0, column=1)

                    indexing_number += 1
                scroll_lord = output_canvas.create_window(0, 0, window=the_other_output_canvas, anchor=NW)
                output_canvas.configure(scrollregion=output_canvas.bbox("all"))

        access_batch_details_button = Button(access_all_toplevel,
                                             text="Next >",
                                             font=("Helvetica", 10),
                                             width=12,
                                             borderwidth=0,
                                             bg="#45b4e7",
                                             fg="white",
                                             activeforeground="white",
                                             activebackground="#1ca0dd",
                                             command=access_batch_details)
        access_batch_details_button.grid(row=3, columnspan=2, column=0, pady=15)




    all_proceed_button = Button(option_frame_2, text="See Batch",
                                font=("Helvetica", 10),
                                width=12,
                                borderwidth=0,
                                bg="#45b4e7",
                                fg="white",
                                activeforeground="white",
                                activebackground="#1ca0dd",
                                command=access_all)
    all_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))