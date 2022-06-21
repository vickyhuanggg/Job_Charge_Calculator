from tkinter import *
from functools import partial   # To prevent unwanted windows


class Start:
    def __init__(self, parent):
        # make a list to store distances
        self.distances = []

        heading="Arial 15 bold"
        
        # start frame
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid(row=0)

        # Distance label
        self.distance_label = Label(self.start_frame, text="Distance:",
                                         font=heading,anchor="w", width=14)
        self.distance_label.grid(row=2, column=0, padx=0,pady=5)

        # Distance entry bo
        self.distance_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.distance_entry.grid(row=2,column=1,padx=0,pady=5)

        self.price_label = Label(self.start_frame, text = "")
        self.price_label.grid(row=3,columnspan=2)

        self.calculate_button = Button(self.start_frame, text = "Calculate",
                                       command=self.check_distance)
        self.calculate_button.grid(row=4,columnspan=2)


    def check_distance(self):
        prices=[]
        # get the distance from the entry and round up the distance
        travel_distance = round(float(self.distance_entry.get()))


        print(round(16.5))

        # store the data in the list
        self.distances.append(travel_distance)
        print(self.distances)

        fixed_price = 10

        # check every distance from the list
        for i in self.distances:

            if i <= 5:
                price = "{:.2f}".format(fixed_price)
                self.price_label.config(text=price)
                prices.append(price)

            elif i >5:
                price = "{:.2f}".format(fixed_price + (i - 5) * 0.5)
                self.price_label.config(text=price)
                prices.append(price)
        print(prices)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Start(root)

    root.mainloop()
