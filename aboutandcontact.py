from tkinter import *
favicon = "favicon.ico"
def contact():
    contact_form_toplevel = Toplevel()
    contact_form_toplevel.iconbitmap(favicon)
    contact_form_toplevel.title("Hello!")
    contact_form_toplevel.geometry("300x500")
    contact_form_toplevel.resizable(0, 0)
    contact_form_toplevel.configure(bg="#d3d3d3")
    fcolo = "#f08080"
    contact_frame = Frame(contact_form_toplevel, height=480, width=280, bg=fcolo)
    contact_frame.pack(padx=10, pady=10, fill="both", expand=True)
    contact_frame.pack_propagate(False)

    contact_label = Label(contact_frame, text="Contact Us", font=("Helvetica", 20, "bold underline"), fg="white", bg=fcolo)
    contact_label.pack(padx=10, pady=(10, 5))

    contact_para = Label(contact_frame,
                         text="e-mail:\nsupport@aexior.com\n\nCall: \n+91 8320 53 9455 \n\nor DM us on Instagram: \n\n@aexior",
                         font=("Helvetica", 13),
                         fg="white",
                         bg=fcolo,
                         )
    contact_para.pack(padx=10)

    about_label = Label(contact_frame, text="About", font=("Helvetica", 20, "bold underline"), fg="white", bg=fcolo)
    about_label.pack(padx=10, pady=(10, 5))

    about_para = Label(contact_frame,
                       text="This is a licensed distribution of the markOS\nversion 2.0 solely developed and distributed\nby the Aexior holdings pvt. limited. Aexior \nholds the copyrights to all the versions \nand distributions of markOS™ and \nSideView™ programs and the namesake.\n\nLicense Key: TYD-798-BNS\n\n\nCopyright © 2020 Aexior. All rights reserved.",
                       font=("Helvetica", 10),
                       fg="white",
                       bg=fcolo,
                       )
    about_para.pack(padx=10)




