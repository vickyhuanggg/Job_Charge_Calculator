from tkinter import *
from functools import partial   # To prevent unwanted windows
from PIL import Image, ImageTk
from math import *
import re
import os.path

class Start:
    def __init__(self, parent):
        # a nested list to store job information of job numbers, customer names and job charge
        self.job_information_list=[[],[],[]]

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
                                               "Press the 'show All Jobs' button can view all "
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
        self.distance_label = Label(self.entry_frame, text="Distance(km):",
                                         font=heading)
        self.distance_label.grid(row=2, column=0, padx=0,pady=5,sticky="w")

        # Distance entry bo
        self.distance_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.distance_entry.grid(row=2,column=1,padx=0,pady=5)

        # Minutes on virus protection
        self.minute_label = Label(self.entry_frame, text="Minutes on\nVirus Protection:",
                                         font=heading,justify=LEFT)
        self.minute_label.grid(row=3, column=0, padx=0,pady=5)

        # minutes on virus protection spinbox
        self.minute_var = IntVar()
        self.minute_var.set(0)
        minute_var = self.minute_var
        # minutes on virus protection entry box
        self.minute_entry = Entry(self.entry_frame, textvariable=minute_var, font="Arial 16 bold")
        self.minute_entry.grid(row=3,column=1,padx=0,pady=5)

        # wof and Tune
        self.wof_and_tune_label = Label(self.entry_frame, text="WOF and Tune:",
                                         font=heading)
        self.wof_and_tune_label.grid(row=4, column=0, padx=0,pady=5,sticky="w")

        # wof and Tune radio button
        self.var = IntVar()
        wof_var=self.var
        self.wof_and_tune_checkbutton = Checkbutton(self.entry_frame,variable=wof_var,
                                                    onvalue=1, offvalue=0)
        self.wof_and_tune_checkbutton.grid(row=4, column=1, padx=0,pady=5,sticky="w")

        # button frame
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=4)

        # error message
        self.error_message_label = Label(self.button_frame,text="",
                                         font="Arial 14 italic",fg="#B22222")
        self.error_message_label.grid(row=0,columnspan=2,pady=10)

        # Buttons
        self.show_all_job_button = Button(self.button_frame, text="Show all Job",
                                      command=lambda:self.to_history(self.job_information_list),
                                      bg="#1E90FF")
        self.show_all_job_button.grid(row=1, column=0,ipadx=20,ipady=5)

        self.enter_job_button = Button(self.button_frame, text="Enter Job",
                                       command=self.check_entries, bg="#EE3B3B")
        self.enter_job_button.grid(row=1, column=1,ipadx=20,ipady=5)

        # disabled show_all_job_button at the start
        self.show_all_job_button.config(state=DISABLED)

    def check_entries(self):
        # get job number, customer name, distance and minute and wof and tune from the entry box or checkbutton or spin box
        job_number = self.job_number_entry.get()
        customer_name = self.customer_name_entry.get()
        distance = self.distance_entry.get()
        minute = self.minute_entry.get()
        wof_and_tune = self.var.get()

        # set error background colours (and assume that there are no errors at the start
        error_back = "#ffafaf"
        has_errors = "no"

        # disabled the button so the show_job button is always disabled at first once the enter_job button is pressed
        self.show_all_job_button.config(state=DISABLED)

        # change background to white
        self.job_number_entry.config(bg="white")
        self.customer_name_entry.config(bg="white")
        self.distance_entry.config(bg="white")
        self.minute_entry.config(bg="white")
        self.error_message_label.config(text="")
        self.error_message_label.config(fg="#B22222")

        try:
            # error handling for both alphabet and number in distance_entry
            distances = float(distance)

            # check at least one service is chosen
            if wof_and_tune == 0 and (len(minute) == 0 or int(minute)==0):
                self.error_message_label.config(text="At least one service needs to be selected")

            # the minute spinbox goes back to default value 0 when the owner doesn't enter anything
            elif wof_and_tune == 1 and len(minute) == 0:
                self.minute_var.set(0)

            # check job_number entry can't be empty
            elif len(job_number) == 0:
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
                    error_feedback = "A positive integer should be entered"
                    any_entry = self.job_number_entry

                # check the job number can't be negative
                elif int(job_number) <= 0:
                    has_errors = "yes"
                    error_feedback = "The integer should bigger than 0"
                    any_entry = self.job_number_entry

                # check distance entry can't be str
                elif all(letter.isalpha() or letter.isspace() for letter in distance):
                    has_errors = "yes"
                    error_feedback = "A positive number should be entered"
                    any_entry = self.distance_entry

                # check minute entry can't be str when the wof_and _tune is not chosen
                elif not minute.isnumeric() and wof_and_tune != 1:
                    has_errors = "yes"
                    error_feedback = "A positive integer should be entered"
                    any_entry = self.minute

                # check job_number entry can't be str when the wof_and_tune is chosen
                elif not minute.isnumeric() and wof_and_tune == 1 and len(minute)>0:
                    has_errors = "yes"
                    error_feedback = "A positive integer should be entered"
                    any_entry = self.minute

                # check customer_name entry can't be integer or decimal number
                elif not all(letter.isalpha() or letter.isspace() for letter in customer_name):
                    has_errors = "yes"
                    error_feedback = "It shouldn't have number or symbol"
                    any_entry = self.customer_name_entry

                # allow the owner to enter 0 when wof_and_tune is chosen
                elif int(minute) <= 0 and wof_and_tune != 1:
                    has_errors = "yes"
                    error_feedback = "The integer should be bigger than 0"
                    any_entry = self.minute

                # error handling for number that is smaller or equal than zero
                elif distances <= 0:
                    has_errors = "yes"
                    error_feedback = "The number should be bigger than 0"
                    any_entry = self.distance_entry

                else:
                    # active the button
                    self.show_all_job_button.config(state=NORMAL)
                    self.job_information_list[0].append(job_number)
                    self.job_information_list[1].append(customer_name.title())
                    self.calculation()
                    # the message of job being saved
                    self.error_message_label.config(text="Job {} is saved".format(self.job_information_list[0][-1]),fg="green")
                    # clear all the job information once the owner press the enter job button
                    self.job_number_entry.delete(0, 'end')
                    self.customer_name_entry.delete(0, 'end')
                    self.distance_entry.delete(0, 'end')
                    self.minute_var.set(0)
                    self.var.set(0)

            if has_errors == "yes":
                any_entry.config(bg=error_back)
                self.error_message_label.config(text=error_feedback)

        except ValueError:
            self.error_message_label.config(text="It should be a number")
            self.distance_entry.config(bg=error_back)

    def calculation(self):
        WOF_AND_TUNE = float(100)
        FIXED_PRICE = float(10)
        DISTANCE_PRICE = 0.5
        MINUTE_PRICE = 0.8
        FIXED_DISTANCE = 5

        # get the distance from the entry and round up the distance, get minute, get checkbutton
        travel_distance = float(self.distance_entry.get())
        minute = self.minute_entry.get()
        wof_and_tune = self.var.get()

        # to check the first decimal place is smaller or bigger than 0.5
        if travel_distance - floor(travel_distance) < 0.5:
            round_travel_distance = floor(travel_distance)
        else:
            round_travel_distance = ceil(travel_distance)

        # check distance
        if round_travel_distance <= FIXED_DISTANCE:
            price = FIXED_PRICE

        elif round_travel_distance > FIXED_DISTANCE:
            price = FIXED_PRICE + (round_travel_distance - FIXED_DISTANCE) * DISTANCE_PRICE

        # check services
        if wof_and_tune == 1 and len(minute) == 0:
            total_price = price + WOF_AND_TUNE
            total_prices = "{:.2f}".format(total_price, 2)
            self.job_information_list[2].append(total_prices)

        elif len(minute) != 0 and wof_and_tune == 0:
            total_price = price + float(minute) * MINUTE_PRICE
            total_prices = "{:.2f}".format(total_price, 2)
            self.job_information_list[2].append(total_prices)

        else:
            total_price = price + WOF_AND_TUNE + float(minute) * MINUTE_PRICE
            total_prices = "{:.2f}".format(total_price, 2)
            self.job_information_list[2].append(total_prices)

        print(self.job_information_list)


    def to_history(self,job_information):

        History(self,job_information)

