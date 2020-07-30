from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import sqlite3
from sqlite3 import Error
import datetime
import os
import json
from telegram import TelegramError
from requests import ConnectionError
import matplotlib.pyplot as plt
import pandas as pd
import globalvariables
import functionsendtext
favicon = "favicon.ico"
result_function_date_month = datetime.date.today().month
result_function_date_month_list_counter = result_function_date_month - 1
result_function_date_month_dict = {"January": "jan", "February": "feb", "March": "mar", "April": "apr", "May": "may", "June": "jun",
                       "July": "jul", "August": "aug", "September": "sep", "October": "oct", "November": "nov",
                       "December": "dec"}
result_function_date_month_list = list(result_function_date_month_dict.keys())
quarterly_list = [['May', 'June', 'July'],
                  ['June', 'July', 'August'],
                  ['July', 'August', 'September'],
                  ['August', 'September', 'October'],
                  ['September', 'October', 'November'],
                  ['October', 'November', 'December'],
                  ['November', 'December', 'January'],
                  ['December', 'January', 'February'],
                  ['January', 'February', 'March'],
                  ['February', 'March', 'April']]

def send_result_data_function():
    send_result_toplevel = Toplevel()
    send_result_toplevel.title("markOS™ Current Year Data.")
    send_result_toplevel.geometry("380x260")
    send_result_toplevel.iconbitmap(favicon)
    send_result_toplevel.resizable(0, 0)
    send_result_toplevel.attributes('-topmost', 'true')
    send_result_toplevel.configure(background="#d3d3d3")

    send_result_label = Label(send_result_toplevel, text="Select one method to see current year data.", bg="#d3d3d3", fg="#585858", font=(("Helvetica"), 10))
    send_result_label.pack(anchor=W, padx=10, pady=(10, 15))

    option_frame_1 = Frame(send_result_toplevel, bg="#bababa", height=100, width=350)
    option_frame_1.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_1.propagate(False)
    empty_label = Label(option_frame_1, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_one_label = Label(option_frame_1, text="Send for One Month", font=("Helvetica", 18), fg="#585858", bg="#bababa")
    send_one_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_one_instruction = Label(option_frame_1, text="Send Test Data for month of test.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    send_one_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def send_one_month_result():
        send_result_toplevel.destroy()
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
        if datetime.date.today().month >= globalvariables.new_academic_year_month_stopper:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
        else:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(int(absolute_year) - 1) + "-" + str(int(absolute_year_0))
        academic_year_list.append(absolute_year_variable)
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

        month_var = StringVar()
        month_var.set(result_function_date_month_list[result_function_date_month_list_counter])

        month_label = Label(test_open,
                            text="Month:",
                            bg="#d3d3d3")
        month_label.grid(row=4, column=0, sticky=W, padx=16, pady=5)

        month_scroll = OptionMenu(test_open,
                                  month_var,
                                  *result_function_date_month_list)
        month_scroll.grid(row=4, column=1, sticky=EW, padx=16, pady=5)

        def call_test():
            test_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[subject_var.get()] + "_" + str(new_test_standard_dict[test_open_standard.get()]) + ".db"
            test_database_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[subject_var.get()] + "_" + str(new_test_standard_dict[test_open_standard.get()])
            standard_name = str(new_test_standard_dict[test_open_standard.get()])
            admission_database = "admission_" + str(admissions_year.get()) + ".db"
            if os.path.isfile(test_name) == True:
                with open("student_test_key_data_for_standard.json", "r") as json_file:
                    test_name_repositary = json.load(json_file)
                try:
                    target_month_list = test_name_repositary[test_database_name][result_function_date_month_dict[month_var.get()]]
                    test_open_prompt_label.configure(text="Please select the test to open.")
                    admissions_year_label.destroy()
                    admissions_year_scroll.destroy()
                    test_open_standard_label.destroy()
                    test_open_standard_scroll.destroy()
                    subject_label.destroy()
                    subject_scroll.destroy()
                    month_statement_label = Label(test_open,
                                                  text=f"Data displayed here belongs to the month of {month_var.get()}",
                                                  font=("Helvetica", 10),
                                                  bg="#d3d3d3")
                    month_scroll.destroy()
                    month_statement_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=16, pady=5)
                    test_name_label = Label(test_open, text="Name of Applicable Tests:", bg="#d3d3d3")
                    test_name_label.grid(row=5, column=0, sticky=W, padx=16, pady=5)

                    target_tests_var = StringVar()
                    target_tests_var.set("Check Selected Tests")

                    target_tests_scroll = OptionMenu(test_open,
                                                     target_tests_var,
                                                     *target_month_list)
                    target_tests_scroll.grid(row=5, column=1, sticky=W, padx=16, pady=5)
                    instruction_label = Label(test_open,
                                              text="Click the button below to apply",
                                              fg="#585858",
                                              bg="#d3d3d3",
                                              font=("Helvetica", 10))
                    instruction_label.grid(row=6, column=0, columnspan=2, sticky=W, padx=16, pady=(3, 1))
                    instruction_label = Label(test_open,
                                              text="details and get the results for",
                                              fg="#585858",
                                              bg="#d3d3d3",
                                              font=("Helvetica", 10))
                    instruction_label.grid(row=7, column=0, columnspan=2, sticky=W, padx=16, pady=1)
                    instruction_label = Label(test_open,
                                              text="selective student.",
                                              fg="#585858",
                                              bg="#d3d3d3",
                                              font=("Helvetica", 10))
                    instruction_label.grid(row=8, column=0, columnspan=2, sticky=W, padx=16, pady=1)

                    def access_batch_details():
                        connection_name = admission_database
                        xcude = str(new_test_standard_dict[test_open_standard.get()])
                        if os.path.isfile(connection_name) == True:
                            print("done")

                            def gen_bar(table_list, database_name, student_id, first_name, last_name):

                                li = []
                                per = []
                                name = []
                                i = 0
                                connection = sqlite3.connect(database_name)
                                cursor = connection.cursor()
                                appen = "select percentage,first,last from {0} where {1}.Rollno='%s'" % student_id

                                try:
                                    for x in table_list:
                                        cursor.execute(appen.format(x, x))
                                        list_element = cursor.fetchone()
                                        if list_element == None:
                                            list_element = (0.0, first_name, last_name)
                                        li.append(list_element)
                                        print(li)
                                        i = i + 1
                                    out = li
                                except Error as e:
                                    out = e
                                    print(out)

                                for x in li:
                                    per.append(x[0])
                                    name.append(x[1] + x[2])
                                table_name_list = []

                                avg = 0
                                for percentage in per:
                                    avg += percentage
                                avg = avg / len(per)

                                for i in table_list:
                                    table_name_list.append(i[13:])
                                bar_dict = {'Tests': table_name_list, 'percentage': per}
                                df = pd.DataFrame(bar_dict)
                                print(df)

                                x = df["Tests"]
                                y = df["percentage"]
                                if avg > 74.0:
                                    plt.bar(x, y, label="Percentage scored", color="green")
                                elif ((avg > 49.0) & (avg < 75.0)):
                                    plt.bar(x, y, label="Percentage scored", color="yellow")
                                elif ((avg > 24.0) & (avg < 50.0)):
                                    plt.bar(x, y, label="Percentage scored", color="orange")
                                elif (avg == 0.0):
                                    plt.bar(x, y, label="Percentage scored", color="black")
                                elif ((avg > 0.00) & (avg < 25)):
                                    plt.bar(x, y, label="Percentage scored", color="red")

                                plt.xlabel(student_id)
                                plt.ylabel('Percentage secured')

                                avg = "{:5.2f}%".format(avg)
                                plt.title(f"Performance of {first_name} {last_name}:\n Percentage Secured:{avg}")

                                plt.legend(["Percentage Secured."])
                                plt.ylim(10, 100)

                                return plt

                            def gen_pie(test_list, test_database, sid, first_name, last_name):
                                slices = []
                                percents = []
                                cols = []
                                plod = []
                                connection = sqlite3.connect(test_database)
                                cursor = connection.cursor()
                                appen = "select percentage from {0} where {1}.Rollno='%s'" % sid
                                for element in test_list:
                                    cursor.execute(appen.format(element, element))
                                    list_element = cursor.fetchone()
                                    if list_element == None:
                                        list_element = (0.0, first_name, last_name)
                                    percents.append(list_element)
                                print(percents)
                                print(1)
                                n = 360 / len(test_list)
                                percentage_summation = []
                                for data in percents:
                                    percentage_summation.append(data[0])
                                avg = sum(percentage_summation) / len(percentage_summation)
                                for x in percents:
                                    slices.append(n)
                                    plod.append(0.025)
                                print(2)
                                print(slices)
                                for percentages in percents:
                                    if percentages[0] > 74.0:
                                        cols.append("green")
                                    elif ((percentages[0] > 49.0) & (percentages[0] < 75.0)):
                                        cols.append("yellow")
                                    elif ((percentages[0] > 24.0) & (percentages[0] < 50.0)):
                                        cols.append("orange")
                                    elif (percentages[0] == 0.0):
                                        cols.append("black")
                                    elif ((percentages[0] > 0.00) & (percentages[0] < 25)):
                                        cols.append("red")
                                table_name_list = []
                                for i in test_list:
                                    table_name_list.append(i[13:])
                                plt.pie(slices, labels=table_name_list, colors=cols, startangle=90, explode=plod,
                                        shadow=False)
                                avg = "{:5.2f}%".format(avg)
                                plt.title(f"Performance of {first_name} {last_name}:\n Percentage Secured:{avg}")

                                return plt

                            def gen_cpie(class_database, class_name, test_database, test_list):
                                global network_permission
                                network_permission = True
                                connect = sqlite3.connect(class_database)
                                curse = connect.cursor()
                                i = 0
                                try:

                                    select_cmd = "select {0}.Rollno,{1}.first,{2}.last,{3}.g_cid,{4}.s_cid from {5}".format(
                                        class_name, class_name, class_name, class_name, class_name, class_name)
                                    curse.execute(select_cmd)
                                    row = curse.fetchall()
                                    print(row)
                                    for element in row:
                                        id = element[0]
                                        out_pie = gen_pie(test_list, test_database, id, element[1], element[2])
                                        cold2 = "pie{}.png".format(i)
                                        out_pie.savefig(cold2)
                                        out_pie.clf()
                                        try:
                                            try:
                                                functionsendtext.send_pie_parent_both(cold2, element[3], element[4])
                                            except TelegramError as e:
                                                print(e)
                                                os.remove(cold2)
                                                pass
                                        except:
                                            loading_toplevel.destroy()
                                            network_permission = False
                                            show_net_error = messagebox.showwarning("No internet connection", "No internet connection, please try again later."  )
                                            if show_net_error == "ok":
                                                os.remove(cold2)
                                                test_open.destroy()
                                                return
                                        os.remove(cold2)
                                        i = i + 1
                                        print("DDDDDDDDDoneeeeeeeee")


                                except Error as e:
                                    print(e)



                            def gen_graph(class_database, class_name, test_database, test_list):
                                global network_permission
                                connect = sqlite3.connect(class_database)
                                curse = connect.cursor()

                                try:

                                    select_cmd = "select {0}.Rollno,{1}.first,{2}.last,{3}.g_cid,{4}.s_cid from {5}".format(
                                        class_name, class_name, class_name, class_name, class_name, class_name)
                                    curse.execute(select_cmd)
                                    row = curse.fetchall()
                                    i = 0
                                    for element in row:
                                        id = element[0]
                                        out = gen_bar(test_list, test_database, id, element[1], element[2])
                                        cold1 = "graph{}.png".format(i)
                                        out.savefig(cold1)
                                        out.clf()
                                        print(network_permission)
                                        if network_permission == True:
                                            try:
                                                try:
                                                    functionsendtext.send_bar_parent_both(cold1, element[3], element[4])
                                                except TelegramError:
                                                    print(TelegramError)
                                                    pass
                                            except:
                                                loading_toplevel.destroy()
                                                show_net_error = messagebox.showwarning("No internet connection", "No internet connection, please try again later."  )
                                                if show_net_error == "ok":
                                                    os.remove(cold1)
                                                    test_open.destroy()
                                                    return
                                        else:
                                            return
                                        os.remove(cold1)
                                        i = i + 1
                                        print("DDDDDDDDDoneeeeeeeee")
                                except Error as e:
                                    print(e)

                            loading_toplevel = Toplevel()
                            loading_toplevel.geometry("500x50")
                            loading_toplevel.title("Loading...")
                            loading_toplevel.iconbitmap(favicon)
                            loading_toplevel.configure(bg="#d3d3d3")
                            tell_label = Label(loading_toplevel,
                                               text="Please wait while we process the sending requests\nDo not touch the program!",
                                               bg="#d3d3d3",
                                               fg="red",
                                               font=("Helevetica", 15))
                            tell_label.pack()
                            cancel_button = Button(loading_toplevel,
                                                   text="CANCEL",
                                                   font=("Helvetica", 10),
                                                   width=15,
                                                   borderwidth=0,
                                                   bg="#ff6565",
                                                   fg="white",
                                                   activeforeground="white",
                                                   activebackground="#ff4f4f",
                                                   command=loading_toplevel.quit)
                            cancel_button.pack()
                            progress_bar = Progressbar(loading_toplevel, orient=HORIZONTAL, length=500, mode="indeterminate")
                            progress_bar.pack

                            progress_bar.start()
                            gen_cpie(connection_name, xcude, test_name, target_month_list)
                            gen_graph(connection_name, xcude, test_name, target_month_list)
                            loading_toplevel.destroy()
                            inform_success = messagebox.showinfo("Request Successful",
                                                                 "All messages has been sent succesfully!")
                            if inform_success == "ok":
                                test_open.destroy()
                    proceed_button.configure(text="Send",

                                             command=access_batch_details,
                                             bg="#67e867",
                                             fg="white",
                                             activeforeground="white",
                                             activebackground="#35e035")
                except:
                    show_warning = messagebox.showwarning("Error", "No Test has been added during this given month, please try again.")
                    if show_warning == "ok":
                        pass
                        
        proceed_button = Button(test_open,
                                text="Show Test",
                                font=("Helvetica", 10),
                                width=12,
                                borderwidth=0,
                                bg="#45b4e7",
                                fg="white",
                                activeforeground="white",
                                activebackground="#1ca0dd",
                                command=call_test)
        proceed_button.grid(row=9, column=0, sticky=EW, padx=16, pady=(10, 0))






    option_frame_1_button = Button(option_frame_1,
                                        text="One Month",
                                        font=("Helvetica", 10),
                                        width=12,
                                        borderwidth=0,
                                        bg="#45b4e7",
                                        fg="white",
                                        activeforeground="white",
                                        activebackground="#1ca0dd",
                                   command=send_one_month_result)
    option_frame_1_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(20, 10))



    option_frame_2 = Frame(send_result_toplevel, bg="#bababa", height=100, width=350)
    option_frame_2.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_2.propagate(False)
    empty_label = Label(option_frame_2, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_one_label = Label(option_frame_2, text="Send Quarterly", font=("Helvetica", 18), fg="#585858", bg="#bababa")
    send_one_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_one_instruction = Label(option_frame_2, text="Send Quarterly Data", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    send_one_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def send_three_month_result():
        send_result_toplevel.destroy()
        test_open = Toplevel()
        test_open.geometry("400x250")
        test_open.resizable(0, 0)
        test_open.title("Open Old Test")
        test_open.iconbitmap(favicon)
        test_open.configure(background="#d3d3d3")
        new_test_standard_list = ["11 SCIENCE", "12 SCIENCE"]
        new_test_standard_dict = {new_test_standard_list[0]: "eleven_science",
                                  new_test_standard_list[1]: "twelve_science"}
        open_test_sub_list = ["Chemistry"]
        open_test_sub_dict = {"Chemistry": "chem"}
        academic_year_list = []
        for year in range(0, 79):
            year_string = "20" + str(20 + year) + "-" + str(21 + year)

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
        if datetime.date.today().month >= globalvariables.new_academic_year_month_stopper:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
        else:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(int(absolute_year) - 1) + "-" + str(int(absolute_year_0))
        academic_year_list.append(absolute_year_variable)
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

        month_var = StringVar()
        month_var.set("Select Quarter")

        month_label = Label(test_open,
                            text="Month:",
                            bg="#d3d3d3")
        month_label.grid(row=4, column=0, sticky=W, padx=16, pady=5)

        month_scroll = OptionMenu(test_open,
                                  month_var,
                                  *quarterly_list)
        month_scroll.grid(row=4, column=1, sticky=EW, padx=16, pady=5)

        def call_test():
            if month_var.get() != "Select Quarter":
                test_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[subject_var.get()] + "_" + str(
                    new_test_standard_dict[test_open_standard.get()]) + ".db"
                test_database_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[
                    subject_var.get()] + "_" + str(new_test_standard_dict[test_open_standard.get()])
                admission_database = "admission_" + str(admissions_year.get()) + ".db"
                if os.path.isfile(test_name) == True:
                    with open("student_test_key_data_for_standard.json", "r") as json_file:
                        test_name_repositary = json.load(json_file)
                    try:
                        # ('June', 'July', 'August')
                        target_month_list = []
                        actual_month_var = []
                        month_var_list = list(str(str(month_var.get())[1:-1]).split(", "))
                        for month_var_ele in month_var_list:
                            actual_month_var.append(month_var_ele[1:-1])
                        print(month_var.get())
                        print(actual_month_var)
                        for month in actual_month_var:
                            try:
                                for test in test_name_repositary[test_database_name][
                                    result_function_date_month_dict[month]]:
                                    target_month_list.append(test)
                            except:
                                print(100)

                        test_open_prompt_label.configure(text="Please select the test to open.")
                        admissions_year_label.destroy()
                        admissions_year_scroll.destroy()
                        test_open_standard_label.destroy()
                        test_open_standard_scroll.destroy()
                        subject_label.destroy()
                        subject_scroll.destroy()

                        month_scroll.destroy()
                        test_name_label = Label(test_open, text="Name of Applicable Tests:", bg="#d3d3d3")
                        test_name_label.grid(row=5, column=0, sticky=W, padx=16, pady=5)

                        target_tests_var = StringVar()
                        target_tests_var.set("Check Selected Tests")

                        target_tests_scroll = OptionMenu(test_open,
                                                         target_tests_var,
                                                         *target_month_list)
                        target_tests_scroll.grid(row=5, column=1, sticky=W, padx=16, pady=5)
                        instruction_label = Label(test_open,
                                                  text="Click the button below to apply",
                                                  fg="#585858",
                                                  bg="#d3d3d3",
                                                  font=("Helvetica", 10))
                        instruction_label.grid(row=6, column=0, columnspan=2, sticky=W, padx=16, pady=(3, 1))
                        instruction_label = Label(test_open,
                                                  text="details and get the results for",
                                                  fg="#585858",
                                                  bg="#d3d3d3",
                                                  font=("Helvetica", 10))
                        instruction_label.grid(row=7, column=0, columnspan=2, sticky=W, padx=16, pady=1)
                        instruction_label = Label(test_open,
                                                  text="selective student.",
                                                  fg="#585858",
                                                  bg="#d3d3d3",
                                                  font=("Helvetica", 10))
                        instruction_label.grid(row=8, column=0, columnspan=2, sticky=W, padx=16, pady=1)

                        def access_batch_details():

                            connection_name = admission_database
                            xcude = str(new_test_standard_dict[test_open_standard.get()])
                            if os.path.isfile(connection_name) == True:
                                print("done")

                                def gen_bar(table_list, database_name, student_id, first_name, last_name):

                                    li = []
                                    per = []
                                    name = []
                                    i = 0
                                    connection = sqlite3.connect(database_name)
                                    cursor = connection.cursor()
                                    appen = "select percentage,first,last from {0} where {1}.Rollno='%s'" % student_id

                                    try:
                                        for x in table_list:
                                            cursor.execute(appen.format(x, x))
                                            list_element = cursor.fetchone()
                                            if list_element == None:
                                                list_element = (0.0, first_name, last_name)
                                            li.append(list_element)
                                            print(li)
                                            i = i + 1
                                        out = li
                                    except Error as e:
                                        out = e
                                        print(out)

                                    for x in li:
                                        per.append(x[0])
                                        name.append(x[1] + x[2])
                                    table_name_list = []

                                    avg = 0
                                    for percentage in per:
                                        avg += percentage
                                    avg = avg / len(per)

                                    for i in table_list:
                                        table_name_list.append(i[13:])
                                    bar_dict = {'Tests': table_name_list, 'percentage': per}
                                    df = pd.DataFrame(bar_dict)
                                    print(df)

                                    x = df["Tests"]
                                    y = df["percentage"]
                                    if avg > 74.0:
                                        plt.bar(x, y, label="Percentage scored", color="green")
                                    elif ((avg > 49.0) & (avg < 75.0)):
                                        plt.bar(x, y, label="Percentage scored", color="yellow")
                                    elif ((avg > 24.0) & (avg < 50.0)):
                                        plt.bar(x, y, label="Percentage scored", color="orange")
                                    elif (avg == 0.0):
                                        plt.bar(x, y, label="Percentage scored", color="black")
                                    elif ((avg > 0.00) & (avg < 25)):
                                        plt.bar(x, y, label="Percentage scored", color="red")

                                    plt.xlabel(student_id)
                                    plt.ylabel('Percentage secured')

                                    avg = "{:5.2f}%".format(avg)
                                    plt.title(f"Performance of {first_name} {last_name}:\n Percentage Secured:{avg}")

                                    plt.legend(["Percentage Secured."])
                                    plt.ylim(10, 100)

                                    return plt

                                def gen_pie(test_list, test_database, sid, first_name, last_name):
                                    slices = []
                                    percents = []
                                    cols = []
                                    plod = []
                                    connection = sqlite3.connect(test_database)
                                    cursor = connection.cursor()
                                    appen = "select percentage from {0} where {1}.Rollno='%s'" % sid
                                    for element in test_list:
                                        cursor.execute(appen.format(element, element))
                                        list_element = cursor.fetchone()
                                        if list_element == None:
                                            list_element = (0.0, first_name, last_name)
                                        percents.append(list_element)
                                    print(percents)
                                    print(1)
                                    n = 360 / len(test_list)
                                    percentage_summation = []
                                    for data in percents:
                                        percentage_summation.append(data[0])
                                    avg = sum(percentage_summation) / len(percentage_summation)
                                    for x in percents:
                                        slices.append(n)
                                        plod.append(0.025)
                                    print(2)
                                    print(slices)
                                    for percentages in percents:
                                        if percentages[0] > 74.0:
                                            cols.append("green")
                                        elif ((percentages[0] > 49.0) & (percentages[0] < 75.0)):
                                            cols.append("yellow")
                                        elif ((percentages[0] > 24.0) & (percentages[0] < 50.0)):
                                            cols.append("orange")
                                        elif (percentages[0] == 0.0):
                                            cols.append("black")
                                        elif ((percentages[0] > 0.00) & (percentages[0] < 25)):
                                            cols.append("red")
                                    table_name_list = []
                                    for i in test_list:
                                        table_name_list.append(i[13:])
                                    plt.pie(slices, labels=table_name_list, colors=cols, startangle=90, explode=plod,
                                            shadow=False)
                                    avg = "{:5.2f}%".format(avg)
                                    plt.title(f"Performance of {first_name} {last_name}:\n Percentage Secured:{avg}")

                                    return plt

                                def gen_cpie(class_database, class_name, test_database, test_list):
                                    global network_permission
                                    network_permission = True
                                    connect = sqlite3.connect(class_database)
                                    curse = connect.cursor()
                                    i = 0
                                    try:

                                        select_cmd = "select {0}.Rollno,{1}.first,{2}.last,{3}.g_cid,{4}.s_cid from {5}".format(
                                            class_name, class_name, class_name, class_name, class_name, class_name)
                                        curse.execute(select_cmd)
                                        row = curse.fetchall()
                                        print(row)

                                        for element in row:
                                            id = element[0]
                                            out_pie = gen_pie(test_list, test_database, id, element[1], element[2])
                                            cold = "pie{}.png".format(i)
                                            out_pie.savefig(cold)
                                            out_pie.clf()
                                            try:
                                                functionsendtext.send_pie_parent_both(cold, element[3], element[4])
                                            except:
                                                network_permission = False
                                                loading_toplevel.destroy()
                                                show_net_error = messagebox.showwarning("No internet connection",
                                                                                        "No internet connection, please try again later.")
                                                if show_net_error == "ok":
                                                    os.remove(cold)
                                                    test_open.destroy()
                                                    return
                                            os.remove(cold)
                                            i = i + 1
                                            print("DDDDDDDDDoneeeeeeeee")

                                    except Error as e:
                                        print(e)

                                def gen_graph(class_database, class_name, test_database, test_list):
                                    global network_permission
                                    connect = sqlite3.connect(class_database)
                                    curse = connect.cursor()

                                    try:

                                        select_cmd = "select {0}.Rollno,{1}.first,{2}.last,{3}.g_cid,{4}.s_cid from {5}".format(
                                            class_name, class_name, class_name, class_name, class_name, class_name)
                                        curse.execute(select_cmd)
                                        row = curse.fetchall()
                                        i = 0
                                        for element in row:
                                            id = element[0]
                                            out = gen_bar(test_list, test_database, id, element[1], element[2])
                                            cold = "graph{}.png".format(i)
                                            out.savefig(cold)
                                            out.clf()
                                            if network_permission == True:
                                                try:
                                                    functionsendtext.send_bar_parent_both(cold, element[3], element[4])
                                                except:
                                                    loading_toplevel.destroy()
                                                    show_net_error = messagebox.showwarning("No internet connection",
                                                                                            "No internet connection, please try again later.")
                                                    if show_net_error == "ok":
                                                        os.remove(cold)
                                                        test_open.destroy()
                                                        return
                                            os.remove(cold)
                                            i = i + 1
                                            print("DDDDDDDDDoneeeeeeeee")
                                    except Error as e:
                                        print(e)

                                loading_toplevel = Toplevel()
                                loading_toplevel.geometry("300x30")
                                loading_toplevel.configure(bg="#d3d3d3")
                                tell_label = Label(loading_toplevel,
                                                   text="Please wait while we process the sending requests\nDo not touch the program!",
                                                   bg="#d3d3d3",
                                                   fg="red",
                                                   font=("Helevetica", 15))
                                tell_label.pack()
                                gen_cpie(connection_name, xcude, test_name, target_month_list)
                                gen_graph(connection_name, xcude, test_name, target_month_list)
                                loading_toplevel.destroy()
                                inform_success = messagebox.showinfo("Request Successful",
                                                                     "All messages has been sent succesfully!")
                                if inform_success == "ok":
                                    test_open.destroy()
                            else:
                                print(1000000000000000)
                        proceed_button.configure(text="Send",
                                                 command=access_batch_details,
                                                 bg="#67e867",
                                                 fg="white",
                                                 activeforeground="white",
                                                 activebackground="#35e035")

                    except:
                        show_warning = messagebox.showwarning("Error",
                                                              "No Test has been added during this given month, please try again.")
                        if show_warning == "ok":
                            pass

            else:
                show_warning = messagebox.showwarning("Error",
                                                      "Please Select a Quarter first to display results.")
                if show_warning == "ok":
                    pass

        proceed_button = Button(test_open,
                                               text="Show Test",
                                               font=("Helvetica", 10),
                                               width=12,
                                               borderwidth=0,
                                               bg="#45b4e7",
                                               fg="white",
                                               activeforeground="white",
                                               activebackground="#1ca0dd",
                                               command=call_test)
        proceed_button.grid(row=9, column=0, sticky=EW, padx=16, pady=(10, 0))

    option_frame_2_button = Button(option_frame_2,
                                        text="Quaterly",
                                        font=("Helvetica", 10),
                                        width=12,
                                        borderwidth=0,
                                        bg="#45b4e7",
                                        fg="white",
                                        activeforeground="white",
                                        activebackground="#1ca0dd",
                                        command=send_three_month_result)
    option_frame_2_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(24, 10))


def see_result_data_function():
    see_result_toplevel = Toplevel()
    see_result_toplevel.title("Result Visualizer")
    see_result_toplevel.geometry("380x260")
    see_result_toplevel.iconbitmap(favicon)
    see_result_toplevel.resizable(0, 0)
    see_result_toplevel.attributes('-topmost', 'true')
    see_result_toplevel.configure(background="#d3d3d3")

    send_result_label = Label(see_result_toplevel, text="Select one method to see current year data.", bg="#d3d3d3",
                              fg="#585858", font=(("Helvetica"), 10))
    send_result_label.pack(anchor=W, padx=10, pady=(10, 15))

    option_frame_1 = Frame(see_result_toplevel, bg="#bababa", height=100, width=350)
    option_frame_1.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_1.propagate(False)
    empty_label = Label(option_frame_1, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_one_label = Label(option_frame_1, text="See for One Month", font=("Helvetica", 18), fg="#585858",
                           bg="#bababa")
    send_one_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_one_instruction = Label(option_frame_1, text="See Test Data for month of test.", font=("Helvetica", 9),
                                 fg="#585858", bg="#bababa")
    send_one_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def send_one_month_result():
        see_result_toplevel.destroy()
        test_open = Toplevel()
        test_open.geometry("400x250")
        test_open.resizable(0, 0)
        test_open.title("Result Visualizer")
        test_open.iconbitmap(favicon)
        test_open.configure(background="#d3d3d3")
        new_test_standard_list = ["11 SCIENCE", "12 SCIENCE"]
        new_test_standard_dict = {new_test_standard_list[0]: "eleven_science",
                                  new_test_standard_list[1]: "twelve_science"}
        open_test_sub_list = ["Chemistry"]
        open_test_sub_dict = {"Chemistry": "chem"}
        academic_year_list = []
        for year in range(0, 79):
            year_string = "20" + str(20 + year) + "-" + str(21 + year)

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
        if datetime.date.today().month >= globalvariables.new_academic_year_month_stopper:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
        else:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(int(absolute_year) - 1) + "-" + str(int(absolute_year_0))
        academic_year_list.append(absolute_year_variable)
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

        month_var = StringVar()
        month_var.set(result_function_date_month_list[result_function_date_month_list_counter])

        month_label = Label(test_open,
                            text="Month:",
                            bg="#d3d3d3")
        month_label.grid(row=4, column=0, sticky=W, padx=16, pady=5)

        month_scroll = OptionMenu(test_open,
                                  month_var,
                                  *result_function_date_month_list)
        month_scroll.grid(row=4, column=1, sticky=EW, padx=16, pady=5)

        def call_test():
            test_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[subject_var.get()] + "_" + str(
                new_test_standard_dict[test_open_standard.get()]) + ".db"
            test_database_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[
                subject_var.get()] + "_" + str(new_test_standard_dict[test_open_standard.get()])
            admission_database = "admission_" + str(admissions_year.get()) + ".db"
            print(admission_database)
            if os.path.isfile(test_name) == True:
                with open("student_test_key_data_for_standard.json", "r") as json_file:
                    test_name_repository = json.load(json_file)
                try:
                    target_month_list = test_name_repository[test_database_name][result_function_date_month_dict[month_var.get()]]
                    print(target_month_list)
                    test_open_prompt_label.configure(text="Please select the test to open.")
                    admissions_year_label.destroy()
                    admissions_year_scroll.destroy()
                    test_open_standard_label.destroy()
                    test_open_standard_scroll.destroy()
                    subject_label.destroy()
                    subject_scroll.destroy()
                    month_statement_label = Label(test_open,
                                                  text=f"Data displayed here belongs to the month of {month_var.get()}",
                                                  font=("Helvetica", 10),
                                                  bg="#d3d3d3")
                    month_scroll.destroy()
                    month_statement_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=16, pady=5)
                    test_name_label = Label(test_open, text="Name of Applicable Tests:", bg="#d3d3d3")
                    test_name_label.grid(row=5, column=0, sticky=W, padx=16, pady=5)

                    target_tests_var = StringVar()
                    target_tests_var.set("Check Selected Tests")

                    target_tests_scroll = OptionMenu(test_open,
                                                     target_tests_var,
                                                     *target_month_list)
                    target_tests_scroll.grid(row=5, column=1, sticky=W, padx=16, pady=5)
                    instruction_label = Label(test_open,
                                              text="Click the button below to apply",
                                              fg="#585858",
                                              bg="#d3d3d3",
                                              font=("Helvetica", 10))
                    instruction_label.grid(row=6, column=0, columnspan=2, sticky=W, padx=16, pady=(3, 1))
                    instruction_label = Label(test_open,
                                              text="details and get the results for",
                                              fg="#585858",
                                              bg="#d3d3d3",
                                              font=("Helvetica", 10))
                    instruction_label.grid(row=7, column=0, columnspan=2, sticky=W, padx=16, pady=1)
                    instruction_label = Label(test_open,
                                              text="selective student.",
                                              fg="#585858",
                                              bg="#d3d3d3",
                                              font=("Helvetica", 10))
                    instruction_label.grid(row=8, column=0, columnspan=2, sticky=W, padx=16, pady=1)

                    def access_batch_details():
                        connection_name = admission_database
                        xcude = str(new_test_standard_dict[test_open_standard.get()])
                        if os.path.isfile(connection_name) == True:
                            print("done")

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

                            student_list_toplevel = Toplevel()
                            student_list_toplevel.iconbitmap(favicon)
                            student_list_toplevel.resizable(0, 10)

                            output_frame = Frame(student_list_toplevel, width=1035, height=300)
                            output_frame.pack(expand=True, fill=BOTH)

                            output_canvas = Canvas(output_frame, width=1035, scrollregion=(0, 0, 10000, 10000))
                            #h = Scrollbar(output_frame, orient=HORIZONTAL, bg="green")
                            #h.pack(side=BOTTOM, fill=X)
                            v = Scrollbar(output_frame, orient=VERTICAL)
                            v.pack(side=RIGHT, fill=Y)
                            output_canvas.configure(yscrollcommand=v.set)
                            #h.config(command=output_canvas.xview)
                            v.config(command=output_canvas.yview)

                            output_canvas.pack()

                            bgcolo = "#585858"

                            the_other_output_canvas = Canvas(output_canvas, width=1035)
                            the_other_output_canvas.pack(side=TOP, anchor=N, pady=0)

                            output_canvas.bind_all('<MouseWheel>', lambda event: output_canvas.yview_scroll(
                                int(-1 * (event.delta / 120)), "units"))

                            roll_number_label = Label(the_other_output_canvas, text="mID", font=("Helvetica", 12),
                                                      bg=bgcolo, width=30, fg="white")
                            roll_number_label.grid(row=0, column=0, ipadx=5)

                            name_label = Label(the_other_output_canvas, text="First Name", font=("Helvetica", 12),
                                               bg=bgcolo, width=30, fg="white")
                            name_label.grid(row=0, column=1, ipadx=5)

                            last_name_label = Label(the_other_output_canvas, text="Last Name", font=("Helvetica", 12),
                                                    bg=bgcolo, width=30, fg="white")
                            last_name_label.grid(row=0, column=2, ipadx=5)

                            send_command_label = Label(the_other_output_canvas, text="Select", font=("Helvetica", 12),
                                                       bg=bgcolo, width=10, fg="white")
                            send_command_label.grid(row=0, column=3, sticky=EW)

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


                            def gen_bar(table_list, database_name, student_id, first_name, last_name):
                                try:
                                    plt.clf()
                                except:
                                    pass
                                li = []
                                per = []
                                name = []
                                i = 0
                                connection = sqlite3.connect(database_name)
                                cursor = connection.cursor()
                                appen = "select percentage,first,last from {0} where {1}.Rollno='%s'" % student_id

                                try:
                                    for x in table_list:
                                        cursor.execute(appen.format(x, x))
                                        list_element = cursor.fetchone()
                                        if list_element == None:
                                            list_element = (0.0, first_name, last_name)
                                        li.append(list_element)
                                        print(li)
                                        i = i + 1
                                    out = li
                                except Error as e:
                                    out = e
                                    print(out)

                                for x in li:
                                    per.append(x[0])
                                    name.append(x[1] + x[2])
                                table_name_list = []
                                avg = 0
                                for percentage in per:
                                    avg += percentage
                                avg = avg / len(per)

                                for i in table_list:
                                    table_name_list.append(i[13:])
                                bar_dict = {'Tests': table_name_list, 'percentage': per}
                                df = pd.DataFrame(bar_dict)
                                print(df)

                                x = df["Tests"]
                                y = df["percentage"]
                                if avg > 74.0:
                                    plt.bar(x, y, label="Percentage scored", color="green")
                                elif ((avg > 49.0) & (avg < 75.0)):
                                    plt.bar(x, y, label="Percentage scored", color="yellow")
                                elif ((avg > 24.0) & (avg < 50.0)):
                                    plt.bar(x, y, label="Percentage scored", color="orange")
                                elif (avg == 0.0):
                                    plt.bar(x, y, label="Percentage scored", color="black")
                                elif ((avg > 0.00) & (avg < 25)):
                                    plt.bar(x, y, label="Percentage scored", color="red")

                                plt.xlabel(student_id)
                                plt.ylabel('Percentage secured')

                                avg = "{:5.2f}%".format(avg)
                                plt.title(f"Performance of {first_name} {last_name}:\n Percentage Secured:{avg}")
                                plt.legend(["Percentage Secured."])
                                plt.ylim(10, 100)

                                plt.show()

                            def gen_pie(test_list, test_database, sid, first_name, last_name):
                                try:
                                    plt.clf()
                                except:
                                    pass
                                slices = []
                                percents = []
                                cols = []
                                plod = []
                                connection = sqlite3.connect(test_database)
                                cursor = connection.cursor()
                                appen = "select percentage from {0} where {1}.Rollno='%s'" % sid
                                for element in test_list:
                                    cursor.execute(appen.format(element, element))
                                    list_element = cursor.fetchone()
                                    if list_element == None:
                                        list_element = (0.0, first_name, last_name)
                                    percents.append(list_element)
                                print(percents)
                                print(1)
                                n = 360 / len(test_list)
                                percentage_summation = []
                                for data in percents:
                                    percentage_summation.append(data[0])
                                avg = sum(percentage_summation) / len(percentage_summation)
                                for x in percents:
                                    slices.append(n)
                                    plod.append(0.025)
                                print(2)
                                print(slices)
                                for percentages in percents:
                                    if percentages[0] > 74.0:
                                        cols.append("green")
                                    elif ((percentages[0] > 49.0) & (percentages[0] < 75.0)):
                                        cols.append("yellow")
                                    elif ((percentages[0] > 24.0) & (percentages[0] < 50.0)):
                                        cols.append("orange")
                                    elif (percentages[0] == 0.0):
                                        cols.append("black")
                                    elif ((percentages[0] > 0.00) & (percentages[0] < 25)):
                                        cols.append("red")
                                table_name_list = []
                                for i in test_list:
                                    table_name_list.append(i[13:])
                                plt.pie(slices, labels=table_name_list, colors=cols, startangle=90, explode=plod, shadow=False)
                                avg = "{:5.2f}%".format(avg)
                                plt.title(f"Performance of {first_name} {last_name}:\n Percentage Secured:{avg}")

                                plt.show()

                            def real_pie_generator(student_id, first_name, last_name, open_b):
                                open_b.configure(bg="#67e867", activebackground="#35e035", text="Opened")
                                gen_pie(target_month_list, test_name, student_id, first_name, last_name)
                            def the_real_generator(student_id, first_name, last_name, open_b):
                                open_b.configure(bg="#67e867", activebackground="#35e035", text="Opened")
                                gen_bar(target_month_list, test_name, student_id, first_name, last_name)

                            the_bogo_color = "#bababa"
                            indexing_number = 1
                            for data_tuple in reversed(sender_list):
                                create_roll_label = Label(the_other_output_canvas, text=data_tuple[0],
                                                          bg=the_bogo_color, width=31, font=9)
                                create_roll_label.grid(row=indexing_number, column=0, pady=(0, 5))

                                create_name_label = Label(the_other_output_canvas, text=data_tuple[3],
                                                          bg=the_bogo_color, width=31, font=9)
                                create_name_label.grid(row=indexing_number, column=1, pady=(0, 5))

                                create_last_name_label = Label(the_other_output_canvas, text=data_tuple[4],
                                                               bg=the_bogo_color, width=31, font=9)
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
                                                     text="Bar",
                                                     font=("Helvetica", 10),
                                                     width=11,
                                                     borderwidth=0,
                                                     bg="#45b4e7",
                                                     fg="white",
                                                     activeforeground="white",
                                                     activebackground="#1ca0dd")
                                open_button.configure(
                                    command=lambda i=data_tuple[0], j=data_tuple[3], k=data_tuple[4], open_b=open_button: the_real_generator(i, j, k, open_b))
                                open_button.grid(row=0, column=1)

                                open_pie_button = Button(create_button_frame,
                                                     text="Pie",
                                                     font=("Helvetica", 10),
                                                     width=11,
                                                     borderwidth=0,
                                                     bg="#45b4e7",
                                                     fg="white",
                                                     activeforeground="white",
                                                     activebackground="#1ca0dd")
                                open_pie_button.configure(
                                    command=lambda i=data_tuple[0], j=data_tuple[3], k=data_tuple[4],
                                                   open_b=open_pie_button: real_pie_generator(i, j, k, open_b))
                                open_pie_button.grid(row=0, column=2, padx=(2, 0))

                                indexing_number += 1
                            scroll_lord = output_canvas.create_window(0, 0, window=the_other_output_canvas, anchor=NW)
                            output_canvas.configure(scrollregion=output_canvas.bbox("all"))



                    graph_proceed_button.configure(text="Apply Details", command=access_batch_details)
                except:
                    show_warning = messagebox.showwarning("Error",
                                                          "No Test has been added during this given month, please try again.")
                    if show_warning == "ok":
                        test_open.destroy()
            else:
                show_warning = messagebox.showwarning("Error",
                                                      "No such entry exists in your markOS database.")
                if show_warning == "ok":
                    test_open.destroy()
        graph_proceed_button = Button(test_open,
                                      text="Show Test",
                                      font=("Helvetica", 10),
                                      width=12,
                                      borderwidth=0,
                                      bg="#45b4e7",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#1ca0dd",
                                      command=call_test)
        graph_proceed_button.grid(row=9, column=0, sticky=EW, padx=16, pady=(10, 0))

    option_frame_1_button = Button(option_frame_1,
                                   text="One Month",
                                   font=("Helvetica", 10),
                                   width=12,
                                   borderwidth=0,
                                   bg="#45b4e7",
                                   fg="white",
                                   activeforeground="white",
                                   activebackground="#1ca0dd",
                                   command=send_one_month_result)
    option_frame_1_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(23, 10))

    option_frame_2 = Frame(see_result_toplevel, bg="#bababa", height=100, width=350)
    option_frame_2.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_2.propagate(False)
    empty_label = Label(option_frame_2, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_one_label = Label(option_frame_2, text="See Quarterly", font=("Helvetica", 18), fg="#585858", bg="#bababa")
    send_one_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_one_instruction = Label(option_frame_2, text="See Quarterly Data", font=("Helvetica", 9), fg="#585858",
                                 bg="#bababa")
    send_one_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def send_three_month_result():
        see_result_toplevel.destroy()
        test_open = Toplevel()
        test_open.geometry("400x250")
        test_open.resizable(0, 0)
        test_open.title("Result Visualizer")
        test_open.iconbitmap(favicon)
        test_open.configure(background="#d3d3d3")
        new_test_standard_list = ["11 SCIENCE", "12 SCIENCE"]
        new_test_standard_dict = {new_test_standard_list[0]: "eleven_science",
                                  new_test_standard_list[1]: "twelve_science"}
        open_test_sub_list = ["Chemistry"]
        open_test_sub_dict = {"Chemistry": "chem"}
        academic_year_list = []
        for year in range(0, 79):
            year_string = "20" + str(20 + year) + "-" + str(21 + year)

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
        if datetime.date.today().month >= globalvariables.new_academic_year_month_stopper:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(absolute_year) + "-" + str(1 + int(absolute_year_0))
        else:
            absolute_year = str(absolute_year)
            absolute_year_0 = absolute_year[2:]
            absolute_year_variable = str(int(absolute_year) - 1) + "-" + str(int(absolute_year_0))
        academic_year_list.append(absolute_year_variable)
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

        month_var = StringVar()
        month_var.set("Select Quarter")

        month_label = Label(test_open,
                            text="Month:",
                            bg="#d3d3d3")
        month_label.grid(row=4, column=0, sticky=W, padx=16, pady=5)

        month_scroll = OptionMenu(test_open,
                                  month_var,
                                  *quarterly_list)
        month_scroll.grid(row=4, column=1, sticky=EW, padx=16, pady=5)

        def call_test():
            if month_var.get() != "Select Quarter":
                test_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[subject_var.get()] + "_" + str(
                    new_test_standard_dict[test_open_standard.get()]) + ".db"
                test_database_name = "Test_" + str(admissions_year.get()) + "_" + open_test_sub_dict[
                    subject_var.get()] + "_" + str(new_test_standard_dict[test_open_standard.get()])
                admission_database = "admission_" + str(admissions_year.get()) + ".db"
                if os.path.isfile(test_name) == True:
                    with open("student_test_key_data_for_standard.json", "r") as json_file:
                        test_name_repositary = json.load(json_file)
                    try:
                        #('June', 'July', 'August')
                        target_month_list = []
                        actual_month_var = []
                        month_var_list = list(str(str(month_var.get())[1:-1]).split(", "))
                        for month_var_ele in month_var_list:
                            actual_month_var.append(month_var_ele[1:-1])
                        print(month_var.get())
                        print(actual_month_var)
                        for month in actual_month_var:

                            try:
                                for test in test_name_repositary[test_database_name][result_function_date_month_dict[month]]:
                                    target_month_list.append(test)
                            except:
                                print(100)
                        test_open_prompt_label.configure(text="Please select the test to open.")
                        admissions_year_label.destroy()
                        admissions_year_scroll.destroy()
                        test_open_standard_label.destroy()
                        test_open_standard_scroll.destroy()
                        subject_label.destroy()
                        subject_scroll.destroy()

                        month_statement_label = Label(test_open,
                                                      text=f"Data displayed here belongs to the month of :",
                                                      font=("Helvetica", 10),
                                                      bg="#d3d3d3")
                        month_scroll.destroy()
                        month_statement_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=16, pady=5)
                        test_name_label = Label(test_open, text="Name of Applicable Tests:", bg="#d3d3d3")
                        test_name_label.grid(row=5, column=0, sticky=W, padx=16, pady=5)

                        target_tests_var = StringVar()
                        target_tests_var.set("Check Selected Tests")

                        target_tests_scroll = OptionMenu(test_open,
                                                         target_tests_var,
                                                         *target_month_list)
                        target_tests_scroll.grid(row=5, column=1, sticky=W, padx=16, pady=5)
                        instruction_label = Label(test_open,
                                                  text="Click the button below to apply",
                                                  fg="#585858",
                                                  bg="#d3d3d3",
                                                  font=("Helvetica", 10))
                        instruction_label.grid(row=6, column=0, columnspan=2, sticky=W, padx=16, pady=(3, 1))
                        instruction_label = Label(test_open,
                                                  text="details and get the results for",
                                                  fg="#585858",
                                                  bg="#d3d3d3",
                                                  font=("Helvetica", 10))
                        instruction_label.grid(row=7, column=0, columnspan=2, sticky=W, padx=16, pady=1)
                        instruction_label = Label(test_open,
                                                  text="selective student.",
                                                  fg="#585858",
                                                  bg="#d3d3d3",
                                                  font=("Helvetica", 10))
                        instruction_label.grid(row=8, column=0, columnspan=2, sticky=W, padx=16, pady=1)

                        def access_batch_details():
                            connection_name = admission_database
                            print(admission_database)
                            xcude = str(new_test_standard_dict[test_open_standard.get()])
                            if os.path.isfile(connection_name) == True:
                                print("done")

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

                                student_list_toplevel = Toplevel()
                                student_list_toplevel.iconbitmap(favicon)
                                student_list_toplevel.resizable(0, 10)

                                output_frame = Frame(student_list_toplevel, width=1035, height=300)
                                output_frame.pack(expand=True, fill=BOTH)

                                output_canvas = Canvas(output_frame, width=1035, scrollregion=(0, 0, 10000, 10000))
                                #h = Scrollbar(output_frame, orient=HORIZONTAL, bg="green")
                                #h.pack(side=BOTTOM, fill=X)
                                v = Scrollbar(output_frame, orient=VERTICAL)
                                v.pack(side=RIGHT, fill=Y)
                                output_canvas.configure(yscrollcommand=v.set)
                                #h.config(command=output_canvas.xview)
                                v.config(command=output_canvas.yview)

                                output_canvas.pack()

                                bgcolo = "#585858"

                                the_other_output_canvas = Canvas(output_canvas, width=1035)
                                the_other_output_canvas.pack(side=TOP, anchor=N, pady=0)

                                output_canvas.bind_all('<MouseWheel>', lambda event: output_canvas.yview_scroll(
                                    int(-1 * (event.delta / 120)), "units"))

                                roll_number_label = Label(the_other_output_canvas, text="mID", font=("Helvetica", 12),
                                                          bg=bgcolo, width=30, fg="white")
                                roll_number_label.grid(row=0, column=0, ipadx=5)

                                name_label = Label(the_other_output_canvas, text="First Name", font=("Helvetica", 12),
                                                   bg=bgcolo, width=30, fg="white")
                                name_label.grid(row=0, column=1, ipadx=5)

                                last_name_label = Label(the_other_output_canvas, text="Last Name", font=("Helvetica", 12),
                                                        bg=bgcolo, width=30, fg="white")
                                last_name_label.grid(row=0, column=2, ipadx=5)

                                send_command_label = Label(the_other_output_canvas, text="Select", font=("Helvetica", 12),
                                                           bg=bgcolo, width=10, fg="white")
                                send_command_label.grid(row=0, column=3, sticky=EW)

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


                                def gen_bar(table_list, database_name, student_id, first_name, last_name):
                                    try:
                                        plt.clf()
                                    except:
                                        pass
                                    li = []
                                    per = []
                                    name = []
                                    i = 0
                                    connection = sqlite3.connect(database_name)
                                    cursor = connection.cursor()
                                    appen = "select percentage,first,last from {0} where {1}.Rollno='%s'" % student_id

                                    try:
                                        for x in table_list:
                                            cursor.execute(appen.format(x, x))
                                            list_element = cursor.fetchone()
                                            if list_element == None:
                                                list_element = (0.0, first_name, last_name)
                                            li.append(list_element)
                                            print(li)
                                            i = i + 1
                                        out = li
                                    except Error as e:
                                        out = e
                                        print(out)

                                    for x in li:
                                        per.append(x[0])
                                        name.append(x[1] + x[2])
                                    table_name_list = []
                                    avg = 0
                                    for percentage in per:
                                        avg += percentage
                                    avg = avg / len(per)

                                    for i in table_list:
                                        table_name_list.append(i[13:])
                                    bar_dict = {'Tests': table_name_list, 'percentage': per}
                                    df = pd.DataFrame(bar_dict)
                                    print(df)

                                    x = df["Tests"]
                                    y = df["percentage"]
                                    if avg > 74.0:
                                        plt.bar(x, y, label="Percentage scored", color="green")
                                    elif ((avg > 49.0) & (avg < 75.0)):
                                        plt.bar(x, y, label="Percentage scored", color="yellow")
                                    elif ((avg > 24.0) & (avg < 50.0)):
                                        plt.bar(x, y, label="Percentage scored", color="orange")
                                    elif (avg == 0.0):
                                        plt.bar(x, y, label="Percentage scored", color="black")
                                    elif ((avg > 0.00) & (avg < 25)):
                                        plt.bar(x, y, label="Percentage scored", color="red")

                                    plt.xlabel(student_id)
                                    plt.ylabel('Percentage secured')

                                    avg = "{:5.2f}%".format(avg)
                                    plt.title(f"Performance of {first_name} {last_name}:\n Percentage Secured:{avg}")

                                    plt.legend(["Percentage Secured."])
                                    plt.ylim(10, 100)

                                    plt.show()

                                def gen_pie(test_list, test_database, sid, first_name, last_name):
                                    try:
                                        plt.clf()
                                    except:
                                        pass
                                    slices = []
                                    percents = []
                                    cols = []
                                    plod = []
                                    connection = sqlite3.connect(test_database)
                                    cursor = connection.cursor()
                                    appen = "select percentage from {0} where {1}.Rollno='%s'" % sid
                                    for element in test_list:
                                        cursor.execute(appen.format(element, element))
                                        list_element = cursor.fetchone()
                                        if list_element == None:
                                            list_element = (0.0, first_name, last_name)
                                        percents.append(list_element)
                                    print(percents)
                                    print(1)
                                    n = 360 / len(test_list)
                                    percentage_summation = []
                                    for data in percents:
                                        percentage_summation.append(data[0])
                                    avg = sum(percentage_summation) / len(percentage_summation)
                                    for x in percents:
                                        slices.append(n)
                                        plod.append(0.025)
                                    print(2)
                                    print(slices)
                                    for percentages in percents:
                                        if percentages[0] > 74.0:
                                            cols.append("green")
                                        elif ((percentages[0] > 49.0) & (percentages[0] < 75.0)):
                                            cols.append("yellow")
                                        elif ((percentages[0] > 24.0) & (percentages[0] < 50.0)):
                                            cols.append("orange")
                                        elif (percentages[0] == 0.0):
                                            cols.append("black")
                                        elif ((percentages[0] > 0.00) & (percentages[0] < 25)):
                                            cols.append("red")
                                    table_name_list = []
                                    for i in test_list:
                                        table_name_list.append(i[13:])
                                    plt.pie(slices, labels=table_name_list, colors=cols, startangle=90, explode=plod, shadow=False)
                                    avg = "{:5.2f}%".format(avg)
                                    plt.title(f"Performance of {first_name} {last_name}:\n Percentage Secured:{avg}")
                                    #plt.legend(["Result Average: {:5.2f}%".format(avg)])

                                    plt.show()

                                def real_pie_generator(student_id, first_name, last_name, open_b):
                                    open_b.configure(bg="#67e867", activebackground="#35e035", text="Opened")
                                    gen_pie(target_month_list, test_name, student_id, first_name, last_name)
                                def the_real_generator(student_id, first_name, last_name, open_b):
                                    open_b.configure(bg="#67e867", activebackground="#35e035", text="Opened")
                                    gen_bar(target_month_list, test_name, student_id, first_name, last_name)

                                the_bogo_color = "#bababa"
                                indexing_number = 1
                                for data_tuple in reversed(sender_list):
                                    create_roll_label = Label(the_other_output_canvas, text=data_tuple[0],
                                                              bg=the_bogo_color, width=31, font=9)
                                    create_roll_label.grid(row=indexing_number, column=0, pady=(0, 5))

                                    create_name_label = Label(the_other_output_canvas, text=data_tuple[3],
                                                              bg=the_bogo_color, width=31, font=9)
                                    create_name_label.grid(row=indexing_number, column=1, pady=(0, 5))

                                    create_last_name_label = Label(the_other_output_canvas, text=data_tuple[4],
                                                                   bg=the_bogo_color, width=31, font=9)
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
                                                         text="Bar",
                                                         font=("Helvetica", 10),
                                                         width=11,
                                                         borderwidth=0,
                                                         bg="#45b4e7",
                                                         fg="white",
                                                         activeforeground="white",
                                                         activebackground="#1ca0dd")
                                    open_button.configure(
                                        command=lambda i=data_tuple[0], j=data_tuple[3], k=data_tuple[4], open_b=open_button: the_real_generator(i, j, k, open_b))
                                    open_button.grid(row=0, column=1)

                                    open_pie_button = Button(create_button_frame,
                                                         text="Pie",
                                                         font=("Helvetica", 10),
                                                         width=11,
                                                         borderwidth=0,
                                                         bg="#45b4e7",
                                                         fg="white",
                                                         activeforeground="white",
                                                         activebackground="#1ca0dd")
                                    open_pie_button.configure(
                                        command=lambda i=data_tuple[0], j=data_tuple[3], k=data_tuple[4],
                                                       open_b=open_pie_button: real_pie_generator(i, j, k, open_b))
                                    open_pie_button.grid(row=0, column=2, padx=(2, 0))

                                    indexing_number += 1
                                scroll_lord = output_canvas.create_window(0, 0, window=the_other_output_canvas, anchor=NW)
                                output_canvas.configure(scrollregion=output_canvas.bbox("all"))
                            else:
                                print(100)


                        graph_proceed_button.configure(text="Apply Details", command=access_batch_details)
                    except:
                        test_open.destroy()
                        show_warning = messagebox.showwarning("Error",
                                                              "No Test has been added during this given month, please try again.")
                        if show_warning == "ok":
                            pass
            else:
                show_warning = messagebox.showwarning("Error",
                                                      "Please Select a Quarter first to display results.")
                if show_warning == "ok":
                    pass

        graph_proceed_button = Button(test_open,
                                               text="Show Test",
                                               font=("Helvetica", 10),
                                               width=12,
                                               borderwidth=0,
                                               bg="#45b4e7",
                                               fg="white",
                                               activeforeground="white",
                                               activebackground="#1ca0dd",
                                               command=call_test)
        graph_proceed_button.grid(row=9, column=0, sticky=EW, padx=16, pady=(10, 0))

    option_frame_2_button = Button(option_frame_2,
                                   text="Quaterly",
                                   font=("Helvetica", 10),
                                   width=12,
                                   borderwidth=0,
                                   bg="#45b4e7",
                                   fg="white",
                                   activeforeground="white",
                                   activebackground="#1ca0dd",
                                   command=send_three_month_result)
    option_frame_2_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(24, 10))

