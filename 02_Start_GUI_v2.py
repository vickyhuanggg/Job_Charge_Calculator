from tkinter import *
from functools import partial   # To prevent unwanted windows
from PIL import Image, ImageTk

class Start:
    def __init__(self, parent):

        heading="Arial 15 bold"

        # start frame
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid(row=0)

        # open the logo image
        image = Image.open("logo.png")

        # resize image
        resize_image = image.resize((320,60))
        img = ImageTk.PhotoImage(resize_image)
        self.logo_label = Label(self.start_frame, image=img)
        self.logo_label.image =img
        self.logo_label.grid(row=0)

        # Heading
        self.job_charge_label = Label(self.start_frame, text="Job Charge Calculator",
                                       font="Arial 21 bold")
        self.job_charge_label.grid(row=1)

        # Instructions label
        self.calculator_instructions = Label(self.start_frame, font="Arial 12 italic",
                                          text="Please fill out the following job information "
                                               "and press the 'Enter Job' button once finished."
                                               " At least one service needs to be selected. "
                                               "Press the 'how All Jobs' button can view all "
                                               "the job information.", wrap=275, justify=LEFT,
                                          padx=10, pady=10)
        self.calculator_instructions.grid(row=2)

        # entry frame(row 1)
        self.entry_frame = Frame(self.start_frame)
        self.entry_frame.grid(row=3)

        # Job number label
        self.job_number_label = Label(self.entry_frame, text="Job Number:",
                                         font=heading, anchor="w", width=14)
        self.job_number_label.grid(row=0, column=0, padx=0,pady=5)
        # Job number entry box
        self.job_number_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.job_number_entry.grid(row=0,column=1,padx=0,pady=5)

        # Customer name label
        self.customer_name_label = Label(self.entry_frame, text="Customer Name:",
                                         font=heading,anchor="w", width=14)
        self.customer_name_label.grid(row=1, column=0, padx=0,pady=5)
        # Customer entry box
        self.customer_name_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.customer_name_entry.grid(row=1,column=1,padx=0,pady=5)

        # Distance label
        self.distance_label = Label(self.entry_frame, text="Distance:",
                                         font=heading,anchor="w", width=14)
        self.distance_label.grid(row=2, column=0, padx=0,pady=5)
        # Distance entry bo
        self.distance_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.distance_entry.grid(row=2,column=1,padx=0,pady=5)

        # Minutes on virus protection
        self.minute_label = Label(self.entry_frame, text="Minutes on\nVirus Protection:",
                                         font=heading,justify=LEFT)
        self.minute_label.grid(row=3, column=0, padx=0,pady=5)
        # minutes on virus protection entry box
        self.minute_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.minute_entry.grid(row=3,column=1,padx=0,pady=5)

        # WOF and Tune
        self.WOF_and_tune_label = Label(self.entry_frame, text="WOF and Tune:",
                                         font=heading,anchor="w", width=14)
        self.WOF_and_tune_label.grid(row=4, column=0, padx=0,pady=5)
        # WOF and Tune radio button
        var = IntVar
        self.WOF_and_tune_radiobutton = Radiobutton(self.entry_frame,variable=var,
                                                    value=1)
        self.WOF_and_tune_radiobutton.grid(row=4, column=1, padx=0,pady=5)

        # button frame
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=4)

        # error message
        self.error_message_label = Label(self.button_frame,text="",
                                         font=heading)
        self.error_message_label.grid(row=0,pady=10)

        # Buttons
        self.show_job_button = Button(self.button_frame, text="Show all Job")
        self.show_job_button.grid(row=1, column=0,ipadx=20,ipady=5)

        self.enter_job_button = Button(self.button_frame, text="Enter Job")
        self.enter_job_button.grid(row=1, column=1,ipadx=20,ipady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start(root)

    root.mainloop()
