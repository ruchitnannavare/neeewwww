from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import admissions
import student_database
import test
import sendcustomtext
import sideview
import aboutandcontact
import resultfunctioncontainer
import globalvariables
favicon = "favicon.ico"
root = Tk()
root.geometry("1000x640")
root.resizable(0, 0)
root.title("markOS 2.0™")
root.iconbitmap(favicon)
girlphoto = Image.open("girlphoto.png")
girlphoto = girlphoto.resize((400, 400), Image.ANTIALIAS)
girlphoto = ImageTk.PhotoImage(girlphoto)

# Promote reminder
if datetime.date.today().month == globalvariables.new_academic_year_month_stopper:
    month_warning = messagebox.showwarning("PROMOTE STUDENTS", "Ignore if already done.\nPLEASE PROMOTE STUDENTS TO NEXT ACADEMIC YEAR.")
    if month_warning == "ok":
        pass

# password frame

color_frame_for_class_name = Frame(root, bg="#c3073f", height=100, width=1000, borderwidth=0, highlightthickness=0)
color_frame_for_class_name.pack(side="top", fill="both", expand=True)
color_frame_for_class_name.pack_propagate(False)
username_frame = Frame(root, bg="#d3d3d3", height=500, width=1000)
username_frame.pack(side="top", fill="both", expand=True)
username_frame.pack_propagate(False)

# For the coloured user name window FRAME1

class_logo = Image.open("classlogodemo.png")
class_logo = class_logo.resize((100, 100), Image.ANTIALIAS)
class_logo = ImageTk.PhotoImage(class_logo)
class_logo_name = Image.open("Bhavik Patel's Chemistry Tuitions.png")
class_logo_name = class_logo_name.resize((900, 100), Image.ANTIALIAS)
class_logo_name = ImageTk.PhotoImage(class_logo_name)

logo_label_frame1 = Label(color_frame_for_class_name, image=class_logo, borderwidth=0)
logo_label_frame1.grid(row=0, column=0, columnspan=2, padx=(15, 5), pady=(15, 15))
name_label_frame1 = Label(color_frame_for_class_name, image=class_logo_name, borderwidth=0)
name_label_frame1.grid(row=0, column=2)

# For the username window that actually contains the username and password
spacerlabel1 = Label(username_frame, text=" ", bg="#d3d3d3")
spacerlabel1.grid(row=0, column=0, ipadx=50, pady=(10, 0))
usernamelabel = Label(username_frame, text="Username:", font=("Helvetica", 10, "bold"), bg="#d3d3d3")
usernamelabel.grid(row=1, column=0, padx=50, pady=(125, 5), sticky=W)
username_entry = Entry(username_frame, width=25, borderwidth=0, font=("Times", 14))
username_entry.grid(row=2, column=0, padx=50)
passwordlabel = Label(username_frame, text="Password:", font=("Helvetica", 10, "bold"), bg="#d3d3d3")
passwordlabel.grid(row=3, column=0, padx=50, sticky=W)
password_entry = Entry(username_frame, width=25, borderwidth=0, show="*", font=("Times", 14))
password_entry.grid(row=4, column=0, padx=50, pady=5)

