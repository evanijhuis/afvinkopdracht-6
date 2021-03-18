import tkinter
import mysql.connector
from tkinter import messagebox

class gui:
    def __init__(self):
        """ Het maken van een GUI die berichten aanmaakt, vernieuwd en
            zoekt

        """
        self.main_window = tkinter.Tk()
        self.main_window.title("PyPiep")

        # aanmaken van frames
        self.top_frame = tkinter.Label(self.main_window)
        self.mid1_frame = tkinter.Label(self.main_window)
        self.mid2_frame = tkinter.Label(self.main_window)
        self.mid3_frame = tkinter.Label(self.main_window)
        self.bottom_frame = tkinter.Label(self.main_window)

        # aanmaken van labels en entry
        self.bericht_label = tkinter.Label(self.top_frame,
                                          text="New bericht")

        self.bericht_entry = tkinter.Entry(self.top_frame,
                                           width=50)

        self.zoeken_label = tkinter.Label(self.mid1_frame,
                                          text="                    "
                                               "                    "
                                               "                    "
                                               "Filter op #tag")

        self.zoeken_entry = tkinter.Entry(self.mid1_frame,
                                         width=15)

        self.vernieuw_text = tkinter.Text(self.mid2_frame,
                                          width=50)
        self.zoek_text = tkinter.Text(self.mid2_frame,
                                          width=50)


        # aanmaken van buttons
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)
        self.post_button = tkinter.Button(self.top_frame,
                                          text="Plaats bericht",
                                          command=self.new_bericht)

        self.vernieuw_button = tkinter.Button(self.mid1_frame,
                                              text="Vernieuw",
                                              command=self.show_piep)
        self.zoek_button = tkinter.Button(self.mid1_frame,
                                          text="Zoeken",
                                          command=self.filter_hashtag)


        # packen buttons
        self.post_button.pack(side="right")
        self.vernieuw_button.pack(side="left")
        self.quit_button.pack()
        self.zoek_button.pack(side="right")

        # packen labels
        self.bericht_label.pack(side="left")
        self.bericht_entry.pack(side="right")
        self.vernieuw_text.pack(side="left")
        self.zoek_text.pack(side="right")
        self.zoeken_label.pack(side="left")
        self.zoeken_entry.pack(side="right")


        # Packen framen
        self.top_frame.pack()
        self.mid1_frame.pack()
        self.mid2_frame.pack()
        self.mid3_frame.pack()
        self.bottom_frame.pack()

        # Laat gui zien
        tkinter.mainloop()

    def new_bericht(self):
        """ Deze functie zet een nieuw bericht in piep tabel

        """
        new_bericht = self.bericht_entry.get()
        conn = mysql.connector.connect(host="145.74.104.145",
                                       user="mmrhk",
                                       db="mmrhk",
                                       password="NativeSQL1@")
        cursor = conn.cursor()
        cursor.execute(f"insert into piep"
                       f" (bericht, datum, tijd, student_nr) "
                       f"values ('{new_bericht}', curdate(), "
                       f"curtime(),123456)")
        conn.commit()
        cursor.fetchall()

        cursor.close()
        conn.close()


    def show_piep(self):
        """ Deze funtie laat alle berichten zien in text stuk

        """
        conn = mysql.connector.connect(host="145.74.104.145",
                                       user="mmrhk",
                                       db="mmrhk",
                                       password="NativeSQL1@")
        cursor = conn.cursor()
        cursor.execute("select s.voornaam, p.bericht "
                       "from student s natural join piep p")

        rows =cursor.fetchall()
        for row in rows:
            self.vernieuw_text.insert(tkinter.END, str(row[0]) +
                        " heeft volgende bericht geplaatst: " + "\n")
            self.vernieuw_text.insert(tkinter.END, str(row[1]) + "\n" +
                                      "\n")
        cursor.close()
        conn.close()


    def filter_hashtag(self):
        """ Deze funtie zoekt naar berichten met #

        """
        zoeken_hashtag = self.zoeken_entry.get()
        conn = mysql.connector.connect(host="145.74.104.145",
                                       user="mmrhk",
                                       db="mmrhk",
                                       password="NativeSQL1@")
        cursor = conn.cursor()

        cursor.execute(f"select s.voornaam, p.bericht "
                       f"from student s natural join piep p "
                       f"where bericht like '%{zoeken_hashtag}%'")

        lines = cursor.fetchall()
        for line in lines:
            self.zoek_text.insert(tkinter.END, str(line[0])+
                        " heeft volgende bericht geplaatst: " + "\n")
            self.zoek_text.insert(tkinter.END, str(line[1]) + "\n" +
                                      "\n")

        cursor.close()
        conn.close()

if __name__ == '__main__':
    myGUI = gui()
