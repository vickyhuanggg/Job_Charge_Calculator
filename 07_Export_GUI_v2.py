from tkinter import *
from functools import partial   # To prevent unwanted windows
from PIL import Image, ImageTk
import re

class Start:
    def __init__(self, parent):

        # In actual program this is blank
        self.job_information_list=[[123,124,125],["Vicky Huang", "Ellite Tang",
                                                  "Amy Zhen"],[116.50, 48.00, 126.20]]
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

        heading="Arial 15 bold"
        content="Areal 15"

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
        self.job_info_heading_label.grid(row=1,padx=0,pady=10)

        # job information (row 2)
        self.detail_frame = Frame(self.hist_frame)
        self.detail_frame.grid(row=2)

         # job number label and its value
        self.show_job_number_label = Label(self.detail_frame, font=heading,
                                           text="Job Number:")
        self.show_job_number_label.grid(row=0,column=0, padx=0, pady=5, sticky="w")

        self.show_job_number_value_label = Label(self.detail_frame,
                                      font=content, text=job_information[0][-1])
        self.show_job_number_value_label.grid(row=0, column=1, padx=0, pady=5)

        # job name label and its value
        self.show_customer_name_label = Label(self.detail_frame, font=heading,
                                           text="Customer Name:")
        self.show_customer_name_label.grid(row=1,column=0, padx=0, pady=5, sticky="w")

        self.show_customer_name_value_label = Label(self.detail_frame,
                                      font=content, text=job_information[1][-1])
        self.show_customer_name_value_label.grid(row=1, column=1, padx=0, pady=5)

        # job charge label and its value
        self.show_job_charge_label = Label(self.detail_frame, font=heading,
                                           text="Job charge:")
        self.show_job_charge_label.grid(row=2,column=0, padx=0, pady=5, sticky="w")

        self.show_job_charge_value_label = Label(self.detail_frame,
                                      font=content, text="$ {}".format(job_information[2][-1]))
        self.show_job_charge_value_label.grid(row=2, column=1, padx=0, pady=5)

        # job information message
        self.information_message_label = Label(self.hist_frame, font=heading,
                                               text="",fg="#B22222")
        self.information_message_label.grid(row=3, columnspan=2, pady=5)

        # buttons frame (row 3)
        self.buttons_frame = Frame(self.hist_frame)
        self.buttons_frame.grid(row=4)

        # previous button
        self.previous_button = Button(self.buttons_frame, text="Previous",
                                      width=10, bg="#87CEFF", font="arial 15 bold",
                                      command=partial(lambda: self.prev_next_btn(job_information, 0)))
        self.previous_button.grid(row=0, column=0,pady=5)

        # disable the previous_button first as it's the first information
        self.previous_button.config(state=DISABLED)

        # next button
        self.next_button = Button(self.buttons_frame, text="Next",
                                  width=10,bg="#FFC1C1", font="arial 15 bold",
                                  command=partial(lambda: self.prev_next_btn(job_information, 1)))
        self.next_button.grid(row=0, column=1,pady=5)

        # Export Button
        self.export_button = Button(self.buttons_frame, text="Export",
                                    width=10, bg="#1E90FF",
                                    font="arial 16 bold",
                                    command=lambda: self.export(job_information))
        self.export_button.grid(row=5, column=0,pady=5)
        # Dismiss Button
        self.dismiss_btn = Button(self.buttons_frame, text="Dismiss",
                                  width=10, bg="#EE3B3B",
                                  font="arial 16 bold",command=partial(self.close_hist, partner))
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

    def export(self,job_information):
        Export(self, job_information)


class Export:
    def __init__(self, partner, job_information):
        print(job_information)

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'release' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # set up child GUI Frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # open the logo image
        image = Image.open("logo.png")

        # resize image
        resize_image = image.resize((320,60))
        img = ImageTk.PhotoImage(resize_image)
        self.logo_label = Label(self.export_frame, image=img)
        self.logo_label.image =img
        self.logo_label.grid(row=0)

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions", font="arial 14 bold")
        self.how_heading.grid(row=1)

        # Export instructions(label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                 "in the box below "
                                 "and press the Save "
                                 "button to save your "
                                 "job information history "
                                 "to a text file.",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=2)

        # Warning text (label,row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                 "you enter below "
                                 "already exists, "
                                 "its contents will "
                                 "be replaced with "
                                 "your job information "
                                 "history", justify=LEFT, bg="#ffafaf", fg="maroon", font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=3,pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=4, pady=10)

         # Error Message Labels
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=5)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=6, pady=10)

        # Save and Cancel Buttons(row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#1E90FF", fg="black",
                                  command=partial(lambda: self.save_history(partner, job_information)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#EE3B3B", fg="black",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, job_information):
        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename -{}".format(problem))
            # change the entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file and then clost
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # heading for job_information
            f.write("Job Information\n\n")

            # add new line at end of each job information
            for job in range(len(job_information)):
                job_details = "Job Number: {}\n" \
                              "Customer Name: {}\n" \
                              "Job Charge: ${}".format(job_information[0][job],job_information[1][job],job_information[2][job])
                f.write(job_details +"\n\n")


            # close file
            f.close()

            # close dialogue
            self.close_export(partner)


    def close_export(self, partner):
        #put export button back to normal...

        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start(root)
    root.mainloop()