class History:
    def __init__(self, partner, job_information):
        # the time of pressing the enter_button
        self.current = -1

        self.currents = IntVar()
        self.currents.set(self.current)

        # disable show all job button and enter job button
        partner.show_all_job_button.config(state=DISABLED)
        partner.enter_job_button.config(state=DISABLED)

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
        self.previous_button = Button(self.buttons_frame, text="< Previous",
                                      width=10, bg="#87CEFF", font="arial 15 bold",
                                      command=partial(lambda: self.prev_next_btn(job_information, 0)))
        self.previous_button.grid(row=0, column=0,pady=5)

        # disable the previous_button first as it's the first information
        self.previous_button.config(state=DISABLED)

        # next button
        self.next_button = Button(self.buttons_frame, text="Next >",
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

        # change the value of the job information once the next or previous button is pressed
        if not last_job_information == "yes":
            self.show_job_number_value_label.config(text=job_information[0][time])
            self.show_customer_name_value_label.config(text=job_information[1][time])
            self.show_job_charge_value_label.config(text="$ {}".format(job_information[2][time]))

        else:
            self.information_message_label.config(text=prev_next_message)

    def close_hist(self, partner):
        # put help button back to normal...

        partner.show_all_job_button.config(state=NORMAL)
        partner.enter_job_button.config(state=NORMAL)
        self.hist_box.destroy()

    def export(self, job_information):
        Export(self, job_information)

class Export:
    def __init__(self, partner, job_information):

        # disable export buttons
        partner.export_button.config(state=DISABLED)
        partner.dismiss_btn.config(state=DISABLED)
        partner.next_button.config(state=DISABLED)
        partner.previous_button.config(state=DISABLED)

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

        # check filename
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

        elif os.path.isfile((filename + ".txt")):
            problem = "This filename is already exist"
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
            for job in range(len(job_information[0])):
                job_details = "Job Number: {}\n" \
                              "Customer Name: {}\n" \
                              "Job Charge: ${}".format(job_information[0][job],job_information[1][job],job_information[2][job])
                f.write(job_details +"\n\n")


            # close file
            f.close()

            # close dialogue
            self.close_export(partner)


    def close_export(self, partner):
        # put buttons back to normal...

        partner.export_button.config(state=NORMAL)
        partner.dismiss_btn.config(state=NORMAL)
        partner.next_button.config(state=NORMAL)
        partner.previous_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start(root)
    root.mainloop()
