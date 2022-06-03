from tkinter import *
from functools import partial   # To prevent unwanted windows

class Start:
    def __init__(self):
        self.job_charge_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # start frame
        self.start_frame = Frame()
        self.start_frame.grid()

        # Heading Row
        self.job_charge_label =Label(self.start_frame, text="Job Charge Calculator",
                                  font="Arial 24 bold", padx=10, pady=10)
        self.job_charge_label.grid(row=0)

         # 'show all job' Button (row 1)
        self.show_job_button = Button(self.start_frame, text="Show All Job",
                                   font="Arial 14", padx=10, pady=10,
                                   command=lambda:self.to_history(self.job_charge_list))
        self.show_job_button.grid(row=1)

    def to_history(self,job_charge):

        History(self,job_charge)

class History:
    def __init__(self, partner,job_charge):
        print(job_charge)
        self.current = 0

        self.balance = IntVar()
        self.balance.set(self.current)

        # disable button
        partner.show_job_button.config(state=DISABLED)


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
        self.charge_heading_label = Label(self.hist_frame, text="Job Information",
                                         font="arial 19 bold")
        self.charge_heading_label.grid(row=0)

        # charge and charge value label
        self.charge_label = Label(self.hist_frame, text="Job Charge:",
                                         font=heading, anchor="e")
        self.charge_label.grid(row=1, column=0, padx=0)

        self.charge_value_label = Label(self.hist_frame, font=content,
                                               text="",
                                               anchor="w")
        self.charge_value_label.grid(row=1, column=1, padx=0)

        # next button
        self.next_button = Button(self.hist_frame, text="next",
                                  width=10,command=partial(lambda: self.nextbtn(job_charge)))
        self.next_button.grid(row=2)

    def close_hist(self, partner):
        # put buttons back to normal...
        partner.show_job_button.config(state=NORMAL)
        self.hist_box.destroy()
    def nextbtn (self,job_charge):
        time = self.balance.get()
        time += 1
        self.balance.set(time)
        self.charge_value_label.configure(text="${}".format(job_charge[time]))

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start()

    root.mainloop()
