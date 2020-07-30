from tkinter import *
from tkinter.scrolledtext import ScrolledText
import datetime
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import json
import os.path
import globalvariables
favicon = "favicon.ico"

def new_test():
    new_test_root = Toplevel()
    new_test_root.geometry("400x460")
    new_test_root.resizable(0, 0)
    new_test_root.title("New Test")
    new_test_root.iconbitmap(favicon)
    new_test_root.configure(background="#d3d3d3")
    todays_date = datetime.date.today()
    todays_date = str(todays_date)[8:11]
    print(todays_date)
    # Lists for the test prompt
    new_test_chapter_number_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                    "15", "16", "17"]
    new_test_sub_list = ["Chemistry"]
    new_test_sub_dict = {"Chemistry": "chem"}
    new_test_date_month = datetime.date.today().month
    new_test_month_list_counter = new_test_date_month - 1
    new_test_month_dict = {"January": "jan", "February": "feb", "March": "mar", "April": "apr", "May": "may", "June": "jun",
                           "July": "jul", "August": "aug", "September": "sep", "October": "oct", "November": "nov",
                           "December": "dec"}
    new_test_month_list = list(new_test_month_dict.keys())
    new_test_standard_list = ["11 SCIENCE", "12 SCIENCE"]
    new_test_semester_list = ["SEM 01", "SEM 02"]

    new_test_standard_dict = {new_test_standard_list[0]: "eleven_science", new_test_standard_list[1]: "twelve_science"}
    new_test_semester_dict = {new_test_semester_list[0]: "01", new_test_semester_list[1]: "02"}
    new_test_number_of_days_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                                    "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                                    "29", "30", "31"]

    # Test prompt
    # Test prompt label
    new_test_label = Label(new_test_root, text="Prompt for new test score entry into your markOS database.",
                           font=("Helvetica", 10),
                           bg="#d3d3d3",
                           fg="#585858")
    new_test_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=(10, 17))

    # Academic year label
    new_test_academic_year_label = Label(new_test_root, text="Academic Year:",
                                         font=("Helvetica", 10),
                                         bg="#d3d3d3")
    new_test_academic_year_label.grid(row=1, column=0, sticky=W, padx=16, pady=(10, 5))

    academic_year_list = []
    for year in range(0, 79):
        year_string = "20" + str(20 + year) + "-" + str(21 + year)
        academic_year_list.append(year_string)
    absolute_year = datetime.date.today().year
    absolute_year = str(absolute_year)
    absolute_year_0 = absolute_year[2:]
    absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
    new_test_academic_year = StringVar()
    new_test_academic_year.set(absolute_year_variable)
    new_test_academic_year_scroll = OptionMenu(new_test_root,
                                               new_test_academic_year,
                                               *academic_year_list)
    new_test_academic_year_scroll.grid(row=1, column=1, sticky=EW, padx=16, pady=(10, 5))

    # Select standard option menu
    new_test_standard_label = Label(new_test_root,
                                    text="Standard:",
                                    bg="#d3d3d3")
    new_test_standard_label.grid(row=2, column=0, sticky=W, padx=16, pady=5)

    new_test_standard = StringVar()
    new_test_standard.set(new_test_standard_list[0])
    new_test_standard_scroll = OptionMenu(new_test_root,
                                          new_test_standard,
                                          *new_test_standard_list)
    new_test_standard_scroll.grid(row=2, column=1, sticky=EW, padx=16)

    # Other test details
    # Score out of
    new_test_max_score_label = Label(new_test_root,
                                     text="Maximum Score:",
                                     bg="#d3d3d3")
    new_test_max_score_label.grid(row=3, column=0, sticky=W, padx=16, pady=(35, 5))

    new_test_max_score_input = Entry(new_test_root,
                                     borderwidth=0,
                                     font=11,
                                     width=14)
    new_test_max_score_input.grid(row=3, column=1, sticky=EW, padx=16, pady=(35, 5))
    # Chapter Number
    new_test_chapter_label = Label(new_test_root,
                                   text="Chapter No:",
                                   bg="#d3d3d3")
    new_test_chapter_label.grid(row=4, column=0, sticky=W, padx=16, pady=5)

    new_test_chapter = StringVar()
    new_test_chapter.set(new_test_chapter_number_list[0])

    new_test_chapter_scroll = OptionMenu(new_test_root,
                                         new_test_chapter,
                                         *new_test_chapter_number_list)
    new_test_chapter_scroll.grid(row=4, column=1, sticky=EW, padx=16, pady=5)

    # Semester Name
    new_test_semester_label = Label(new_test_root,
                                    text="Semester:",
                                    bg="#d3d3d3")
    new_test_semester_label.grid(row=5, column=0, sticky=W, padx=16, pady=5)

    new_test_semester = StringVar()
    new_test_semester.set(new_test_semester_list[0])

    new_test_semester_scroll = OptionMenu(new_test_root,
                                          new_test_semester,
                                          *new_test_semester_list)
    new_test_semester_scroll.grid(row=5, column=1, sticky=EW, padx=16, pady=5)

    # Subject Select
    new_test_subject_label = Label(new_test_root,
                                   text="Subject:",
                                   bg="#d3d3d3")
    new_test_subject_label.grid(row=6, column=0, sticky=W, padx=16, pady=5)

    new_test_subject = StringVar()
    new_test_subject.set(new_test_sub_list[0])

    new_test_subject_scroll = OptionMenu(new_test_root,
                                         new_test_subject,
                                         *new_test_sub_list)
    new_test_subject_scroll.grid(row=6, column=1, sticky=EW, padx=16, pady=5)

    # Date Select
    new_test_date_label = Label(new_test_root,
                                text="Date:",
                                bg="#d3d3d3")
    new_test_date_label.grid(row=7, column=0, sticky=W, padx=16, pady=5)

    new_test_date = StringVar()
    new_test_date.set(todays_date)

    new_test_date_scroll = OptionMenu(new_test_root,
                                      new_test_date,
                                      *new_test_number_of_days_list)
    new_test_date_scroll.grid(row=7, column=1, sticky=EW, padx=16, pady=5)

    # Date Select
    new_test_month_label = Label(new_test_root,
                                 text="Month:",
                                 bg="#d3d3d3")
    new_test_month_label.grid(row=8, column=0, sticky=W, padx=16, pady=5)

    new_test_month = StringVar()
    new_test_month.set(new_test_month_list[new_test_date_month - 1])

    new_test_month_scroll = OptionMenu(new_test_root,
                                       new_test_month,
                                       *new_test_month_list)
    new_test_month_scroll.grid(row=8, column=1, sticky=EW, padx=16, pady=5)

    # Loading it with functions
    def check_value(input, value):
        permission = True
        if float(input.get()) > value:
            new_test_root.attributes('-topmost', 'true')
            permission = False
            give_warning = messagebox.showerror("Maximum digit error", f"Maximum score cannot exceed {value}!")
            if give_warning == "ok":
                input.delete(0, END)
        return permission

    def check_length(input, value):
        permission = True
        if len(input.get()) > value:
            new_test_root.attributes('-topmost', 'true')
            permission = False
            give_warning = messagebox.showerror("Maximum digit error", "mID cannot exceed 4 digits!")
            if give_warning == "ok":
                input.delete(0, END)
        return permission

    def check_empty(input, value):
        new_test_root.attributes('-topmost', 'true')
        permission = True
        if len(input.get()) == value:
            permission = False
            give_warning = messagebox.showerror("Digit error", "Blanks cannot be left empty!")
            if give_warning == "ok":
                input.delete(0, END)
        return permission

    def check_int(input):
        permission = True
        if input.get() > 0:
            try:
                float(input.get())
            except ValueError:
                permission = False
                integer_error = messagebox.showerror("Score Error", "Test score can only contain numbers!")
                if integer_error == "ok":
                    input.delete(0, END)
        else:
            permission = False
            integer_error = messagebox.showerror("Score Error", "Maximum test score cannot be zero or less than zero!")
            if integer_error == "ok":
                input.delete(0, END)
        return permission

    def create_test():
        global test_connection, test_name
        if check_empty(new_test_max_score_input, 0) == True and check_int(new_test_max_score_input) == True and check_value(new_test_max_score_input, 999.99) == True :
            new_test_root.attributes('-topmost', 'false')
            # Test database creator
            test_connection = "Test_" + new_test_academic_year.get() + "_" + str(new_test_sub_dict[str(new_test_subject.get())]) + "_" + str(new_test_standard_dict[new_test_standard.get()]) + ".db"
            test_database_name = "Test_" + new_test_academic_year.get() + "_" + str(new_test_sub_dict[str(new_test_subject.get())]) + "_" + str(new_test_standard_dict[new_test_standard.get()])
            test_name = "CH" + str(new_test_chapter.get()) + "SEM" + str(new_test_semester_dict[str(new_test_semester.get())]) + "DATE" + str(new_test_date.get()) + new_test_month_dict[new_test_month.get()]
            print(test_name)
            connect = sqlite3.connect(test_connection)
            cursor = connect.cursor()
            create_table = f"""create table if not exists {test_name}(
                            Rollno  text    primary key     not null,
                            first   text    not null,
                            last    text    not null,
                            marks_scored    float not null,
                            max_marks   float not null,
                            percentage float not null,
                            g_cid   int not null,
                            s_cid   int not null);"""
            try:
                with open("student_test_key_data_for_standard.json", "r") as json_file:
                    test_name_repositary = json.load(json_file)
                try:
                    if len(test_name_repositary[test_database_name][new_test_month_dict[new_test_month.get()]]) == 0:
                        test_name_repositary[test_database_name][new_test_month_dict[new_test_month.get()]].append(
                            test_name)
                    else:
                        permission = True
                        for ele in test_name_repositary[test_database_name][new_test_month_dict[new_test_month.get()]]:
                            if ele == test_name:
                                permission = False
                                break
                        if permission == True:
                            test_name_repositary[test_database_name][new_test_month_dict[new_test_month.get()]].append(test_name)

                except:
                    permission_1 = False
                    """test_name_repositary[test_database_name] = {}"""
                    keylist = list(test_name_repositary.keys())
                    for ele in keylist:
                        if ele == test_database_name:
                            test_name_repositary[test_database_name][new_test_month_dict[new_test_month.get()]] = [test_name]
                            break
                        else:
                            permission_1 = True
                    if permission_1 == True:
                        test_name_repositary[test_database_name] = {}

                        test_name_repositary[test_database_name][new_test_month_dict[new_test_month.get()]] = [test_name]

                """try:
                    test_name_repositary[str(new_test_standard_dict[new_test_standard.get()])].append(test_name)
                except:
                    test_name_repositary[str(new_test_standard_dict[new_test_standard.get()])] = [test_name]
                try:
                    test_name_repositary[str(new_test_semester_dict[new_test_semester.get()])].append(test_name)
                except:
                    test_name_repositary[str(new_test_semester_dict[new_test_semester.get()])] = [test_name]
                try:
                    DATE = str(new_test_date.get()) + new_test_month_dict[new_test_month.get()]
                    test_name_repositary["DATE"] = {test_name: DATE}
                except:
                    DATE = str(new_test_date.get()) + new_test_month_dict[new_test_month.get()]
                    test_name_repositary["DATE"][test_name].update(DATE)"""
                with open("student_test_key_data_for_standard.json", "w") as json_file:
                    json.dump(test_name_repositary, json_file)
                cursor.execute(create_table)
                print("table_created")
            except Error as e:
                print(e)

            cursor.close()
            connect.close()



            score_entry = Toplevel()
            score_entry.geometry("203x200")
            score_entry.resizable(0, 0)
            score_entry.title("Enter Scores")
            score_entry.iconbitmap(favicon)
            score_entry.configure(background="#d3d3d3")
            score_entry.attributes('-topmost', 'true')
            score_entry.grab_set()
            # Entry prompt
            score_entry_label = Label(score_entry,
                                      text=f"Enter score for the test taken.\n "
                                           f" scored marks shall \n"
                                           f" not be greater than {new_test_max_score_input.get()}.",
                                      font=("Helvetica", 9),
                                      bg="#d3d3d3",
                                      fg="red")
            score_entry_label.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky=W)
            # Student ID input
            student_id = Label(score_entry,
                               text="Student mID:",
                               bg="#d3d3d3")
            student_id.grid(row=1, column=0, sticky=W, padx=5, pady=(15, 5))
            student_score = Label(score_entry,
                                  text="Obtained Score:",
                                  bg="#d3d3d3")
            student_id_input = Entry(score_entry,
                                     borderwidth=0,
                                     font=11,
                                     width=10)
            # Student marks obtained

            student_id_input.grid(row=1, column=1, sticky=EW, padx=5, pady=(15, 5))
            student_score.grid(row=2, column=0, sticky=W, padx=5, pady=(15, 5))

            student_score_input = Entry(score_entry,
                                        borderwidth=0,
                                        font=11,
                                        width=10)
            student_score_input.grid(row=2, column=1, sticky=EW, padx=5, pady=(15, 5))
            # Next and Done button functions
            def next_function():
                score_entry.attributes('-topmost', 'true')
                unique_id = str(student_id_input.get()).upper()
                with open("student_key_data.json", "r") as file:
                    try:
                        dictionary = json.load(file)
                        found_list = dictionary[unique_id]
                        permission = True
                    except KeyError:
                        error_message = messagebox.showerror("Student Not found!",
                                                             "The mID unique key you entered isn't assigned to anyone yet.")
                        if error_message == "ok":
                            pass
                        student_id_input.delete(0, END)
                        permission = False
                if check_empty(student_score_input, 0) == True and check_empty(student_id_input, 0) and check_length(student_id_input, 4) == True and check_value(student_score_input, float(new_test_max_score_input.get())) == True:
                    if  permission == True:
                        with open("student_key_data.json", "r") as file:
                            try:
                                dictionary = json.load(file)
                                found_list = dictionary[unique_id]
                                permission = True
                            except KeyError:
                                error_message = messagebox.showerror("Student Not found!",
                                                                     "The mID unique key you entered isn't assigned to anyone yet.")
                                if error_message == "ok":
                                    permission = False
                        if permission == True:
                                admission_database = "admission_" + str(found_list[0]) + ".db"
                                standard_table_name = new_test_standard_dict[str(found_list[1])]

                        def retrv_det(rollcall, admin_database, std):
                            aconn = sqlite3.connect(admin_database)
                            curse = aconn.cursor()
                            retrv_comm = "select first,last,s_cid,g_cid from {0} where rollno='{1}' ".format(std, rollcall)
                            try:
                                curse.execute(retrv_comm)
                                row = curse.fetchone()
                                print(row)
                            except Error as e:
                                print(e)
                            return row
                            aconn.close()
                            curse.close()

                        def cal_percent(score, maxval):
                            if score == globalvariables.absent_value_marker:
                                return globalvariables.absent_value_marker
                            else:
                                return ((score / maxval) * 100)

                        def insertion(Rollno, marks_scored, max_marks, admin_database, std):
                            det = retrv_det(Rollno, admin_database, std)
                            percentage = cal_percent(marks_scored, max_marks)

                            connect = sqlite3.connect(test_connection)
                            cursor = connect.cursor()
                            insert = f"""insert into {test_name}(Rollno,first,last,marks_scored,max_marks,percentage,s_cid,g_cid) values ('%s','%s','%s','%5.2f','%5.2f','%5.2f','%s','%s')"""
                            args = (Rollno, det[0], det[1], marks_scored, max_marks, percentage, det[2], det[3])

                            try:
                                cursor.execute(insert % args)
                                connect.commit()
                                print("inserted")
                            except Error as e:
                                print(e)
                                connect.rollback()
                                out = e
                                show_warning = messagebox.askyesno("Warning!", "Entry for the given roll has already been done in the database, click YES to update marks!")
                                if show_warning == True:
                                    def update_marks(Rollno, marks_scored, max_marks, percentage):

                                        connection = sqlite3.connect(test_connection)
                                        cursor = connection.cursor()

                                        update_marks = f"""update {test_name} set
                                                    marks_scored='%5.2f',
                                                    max_marks='%5.2f',
                                                    percentage='%5.2f'
                                                    where Rollno='%s' """
                                        args = (marks_scored, max_marks, percentage, Rollno)

                                        try:
                                            cursor.execute(update_marks % args)
                                            connection.commit()
                                            out = "Done."

                                        except Error as e:
                                            connection.rollback()
                                            out = e
                                        return out
                                        cursor.close()
                                        connection.close()
                                    update_marks(Rollno, marks_scored, max_marks, percentage)
                                print(show_warning)
                                out = e
                            cursor.close()
                            connect.close()
                        insertion(str(student_id_input.get()).upper(), float(student_score_input.get()), float(new_test_max_score_input.get()), admission_database, standard_table_name)
                        print(100)
                        student_id_input.delete(0, END)
                        student_score_input.delete(0, END)
                student_id_input.icursor(0)
            # Next button
            def enter_self(self):
                next_function()
                score_entry.attributes('-topmost', 'true')

            next_button = Button(score_entry,
                                 text="Next",
                                 font=("Helvetica", 10),
                                 width=8,
                                 borderwidth=0,
                                 bg="#67e867",
                                 fg="white",
                                 activeforeground="white",
                                 activebackground="#35e035",
                                 command=next_function)
            next_button.grid(row=3, column=0, sticky=EW, padx=5, pady=(15, 5))
            score_entry.bind("<Return>", enter_self)
            # Done button
            def done_self(self):
                score_entry.destroy()
            done_button = Button(score_entry,
                                 text="Done",
                                 font=("Helvetica", 10),
                                 width=8,
                                 borderwidth=0,
                                 bg="#ff6565",
                                 fg="white",
                                 activeforeground="white",
                                 activebackground="#ff4f4f",
                                 command=score_entry.destroy)
            done_button.grid(row=3, column=1, sticky=EW, padx=5, pady=(15, 5))
            score_entry.bind("<Escape>", done_self)
            new_test_button.configure(state=DISABLED)
    # Create Test Button
    new_test_button = Button(new_test_root,
                             text="Create Test",
                             width=25,
                             borderwidth=0,
                             font=("Helvetica", 10),
                             bg="#45b4e7",
                             fg="white",
                             activeforeground="white",
                             activebackground="#1ca0dd",
                             command=create_test)
    new_test_button.grid(row=9, column=0, sticky=W, padx=16, pady=30)


