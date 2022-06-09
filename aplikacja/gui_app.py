#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename,askdirectory
import os
from controller import Controller
from PIL import ImageTk, Image
from tkinter import messagebox


def show_msg():
   messagebox.showinfo("Message","Hey There! I hope you are doing well.")


class Model:

    def print_results(self, results):
        self.text17.configure(state="normal")
        _text_ = results
        self.text17.delete(1.0,tk.END)
        self.text17.insert(tk.END,_text_)
        self.text17.configure(state="disabled")

    def import_and_analyze_csv(self):
        filename = askopenfilename(initialdir = ".",title = "Select csv file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.masterWindow.title(f"Analyzing {filename}")

        self.c.predict_from_csv(filename)
        self.results = self.c.last_pred_summary()

        self._analyze(filename=filename)


    def import_and_analyze_pcap(self):
        filename = askopenfilename(initialdir = ".",title = "Select pcap file",filetypes = (("pcap files","*.pcap"),("all files","*.*")))
        self.masterWindow.title(f"Analyzing {filename}")

        self.c.predict_from_pcap(filename)
        self.results = self.c.last_pred_summary()

        self._analyze(filename=filename)

    def _analyze(self,filename):
        self.masterWindow.title(f"Printing results")

        # GUI updates
        # # print results as numbers
        self.print_results(self.results)

        # # update results field according to results
        if self.c.is_safe():
            self.message1.configure(text="SAFE", width="500", background="green", font=("Arial", 25))
        else:
            self.message1.configure(text="UNSAFE", width="500", background="red", font=("Arial", 25))

        self.masterWindow.title(f"Finished analyzing {filename}")

    def save_results(self):
        self.masterWindow.title(f"Exporting results to file")
        dirname = askdirectory(initialdir = ".",title = "Select directory to save results")
        filename = os.path.join(dirname,"analysis_export.txt")
        with open(filename, "a") as output_file:
            output_file.write(self.results)
        self.masterWindow.title(f"Results saved to {filename}")

    def clear_results(self):
        self.results = 'None'
        
        self.text17.configure(state="normal")
        self.text17.configure(height="10", setgrid="false", width="80")
        _text_ = """Results will appear here
- - - - - """
        self.text17.delete(1.0,tk.END)
        self.text17.insert("0.0", _text_)
        self.text17.configure(state="disabled")

        self.masterWindow.title(f"Results cleared")


    def __init__(self, master=None):
        self.results = 'None'
        self.c = Controller(model_path = './model_files/rf_final.model', column_names_path = './model_files/column_changed.names', class_names_path='./model_files/classes.names')

        self.masterWindow = master
        self.masterWindow.title(f"Welcome! Run analysis and see if you are safe")

        # build ui
        self.frame11 = ttk.Frame(master)
        self.frame12 = ttk.Frame(self.frame11)
        self.text7 = tk.Text(self.frame12)
        self.text7.configure(
            blockcursor="false", height="2", insertunfocussed="none", relief="flat",width="40"
        )
        self.text7.configure(
            state="normal", tabstyle="tabular", takefocus=False, wrap="char"
        )
        _text_ = "Model uczenia maszynowego\ndo wykrywania wybranych anomalii sieciowych"
        self.text7.insert("0.0", _text_)
        self.text7.configure(state="disabled", font=("Arial", 20))
        self.text7.pack(side="left")
        self.text12 = tk.Text(self.frame12)
        self.text12.configure(
            height="4", insertunfocussed="hollow", state="normal", undo="true"
        )
        self.text12.configure(width="17", wrap="word")
        _text_ = """Autorzy:
Adrian Stańdo
Mateusz Stączek
Kinga Ułasik"""
        self.text12.insert("0.0", _text_)
        self.text12.configure(state="disabled")
        self.text12.pack(side="top")
        self.frame12.configure(height="30", width="50")
        self.frame12.pack(side="top")
        self.frame1 = ttk.Frame(self.frame11)
        self.frame6 = ttk.Frame(self.frame1)
        self.frame8 = ttk.Frame(self.frame6)
        self.button6 = ttk.Button(self.frame8)
        self.button6.configure(text="Import and Analyze PCAP", command=self.import_and_analyze_pcap)
        self.button6.pack(ipadx="10", ipady="10", padx="15", pady="10", side="left")
        self.button7 = ttk.Button(self.frame8)
        self.button7.configure(text="Import and Analyze CSV", command=self.import_and_analyze_csv)
        self.button7.pack(ipadx="10", ipady="10", padx="10", pady="10", side="left")
        # self.button8 = ttk.Button(self.frame8)
        # self.button8.configure(text="Stop live analysis")
        # self.button8.pack(ipadx="10", ipady="10", padx="10", pady="10", side="left")
        self.button9 = ttk.Button(self.frame8)
        self.button9.configure(text="Export", command=self.save_results)
        self.button9.pack(ipadx="10", ipady="10", padx="10", pady="10", side="left")
        self.button10 = ttk.Button(self.frame8)
        self.button10.configure(text="Clear results", command=self.clear_results)
        self.button10.pack(ipadx="10", ipady="10", padx="10", pady="10", side="left")
        self.frame8.configure(height="100", padding="0", width="200")
        self.frame8.pack(padx="0", pady="10", side="top")
        self.frame9 = ttk.Frame(self.frame6)
        self.text4 = tk.Text(self.frame9)
        self.text4.configure(height="1", relief="flat", width="8", font=("Arial", 25))
        _text_ = """Results:"""
        self.text4.insert("0.0", _text_)
        self.text4.configure(state="disabled")
        self.text4.pack(padx="0", pady="0", side="left")
        self.message1 = tk.Message(self.frame9)
        self.message1.configure(text="analyze file first!", width="500" , font=("Arial", 25))
        self.message1.pack(padx="20", side="right")
        self.frame9.configure(height="200", width="200")
        self.frame9.pack(padx="0", pady="20", side="left")
        self.frame6.configure(height="200", width="200")
        self.frame6.pack(side="left")
        self.frame1.configure(height="200", width="200")
        self.frame1.pack(side="top")
        self.frame16 = ttk.Frame(self.frame11)
        self.frame17 = ttk.Frame(self.frame16)

        # self.frame17.pack()
        # self.frame17.place(anchor='center', relx=0.5, rely=0.5)
        # img = ImageTk.PhotoImage(Image.open("logo_img.png"))
        # self.label = tk.Label(self.frame17, image = img)
        # self.label.pack()

        canvas_for_image = tk.Canvas(self.frame16, bg='green', height=200, width=200, borderwidth=0, highlightthickness=0)
        canvas_for_image.grid(row=0, column=0, sticky='nesw', padx=0, pady=0)

        # create image from image location resize it to 200X200 and put in on canvas
        image = Image.open("model_files/logo_img.png")
        canvas_for_image.image = ImageTk.PhotoImage(image.resize((200, 200), Image.ANTIALIAS))
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')

        self.frame16.configure(height="200", width="200")
        self.frame16.pack(padx="20", pady="20",side="left")


#         self.text15 = tk.Text(self.frame17)
#         self.text15.configure(height="10", width="30")
#         _text_ = """Results statistics
# - - - - -"""
#         self.text15.insert("0.0", _text_)
#         self.text15.configure(state="disabled")
#         self.text15.pack(pady="20", side="left")
        # self.frame17.configure(height="200", width="200")
        # self.frame17.pack(side="left")
        # self.frame16.configure(height="200", width="200")
        # self.frame16.pack(padx="65", side="left")

        self.frame19 = ttk.Frame(self.frame11)
        self.text17 = tk.Text(self.frame19)
        self.text17.configure(height="10", setgrid="false", width="80")
        _text_ = """Results will appear here
- - - - - """
        self.text17.insert("0.0", _text_)
        self.text17.configure(state="disabled")
        self.text17.pack(padx="10", pady="20", side="top")
        self.frame19.configure(height="200", width="200")
        self.frame19.pack(side="top")
        self.frame11.configure(height="200", width="200")
        self.frame11.pack(side="top")

        # Main widget
        self.mainwindow = self.frame11

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Model(root)
    app.run()

