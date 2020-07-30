from tkinter import *
from tkinter import messagebox
import datetime
import random_roll_generator
import json
import sqlite3
from sqlite3 import Error
import os.path
import promotion
favicon = "favicon.ico"
admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
admissions_standard_dict = {admissions_standard_list[0]: "eleven_science", admissions_standard_list[1]: "twelve_science"}
admissions_standard_dict_invert = {"eleven_science": admissions_standard_list[0],
                                       "twelve_science": admissions_standard_list[1]}
def new_admissions():
    admissions_root = Toplevel()
    admissions_root.geometry("496x545")
    admissions_root.resizable(0, 0)
    admissions_root.title("New Admission")
    admissions_root.iconbitmap(favicon)
    admissions_root.configure(background="#d3d3d3")




    admissions_subject_list = ["Chemistry"]
    admissions_branch_list = ["Harni", "Karelibaug"]
    admissions_year_list = []
    for year in range(0, 79):
        year_string = "20" + str(20 + year) + "-" + str(21 + year)
        admissions_year_list.append(year_string)
    admissions_parent_relation_list = ["Mother", "Father", "Guardian"]

    # Admission prompt
    admissions_label = Label(admissions_root,
                             text="Prompt for new admission, fill in the details.",
                             anchor=W,
                             bg="#d3d3d3",
                             fg="#585858",
                             font=("Helevetica", 10))
    admissions_label.grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 15), sticky=W)
    # Student details
    # Students first name
    admissions_firstname_label = Label(admissions_root,
                                  text="Student's First Name:",
                                  bg="#d3d3d3")
    admissions_firstname_label.grid(row=1, column=0, padx=10, sticky=W)
    admissions_firstname_input = Entry(admissions_root,
                                  width=30,
                                  font=(11),
                                  bg="white",
                                  borderwidth=0)
    admissions_firstname_input.grid(row=1, column=1, padx=15, sticky=W)

    # Student's last name
    admissions_lastname_label = Label(admissions_root,
                                  text="Student's Last Name:",
                                  bg="#d3d3d3")
    admissions_lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    admissions_lastname_input = Entry(admissions_root,
                                  width=30,
                                  font=(11),
                                  bg="white",
                                  borderwidth=0)
    admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

    # Relation dropdown menu
    guardian_relation = StringVar()
    guardian_relation.set("Guardian")
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
    admissions_guardian_name_input = Entry(admissions_root,
                                           width=30,
                                           font=(11),
                                           bg="white",
                                           borderwidth=0)
    admissions_guardian_name_input.grid(row=4, column=1, padx=15, pady=10, sticky=W)

    # Student Address
    admissions_student_address_label = Label(admissions_root,
                                             text="Student Address:",
                                             bg="#d3d3d3")
    admissions_student_address_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    admissions_student_address_input = Entry(admissions_root,
                                             width=30,
                                             font=(11),
                                             bg="white",
                                             borderwidth=0)
    admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

    # Admission year frame
    admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
    admissions_year_frame.grid(row=6, column=0)

    absolute_year = datetime.date.today().year
    absolute_year = str(absolute_year)
    absolute_year_0 = absolute_year[2:]
    absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
    admissions_year = StringVar()
    admissions_year.set(absolute_year_variable)
    admissions_year_label = Label(admissions_year_frame,
                                  text="Academic Year:",
                                  bg="#d3d3d3")
    admissions_year_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    admissions_year_scroll = OptionMenu(admissions_year_frame,
                                        admissions_year,
                                        *admissions_year_list,)
    admissions_year_scroll.grid(row=0, column=1, sticky=W)

    # Standard frame
    admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
    admissions_standard_frame.grid(row=6, column=1)
    admissions_standard_label = Label(admissions_standard_frame,
                                  text="                              Standard:",
                                  bg="#d3d3d3")
    admissions_standard_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

    admissions_standard = StringVar()
    admissions_standard.set(admissions_standard_list[0])

    admissions_standard_scroll = OptionMenu(admissions_standard_frame,
                                        admissions_standard,
                                        *admissions_standard_list,)
    admissions_standard_scroll.grid(row=0, column=1, sticky=W)

    # Branch Frame
    admissions_branch_label = Label(admissions_root,
                                      text="Branch:",
                                      bg="#d3d3d3")
    admissions_branch_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

    admissions_branch = StringVar()
    admissions_branch.set(admissions_branch_list[0])

    admissions_branch_scroll = OptionMenu(admissions_root,
                                            admissions_branch,
                                            *admissions_branch_list, )
    admissions_branch_scroll.grid(row=7, column=1,  padx=14, pady=10, sticky=EW)

    # parents mobile number
    admissions_parent_number_label = Label(admissions_root,
                                           text="Guardian Phone Number:",
                                           bg="#d3d3d3")
    admissions_parent_number_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
    admissions_parent_number_input = Entry(admissions_root,
                                           width=30,
                                           font=(11),
                                           bg="white",
                                           borderwidth=0)
    admissions_parent_number_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

    # Student phone Number
    admissions_student_number_label = Label(admissions_root,
                                            text="Student Phone Number:",
                                            bg="#d3d3d3")
    admissions_student_number_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
    admissions_student_number_input = Entry(admissions_root,
                                            width=30,
                                            font=11,
                                            bg="white",
                                            borderwidth=0)
    admissions_student_number_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

    # Guardian email address
    admissions_guardian_email_label = Label(admissions_root,
                                            text="Guardian Email Address:",
                                            bg="#d3d3d3")
    admissions_guardian_email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
    admissions_guardian_email_input = Entry(admissions_root,
                                            width=30,
                                            font=11,
                                            bg="white",
                                            borderwidth=0)
    admissions_guardian_email_input.grid(row=10, column=1, padx=15, pady=10, sticky=W)

    # Student email address
    admissions_student_email_label = Label(admissions_root,
                                           text="Student Email Address:",
                                           bg="#d3d3d3")
    admissions_student_email_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
    admissions_student_email_input = Entry(admissions_root,
                                           width=30,
                                           font=11,
                                           bg="white",
                                           borderwidth=0)
    admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)

    # Functions for checking admission details
    def check_admission_details():
        input_list = [admissions_firstname_input, admissions_lastname_input, admissions_guardian_name_input, admissions_student_address_input, admissions_parent_number_input, admissions_student_number_input, admissions_guardian_email_input, admissions_student_email_input]
        input_label_list = [admissions_firstname_label, admissions_lastname_label, admissions_guardian_name_label, admissions_student_address_label, admissions_parent_number_label, admissions_student_number_label, admissions_guardian_email_label, admissions_student_email_label]
        permission = True
        for i in input_list:
            if len(i.get()) == 0:
                permission = False
                admissions_root.attributes('-topmost', 'true')
                missing_text = input_label_list[input_list.index(i)].cget("text")
                give_warning = messagebox.showerror("Blank is Empty", f"{missing_text} Can not be left empty!")
                if give_warning == "ok":
                    i.delete(0, END)
                    break
        return permission

    # Check Int and strings
    def check_int_str():
        variable_int_list = [admissions_student_number_input, admissions_parent_number_input]
        variable_int_list_label = [admissions_student_number_label, admissions_parent_number_label]
        permission = True
        for integer in variable_int_list:
            try:
                int(integer.get())
            except ValueError:
                permission = False
                integer_error_variable = variable_int_list_label[variable_int_list.index(integer)].cget("text")
                integer_error = messagebox.showerror("Number Error", f"{integer_error_variable} Can only contain numbers!")
                admissions_root.attributes('-topmost', 'true')
                if integer_error == "ok":
                    integer.delete(0, END)

        variable_str_list = [admissions_firstname_input, admissions_lastname_input, admissions_guardian_name_input]
        variable_str_list_label = [admissions_firstname_label, admissions_lastname_label, admissions_guardian_name_label]
        for string in variable_str_list:
            string_list = list(string.get())
            occurance = 0
            for element in string_list:
                for num in list(range(0, 10)):
                    if str(num) == element:
                        string_error_variable = variable_str_list_label[variable_str_list.index(string)].cget("text")
                        string_error = messagebox.showerror("Character Error", f"{string_error_variable} Can only contain alphabetic characters.")
                        occurance += 1
                        admissions_root.attributes('-topmost', 'true')
                        permission = False
                        if string_error == "ok":
                            string.delete(0, END)
                if occurance >= 1:
                    break
        return permission
    # Submit button function

    def admissions_submit():
        if check_admission_details() == True and check_int_str() == True:
            admissions_root.attributes('-topmost', 'false')

            admissions_confirmation = messagebox.askyesno("Confirm Admission",
                                                          "All the details are filled in!\nClick YES to add new admission in your markOS database.",
                                                          master=admissions_root)
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

                def admission_succesfull():
                    if str(password_window_input.get()) == "1234":
                        admissions_root.attributes('-topmost', 'false')
                        mID = random_roll_generator.randon_roll_number()
                        xcude = list(mID)
                        password_window.attributes('-topmost', 'false')
                        admission_succesfull_message = messagebox.showinfo("Admission Successful!",
                                                                           f"Admission process has been succesfull.\nPlease note down {str(admissions_firstname_input.get()).capitalize()}'s Roll Number.\n{str(admissions_firstname_input.get()).capitalize()}'s roll number is  {xcude[0] + ' ' + xcude[1] + ' ' + xcude[2] + ' ' + xcude[3]}")

                        if admission_succesfull_message == "ok":
                            # Sqlite database entry
                            connection_name = "admission_" + str(admissions_year.get()) + ".db"
                            connect = sqlite3.connect(connection_name)
                            print("database connected")
                            admission_cursor = connect.cursor()

                            standard_table = f"""create table if not exists {admissions_standard_dict[str(admissions_standard.get())]}(
                                                                 rollno   text    primary key not null,
                                                                 first   text    not null,
                                                                 last   text    not null,
                                                                 gr    text    not null,
                                                                 guardian   text    not null,
                                                                 address    text    not null,
                                                                 year    text    not null,
                                                                 standard   text    not null,
                                                                 branch    text    not null,
                                                                 g_no   text    not null,
                                                                 s_no   text    not null,
                                                                 g_em   text    not null,
                                                                 s_em   text    not null,
                                                                 g_cid  text,
                                                                 s_cid  text);"""

                            admission_cursor.execute(standard_table)
                            connect.commit()
                            connect.close()
                            print("table created")

                            def insertion_operation(connect, RollNo, first_name, last_name, gr, guardian_name, address,
                                                    year, standard, branch, g_no, s_no, g_em, s_em):
                                connect_admission = sqlite3.connect(connect)
                                cursor = connect_admission.cursor()
                                args = (
                                RollNo, first_name, last_name, gr, guardian_name, address, year, standard, branch, g_no,
                                s_no, g_em,
                                s_em)
                                insert = f"""insert into {admissions_standard_dict[admissions_standard.get()]}(rollno, first, last, gr, guardian, address, year, standard, branch, g_no, s_no, g_em, s_em) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"""
                                print(insert)
                                try:

                                    cursor.execute(insert % args)
                                    connect_admission.commit()
                                    connect_admission.close()
                                    print(123456)
                                except Error as e:
                                    print(e)
                                    connect_admission.rollback()

                            insertion_operation(connection_name,
                                                str(mID)[:4],
                                                str(admissions_firstname_input.get()).upper(),
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
                            with open("student_key_data.json", "r") as json_file:
                                json_decoded = json.load(json_file)
                                json_decoded[str(mID)[:4]] = [str(admissions_year.get()), str(admissions_standard.get())]
                            with open("student_key_data.json", "w") as file:
                                json.dump(json_decoded, file)
                            admissions_root.destroy()
                            password_window.destroy()

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
                                                             command=admission_succesfull)
                password_window_confirmation_button.pack(pady=(15, 0))
            else:
                admissions_root.destroy()
    # Submit button
    admissions_submit_button = Button(admissions_root,
                                      text="Submit Details",
                                      width=25,
                                      borderwidth=0,
                                      font=("Helvetica", 9),
                                      bg="#45b4e7",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#1ca0dd",
                                      command=admissions_submit)
    admissions_submit_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)



