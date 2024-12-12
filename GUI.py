from methods import *
from tkinter import *
import methods


class GUI:
    def __init__(self, window):
        "creates label and entry box for id"
        self.window = window
        self.frame_1 = Frame(self.window)
        self.label1 = Label(self.frame_1, text="Identification ")
        self.id_txt = Entry(self.frame_1, width=30)
        self.label1.pack(side="left", padx=5)
        self.id_txt.pack(side="left")
        self.frame_1.pack(anchor='w', pady=10)

        "creates label for above the candidates and write ins"
        self.frame_2 = Frame(self.window)
        self.label2 = Label(self.frame_2, text="Candidates ")
        self.label2.pack(side="left", padx=150)
        self.frame_2.pack(anchor='w', pady=20)

        "creates radio buttons for voting"
        self.frame_3 = Frame(self.window)
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_can_1 = Radiobutton(self.frame_3, text="Jill", variable=self.radio_1, value=1,command = self.shape )
        self.radio_can_2 = Radiobutton(self.frame_3, text="Bill", variable=self.radio_1, value=2, command = self.shape)
        self.radio_can_3 = Radiobutton(self.frame_3, text="Write in", variable=self.radio_1, value=3, command = self.shape)
        self.radio_can_1.pack(side="left", padx=50)
        self.radio_can_2.pack(side="left")
        self.radio_can_3.pack(side="left")
        self.frame_3.pack(anchor='w', pady=20)


        "creates write in box,Lock in button,write_in label, and response"
        self.frame_5 = Frame(self.window)
        self.label_w = Label(self.frame_5, text="")
        self.writein = Entry(self.frame_5, width=15)
        self.label_response = Label(self.frame_5, text="Result:")
        self.vote_button = Button(self.frame_5, text="Lock in Vote", command=self.vote)
        self.vote_button.pack(side="bottom", padx=100)
        self.label_response.pack(side="bottom", padx=100)
        self.label_w.pack(side="left")
        self.writein.pack(side="left",padx = 100)
        self.frame_5.pack(anchor="w")
        self.writein.pack_forget()



    def vote(self):
        "sends the votes to be checked and changes labels if the voter already has or isnt valid"
        safer_id = self.id_txt.get()
        vote_num = self.radio_1.get()
        try:
            "checks if the id has already voted"
            if methods.check_id(safer_id):
                self.label_response.config(text=(f"Already voted"))
            else:
                "makes sure the id is a posotive number"
                if id_is_pos(safer_id):
                    raise TypeError

                if  vote_num == 3:
                        "if voted the selection is 3 then it will check if it is string or not"
                        write_in_name= self.writein.get()
                        if methods.valid_write_in(write_in_name):
                            "if it is then it will will display  who you voted for and add it to the csv file and clear all entry boxes "
                            self.label_response.config(text=(f"Voted {self.writein.get()}"))
                            methods.add_vote(safer_id,self.writein.get())
                            self.writein.delete(0, END)
                            self.id_txt.delete(0,END)
                            self.radio_1.set(0)
                            self.writein.pack_forget()
                            self.label_w.config(text = "")
                            self.label_response.config(fg="black")
                        else:
                            "changes label_response to say you must have a name to write in and clears everything"
                            self.label_response.config(text=(f"Must be a Name"))
                            self.writein.delete(0, END)
                            self.id_txt.delete(0,END)
                            self.radio_1.set(0)
                            self.writein.pack_forget()
                            self.label_w.config(text="")
                            self.label_response.config(fg="red")
                elif vote_num == 2:
                    "adds vote of bill to the csv and tell who you voted for on label_response"
                    self.label_response.config(text=(f"Voted Bill"))
                    methods.add_vote(safer_id, "bill")
                    self.writein.delete(0, END)
                    self.id_txt.delete(0,END)
                    self.radio_1.set(0)
                    self.label_response.config(fg="black")
                elif vote_num == 1:
                    "adds vote of jill to the csv and tell who you voted for on label_response"
                    self.label_response.config(text=(f"Voted Jill"))
                    methods.add_vote(safer_id, "jill")
                    self.writein.delete(0, END)
                    self.id_txt.delete(0,END)
                    self.radio_1.set(0)
                    self.label_response.config(fg="black")
                else:
                    "this will pop up if you didn't pick a candidate"
                    self.label_response.config(text=(f"Select a Candidate"))
        except ValueError:
            "catches value error with id"
            self.label_response.config(text = "Mist be a valid numerical id")
            self.label_response.config(fg="red")
            self.writein.delete(0, END)
            self.id_txt.delete(0, END)
            self.radio_1.set(0)
            self.label_w.config(text="")

        except TypeError:
            "catches if the id is negative"
            self.label_response.config(text=(f"ID needs to be positive"))
            self.label_response.config(fg="red")
            self.writein.delete(0, END)
            self.id_txt.delete(0, END)
            self.radio_1.set(0)
            self.label_w.config(text="")


    def shape(self):
        "shape changes the visibility of the write in text box based on which radio button is selected"
        shape = self.radio_1.get()

        if shape == 1:
            self.writein.delete(0, END)
            self.writein.pack_forget()
            self.label_w.config(text = " ")
        elif shape == 2:
            self.writein.delete(0,END)
            self.writein.pack_forget()
            self.label_w.config(text=" ")

        elif shape == 3:
            self.writein.pack()
            self.label_w.config(text="Write-in")