# Command that will contain everything
def getIN():
    username_frame.pack_forget()
    status_bar_frame.pack_forget()
    mainframe = Frame(root, bg="#d3d3d3", height=488, width=1000)
    mainframe.pack()
    mainmenuframe = Frame(mainframe, height=488, width=150, bg="#dc0847",
                          borderwidth=0, highlightthickness=0)
    mainmenuframe.grid(row=0, column=0)
    mainmenuframe.grid_propagate(False)
    playframe = Frame(mainframe, bg="#d3d3d3", height=488, width=858)
    playframe.grid(row=0, column=1)
    playframe.grid_propagate(False)
    playframe_showcase_0 = Frame(playframe, bg="#d3d3d3", height=488, width=858)
    playframe_showcase_0.pack(side="top", fill="both", expand=True)
    playframe_showcase_0.pack_propagate(False)
    girlphoto_label = Label(playframe_showcase_0, image=girlphoto, borderwidth=0)
    girlphoto_label.pack(padx=214, pady=25)

    # Colours
    coral = "#bababa"

    # Button functions for main menu
    def testButton():
        # Deleting old frames and rendering new ones.
        playframe_showcase_0.pack_forget()
        global playframe_showcase_1, playframe_showcase_2, playframe_showcase_3, playframe_showcase_4,playframe_showcase_5
        try:
            playframe_showcase_2.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_3.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_4.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_5.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_1.pack_forget()
        except NameError:
            pass
        playframe_showcase_1 = Frame(playframe, bg="#d3d3d3", height=488, width=858)
        playframe_showcase_1.pack(side="top", fill="both", expand=True)
        playframe_showcase_1.pack_propagate(False)
        # smaller frames.
        test_frame1 = Frame(playframe_showcase_1, bg=coral, height=150, width=770, borderwidth=0,
                            highlightthickness=0)
        test_frame1.pack(padx=(0, 25), side="top", expand=True)
        test_frame1.pack_propagate(False)
        test_frame2 = Frame(playframe_showcase_1, bg="#bababa", height=150, width=770, borderwidth=0,
                            highlightthickness=0)
        test_frame2.pack(padx=(0, 25), side="top", expand=True)
        test_frame2.pack_propagate(False)
        # Filling the newly rendered frames.
        create_new_test_heading = Label(test_frame1, text="Create New Test",
                                        fg="#585858",
                                        bg=coral,
                                        font=("Helvetica", 25))
        create_new_test_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        create_new_test_instruction1 = Label(test_frame1, text="This option helps to create a new test entry to put up the batch's obtained marks into the database.",
                                             fg="#585858",
                                             bg=coral,
                                             font=("Helvetica", 8))
        create_new_test_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        create_new_test_instruction2 = Label(test_frame1,
                                             text="Click CREATE TEST to begin.",
                                             fg="#585858",
                                             bg=coral,
                                             font=("Helvetica", 8))
        create_new_test_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)

        create_test_button = Button(test_frame1, text="Create Test",
                                    font=("Helvetica", 10),
                                    width=12,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=test.new_test)
        create_test_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        open_old_test_heading = Label(test_frame2,
                                      text="Open Old Test",
                                      fg="#585858",
                                      bg="#bababa",
                                      font=("Helvetica", 25))
        open_old_test_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        open_old_test_instruction1 = Label(test_frame2,
                                           text="This option helps to open an old test and review it. It also provides an option to send the result to the parents through our Telegram and Mailjet tech.",
                                           fg="#585858",
                                           bg="#bababa",
                                           font=("Helvetica", 8))
        open_old_test_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        open_old_test_instruction2 = Label(test_frame2,
                                           text="Click OPEN OLD TEST to begin.",
                                           fg="#585858",
                                           bg="#bababa",
                                           font=("Helvetica", 8))
        open_old_test_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)

        old_test_button = Button(test_frame2,
                                 text="Open Old Test",
                                 font=("Helvetica", 10),
                                 width=12,
                                 borderwidth=0,
                                 bg="#45b4e7",
                                 fg="white",
                                 activeforeground="white",
                                 activebackground="#1ca0dd",
                                 command=test.open_old_test)
        old_test_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)

    def sendText():
        # Erasing old frames and rendering new ones.
        playframe_showcase_0.pack_forget()
        global playframe_showcase_2, playframe_showcase_1, playframe_showcase_3, playframe_showcase_4, playframe_showcase_5
        try:
            playframe_showcase_1.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_3.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_4.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_5.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_2.pack_forget()
        except NameError:
            pass
        playframe_showcase_2 = Frame(playframe, bg="#d3d3d3", height=488, width=858)
        playframe_showcase_2.pack(side="top", fill="both", expand=True)
        playframe_showcase_2.pack_propagate(False)
        sendText_frame1 = Frame(playframe_showcase_2,
                                bg="#bababa",
                                height=150,
                                width=770,
                                borderwidth=0,
                                highlightthickness=0)
        sendText_frame1.pack(padx=(0, 25), side="top", expand=True)
        sendText_frame1.pack_propagate(False)
        sendText_frame2 = Frame(playframe_showcase_2,
                                bg="#bababa",
                                height=150,
                                width=770,
                                borderwidth=0,
                                highlightthickness=0)
        sendText_frame2.pack(padx=(0, 25), side="top", expand=True)
        sendText_frame2.pack_propagate(False)
        # Filling the newly rendered frames
        sendText_Test_heading = Label(sendText_frame1,
                                      text="Send Test Results",
                                      fg="#585858",
                                      bg="#bababa",
                                      font=("Helvetica", 25))
        sendText_Test_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        sendText_Test_instruction1 = Label(sendText_frame1,
                                           text="This option sends the Test scores of a given batch of students from the Test stored in your markOS databases.",
                                           fg="#585858",
                                           bg="#bababa",
                                           font=("Helvetica", 8))
        sendText_Test_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        sendText_Test_instruction2 = Label(sendText_frame1,
                                           text="Click CONTINUE to begin.",
                                           fg="#585858",
                                           bg="#bababa",
                                           font=("Helvetica", 8))
        sendText_Test_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        sendText_Test_button = Button(sendText_frame1,
                                      text="Send Test",
                                      font=("Helvetica", 10),
                                      width=12,
                                      borderwidth=0,
                                      bg="#45b4e7",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#1ca0dd",
                                      command=sendcustomtext.send_scores)
        sendText_Test_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        sendTest_custom_heading = Label(sendText_frame2,
                                        text="Send Custom Texts",
                                        fg="#585858",
                                        bg="#bababa",
                                        font=("Helvetica", 25))
        sendTest_custom_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        sendTest_custom_instruction1 = Label(sendText_frame2,
                                             text="This option helps deliver custom texts to wards and their respective parents using our Telegram and Mailjet tech.",
                                             fg="#585858",
                                             bg="#bababa",
                                             font=("Helvetica", 8))
        sendTest_custom_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        sendTest_custom_instruction2 = Label(sendText_frame2,
                                             text="Click CUSTOM TEXT to begin.",
                                             fg="#585858",
                                             bg="#bababa",
                                             font=("Helvetica", 8))
        sendTest_custom_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)

        sendTest_custom_button = Button(sendText_frame2,
                                        text="Custom Text",
                                        font=("Helvetica", 10),
                                        width=12,
                                        borderwidth=0,
                                        bg="#45b4e7",
                                        fg="white",
                                        activeforeground="white",
                                        activebackground="#1ca0dd",
                                        command=sendcustomtext.custom_text)
        sendTest_custom_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)

    # Result function
    def result():
        # Deleting old frames and rendering new ones
        playframe_showcase_0.pack_forget()
        global playframe_showcase_1, playframe_showcase_2, playframe_showcase_3, playframe_showcase_4, playframe_showcase_5
        try:
            playframe_showcase_1.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_2.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_4.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_5.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_3.pack_forget()
        except NameError:
            pass
    # New frame for results section
        playframe_showcase_3 = Frame(playframe, bg="#d3d3d3", height=488, width=858)
        playframe_showcase_3.pack(side="top", fill="both", expand=True)
        playframe_showcase_3.pack_propagate(False)
        # Small frame
        result_frame1 = Frame(playframe_showcase_3, bg="#bababa", height=150, width=770, borderwidth=0,
                                highlightthickness=0)
        result_frame1.pack(padx=(0, 25), side="top", expand=True)
        result_frame1.pack_propagate(False)

        result_frame2 = Frame(playframe_showcase_3, bg="#bababa", height=150, width=770, borderwidth=0,
                              highlightthickness=0)
        result_frame2.pack(padx=(0, 25), side="top", expand=True)
        result_frame2.pack_propagate(False)
        # packing stuff into the smaller frame
        see_result_heading = Label(result_frame1,
                                          text="See Results",
                                          fg="#585858",
                                          bg="#bababa",
                                          font=("Helvetica", 25))
        see_result_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        see_result_instruction1 = Label(result_frame1,
                                               text="This feature helps to visualize the performance of the student in a given time frame.",
                                               fg="#585858",
                                               bg="#bababa",
                                               font=("Helvetica", 8))
        see_result_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        see_result_instruction2 = Label(result_frame1,
                                                 text="Click SEE RESULTS to begin.",
                                                 fg="#585858",
                                                 bg="#bababa",
                                                 font=("Helvetica", 8))
        see_result_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        # Result button
        see_result_button = Button(result_frame1,
                                            text="See Results",
                                            font=("Helvetica", 10),
                                            width=12,
                                            borderwidth=0,
                                            bg="#45b4e7",
                                            fg="white",
                                            activeforeground="white",
                                            activebackground="#1ca0dd",
                               command=resultfunctioncontainer.see_result_data_function)
        see_result_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        send_result_heading = Label(result_frame2,
                               text="Send Results",
                               fg="#585858",
                               bg="#bababa",
                               font=("Helvetica", 25))
        send_result_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        send_result_instruction1 = Label(result_frame2,
                                    text="This option delivers the average score of tests taken in a given time frame to the parents of the ward with visual representation.",
                                    fg="#585858",
                                    bg="#bababa",
                                    font=("Helvetica", 8))
        send_result_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        send_result_instruction2 = Label(result_frame2,
                                    text="Click SEND RESULTS to begin.",
                                    fg="#585858",
                                    bg="#bababa",
                                    font=("Helvetica", 8))
        send_result_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        # Result button
        send_result_button = Button(result_frame2,
                               text="Send Results",
                               font=("Helvetica", 10),
                               width=12,
                               borderwidth=0,
                               bg="#45b4e7",
                               fg="white",
                               activeforeground="white",
                               activebackground="#1ca0dd",
                               command=resultfunctioncontainer.send_result_data_function)
        send_result_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)
    # Admissions
    def admission():
        # Dealeting old frames and rendering new frames.
        playframe_showcase_0.pack_forget()
        global playframe_showcase_1, playframe_showcase_2, playframe_showcase_3, playframe_showcase_4, playframe_showcase_5, new_admission_button
        try:
            playframe_showcase_1.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_2.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_3.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_5.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_4.pack_forget()
        except NameError:
            pass
        # New blank frame in front of play frame.
        playframe_showcase_4 = Frame(playframe, bg="#d3d3d3", height=488, width=858)
        playframe_showcase_4.pack(side="top", fill="both", expand=True)
        playframe_showcase_4.pack_propagate(False)

        admission_frame1 = Frame(playframe_showcase_4, bg="#bcf5bc", height=150, width=770, borderwidth=0,
                              highlightthickness=0)
        admission_frame1.pack(padx=(0, 25), side="top", expand=True)
        admission_frame1.pack_propagate(False)

        admission_frame2 = Frame(playframe_showcase_4, bg="#8ad0f0", height=150, width=770, borderwidth=0,
                              highlightthickness=0)
        admission_frame2.pack(padx=(0, 25), side="top", expand=True)
        admission_frame2.pack_propagate(False)

        admission_frame3 = Frame(playframe_showcase_4, bg="#ffb1b1", height=150, width=770, borderwidth=0,
                              highlightthickness=0)
        admission_frame3.pack(padx=(0, 25), side="top", expand=True)
        admission_frame3.pack_propagate(False)
        # Packing stuff into the smaller frame
        # New admission
        new_admission_heading = Label(admission_frame1,
                                      text="New Admissions",
                                      fg="#585858",
                                      bg="#bcf5bc",
                                      font=("Helvetica", 25))
        new_admission_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        new_admission_instruction1 = Label(admission_frame1,
                                           text="Opens a prompt to add new admissions.",
                                           fg="#585858",
                                           bg="#bcf5bc",
                                           font=("Helvetica", 8))
        new_admission_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        new_admission_instruction2 = Label(admission_frame1,
                                           text="Click NEW ADMISSION to begin.",
                                           fg="#585858",
                                           bg="#bcf5bc",
                                           font=("Helvetica", 8))
        new_admission_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        # New Admission button
        new_admission_button = Button(admission_frame1,
                                      text="New Admission",
                                      font=("Helvetica", 10),
                                      width=12,
                                      borderwidth=0,
                                      bg="#67e867",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#35e035",
                                      command=admissions.new_admissions)
        new_admission_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)
        # Promote Admissions
        promteAdmissions_heading = Label(admission_frame2,
                                         text="Promote",
                                         fg="#585858",
                                         bg="#8ad0f0",
                                         font=("Helvetica", 25))
        promteAdmissions_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        promteAdmissions_instruction1 = Label(admission_frame2,
                                              text="Opens a prompt to promote students of existing batches to next year.",
                                              fg="#585858",
                                              bg="#8ad0f0",
                                              font=("Helvetica", 8))
        promteAdmissions_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        promteAdmissions_instruction2 = Label(admission_frame2,
                                              text="Click PROMOTE to begin.",
                                              fg="#585858",
                                              bg="#8ad0f0",
                                              font=("Helvetica", 8))
        promteAdmissions_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        # Result button
        promteAdmissions_button = Button(admission_frame2,
                                         text="Promote",
                                         font=("Helvetica", 10),
                                         width=12,
                                         borderwidth=0,
                                         bg="#45b4e7",
                                         fg="white",
                                         activeforeground="white",
                                         activebackground="#1ca0dd",
                                         command=admissions.admissions_promote)
        promteAdmissions_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)
        # Delete admissions
        delete_admissions_heading = Label(admission_frame3,
                                          text="Delete Admission",
                                          fg="#585858",
                                          bg="#ffb1b1",
                                          font=("Helvetica", 25))
        delete_admissions_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        delete_admissions_instruction1 = Label(admission_frame3,
                                               text="Opens a prompt to delete an admission.",
                                               fg="#585858",
                                               bg="#ffb1b1",
                                               font=("Helvetica", 8))
        delete_admissions_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        delete_admissions_instruction2 = Label(admission_frame3,
                                               text="Click DELETE ADMISSION to begin.",
                                               fg="#585858",
                                               bg="#ffb1b1",
                                               font=("Helvetica", 8))
        delete_admissions_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        # Result button
        delete_admissions_button = Button(admission_frame3,
                                          text="Delete Admission",
                                          font=("Helvetica", 10),
                                          width=15,
                                          borderwidth=0,
                                          bg="#ff6565",
                                          fg="white",
                                          activeforeground="white",
                                          activebackground="#ff4f4f",
                                          command=admissions.delete_admission)
        delete_admissions_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)

    def showDatabase():
        playframe_showcase_0.pack_forget()
        global playframe_showcase_1, playframe_showcase_2, playframe_showcase_3, playframe_showcase_4, playframe_showcase_5
        try:
            playframe_showcase_1.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_2.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_3.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_4.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_5.pack_forget()
        except NameError:
            pass
    # Small frame for database button
        playframe_showcase_5 = Frame(playframe, bg="#d3d3d3", height=488, width=858)
        playframe_showcase_5.pack(side="top", fill="both", expand=True)
        playframe_showcase_5.pack_propagate(False)
        # Small frame
        student_database_frame1 = Frame(playframe_showcase_5, bg="#76ffff", height=150, width=770, borderwidth=0,
                                        highlightthickness=0)
        student_database_frame1.pack(padx=(0, 25), side="top", expand=True)
        student_database_frame1.pack_propagate(False)

        student_database_frame2 = Frame(playframe_showcase_5, bg="#76ffff", height=150, width=770, borderwidth=0,
                                        highlightthickness=0)
        student_database_frame2.pack(padx=(0, 25), side="top", expand=True)
        student_database_frame2.pack_propagate(False)

        student_database_frame3 = Frame(playframe_showcase_5, bg="#76ffff", height=150, width=770, borderwidth=0,
                                        highlightthickness=0)
        student_database_frame3.pack(padx=(0, 25), side="top", expand=True)
        student_database_frame3.pack_propagate(False)
        # packing stuff into the smaller frame
        show_data_heading = Label(student_database_frame1,
                                  text="Student Database",
                                  fg="#585858",
                                  bg="#76ffff",
                                  font=("Helvetica", 25))
        show_data_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        show_data_instruction1 = Label(student_database_frame1,
                                       text="Opens a prompt to access student data from your markOS databases.",
                                       fg="#585858",
                                       bg="#76ffff",
                                       font=("Helvetica", 8))
        show_data_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        show_data_instruction2 = Label(student_database_frame1,
                                       text="Click ACCESS DATA to begin.",
                                       fg="#585858",
                                       bg="#76ffff",
                                       font=("Helvetica", 8))
        show_data_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        # Result button
        show_data_button = Button(student_database_frame1,
                                  text="Access Data",
                                  font=("Helvetica", 10),
                                  width=12,
                                  borderwidth=0,
                                  bg="#00b1b1",
                                  fg="white",
                                  activeforeground="white",
                                  activebackground="#009898",
                                  command=student_database.access_data_function)
        show_data_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        update_database_heading = Label(student_database_frame2,
                                        text="Update Database",
                                        fg="#585858",
                                        bg="#76ffff",
                                        font=("Helvetica", 25))
        update_database_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        update_database_instruction1 = Label(student_database_frame2,
                                             text="Opens a prompt to update student data from your markOS databases.",
                                             fg="#585858",
                                             bg="#76ffff",
                                             font=("Helvetica", 8))
        update_database_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        update_database_instruction2 = Label(student_database_frame2,
                                             text="Click UPDATE DATA to begin.",
                                             fg="#585858",
                                             bg="#76ffff",
                                             font=("Helvetica", 8))
        update_database_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        # Result button
        update_database_button = Button(student_database_frame2,
                                        text="Update Data",
                                        font=("Helvetica", 10),
                                        width=12,
                                        borderwidth=0,
                                        bg="#00b1b1",
                                        fg="white",
                                        activeforeground="white",
                                        activebackground="#009898",
                                        command=student_database.update_data_function)
        update_database_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        # archives
        # packing stuff into the smaller frame
        archives_data_heading = Label(student_database_frame3,
                                      text="Archives",
                                      fg="#585858",
                                      bg="#76ffff",
                                      font=("Helvetica", 25))
        archives_data_heading.pack(padx=(15, 0), pady=(15, 0), anchor=W)

        archives_data_instruction1 = Label(student_database_frame3,
                                           text="Access archives from your markOS databases.",
                                           fg="#585858",
                                           bg="#76ffff",
                                           font=("Helvetica", 8))
        archives_data_instruction1.pack(padx=(15, 0), pady=(5, 0), anchor=W)

        archives_data_instruction2 = Label(student_database_frame3,
                                           text="Click ARCHIVES DATA to begin.",
                                           fg="#585858",
                                           bg="#76ffff",
                                           font=("Helvetica", 8))
        archives_data_instruction2.pack(padx=(15, 0), pady=(0, 5), anchor=W)
        # Result button
        archives_data_button = Button(student_database_frame3,
                                      text="Archives",
                                      font=("Helvetica", 10),
                                      width=12,
                                      borderwidth=0,
                                      bg="#00b1b1",
                                      fg="white",
                                      activeforeground="white",
                                      activebackground="#009898",
                                      command=student_database.archive_function)
        archives_data_button.pack(padx=(15, 0), pady=(5, 0), anchor=W)
    # Shows the contact card
    def about():
        playframe_showcase_0.pack_forget()
        global playframe_showcase_1, playframe_showcase_2, playframe_showcase_3, playframe_showcase_4, playframe_showcase_5, playframe_showcase_6
        try:
            playframe_showcase_1.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_2.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_3.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_4.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_5.pack_forget()
        except NameError:
            pass
        try:
            playframe_showcase_6.pack_forget()
        except NameError:
            pass
        playframe_showcase_5 = Frame(playframe, bg="#d3d3d3", height=440, width=858)
        playframe_showcase_5.pack(side="top", fill="both", expand=True)
        playframe_showcase_5.pack_propagate(False)
        # Small frame
        fcolo = "#ffff99"
        about_frame1 = Frame(playframe_showcase_5, bg=fcolo, height=200, width=770, borderwidth=0,
                             highlightthickness=0)
        about_frame1.pack(padx=(0, 25), side="top", expand=True)
        about_frame1.pack_propagate(False)
        # packing stuff into the smaller frame
        sideview_heading = Label(about_frame1,
                                 text="SideView™",
                                 fg="#585858",
                                 bg=fcolo,
                                 font=("Helvetica", 25))
        sideview_heading.pack(padx=(35, 0), pady=(25, 0), anchor=W)

        sideview_info1 = Label(about_frame1,
                               text="SideView™ is a piece of accessory software developed by Aexior.",
                               fg="#585858",
                               bg=fcolo,
                               font=("Helvetica", 8, "italic"))
        sideview_info1.pack(padx=(35, 0), pady=5, anchor=W)

        sideview_info2 = Label(about_frame1,
                               text="This particular implementation aids to establish a",
                               fg="#585858",
                               bg=fcolo,
                               font=("Helvetica", 8, "italic"))
        sideview_info2.pack(padx=(35, 0), pady=5, anchor=W)

        sideview_info3 = Label(about_frame1,
                               text="connection of your markOS™ distribution to Telegram™ servers.",
                               fg="#585858",
                               bg=fcolo,
                               font=("Helvetica", 8, "italic"))
        sideview_info3.pack(padx=(35, 0), pady=(5, 0), anchor=W)

        launch_button = Button(about_frame1,
                               text="Launch SideView™",
                               font=("Helvetica", 10, "bold"),
                               width=20,
                               borderwidth=0,
                               bg="#ffcc00",
                               fg="white",
                               activeforeground="white",
                               activebackground="#ff8c00",
                               command=sideview.sideview_app)
        launch_button.pack(padx=(35, 0), pady=(10, 15), anchor=W)

        # THe contact us frame
        about_frame2 = Frame(playframe_showcase_5, bg=fcolo, height=200, width=770, borderwidth=0,
                             highlightthickness=0)
        about_frame2.pack(padx=(0, 25), side="top", expand=True)
        about_frame2.pack_propagate(False)
        # packing stuff into the smaller frame
        contact_heading = Label(about_frame2,
                                 text="Contact Aexior™",
                                 fg="#585858",
                                 bg=fcolo,
                                 font=("Helvetica", 25))
        contact_heading.pack(padx=(35, 0), pady=(25, 0), anchor=W)

        contact_info1 = Label(about_frame2,
                               text="Questions? Doubts? Problems? Feel free to contact us.",
                               fg="#585858",
                               bg=fcolo,
                               font=("Helvetica", 8, "italic"))
        contact_info1.pack(padx=(35, 0), pady=5, anchor=W)

        contact_info2 = Label(about_frame2,
                               text="We here at Aexior, love consumer feedback and try ",
                               fg="#585858",
                               bg=fcolo,
                               font=("Helvetica", 8, "italic"))
        contact_info2.pack(padx=(35, 0), pady=5, anchor=W)

        contact_info3 = Label(about_frame2,
                               text="to provide best solution and assistance we can offer.",
                               fg="#585858",
                               bg=fcolo,
                               font=("Helvetica", 8, "italic"))
        contact_info3.pack(padx=(35, 0), pady=(5, 0), anchor=W)

        launch_button = Button(about_frame2,
                               text="Proceed To Contact",
                               font=("Helvetica", 10, "bold"),
                               width=20,
                               borderwidth=0,
                               bg="#ffcc00",
                               fg="white",
                               activeforeground="white",
                               activebackground="#ff8c00",
                               command=aboutandcontact.contact)
        launch_button.pack(padx=(35, 0), pady=(10, 15), anchor=W)



    # Packing options in menu frame.
    test_button = Button(mainmenuframe, text="  Tests", font=("Helvetica", 14), width=15, bg="#dc0847", fg="white",
                         borderwidth=0, activebackground="#92052f", activeforeground="white", anchor=W,
                         command=testButton)
    test_button.pack(pady=(91, 10))

    sendtext_button = Button(mainmenuframe, text="  Send Texts", font=("Helvetica", 14), width=15, bg="#dc0847", fg="white",
                         borderwidth=0, activebackground="#92052f", activeforeground="white", anchor=W, command=sendText)
    sendtext_button.pack(pady=10)

    result_button = Button(mainmenuframe, text="  Result", font=("Helvetica", 14), width=15, bg="#dc0847", fg="white",
                         borderwidth=0, activebackground="#92052f", activeforeground="white", anchor=W, command=result)
    result_button.pack(pady=10)

    admission_button = Button(mainmenuframe, text="  Admissions", font=("Helvetica", 14), width=15, bg="#dc0847", fg="white",
                         borderwidth=0, activebackground="#92052f", activeforeground="white", anchor=W, command=admission)
    admission_button.pack(pady=10)

    studentInfo_button = Button(mainmenuframe, text="  Student Database", font=("Helvetica", 14), width=15, bg="#dc0847", fg="white",
                         borderwidth=0, activebackground="#92052f", activeforeground="white", anchor=W, command=showDatabase)
    studentInfo_button.pack(pady=10)

    sideview_button = Button(mainmenuframe, text="  SideView™", font=("Helvetica", 14), width=15, bg="#dc0847", fg="white",
                         borderwidth=0, activebackground="#92052f", activeforeground="white", anchor=W, command=about)
    sideview_button.pack(pady=(10, 87))


    status_bar_frame2 = Frame(root, bg="#adadad", height=28, width=1000, borderwidth=0, highlightthickness=0)
    status_bar_frame2.pack(side="top", fill="both", expand=True)
    status_bar_label2 = Label(status_bar_frame2, text="Powered by markOS, an Aexior production.", fg="white", bg="#adadad")
    status_bar_label2.pack(anchor=E)