def admissions_promote():
    promote_root = Toplevel()
    from_std = ["11 SCIENCE", "12 SCIENCE"]
    promote_root.geometry("280x170")
    promote_root.title("Promote Admissions")
    promote_root.iconbitmap(favicon)
    promote_root.resizable(0, 0)
    promote_root.configure(background="#d3d3d3")
    promote_label = Label(promote_root, text="Prompt for promoting students to next year.", font=("Helvetica", 10), fg="#585858", bg="#d3d3d3")
    promote_label.grid(row=0, column=0, columnspan=2, ipadx=10, pady=(10, 5))
    admissions_year_list = []
    for year in range(0, 20):
        year_string = "20" + str(20 + year) + "-" + str(21 + year)
        admissions_year_list.append(year_string)
    absolute_year = datetime.date.today().year
    absolute_year = str(absolute_year)
    absolute_year_0 = absolute_year[2:]
    absolute_year_variable = str(int(absolute_year) - 1) + "-" + str(int(absolute_year_0))
    absolute_year_variable_new = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
    from_year = StringVar()
    from_year.set(str(absolute_year_variable))
    to_year = StringVar()
    to_year.set(str(absolute_year_variable_new))
    from_year_label = Label(promote_root, text="From academic year:", anchor=W, bg="#d3d3d3")
    from_year_label.grid(row=2, column=0, pady=(0, 5))
    from_year_input = OptionMenu(promote_root, from_year, *admissions_year_list)
    from_year_input.grid(row=2, column=1, padx=5, pady=5)
    to_year_label = Label(promote_root, text="To academic year:", anchor=W, bg="#d3d3d3")
    to_year_label.grid(row=3, column=0, pady=(0, 5))
    to_year_input = OptionMenu(promote_root, to_year, *admissions_year_list)
    to_year_input.grid(row=3, column=1, padx=5, pady=5)

    # Function to check student details.
    def promote_detail_check():
        promotion_confirmation = messagebox.askyesno("Confirm Promotion",
                                                      "All the details are filled in!\nClick YES to edit your markOS database.")
        if promotion_confirmation == True:
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

            def promotion_succesfull():
                if str(password_window_input.get()) == "1234":
                    promote_details_button.configure(state=DISABLED)
                    password_window.destroy()
                    from_data_base = "admission_" + str(from_year.get()) + ".db"
                    to_data_base = "admission_" + str(to_year.get()) + ".db"
                    if os.path.isfile(from_data_base) == True:
                        promotion_dictionary = promotion.promotion_function(from_data_base, to_data_base)
                        promotion_class_name_list = list(promotion_dictionary.keys())
                        with open("student_key_data.json", "r") as json_file:
                            json_dictionary = json.load(json_file)

                        for tablename in promotion_class_name_list:
                            for id in promotion_dictionary[tablename]:
                                dictinaire = {}
                                dictinaire[id] = [str(to_year.get()), admissions_standard_dict_invert[tablename]]
                                json_dictionary.update(dictinaire)
                                dictinaire.clear()
                        with open("student_key_data.json", "w") as json_file:
                            json.dump(json_dictionary, json_file)

                    else:
                        show_error = messagebox.showerror("Database Not found!", "The data you enetered cannot be synced to any of the existing databases, please try again.")
                        if show_error == "ok":
                            pass
                else:
                    messagewarning = messagebox.showwarning("Incorrect Password",
                                                            "The Password you have entered is incorrect,\nplease try again.")
                    if messagewarning == "ok":
                        password_window_input.delete(0, END)

            password_window_confirmation_button = Button(password_window,
                                                         text="Promote",
                                                         font=("Helvetica", 9),
                                                         width=15,
                                                         borderwidth=0,
                                                         bg="#67e867",
                                                         fg="white",
                                                         activeforeground="white",
                                                         activebackground="#35e035",
                                                         command=promotion_succesfull)
            password_window_confirmation_button.pack(pady=(15, 0))
        else:
            promote_root.destroy()






    promote_details_button = Button(promote_root,
                                    text="Proceed",
                                    font=("Helvetica", 10),
                                    width=12,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=promote_detail_check)
    promote_details_button.grid(row=4, columnspan=2, padx=5, pady=5)



