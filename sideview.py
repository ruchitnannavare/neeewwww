from tkinter import *
from tkinter import messagebox
import requests
from requests import ConnectionError
import sqlite3
from sqlite3 import Error
import json
import functionsendtext
favicon = "favicon.ico"
def sideview_app():
    sideview = Toplevel()
    sideview.title("SideView™")
    sideview.geometry("300x150")
    sideview.iconbitmap(favicon)
    sideview.resizable(0, 0)
    sideview.attributes('-topmost', 'true')
    sideview.configure(background="#d3d3d3")
    update_label = Label(sideview, text="Prompt for updating student information.", font=("Helvetica", 10), fg="#585858", bg="#d3d3d3")
    update_label.grid(row=0, column=0, columnspan=2, ipadx=10, pady=(10, 5))
    student_roll_label = Label(sideview, text="Enter student's unique ID:", anchor=W, bg="#d3d3d3")
    student_roll_label.grid(row=1, column=0, padx=5, pady=5)
    student_roll_input = Entry(sideview, borderwidth=0)
    student_roll_input.grid(row=1, column=1, padx=5, pady=5)
    admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
    admissions_standard_dict = {"11 SCIENCE": "eleven_science", admissions_standard_list[1]: "twelve_science"}

    def update_data():
        update_data_buttom = Button(sideview,
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
            print(data_tuple)
            sideview.attributes('-topmost', 'false')
            admissions_root = Toplevel()
            admissions_root.geometry("496x450")
            admissions_root.resizable(0, 0)
            admissions_root.title("SideView™")
            admissions_root.iconbitmap(favicon)
            admissions_root.configure(background="#d3d3d3")
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
                                              bg="white",
                                              borderwidth=0,
                                              textvariable=lastname_var,
                                              state="readonly")
            admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

            # Relation dropdown menu

            """guardian_relation = StringVar()
            guardian_relation.set(data_tuple[3])
            admissions_guardian_relation_label = Label(admissions_root,
                                                       text="Guardian Relation:",
                                                       bg="#d3d3d3")
            admissions_guardian_relation_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
            admissions_relation_label = OptionMenu(admissions_root, guardian_relation, *admissions_parent_relation_list)
            admissions_relation_label.grid(row=3, column=1, padx=14, pady=10, sticky=W)"""

            # Guardian name input
            admissions_guardian_name_label = Label(admissions_root,
                                                   text=f"{data_tuple[3]} Full Name:",
                                                   bg="#d3d3d3")
            admissions_guardian_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
            guardianname_var = StringVar()
            guardianname_var.set(data_tuple[4])
            admissions_guardian_name_input = Entry(admissions_root,
                                                   width=30,
                                                   font=11,
                                                   bg="white",
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
                                                     bg="white",
                                                     borderwidth=0,
                                                     textvariable=address_var,
                                                     state="readonly")
            admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

            # Admission year frame
            """admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
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
            admissions_year_scroll.grid(row=0, column=1, sticky=W)"""

            # Standard frame
            """admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
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
            admissions_branch_scroll.grid(row=7, column=1, padx=14, pady=10, sticky=EW)"""

            # parents cid number
            parent_cid_label = Label(admissions_root,
                                     text="Guardian UniCom ID:",
                                     bg="#d3d3d3")
            parent_cid_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
            parent_var = IntVar()
            parent_var.set(data_tuple[13])
            parent_cid_input = Entry(admissions_root,
                                     width=30,
                                     font=11,
                                     bg="white",
                                     borderwidth=0,
                                     textvariable=parent_var)
            parent_cid_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

            # Student cid Number
            student_cid_label = Label(admissions_root,
                                      text="Student UniCom ID:",
                                      bg="#d3d3d3")
            student_cid_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
            student_var = IntVar()
            student_var.set(data_tuple[14])
            student_cid_input = Entry(admissions_root,
                                      width=30,
                                      font=11,
                                      bg="white",
                                      borderwidth=0,
                                      textvariable=student_var)
            student_cid_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

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
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=student_mail_var,
                                                   state="readonly")
            admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)

            # Functions for checking admission details
            def check_admission_details():
                input_list = [admissions_firstname_input, admissions_lastname_input, admissions_guardian_name_input,
                              admissions_student_address_input, parent_cid_input,
                              student_cid_input,
                              admissions_guardian_email_input, admissions_student_email_input]
                input_label_list = [admissions_firstname_label, admissions_lastname_label, admissions_guardian_name_label,
                                    admissions_student_address_label, parent_cid_label,
                                    student_cid_label, admissions_guardian_email_label,
                                    admissions_student_email_label]
                permission = True
                for i in input_list:
                    if len(i.get()) == 0:
                        missing_text = input_label_list[input_list.index(i)].cget("text")
                        give_warning = messagebox.showerror("Blank is Empty", f"{missing_text} Can not be left empty!")
                        permission = False
                        if give_warning == "ok":
                            i.delete(0, END)
                return permission
            # Check Int and strings
            def check_int_str():
                variable_int_list = [student_cid_input, parent_cid_input]
                variable_int_list_label = [student_cid_label, parent_cid_label]
                permission = True
                for integer in variable_int_list:
                    try:
                        int(integer.get())
                    except ValueError:
                        permission = False
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
                                permission = False
                                string_error_variable = variable_str_list_label[variable_str_list.index(string)].cget(
                                    "text")
                                string_error = messagebox.showerror("Character Error",
                                                                    f"{string_error_variable} Can only contain alphabetic characters.")
                                occurance += 1
                                if string_error == "ok":
                                    string.delete(0, END)
                        if occurance >= 1:
                            break
                return permission

            # Submit button function
            def update_submit():
                global data_tuple_2
                if check_admission_details() == True and check_int_str() == True:
                    admissions_confirmation = messagebox.askyesno("Confirm Update",
                                                                  "All the details are filled in!\nClick YES to update your markOS database.",
                                                                  master=admissions_root)
                    data_tuple_2 = (str(admissions_firstname_input.get()).upper(),
                                    str(admissions_lastname_input.get()).upper(),
                                    str(admissions_guardian_name_input.get()).upper(),
                                    str(admissions_student_address_input.get()).upper(),
                                    int(parent_cid_input.get()),
                                    int(student_cid_input.get()),
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
                                    def update_given(Rollno, sfn, sln, gfn, sa, g_cid, s_cid, gea, sea):
                                        connection_name = "admission_" + str(found_list[0]) + ".db"
                                        print(connection_name)
                                        xcude = admissions_standard_dict[str(found_list[1])]
                                        print(xcude)
                                        connection = sqlite3.connect(connection_name)
                                        cursor = connection.cursor()

                                        updategiven = f"""update {xcude} set
                                                       first='%s',
                                                       last='%s',
                                                       guardian='%s',
                                                       address='%s',
                                                       g_cid='%s',
                                                       s_cid='%s',
                                                       g_em='%s',
                                                       s_em='%s'
                                                       where rollno='%s' """
                                        args = (sfn, sln, gfn, sa, g_cid, s_cid, gea, sea, Rollno)

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
                                                 data_tuple_2[7])
                                    sideview.destroy()
                                    try:
                                        name = str(str(data_tuple_2[0]).lower()).capitalize() + " " + str(str(data_tuple_2[1]).lower()).capitalize()
                                        functionsendtext.admission_successful(data_tuple_2[4], name)
                                        functionsendtext.admission_successful(data_tuple_2[5], name)
                                    except:
                                        show_error = messagebox.showerror("Error", "The admission of the ward is succefull but system had some error to process the Telegram addmission confirmation message.")
                                        if show_error == "ok":
                                            pass
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
            submit_button = Button(admissions_root,
                                   text="Submit",
                                   width=25,
                                   borderwidth=0,
                                   font=("Helvetica", 9),
                                   bg="#45b4e7",
                                   fg="white",
                                   activeforeground="white",
                                   activebackground="#1ca0dd",
                                   command=update_submit)
            submit_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)

            done_button = Button(admissions_root,
                                 text="Done",
                                 width=25,
                                 borderwidth=0,
                                 font=("Helvetica", 9),
                                 bg="#45b4e7",
                                 fg="white",
                                 activeforeground="white",
                                 activebackground="#1ca0dd",
                                 command=sideview.destroy)
            done_button.grid(row=13, column=0, padx=(14, 0), pady=10, sticky=W)

    update_button = Button(sideview,
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


    try:
        url = "https://api.telegram.org/bot1339449529%3AAAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0/getUpdates"
        dic = requests.get(url)
        new_load = json.loads(dic.content)
        result_list = new_load["result"]
        communication_id_list = []
        for dict in result_list:
            try:
                from_person = dict["message"]["from"]
                first_name = from_person["first_name"]
                try:
                    last_name = from_person["last_name"]
                except:
                    last_name = "None"
                chat_id = from_person["id"]
                data_tuple = (first_name, last_name, chat_id)
                place_holder_list = [data_tuple]
                communication_id_list = place_holder_list + communication_id_list
            except KeyError:
                pass

        print(communication_id_list)
        list_2 = [("First Name", "Last Name", "Unique ID")]
        final_list = list_2 + communication_id_list


        class Mytable:
            def __init__(self, show_test_root):
                for i in range(totalrows):
                    for j in range(totalcolumns):
                        self.e = Entry(show_test_root, width=20, fg="black", font=("Arial", 11))
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, final_list[i][j])
                        self.e.configure(state="readonly")

        try:
            totalrows = len(final_list)
            totalcolumns = len(final_list[1])
            show_chat_detail_root = Toplevel()
            show_chat_detail_root.iconbitmap(favicon)
            show_chat_detail_root.title("SideView™")
            show_chat_detail_root.resizable(0, 0)
            mt = Mytable(show_chat_detail_root)
        except IndexError:
            error_message = messagebox.showwarning("SideView™ error", "SideView™ found no new entries, please try again.")
            if error_message == "ok":
                sideview.destroy()
    except ConnectionError as e:
        show_warning = messagebox.showwarning("Not connected to the internet.", "You are not connected to the internet! Try again later.")
        if show_warning == "ok":
            sideview.destroy()