# Quit command
def quitCommand():
    root.quit()
# Pass word check command
def checkPassword():
    getIN()
    #if str(username_entry.get()).upper() == "RUCHIT" and str(password_entry.get()).upper() == "NANNAVARE":
     #   getIN()
    #else:
     #   messageWarning = messagebox.showwarning("Incorrect Username or Password", "The Username or Password you have entered is incorrect,\nplease try again or QUIT program.")
      #  if messageWarning == "ok":
       #     username_entry.delete(0, END)
        #    password_entry.delete(0, END)

# Button for submitting
submit_button = Button(username_frame, text="Submit", font=("Helvetica", 10), width=12, borderwidth=0, bg="#45b4e7", fg="white", activeforeground="white", activebackground="#1ca0dd", command=checkPassword)
quit_button = Button(username_frame, text="Quit", font=("Helvetica", 10), width=12, borderwidth=0, bg="#f4094f", fg="white", activeforeground="white", activebackground="#c3073f", command=quitCommand)
submit_button.grid(row=5, column=0, padx=(50, 5), pady=(5, 200), sticky=W)
quit_button.grid(row=5, column=0, padx=(5, 50), pady=(5, 200), sticky=E)
# status bars
status_bar_frame = Frame(root, bg="#adadad", height=20, width=1000, borderwidth=0, highlightthickness=0)
status_bar_frame.pack(side="top", fill="both", expand=True)
status_bar_label = Label(status_bar_frame, text="Powered by markOS, an Aexior production.", fg="white", bg="#adadad")
status_bar_label.pack(anchor=E)
root.mainloop()