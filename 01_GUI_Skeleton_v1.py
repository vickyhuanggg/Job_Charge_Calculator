from tkinter import *
from functools import partial   # To prevent unwanted windows

class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self.job_charge_label = Label(self.start_frame, text="Job Charge Calculator",
                                       font="Arial 19 bold")
        self.job_charge_label.grid(row=0)

        # Entry box (row 1)
        self.job_charge_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.job_charge_entry.grid(row=1)

        # 'show job' button and 'enter job' button (row 2)
        self.show_job_button = Button(text="Show all Job", command=self.to_history)
        self.show_job_button.grid(row=2, column=0, pady=10)

        self.enter_job_button = Button(text="Enter Job")
        self.enter_job_button.grid(row=2, column=1, pady=10)


    def to_history(self):
        charge_info = self.job_charge_entry.get()
        History(self, charge_info)

class History:
    def __init__(self, partner, charge_info):
        print(charge_info)

        # disable buttons
        partner.show_job_button.config(state=DISABLED)
        partner.enter_job_button.config(state=DISABLED)

        # initialise variables
        self.balance = IntVar()
        self.balance.set(charge_info)

        # GUI Setup
        self.information_box = Toplevel()
        self.information_frame = Frame(self.information_box)
        self.information.grid()

        # Heading Row
        self.heading_label = Label(self.information_frame, text="Job Information",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)


        self.info_label = Label(self.information_frame, text="")
        self.info_label.grid(row=1)

        self.next_button = Button(self.information_frame, text="Next",
                                  command=partial(self.next_information))
        self.next_button.grid(row=2)

    def next_information(self):
        # retrieve the balance from the initial function
        current_balance = self.balance.get()


        # for testing purposes, just add 1
        current_balance += 1

        # set balance to adjusted balance
        self.balance.set(current_balance)

        # Edit label so user can see their job charge
        self.info_label.configure(text="Job Charge: ${}".format(current_balance))

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start(root)

    root.mainloop()