def delete_admission():
    delete_admisson_root = Toplevel()
    delete_admisson_root.geometry("300x120")
    delete_admisson_root.title("Delete an Admission")
    delete_admisson_root.iconbitmap(favicon)
    delete_admisson_root.resizable(0, 0)
    delete_admisson_root.configure(background="#d3d3d3")
    delete_label = Label(delete_admisson_root, text="Prompt for DELETING student admission.", font=("Helvetica", 10), fg="#585858", bg="#d3d3d3")
    delete_label.grid(row=0, column=0, columnspan=2, ipadx=10, pady=(10, 5))
    student_roll_label = Label(delete_admisson_root, text="Enter student's unique ID:", anchor=W, bg="#d3d3d3")
    student_roll_label.grid(row=1, column=0, padx=5, pady=5)
    student_roll_input = Entry(delete_admisson_root, borderwidth=0)
    student_roll_input.grid(row=1, column=1, padx=5, pady=5)




    admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
    admissions_standard_dict = {"11 SCIENCE": "eleven_science", "12 SCIENCE": "twelve_science"}

    def access_data():
        access_data_button.configure(state=DISABLED)
        unique_id = str(student_roll_input.get()).upper()
        unique_id_0 = unique_id
        with open("student_key_data.json", "r") as file:
            try:
                dictionary = json.load(file)
                found_list = dictionary[unique_id]
                delete_admisson_root.attributes('-topmost', 'false')
                permission = True
            except KeyError:
                error_message = messagebox.showerror("Student Not found!",
                                                     "The mID unique key you entered isn't assigned to anyone yet.")
                if error_message == "ok":
                    pass
                delete_admisson_root.attributes('-topmost', 'true')
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
            admissions_root.title("Delete Admission")
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
                                     text="Prompt for deleting student records, check the filled details.",
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
                                                   font=11,
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=student_mail_var)
            admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)

            # Submit button
            def delete_permenantly_function():
                delete_confirmation = messagebox.showwarning("Confirm Delete",
                                                              "All the details in place!\nThis action will delete student record from your markOS database for THIS academic year.\nYou will still find a copy of record in the year in which the admission was given.")

                if delete_confirmation == "ok":
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
                    password_window_input = Entry(password_window, borderwidth=0, show="*", width=25,
                                                  font=("Times", 9, "bold"))
                    password_window_input.pack(pady=(15, 0))
                    def delete_successfull():
                        print(password_window_input.get())
                        if str(password_window_input.get()) == "1234":
                            connection_name = "admission_" + str(found_list[0]) + ".db"
                            print(connection_name)
                            connection = sqlite3.connect(connection_name)
                            cursor = connection.cursor()
                            xcude = admissions_standard_dict[str(found_list[1])]
                            print(xcude)
                            deletegiven = f"delete from {xcude} where rollno='%s'"
                            args = (unique_id)
                            deleteto = deletegiven % args

                            try:
                                cursor.execute(deleteto)
                                print(deleteto)
                                connection.commit()
                                delete_successfull_info = messagebox.showinfo("Delete Successful",
                                                                              "Deletion process hass been successful!",
                                                                              master=delete_admisson_root)

                                if delete_successfull_info == "ok":
                                    delete_admisson_root.destroy()
                                    admissions_root.destroy()
                                    password_window.destroy()
                                with open("student_key_data.json", "r") as file:
                                    dictionary_0 = json.load(file)
                                    print(unique_id_0)
                                    del dictionary_0[unique_id_0]
                                with open("student_key_data.json", "w") as file:
                                    json.dump(dictionary_0, file)
                                out = "deleted"
                            except Error as e:
                                show_error = messagebox.showerror("Error!", "There has been some error please try again.")
                                print(e)
                                connection.rollback()
                                if show_error == "ok":
                                    admissions_root.destroy()
                                    password_window.destroy()
                                    delete_admisson_root.wm_attributes('-topmost', 'true')
                                    delete_admissions_button.configure(state=ACTIVE)
                                out = e

                            return out
                            cursor.close()
                            connection.close()

                        else:
                            messagewarning = messagebox.showwarning("Incorrect Password",
                                                                    "The Password you have entered is incorrect,\nplease try again.")
                            if messagewarning == "ok":
                                password_window_input.delete(0, END)
                    print(100)

                    password_window_confirmation_button = Button(password_window,
                                                                 text="Delete Admission",
                                                                 font=("Helvetica", 9),
                                                                 width=15,
                                                                 borderwidth=0,
                                                                 bg="#ff6565",
                                                                 fg="white",
                                                                 activeforeground="white",
                                                                 activebackground="#ff4f4f",
                                                                 command=delete_successfull)
                    password_window_confirmation_button.pack(pady=(15, 0))
                else:
                    admissions_root.destroy()
                    delete_admisson_root.destroy()

            delete_permanently_button = Button(admissions_root,
                                               text="Delete Permanently",
                                               width=25,
                                               borderwidth=0,
                                               font=("Helvetica", 9),
                                               bg="#ff6565",
                                               fg="white",
                                               activeforeground="white",
                                               activebackground="#ff4f4f",
                                               command=delete_permenantly_function)
            delete_permanently_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)

    access_data_button = Button(delete_admisson_root,
                                text="Enter",
                                font=("Helvetica", 10),
                                width=15,
                                borderwidth=0,
                                bg="#ff6565",
                                fg="white",
                                activeforeground="white",
                                activebackground="#ff4f4f",
                                command=access_data)
    access_data_button.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))



    delete_admissions_button = Button(delete_admisson_root,
                                      text="Delete Admission",
                                      font=("Helvetica", 10),
                                      width=15,
                                      borderwidth=0,
                                      bg="#ff6565",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#ff4f4f",
                                      command=access_data)
    delete_admissions_button.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))




    delete_admisson_root.mainloop()

