from tkinter import *
from functools import partial   # To prevent unwanted windows

class Start:
    def __init__(self, parent):
        self.charge=[]

        # start frame
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Heading (row 0)
        self.job_charge_label = Label(self.start_frame, text="Job Charge Calculator",
                                       font="Arial 19 bold")
        self.job_charge_label.grid(row=0)

        # entry frame(row 1)
        self.entry_frame = Frame(self.start_frame)
        self.entry_frame.grid(row=1)

        # Entry box
        self.job_charge_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.job_charge_entry.grid(row=0)

        # button frame (row 2)
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=2)
        # Buttons
        self.show_job_button = Button(self.button_frame, text="Show all Job", command=lambda: self.to_history(self.charge))
        self.show_job_button.grid(row=0, column=0)

        self.enter_job_button = Button(self.button_frame, text="Enter Job", command=self.history_stored)
        self.enter_job_button.grid(row=0, column=1)



    def history_stored(self):

        charge_info = self.job_charge_entry.get()
        self.charge.append(charge_info)


    def to_history(self,show_job):

        History(self,show_job)

class History:
    def __init__(self, partner,show_job):
        # the time of pressing the enter_button
        self.current = 0

        self.currents = IntVar()
        self.currents.set(self.current)


        # disable buttons
        partner.show_job_button.config(state=DISABLED)
        partner.enter_job_button.config(state=DISABLED)

        heading="Arial 12 bold"
        content="Areal 12"

        # sets up child window
        self.hist_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.hist_box.protocol('WM_DELETE_WINDOW', partial(self.close_hist, partner))

        # set up Gui frame
        self.hist_frame = Frame(self.hist_box)
        self.hist_frame.grid()

        # set up heading (row 0)
        self.charge_heading_label = Label(self.hist_frame, text="Charge Information",
                                         font="arial 19 bold")
        self.charge_heading_label.grid(row=0)

        # charge frame (row 1)
        self.charge_frame = Frame(self.hist_frame)
        self.charge_frame.grid(row=1)

        # Charge and Charge value label
        self.charge_label = Label(self.charge_frame, text="Job charge:",
                                         font=heading, anchor="e")
        self.charge_label.grid(row=0, column=0, padx=0)

        self.charge_value_label = Label(self.charge_frame, font=content,
                                               text="${}".format(show_job[0]),
                                               anchor="w")
        self.charge_value_label.grid(row=0, column=1, padx=0)

        # button frame(row 2)
        self.nextbtn_frame = Frame(self.hist_frame)
        self.nextbtn_frame.grid(row=2)

        # 'next' button
        self.next_button = Button(self.nextbtn_frame, text="next",
                                  width=10,command=partial(lambda: self.nextbtn(show_job)))
        self.next_button.grid(row=0)

    def close_hist(self, partner):
        # put buttons back to normal...
        partner.show_job_button.config(state=NORMAL)
        partner.enter_job_button.config(state=DISABLED)
        self.hist_box.destroy()

    def nextbtn (self,show_job):
        time = self.currents.get()
        time += 1
        self.currents.set(time)
        self.charge_value_label.configure(text="${}".format(show_job[time]))

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start(root)

    root.mainloop()