def open_old_test():
    test_open = Toplevel()
    test_open.geometry("400x250")
    test_open.resizable(0, 0)
    test_open.title("Open Old Test")
    test_open.iconbitmap(favicon)
    test_open.configure(background="#d3d3d3")
    new_test_standard_list = ["11 SCIENCE", "12 SCIENCE"]
    new_test_standard_dict = {new_test_standard_list[0]: "eleven_science", new_test_standard_list[1]: "twelve_science"}
    open_test_sub_list = ["Chemistry"]
    open_test_sub_dict = {"Chemistry": "chem"}
    academic_year_list = []
    for year in range(0, 79):
        year_string = "20" + str(20 + year) + "-" + str(21 + year)
        academic_year_list.append(year_string)

    test_open_prompt_label = Label(test_open, text="Prompt for opening an old test from your markOS database.",
                            font=("Helvetica", 10),
                            bg="#d3d3d3",
                            fg="#585858")
    test_open_prompt_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=(10, 17))

    test_open_standard_label = Label(test_open,
                                     text="Standard:",
                                     bg="#d3d3d3")
    test_open_standard_label.grid(row=1, column=0, sticky=W, padx=16, pady=5)

    test_open_standard = StringVar()
    test_open_standard.set(new_test_standard_list[0])

    test_open_standard_scroll = OptionMenu(test_open,
                                           test_open_standard,
                                           *new_test_standard_list)
    test_open_standard_scroll.grid(row=1, column=1, sticky=EW, padx=16)

    absolute_year = datetime.date.today().year
    absolute_year = str(absolute_year)
    absolute_year_0 = absolute_year[2:]
    absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
    admissions_year = StringVar()
    admissions_year.set(absolute_year_variable)
    admissions_year_label = Label(test_open,
                                  text="Academic Year:",
                                  bg="#d3d3d3")
    admissions_year_label.grid(row=2, column=0, sticky=W, padx=16, pady=5)

    admissions_year_scroll = OptionMenu(test_open,
                                        admissions_year,
                                        *academic_year_list)
    admissions_year_scroll.grid(row=2, column=1, sticky=EW, padx=16, pady=5)

    subject_var = StringVar()
    subject_var.set(open_test_sub_list[0])

    subject_label = Label(test_open,
                          text="Subject:",
                          bg="#d3d3d3")
    subject_label.grid(row=3, column=0, sticky=W, padx=16, pady=5)

    subject_scroll = OptionMenu(test_open,
                                subject_var,
                                *open_test_sub_list)
    subject_scroll.grid(row=3, column=1, sticky=EW, padx=16, pady=5)

    def call_test():
        test_open_prompt_label.configure(text="Please select the test to open.")
        admissions_year_label.destroy()
        admissions_year_scroll.destroy()
        test_open_standard_label.destroy()
        test_open_standard_scroll.destroy()
        subject_label.destroy()
        subject_scroll.destroy()
        test_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[subject_var.get()] + "_" + str(new_test_standard_dict[test_open_standard.get()]) + ".db"
        if os.path.isfile(test_name) == True:
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
            test_name_label = Label(test_open,
                                    text="Test Name:",
                                    bg="#d3d3d3")
            test_name_label.grid(row=1, column=0, sticky=W, padx=16, pady=5)

            test_name_var = StringVar()
            test_name_var.set("Select the test you want to see.")
            test_name_scroll = OptionMenu(test_open,
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
                    rows = e
                    print(e)
                rows = row + rowss

                return rows

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
                show_test_root.geometry("1122x200")

                output_frame = Frame(show_test_root)
                output_frame.pack(expand=True, fill=BOTH)
                output_canvas = Canvas(output_frame, height=200, scrollregion=(0, 0, 10000, 10000))

                v = Scrollbar(output_frame, orient=VERTICAL)
                v.pack(side=RIGHT, fill=Y)
                v.config(command=output_canvas.yview)
                output_canvas.configure(yscrollcommand=v.set)
                output_canvas.pack(side=LEFT, expand=True, fill=BOTH)

                the_other_output_canvas = Canvas(output_canvas, width=948)
                the_other_output_canvas.pack(side=LEFT)
                output_canvas.bind_all('<MouseWheel>',
                                       lambda event: output_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

                show_test_root.title(test_name_var.get())
                show_test_root.iconbitmap(favicon)
                show_test_root.resizable(0, 0)
                mt = Mytable(the_other_output_canvas)
                scroll_lord = output_canvas.create_window(0, 0, window=the_other_output_canvas, anchor=NW)
                output_canvas.configure(scrollregion=output_canvas.bbox("all"))

            open_old_test_old_test_button.configure(text="See Test", command=show_table)
        else:
            show_error = messagebox.showerror("Data does not exist!", "No such test has been created!")
            if show_error == "ok":
                test_open.destroy()
    open_old_test_old_test_button = Button(test_open,
                                           text="Show Test",
                                           font=("Helvetica", 10),
                                           width=12,
                                           borderwidth=0,
                                           bg="#45b4e7",
                                           fg="white",
                                           activeforeground="white",
                                           activebackground="#1ca0dd",
                                           command=call_test)
    open_old_test_old_test_button.grid(row=4, column=0, sticky=EW, padx=16, pady=(30, 0))

