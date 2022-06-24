from tkinter import *
from functools import partial   # To prevent unwanted windows
from PIL import Image, ImageTk

class Start:
    def __init__(self, parent):

        # In actual program this is blank
        self.job_information_list=[[123,124,125],["Vicky Huang", "Ellite Tang",
                                                  "Amy zhen"],[116.50, 48.00, 126.20]]
        print(self.job_information_list)
        # start frame
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Job charge calculating heading
        self.job_charge_label = Label(self.start_frame, text="Job Charge Calculator",
                                       font="Arial 21 bold")
        self.job_charge_label.grid(row=0)

        # Show all job button
        self.show_all_job_button = Button(self.start_frame, text="Show all Job",
                                      bg="#1E90FF",command=lambda: self.to_hist(self.job_information_list))
        self.show_all_job_button.grid(row=1)

    def to_hist(self, job_information):
        History(self, job_information)


class History:
    def __init__(self, partner, job_information):
        # the time of pressing the enter_button
        self.current = -1

        self.currents = IntVar()
        self.currents.set(self.current)

        # disable show all job button
        partner.show_all_job_button.config(state=DISABLED)

        heading="Arial 12 bold"
        content="Areal 12"

        # sets up child window
        self.hist_box = Toplevel()

        # if the owner presses cross at top, closes help and 'releases' help button
        self.hist_box.protocol('WM_DELETE_WINDOW', partial(self.close_hist, partner))

        # set up Gui frame
        self.hist_frame = Frame(self.hist_box)
        self.hist_frame.grid()

        # open the logo image
        image = Image.open("logo.png")

        # resize image
        resize_image = image.resize((320,60))
        img = ImageTk.PhotoImage(resize_image)
        self.logo_label = Label(self.hist_frame, image=img)
        self.logo_label.image =img
        self.logo_label.grid(row=0)

        # set up heading (row 0)
        self.job_info_heading_label = Label(self.hist_frame, text="Job Information",
                                         font="arial 19 bold")
        self.job_info_heading_label.grid(row=1,padx=0)

        # job information (row 2)
        self.detail_frame = Frame(self.hist_frame)
        self.detail_frame.grid(row=2)

         # job number label and its value
        self.show_job_number_label = Label(self.detail_frame, font=heading,
                                           text="Job Number:")
        self.show_job_number_label.grid(row=0,column=0, padx=0, pady=5, sticky="w")

        self.show_job_number_value_label = Label(self.detail_frame,
                                      font=content, text=job_information[0][-1])
        self.show_job_number_value_label.grid(row=0, column=1, padx=0, pady=5, sticky="w")

        # job name label and its value
        self.show_customer_name_label = Label(self.detail_frame, font=heading,
                                           text="Customer Name:")
        self.show_customer_name_label.grid(row=1,column=0, padx=0, pady=5, sticky="w")

        self.show_customer_name_value_label = Label(self.detail_frame,
                                      font=content, text=job_information[1][-1])
        self.show_customer_name_value_label.grid(row=1, column=1, padx=0, pady=5, sticky="w")

        # job charge label and its value
        self.show_job_charge_label = Label(self.detail_frame, font=heading,
                                           text="Job charge:")
        self.show_job_charge_label.grid(row=2,column=0, padx=0, pady=5, sticky="w")

        self.show_job_charge_value_label = Label(self.detail_frame,
                                      font=content, text="$ {}".format(job_information[2][-1]))
        self.show_job_charge_value_label.grid(row=2, column=1, padx=0, pady=5, sticky="w")

        # job information message
        self.information_message_label = Label(self.hist_frame, font=heading,
                                               text="",fg="#B22222")
        self.information_message_label.grid(row=3, columnspan=2, pady=5)

        # buttons frame (row 3)
        self.buttons_frame = Frame(self.hist_frame)
        self.buttons_frame.grid(row=4)

        # previous button
        self.previous_button = Button(self.buttons_frame, text="Previous",
                                  width=10, bg="#87CEFF", command=partial(lambda: self.prev_next_btn(job_information, 0)))
        self.previous_button.grid(row=0, column=0,pady=5)

        # disable the previous_button first as it's the first information
        self.previous_button.config(state=DISABLED)

        # next button
        self.next_button = Button(self.buttons_frame, text="Next",
                                  width=10,bg="#FFC1C1", command=partial(lambda: self.prev_next_btn(job_information, 1)))
        self.next_button.grid(row=0, column=1,pady=5)

         # Export Button
        self.export_button = Button(self.buttons_frame, text="Export",
                                    width=10, bg="#1E90FF",
                                    font="arial 15 bold")
        self.export_button.grid(row=5, column=0,pady=5)
        # Dismiss Button
        self.dismiss_btn = Button(self.buttons_frame, text="Dismiss",
                                  width=10, bg="#EE3B3B",
                                  font="arial 15 bold",command=partial(self.close_hist, partner))
        self.dismiss_btn.grid(row=5, column=1,pady=5)

    def prev_next_btn(self, job_information, button):
        # get value of which button is pressed
        self.buttons = IntVar()
        self.buttons.set(button)

        # assume there is no only a job information
        last_job_information = "no"

        # assume there is no prev_next_message first
        self.information_message_label.config(text="")

        # retrieve the which button is pressed
        chosen_button = self.buttons.get()

        # get the time of pressing the button
        time = self.currents.get()

        # check if next_button or previous button is pressed, 0 is prev and 1 is nex
        if chosen_button == 0:
            # go back to the previous information
            time += 1
            self.currents.set(time)

        else:
            # turn to the next information
            time -= 1
            self.currents.set(time)
            self.previous_button.config(state=NORMAL)

        # Previous button is disabled at the first page
        if time == -1:
            self.next_button.config(state=NORMAL)
            self.previous_button.config(state=DISABLED)

        # Next button is disabled when there is only one job information
        elif -(time) > len(job_information[0]):
            self.next_button.config(state=DISABLED)
            self.previous_button.config(state=DISABLED)
            last_job_information = "yes"
            prev_next_message = "Here is only one job information"

        # Next button is disabled when it's at the last page
        elif -(time) == len(job_information[0]):
            self.next_button.config(state=DISABLED)
            self.previous_button.config(state=NORMAL)
            self.information_message_label.config(text="This is the last job information")

        else:
            self.next_button.config(state=NORMAL)
            self.previous_button.config(state=NORMAL)

        if not last_job_information == "yes":
            self.show_job_number_value_label.config(text=job_information[0][time])
            self.show_customer_name_value_label.config(text=job_information[1][time])
            self.show_job_charge_value_label.config(text="$ {}".format(job_information[2][time]))

        else:
            self.information_message_label.config(text=prev_next_message)

    def close_hist(self, partner):
        # put help button back to normal...

        partner.show_all_job_button.config(state=NORMAL)
        self.hist_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start(root)

    root.mainloop()
