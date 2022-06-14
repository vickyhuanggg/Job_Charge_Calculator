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
                                          padx=10, pady=10,fg="#458B00")
        self.calculator_instructions.grid(row=2)

        # entry frame(row 1)
        self.entry_frame = Frame(self.start_frame)
        self.entry_frame.grid(row=3)

        # Job number label
        self.job_number_label = Label(self.entry_frame, text="Job Number:",
                                         font=heading)
        self.job_number_label.grid(row=0, column=0, padx=0,pady=5, sticky="w")
        # Job number entry box
        self.job_number_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.job_number_entry.grid(row=0,column=1,padx=0,pady=5)

        # Customer name label
        self.customer_name_label = Label(self.entry_frame, text="Customer Name:",
                                         font=heading)
        self.customer_name_label.grid(row=1, column=0, padx=0,pady=5,sticky="w")
        # Customer entry box
        self.customer_name_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.customer_name_entry.grid(row=1,column=1,padx=0,pady=5)

        # Distance label
        self.distance_label = Label(self.entry_frame, text="Distance:",
                                         font=heading)
        self.distance_label.grid(row=2, column=0, padx=0,pady=5,sticky="w")
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

        # wof and Tune
        self.wof_and_tune_label = Label(self.entry_frame, text="WOF and Tune:",
                                         font=heading)
        self.wof_and_tune_label.grid(row=4, column=0, padx=0,pady=5,sticky="w")
        # wof and Tune radio button
        self.var = IntVar()
        wof_var=self.var
        self.wof_and_tune_radiobutton = Radiobutton(self.entry_frame,variable=wof_var,
                                                    value=1)
        self.wof_and_tune_radiobutton.grid(row=4, column=1, padx=0,pady=5)

        # button frame
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=4)

        # error message
        self.error_message_label = Label(self.button_frame,text="",
                                         font="Arial 14 italic",fg="#B22222")
        self.error_message_label.grid(row=0,columnspan=2,pady=10)

        # Buttons
        self.show_job_button = Button(self.button_frame, text="Show all Job",
                                      command=self.to_history,bg="#1E90FF")
        self.show_job_button.grid(row=1, column=0,ipadx=20,ipady=5)

        self.enter_job_button = Button(self.button_frame, text="Enter Job",
                                       command=self.check_entries, bg="#EE3B3B")
        self.enter_job_button.grid(row=1, column=1,ipadx=20,ipady=5)

        # disabled show_job_button at the start
        self.show_job_button.config(state=DISABLED)

    def check_entries(self):
        job_number = self.job_number_entry.get()
        customer_name = self.customer_name_entry.get()
        distance = self.distance_entry.get()
        minute = self.minute_entry.get()
        wof_and_tune = self.var.get()

        # set error background colours (and assume that there are no errors at the start
        error_back = "#ffafaf"
        has_errors = "no"

        # disabled the button so the show_job button is always disabled at first once the enter_job button is pressed
        self.show_job_button.config(state=DISABLED)

        # change background to white
        self.job_number_entry.config(bg="white")
        self.customer_name_entry.config(bg="white")
        self.distance_entry.config(bg="white")
        self.minute_entry.config(bg="white")
        self.error_message_label.config(text="")

        # check at least one service is chosen
        if wof_and_tune == 1 or len(minute) != 0:

            # check job_number entry can't be empty
            if len(job_number) == 0:
                has_errors = "yes"
                error_feedback = "It shouldn't be empty"
                any_entry = self.job_number_entry

            # check customer_name entry can't be empty
            elif len(customer_name) == 0:
                has_errors = "yes"
                error_feedback = "It shouldn't be empty"
                any_entry = self.customer_name_entry

            # check distance entry can't be empty
            elif len(distance) == 0:
                has_errors = "yes"
                error_feedback = "It shouldn't be empty"
                any_entry = self.distance_entry

            else:
                # check job_number entry can't be str
                if not job_number.isnumeric():
                    has_errors = "yes"
                    error_feedback = "Number(s) should be entered"
                    any_entry = self.job_number_entry

                # check distance entry can't be str
                elif distance.isalpha():
                    has_errors = "yes"
                    error_feedback = "Number(s) should be entered"
                    any_entry = self.distance_entry

                # check minute entry can't be str when the wof_and _tune is not chosen
                elif not minute.isnumeric() and wof_and_tune != 1:
                    has_errors = "yes"
                    error_feedback = "Number(s) should be entered"
                    any_entry = self.minute_entry

                # check minute entry can't be str when the wof_and_tune is chosen
                elif not minute.isnumeric() and wof_and_tune == 1 and len(minute)>0:
                    has_errors = "yes"
                    error_feedback = "Number(s) should be entered"
                    any_entry = self.minute_entry

                # check customer_name entry can't be digit
                elif not customer_name.isalpha():
                    has_errors = "yes"
                    error_feedback = "It shouldn't have number(s)"
                    any_entry = self.customer_name_entry


                else:
                    # active the button
                    self.show_job_button.config(state=NORMAL)

        else:
            self.error_message_label.config(text="At least one service needs to be selected")

        if has_errors == "yes":
            any_entry.config(bg=error_back)
            self.error_message_label.config(text=error_feedback)




    def to_history(self):

        History(self)

class History:
     def __init__(self,partner):


        heading="Arial 12 bold"
        content="Areal 12"

        # disable buttons
        partner.show_job_button.config(state=DISABLED)
        partner.enter_job_button.config(state=DISABLED)

        # sets up child window
        self.hist_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.hist_box.protocol('WM_DELETE_WINDOW', partial(self.close_hist, partner))

        # set up Gui frame
        self.hist_frame = Frame(self.hist_box)
        self.hist_frame.grid()

        # set up heading (row 0)
        self.job_info_heading_label = Label(self.hist_frame, text="Job Information",
                                         font="arial 19 bold")
        self.job_info_heading_label.grid(row=0)



     def close_hist(self, partner):
        # put buttons back to normal...
        partner.show_job_button.config(state=NORMAL)
        partner.enter_job_button.config(state=NORMAL)
        self.hist_box.destroy()





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start(root)

    root.mainloop()
