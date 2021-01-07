"""
    Frontend program for GUI based implementation using tkinter
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq

LABEL_FONT = ("Arial Regular", 18)
INPUT_FONT = ("Chilanka", 16)
HEADING_PAGE_FONT = ("Helvetica", 25, "bold")
CHECKBUTTON_FONT = ("Arial", 15)
QUES_PROMPT_FONT = ("Times New Roman", 20)

(F_WIDTH, F_HEIGHT) = (1366, 768)  # frame width and height

MAINPAGE_BG = "#343434"

SIGNPAGE_BG = "white"
SIGNPAGE_INP_FG = "#2a12f0"
SIGNPAGE_INP_BG = "#ecf0f1"

(TABLE_HEAD_BG, TABLE_HEAD_FG, TABLE_HEAD_FONT) = ("#aa73de", "#343434", ('Arial', 22, 'bold'))
TABLE_ROW_FONT = INPUT_FONT

(H_X1, H_X2, H_X3) = (208, 594, 980)  # X-axis coordinates of user Homepage for placing buttons
(H_Y1, H_Y2, H_Y3) = (75, 325, 570)

(E_X1, E_Y1, E_Y2, E_Y3, E_Y4) = (970, 147, 247, 347, 447)  # coordinates for daily entry page

(HEAD_X, HEAD_Y) = (550, 35)  # HEADING COORDINATES FOR DAILY ENTRIES ETC ...(X CAN BE VARIED UPON TEXT)

(INSERT_EX1, INSERT_EX2, INSERT_EY) = (275, 890, 160)  # InsertPage coordinates for entry and heading reference
(INSERT_HEAD_QUES_GAP_Y, INSERT_QUES_GAP_Y) = (250, 60)  # INSERT_HEAD_QUES_GAP_Y is the gap b/w heading and question


# INSERT_QUES_GAP_Y is the gap/padding in Y-axis


class Ajna(Tk):
    """
    Ajna class inherits tkinter.Frame()
    """

    def __init__(self):
        Tk.__init__(self)

        self.title(" Ajna ")
        self.geometry(str(F_WIDTH) + "x" + str(F_HEIGHT))  # another dimension for resolution 1400 × 1050
        # we can also put like self.geometry("1366x768")

        container = Frame(self)
        container.pack()

        self.frames = {}

        pages = (MainPage, SigninPage, RegisterPage, UserHomePage, DailyEntryPage, CovidCheckPage
                 , CovidSymptomsPage, MeetHistoryPage, CovidZonePage, CovidHelpLineNumberPage
                 , TravelHistoryPage, InsertPage, SearchPage)

        for F in pages:
            fr = F(container, self)
            self.frames[F] = fr
            fr.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, key):
        """
        This function used to raise the frames on the root window
        :param key: this key is for Frames to raise
        :return: returns nothing
        """
        f = self.frames[key]
        f.tkraise()


class MainPage(Frame):
    """
    This class contains the main page which have tagline, signup and login widgets
    Buttons -
        sign_butt : sign up button
        register_butt : register nutton
    Label -
        tagLine (img)
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global tagLine, signin, register

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)  # as a option for resolution 1400 × 1050
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=MAINPAGE_BG)

        tagLine = PhotoImage(file="backgrounds/Ajna - artboards/tag.png")
        signin = PhotoImage(file="backgrounds/Ajna - artboards/signIn.png")
        register = PhotoImage(file="backgrounds/Ajna - artboards/register.png")

        Label(frame, image=tagLine, bg=MAINPAGE_BG).pack(fill="both", side="top")

        style = ttk.Style()
        style.configure("TButton", padding=0, relief=FLAT, background=MAINPAGE_BG, foreground=MAINPAGE_BG,
                        borderwidth=-2, highlightthickness=0, activebackground=MAINPAGE_BG,
                        activeforeground=MAINPAGE_BG)

        sign_butt = ttk.Button(frame, command=lambda: controller.show_frame(SigninPage))
        sign_butt.config(image=signin)
        sign_butt.pack(pady=15)

        register_butt = ttk.Button(frame, command=lambda: controller.show_frame(RegisterPage))
        register_butt.config(image=register)
        register_butt.pack(pady=2)


class SigninPage(Frame):
    """
    Sign in page which have sign in credentials to input
    Buttons -
        forgot_butt : button pressed when user forgot password
        login_butt : login button that jumps to user home page if credentials matched
        back_butt   : back button
    Entry -
        username : entry field for username
        passwd : entry field for password
    Label -
        s_img : signin image
    Function -
        popup_passwd() : static function that popup a msg when we click forgot password
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global s_img, forgotimg, logimg, backimg
        # This backimg is used all around in project

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        s_img = PhotoImage(file="backgrounds/Ajna - artboards/signimg1.png")
        Label(frame, image=s_img, bg=SIGNPAGE_BG).pack(fill="both", side="top")

        frame1 = Frame(frame, width=F_WIDTH, height=F_HEIGHT - 100)
        frame1.pack(pady=65)
        frame1.config(background=SIGNPAGE_BG)

        l1 = Label(frame1, text="Username :", width=10, font=LABEL_FONT, bg=SIGNPAGE_BG)
        l1.grid(row=0, column=10, sticky="w", pady=15, columnspan=2)

        username = Entry(frame1, width=20, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                         bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        username.grid(row=0, column=12, sticky="w", pady=7)

        l2 = Label(frame1, text="Password :", width=10, font=LABEL_FONT, bg=SIGNPAGE_BG)
        l2.grid(row=1, column=10, sticky="w", pady=1, columnspan=2)

        passwd = Entry(frame1, width=20, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                       bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        passwd.grid(row=1, column=12, sticky="w", pady=1)
        passwd.config(show="*")

        frame2 = Frame(frame, width=F_WIDTH, height=F_HEIGHT - 100)
        frame2.pack()
        frame2.config(background=SIGNPAGE_BG)

        forgotimg = PhotoImage(file="backgrounds/Ajna - artboards/forgotpwd.png")
        logimg = PhotoImage(file="backgrounds/Ajna - artboards/loginimg1.png")
        backimg = PhotoImage(file="backgrounds/Ajna - artboards/backButto.png")

        style = ttk.Style()
        style.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                        borderwidth=-2, highlightthickness=0, activebackground=SIGNPAGE_BG,
                        activeforeground=SIGNPAGE_BG)

        forgot_butt = ttk.Button(frame2, command=self.popup_passwd)
        forgot_butt.config(image=forgotimg)
        forgot_butt.grid(pady=10, sticky="ne")

        login_butt = ttk.Button(frame2, command=lambda: controller.show_frame(UserHomePage))
        login_butt.config(image=logimg)
        login_butt.grid(pady=12)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(MainPage))
        back_butt.config(image=backimg)
        back_butt.pack(pady=5, padx=75, side="left")

    @staticmethod
    def popup_passwd():
        """
        PopUp window will splash when we hit Forgot_button
        It's static function which can't be inheritted
        """
        messagebox.showinfo("Forgot Password", message="Your phone number is your new password !")


class RegisterPage(Frame):
    """
    RegisterPage class used to register an account
    Buttons -
        createAcc_butt : create account button
        back_butt : back button
    Entry -
        name
        usn
        username
        phone
        passwd1
        passwd2
    Label -
        signimg
    Function -
        passwd_match(passwd1, passwd2, controller) : static function that popup a msg when password mismatch
                                                     otherwise jump to user homepage

    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global r_img, create_img

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        r_img = PhotoImage(file="backgrounds/Ajna - artboards/createAcc.png")
        create_img = PhotoImage(file="backgrounds/Ajna - artboards/createButt.png")

        Label(frame, image=r_img, bg=SIGNPAGE_BG).pack(fill="both", side="top")

        frame1 = Frame(frame, width=F_WIDTH, height=F_HEIGHT - 100)
        frame1.pack(pady=50)
        frame1.config(background=SIGNPAGE_BG)

        l1 = Label(frame1, text="Name :", font=LABEL_FONT, bg=SIGNPAGE_BG)
        l1.grid(row=0, column=10, sticky="w", pady=7, columnspan=2)
        name = Entry(frame1, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                     bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        name.grid(row=0, column=12, sticky="w", pady=3)

        l2 = Label(frame1, text="USN :", font=LABEL_FONT, bg=SIGNPAGE_BG)
        l2.grid(row=1, column=10, sticky="w", pady=1, columnspan=2)
        usn = Entry(frame1, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                    bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        usn.grid(row=1, column=12, sticky="w", pady=1)

        l3 = Label(frame1, text="Username :", font=LABEL_FONT, bg=SIGNPAGE_BG)
        l3.grid(row=2, column=10, sticky="w", pady=7, columnspan=2)
        username = Entry(frame1, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                         bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        username.grid(row=2, column=12, sticky="w", pady=3)

        l4 = Label(frame1, text="Phone Number : ", font=LABEL_FONT, bg=SIGNPAGE_BG)
        l4.grid(row=3, column=10, sticky="w", pady=1, columnspan=2)
        phone = Entry(frame1, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                      bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        phone.grid(row=3, column=12, sticky="w", pady=1)

        l5 = Label(frame1, text="Password :", font=LABEL_FONT, bg=SIGNPAGE_BG)
        l5.grid(row=4, column=10, sticky="w", pady=7, columnspan=2)
        passwd1 = Entry(frame1, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                        bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        passwd1.grid(row=4, column=12, sticky="w", pady=3)
        passwd1.config(show="*")

        l6 = Label(frame1, text="Confirm Password : ", font=LABEL_FONT, bg=SIGNPAGE_BG)
        l6.grid(row=5, column=10, sticky="w", pady=1, columnspan=2)
        passwd2 = Entry(frame1, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                        bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        passwd2.grid(row=5, column=12, sticky="w", pady=1)
        passwd2.config(show="*")

        style = ttk.Style()
        style.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                        borderwidth=-2, highlightthickness=0, activebackground=SIGNPAGE_BG,
                        activeforeground=SIGNPAGE_BG)

        createAcc_butt = ttk.Button(frame, command=lambda: self.passwd_match(passwd1.get(), passwd2.get(), controller))
        createAcc_butt.config(image=create_img)
        createAcc_butt.pack(pady=0)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(MainPage))
        back_butt.config(image=backimg)
        back_butt.pack(pady=0, padx=75, side="left")

    @staticmethod
    def passwd_match(passwd1, passwd2, controller):
        """
        This function will check whether password and confirm password fileds match
        :param controller: used to jump to the user home page
        :param passwd1: string enter into the password feild
        :param passwd2: string enter into the confirm password filed
        """
        if passwd1 != passwd2:
            messagebox.showerror("Password", "Password mismatch !!!")
        else:
            controller.show_frame(UserHomePage)  # jumps to user Homepage


class UserHomePage(Frame):
    """
    UserHome Page which contains most of the page jumps
    Buttons -
        1.entry_butt
        2.covidchk_butt
        3.travelhist_butt
        4.meethist_butt
        5.help_butt
        6.zone_butt
        7.logout_butt
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global entry_img, covidchk_img, travelhist_img, meethist_img, help_img, zone_img, logout_img

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        entry_img = PhotoImage(file="backgrounds/Ajna - artboards/entries_img.png")
        covidchk_img = PhotoImage(file="backgrounds/Ajna - artboards/covidchk_img.png")
        travelhist_img = PhotoImage(file="backgrounds/Ajna - artboards/travelHist_img.png")
        meethist_img = PhotoImage(file="backgrounds/Ajna - artboards/meetHist_img.png")
        help_img = PhotoImage(file="backgrounds/Ajna - artboards/help_img.png")
        zone_img = PhotoImage(file="backgrounds/Ajna - artboards/zone_img.png")
        logout_img = PhotoImage(file="backgrounds/Ajna - artboards/logout_img.png")

        u_name = "UserName"
        wel_note = "Hello, " + u_name
        l1 = Label(frame, text=wel_note, font=LABEL_FONT, bg=SIGNPAGE_BG)
        l1.place(x=15, y=15)

        style = ttk.Style()
        style.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                        borderwidth=-2, highlightthickness=0, activebackground=SIGNPAGE_BG,
                        activeforeground=SIGNPAGE_BG)

        # placed using window gerometry dimension and image dimension ie. 178x178

        entry_butt = ttk.Button(frame, command=lambda: controller.show_frame(DailyEntryPage))
        entry_butt.config(image=entry_img)
        entry_butt.place(x=H_X1, y=H_Y1)

        covidchk_butt = ttk.Button(frame, command=lambda: controller.show_frame(CovidCheckPage))
        covidchk_butt.config(image=covidchk_img)
        covidchk_butt.place(x=H_X2, y=H_Y1)

        travelhist_butt = ttk.Button(frame, command=lambda: controller.show_frame(TravelHistoryPage))
        travelhist_butt.config(image=travelhist_img)
        travelhist_butt.place(x=H_X3, y=H_Y1)

        meethist_butt = ttk.Button(frame, command=lambda: controller.show_frame(MeetHistoryPage))
        meethist_butt.config(image=meethist_img)
        meethist_butt.place(x=H_X1, y=H_Y2)

        help_butt = ttk.Button(frame, command=lambda: controller.show_frame(CovidHelpLineNumberPage))
        help_butt.config(image=help_img)
        help_butt.place(x=H_X2, y=H_Y2)

        zone_butt = ttk.Button(frame, command=lambda: controller.show_frame(CovidZonePage))
        zone_butt.config(image=zone_img)
        zone_butt.place(x=H_X3, y=H_Y2)

        logout_butt = ttk.Button(frame, command=lambda: controller.show_frame(MainPage))
        logout_butt.config(image=logout_img)
        logout_butt.place(x=597, y=H_Y3)


class DailyEntryPage(Frame):
    """
    Daily entry page which provides daily data feed functionality
    Buttons -
        1.insert_butt : open a new page where user insert daily meet history ,travel history
        2.search_butt : to serach for met persons
        3.reset_butt : to reset everything ie. to delete meet and travel history for current history
        4.exit_butt : to exit/back/jump to UserHomePage
        5.back_butt : same as above
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global covidaware_img, insert_img, search_img, reset_img, notification_img

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        covidaware_img = PhotoImage(file="backgrounds/Ajna - artboards/covidAware_img.png")
        insert_img = PhotoImage(file="backgrounds/Ajna - artboards/insert_img.png")
        search_img = PhotoImage(file="backgrounds/Ajna - artboards/search_img.png")
        reset_img = PhotoImage(file="backgrounds/Ajna - artboards/reset_img.png")
        notification_img = PhotoImage(file="backgrounds/Ajna - artboards/notification_img.png")

        l1 = Label(frame, text="DAILY ENTRIES", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        l1.place(x=HEAD_X, y=HEAD_Y)

        l2 = Label(frame, image=covidaware_img, bg=SIGNPAGE_BG)
        l2.place(x=80, y=130)

        style = ttk.Style()
        style.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                        borderwidth=-2, highlightthickness=0, activebackground=SIGNPAGE_BG,
                        activeforeground=SIGNPAGE_BG)

        insert_butt = ttk.Button(frame, command=lambda: controller.show_frame(InsertPage))
        insert_butt.config(image=insert_img)
        insert_butt.place(x=E_X1, y=E_Y1)

        search_butt = ttk.Button(frame, command=lambda: controller.show_frame(SearchPage))
        search_butt.config(image=search_img)
        search_butt.place(x=E_X1, y=E_Y2)

        reset_butt = ttk.Button(frame)
        reset_butt.config(image=reset_img)
        reset_butt.place(x=E_X1, y=E_Y3)

        notification_butt = ttk.Button(frame)  # , command=lambda: controller.show_frame(UserHomePage))
        notification_butt.config(image=notification_img)
        notification_butt.place(x=E_X1, y=E_Y4)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)


class CovidCheckPage(Frame):
    """
    This page used to check whether user is Covid Positive or not
    Buttons -
        1.covid_symp_butt : opens a new page which contains covid information (symptoms)
        2.self_declare_butt : self declare button for covid +ve users
        3.back_butt : jumps to userHomepage
    CheckButtons -
        1.cough_cb1
        2.fever_cb1
        3.breathless_cb1
        4.loss_taste_cb1
        5.q1_none
        6.interaction_cb2
        7.healthcare_cb2
        8.q2_none
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global ques1_img, ques2_img, covid_symp_img, self_declare_img

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        ques1_img = PhotoImage(file="backgrounds/Ajna - artboards/ques1_img.png")
        ques2_img = PhotoImage(file="backgrounds/Ajna - artboards/ques2_img.png")
        covid_symp_img = PhotoImage(file="backgrounds/Ajna - artboards/covid_symp_img.png")
        self_declare_img = PhotoImage(file="backgrounds/Ajna - artboards/self_declare_img.png")

        l1 = Label(frame, text="COVID CHECK", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        l1.place(x=565, y=HEAD_Y)

        ################################## Question-1 layout #####################################################
        l2 = Label(frame, image=ques1_img, bg=SIGNPAGE_BG)
        l2.place(x=50, y=130)

        cough = IntVar()
        fever = IntVar()
        breathless = IntVar()
        loss_taste = IntVar()
        q1_none = IntVar()

        cough_cb1 = Checkbutton(frame, text=" COUGH ", variable=cough, font=CHECKBUTTON_FONT, bg=SIGNPAGE_BG,
                                height=1, selectcolor=SIGNPAGE_INP_BG, fg=MAINPAGE_BG, bd=0, highlightcolor=SIGNPAGE_BG,
                                highlightthickness=0)
        cough_cb1.place(x=60, y=235)

        fever_cb1 = Checkbutton(frame, text=" FEVER ", variable=fever, font=CHECKBUTTON_FONT, bg=SIGNPAGE_BG,
                                height=1, selectcolor=SIGNPAGE_INP_BG, fg=MAINPAGE_BG, bd=0, highlightcolor=SIGNPAGE_BG,
                                highlightthickness=0)
        fever_cb1.place(x=185, y=235)

        breathless_cb1 = Checkbutton(frame, text=" DIFFICULTY IN BREATHING ", variable=breathless,
                                     font=CHECKBUTTON_FONT, bg=SIGNPAGE_BG,
                                     height=1, selectcolor=SIGNPAGE_INP_BG, fg=MAINPAGE_BG, bd=0,
                                     highlightcolor=SIGNPAGE_BG,
                                     highlightthickness=0)
        breathless_cb1.place(x=305, y=235)

        loss_taste_cb1 = Checkbutton(frame, text=" LOSS OF TASTE/SMELL ", variable=loss_taste, font=CHECKBUTTON_FONT,
                                     bg=SIGNPAGE_BG,
                                     height=1, selectcolor=SIGNPAGE_INP_BG, fg=MAINPAGE_BG, bd=0,
                                     highlightcolor=SIGNPAGE_BG,
                                     highlightthickness=0)
        loss_taste_cb1.place(x=60, y=275)

        q1_none_cb1 = Checkbutton(frame, text=" NONE OF THEM ", variable=q1_none, font=CHECKBUTTON_FONT, bg=SIGNPAGE_BG,
                                  height=1, selectcolor=SIGNPAGE_INP_BG, fg=MAINPAGE_BG, bd=0,
                                  highlightcolor=SIGNPAGE_BG,
                                  highlightthickness=0)
        q1_none_cb1.place(x=345, y=275)

        ################################## Question-2 layout ######################################################
        l3 = Label(frame, image=ques2_img, bg=SIGNPAGE_BG)
        l3.place(x=695, y=133)

        interaction = IntVar()
        interaction_quest = "I HAVE RECENTLY INTERACTED OR LIVED WITH \n SOMEONE WHO HAS TESTED POSITIVE FOR COVID - 19"
        healthcare = IntVar()
        healthcare_quest = "I AM A HEALTHCARE WORKER AND I EXAMINED A \n COVID - 19 CONFIRMED CASE WITHOUT PROTECTIVE GEAR"
        q2_none = IntVar()

        interaction_cb2 = Checkbutton(frame, text=interaction_quest, variable=interaction, font=CHECKBUTTON_FONT,
                                      bg=SIGNPAGE_BG,
                                      height=3, selectcolor=SIGNPAGE_INP_BG, fg=MAINPAGE_BG, bd=0,
                                      highlightcolor=SIGNPAGE_BG,
                                      highlightthickness=0)
        interaction_cb2.place(x=700, y=210)

        healthcare_cb2 = Checkbutton(frame, text=healthcare_quest, variable=healthcare, font=CHECKBUTTON_FONT,
                                     bg=SIGNPAGE_BG,
                                     height=3, selectcolor=SIGNPAGE_INP_BG, fg=MAINPAGE_BG, bd=0,
                                     highlightcolor=SIGNPAGE_BG,
                                     highlightthickness=0)
        healthcare_cb2.place(x=700, y=275)

        q2_none_cb2 = Checkbutton(frame, text="NONE OF THEM", variable=q2_none, font=CHECKBUTTON_FONT, bg=SIGNPAGE_BG,
                                  height=3, selectcolor=SIGNPAGE_INP_BG, fg=MAINPAGE_BG, bd=0,
                                  highlightcolor=SIGNPAGE_BG,
                                  highlightthickness=0)
        q2_none_cb2.place(x=700, y=340)

        ########################################### Buttons #################################################
        style = ttk.Style()
        style.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                        borderwidth=-2, highlightthickness=0, activebackground=SIGNPAGE_BG,
                        activeforeground=SIGNPAGE_BG)

        covid_symp_butt = ttk.Button(frame, command=lambda: controller.show_frame(CovidSymptomsPage))
        covid_symp_butt.config(image=covid_symp_img)
        covid_symp_butt.place(x=470, y=500)

        self_declare_butt = ttk.Button(frame)
        self_declare_butt.config(image=self_declare_img)
        self_declare_butt.place(x=680, y=500)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)


class CovidSymptomsPage(Frame):
    """
    Displays Covid Symptoms msg only
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global covid_symp1_img, covid_symp2_img, covid_symp3_img, covid_symp4_img, covid_symp5_img

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        label = Label(frame, text="COVID SYMPTOMS", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        label.place(x=525, y=HEAD_Y)

        covid_symp1_img = PhotoImage(file="backgrounds/Ajna - artboards/covid_symp1_img.png")
        covid_symp2_img = PhotoImage(file="backgrounds/Ajna - artboards/covid_symp2_img.png")
        covid_symp3_img = PhotoImage(file="backgrounds/Ajna - artboards/covid_symp3_img.png")
        covid_symp4_img = PhotoImage(file="backgrounds/Ajna - artboards/covid_symp4_img.png")
        covid_symp5_img = PhotoImage(file="backgrounds/Ajna - artboards/covid_symp5_img.png")

        l1 = Label(frame, image=covid_symp1_img, bg=SIGNPAGE_BG)
        l1.place(x=100, y=130)

        l2 = Label(frame, image=covid_symp2_img, bg=SIGNPAGE_BG)
        l2.place(x=900, y=100)

        l3 = Label(frame, image=covid_symp3_img, bg=SIGNPAGE_BG)
        l3.place(x=30, y=300)

        l4 = Label(frame, image=covid_symp4_img, bg=SIGNPAGE_BG)
        l4.place(x=650, y=250)

        l5 = Label(frame, image=covid_symp5_img, bg=SIGNPAGE_BG)
        l5.place(x=580, y=420)

        style = ttk.Style()
        style.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                        borderwidth=-2, highlightthickness=0, activebackground=SIGNPAGE_BG,
                        activeforeground=SIGNPAGE_BG)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(CovidCheckPage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)


class MeetHistoryPage(Frame):
    """
    This page contains details of whom user met
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        label = Label(frame, text="MEET HISTORY", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        label.place(x=555, y=HEAD_Y)

        style = ttk.Style()
        style.configure("Treeview", background="white", foreground="black", rowheight=45, fieldbackground="white"
                        , font=TABLE_ROW_FONT, bd=0, highlightthickness=0)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=TABLE_HEAD_FONT,
                        background=TABLE_HEAD_BG, foreground=TABLE_HEAD_FG)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        style.map("Treeview", background=[('selected', 'green')])

        my_tree = ttk.Treeview(frame, style="mystyle.Treeview")
        my_tree['columns'] = (" DATE ", " USN ", " NAME ")

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("#1", anchor=CENTER, width=400, minwidth=300)
        my_tree.column("#2", anchor=CENTER, width=400, minwidth=300)
        my_tree.column("#3", anchor=CENTER, width=400, minwidth=300)

        my_tree.heading("#1", text=" DATE ", anchor=CENTER)
        my_tree.heading("#2", text=" USN ", anchor=CENTER)
        my_tree.heading("#3", text=" NAME ", anchor=CENTER)

        record = [["18.12.2020", "1AT18CS129", "Sumukha Hegde"], ["25.12.2020", "1AT18CS125", "Mujeeb"]
            , ["31.12.2020", "1AT18CS006", "Sandeep"]]

        my_tree.tag_configure('oddrow', background="#9de892")
        my_tree.tag_configure('evenrow', background="lightblue")

        count = 0
        for data in record:
            if count % 2 == 0:
                my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                               tags=('oddrow',))

            count += 1

        my_tree.place(x=80, y=120)

        style1 = ttk.Style()
        style1.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                         borderwidth=-2, highlightthickness=-10, activebackground=SIGNPAGE_BG,
                         activeforeground=SIGNPAGE_BG)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)


class CovidZonePage(Frame):
    """
    This page contains zonal data ie. whether zone is green, orange or red
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        label = Label(frame, text="ZONES", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        label.place(x=610, y=HEAD_Y)

        style = ttk.Style()
        style.configure("Treeview", background="white", foreground="black", rowheight=45, fieldbackground="white"
                        , font=TABLE_ROW_FONT, bd=0, highlightthickness=0)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=TABLE_HEAD_FONT,
                        background=TABLE_HEAD_BG, foreground=TABLE_HEAD_FG)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        style.map("Treeview", background=[('selected', 'blue')])

        my_tree = ttk.Treeview(frame, style="mystyle.Treeview")
        my_tree['columns'] = (" STATE ", " DISTRICT ", " ZONE ")

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("#1", anchor=CENTER, width=400, minwidth=300)
        my_tree.column("#2", anchor=CENTER, width=400, minwidth=300)
        my_tree.column("#3", anchor=CENTER, width=400, minwidth=300)

        my_tree.heading("#1", text=" STATE ", anchor=CENTER)
        my_tree.heading("#2", text=" DISTRICT ", anchor=CENTER)
        my_tree.heading("#3", text=" ZONE ", anchor=CENTER)

        my_tree.tag_configure('Green Zone', background="#90ef42")
        my_tree.tag_configure('Orange Zone', background="#ef7d42")
        my_tree.tag_configure('Red Zone', background="#ef4242")

        try:
            con = sq.connect("backgrounds/Ajna.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM Zonal")
            rows = cur.fetchall()

            count = 0
            for data in rows:
                if data[2] == 'Green Zone':
                    my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                                   tags=('Green Zone',))
                elif data[2] == 'Orange Zone':
                    my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                                   tags=('Orange Zone',))
                elif data[2] == 'Red Zone':
                    my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                                   tags=('Red Zone',))
                count += 1

            cur.close()
        except Exception as e:
            print("CovidZonePage error occured :- ", e)

        my_tree.place(x=80, y=120)

        style1 = ttk.Style()
        style1.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                         borderwidth=-2, highlightthickness=-10, activebackground=SIGNPAGE_BG,
                         activeforeground=SIGNPAGE_BG)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)


class CovidHelpLineNumberPage(Frame):
    """
    This page contains Covid Helpline numbers
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global central_helpline

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        central_helpline = PhotoImage(file="backgrounds/Ajna - artboards/central_helpline.png")

        label = Label(frame, text=" HELPLINE ", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        label.place(x=590, y=HEAD_Y - 20)

        label1 = Label(frame, image=central_helpline, bg=SIGNPAGE_BG)
        label1.place(x=407, y=60 - 15)

        style = ttk.Style()
        style.configure("Treeview", background="white", foreground="black", rowheight=5, fieldbackground="white"
                        , font=TABLE_ROW_FONT, bd=0, highlightthickness=0)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=TABLE_HEAD_FONT,
                        background=TABLE_HEAD_BG, foreground=TABLE_HEAD_FG)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        style.map("Treeview", background=[('selected', 'green')])

        my_tree = ttk.Treeview(frame, style="mystyle.Treeview")
        my_tree['columns'] = (" STATE ", " HELPLINE NUMBERS ")

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("#1", anchor=CENTER, width=600, minwidth=300)
        my_tree.column("#2", anchor=CENTER, width=600, minwidth=300)

        my_tree.heading("#1", text=" STATE ", anchor=CENTER)
        my_tree.heading("#2", text=" HELPLINE NUMBERS ", anchor=CENTER)

        my_tree.tag_configure('oddrow', background="#9de892")
        my_tree.tag_configure('evenrow', background="lightblue")

        try:
            con = sq.connect("backgrounds/Ajna.db")
            cur = con.cursor()
            cur.execute('''SELECT * FROM "Covid HelpLine Numbers" ''')
            rows = cur.fetchall()

            count = 0
            for data in rows:
                if count % 2 == 0:
                    my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1]),
                                   tags=('evenrow',))
                else:
                    my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1]),
                                   tags=('oddrow',))
                count += 1
            cur.close()

        except Exception as e:
            print("CovidZonePage error occured :- ", e)

        my_tree.place(x=80, y=130)

        style1 = ttk.Style()
        style1.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                         borderwidth=-2, highlightthickness=-10, activebackground=SIGNPAGE_BG,
                         activeforeground=SIGNPAGE_BG)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)


class TravelHistoryPage(Frame):
    """
    This page contains travel history of user that user feeds daily
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        label = Label(frame, text="TRAVEL HISTORY", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        label.place(x=540, y=HEAD_Y)

        style = ttk.Style()
        style.configure("Treeview", background="white", foreground="black", rowheight=45, fieldbackground="white"
                        , font=TABLE_ROW_FONT, bd=0, highlightthickness=0)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=TABLE_HEAD_FONT,
                        background=TABLE_HEAD_BG, foreground=TABLE_HEAD_FG)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        style.map("Treeview", background=[('selected', 'green')])

        my_tree = ttk.Treeview(frame, style="mystyle.Treeview")
        my_tree['columns'] = (" DATE ", " STATE ", " DISTRICT ")

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("#1", anchor=CENTER, width=400, minwidth=300)
        my_tree.column("#2", anchor=CENTER, width=400, minwidth=300)
        my_tree.column("#3", anchor=CENTER, width=400, minwidth=300)

        my_tree.heading("#1", text=" DATE ", anchor=CENTER)
        my_tree.heading("#2", text=" STATE ", anchor=CENTER)
        my_tree.heading("#3", text=" DISTRICT ", anchor=CENTER)

        record = [["18.12.2020", "Karnataka", "Bangalore Rural"], ["25.12.2020", "Karnataka", "Bangalore Urban"],
                  ["31.12.2020", "Uttar Pradesh", "Mathura"]]

        my_tree.tag_configure('oddrow', background="#9de892")
        my_tree.tag_configure('evenrow', background="lightblue")

        count = 0
        for data in record:
            if count % 2 == 0:
                my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                               tags=('oddrow',))

            count += 1

        my_tree.place(x=80, y=120)

        style1 = ttk.Style()
        style1.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                         borderwidth=-2, highlightthickness=-10, activebackground=SIGNPAGE_BG,
                         activeforeground=SIGNPAGE_BG)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)


class InsertPage(Frame):
    """
    This page is used to take data from user such as meet and travel entries
    Buttons -
        1.back_butt
        2.update_butt
        3.add_more_butt
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global update_butt_img, add_more_img

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        try:
            con = sq.connect("backgrounds/Ajna.db")
            cur = con.cursor()
        except Exception as e:
            print('Unable to create a connection with Ajna.db in InsertPage, error -', e)

        update_butt_img = PhotoImage(file="backgrounds/Ajna - artboards/update_butt_img.png")
        add_more_img = PhotoImage(file="backgrounds/Ajna - artboards/add_more_butt.png")

        label = Label(frame, text="INSERT", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        label.place(x=620, y=HEAD_Y)

        label1 = Label(frame, text="  TRAVEL ENTRY  ", font=("Arial", 20, "bold"), bg="pink", fg="#343434")
        label1.place(x=INSERT_EX1, y=INSERT_EY)

        label2 = Label(frame, text="  MEET ENTRY  ", font=("Arial", 20, "bold"), bg="pink", fg="#343434")
        label2.place(x=INSERT_EX2, y=INSERT_EY)

        ###################################### TRAVEL ENTRY ###################################################
        date_l1 = Label(frame, text="Date :", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        date_l1.place(x=INSERT_EX1 - 120 - 60, y=INSERT_HEAD_QUES_GAP_Y)
        date_entry_l1 = Entry(frame, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                              bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        date_entry_l1.insert(0, "dd/mm/yyyy")
        date_entry_l1.place(x=INSERT_EX1 - 70, y=INSERT_HEAD_QUES_GAP_Y)

        ###############
        state_l1 = Label(frame, text="State :", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        state_l1.place(x=INSERT_EX1 - 120 - 60, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y)
        try:
            cur.execute("SELECT State FROM Zonal ")
            s = set(cur.fetchall())
            lst_state = list(s)
            lst_state.sort()

            new_lst = list()
            [new_lst.append(st[0]) for st in lst_state]

            state_select = StringVar()

            combostyle = ttk.Style()
            combostyle.configure('ARD.TCombobox', background="#ffcc66", fieldbackground="#ffff99")

            state = ttk.Combobox(frame, style="ARD.TCombobox", width=30, textvariable=state_select,
                                 font=INPUT_FONT, state="readonly")
            state['values'] = new_lst
            state.place(x=INSERT_EX1 - 70, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y)
            state.current(1)

        except Exception as e:
            print("Error occured in InsertPage in State Combobox section -", e)

        ############
        district_l1 = Label(frame, text="District :", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        district_l1.place(x=INSERT_EX1 - 120 - 60, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y * 2)
        try:
            cur.execute("SELECT District FROM Zonal ")
            s = set(cur.fetchall())
            lst_district = list(s)
            lst_district.sort()

            new_lst_district = list()
            [new_lst_district.append(st[0]) for st in lst_district]

            district_select = StringVar()
            combostyle = ttk.Style()
            combostyle.configure('ARD.TCombobox', background="#ffcc66", fieldbackground="#ffff99")

            state = ttk.Combobox(frame, width=30, style='ARD.TCombobox', textvariable=district_select,
                                 font=INPUT_FONT, state="readonly")
            state['values'] = new_lst_district
            state.place(x=INSERT_EX1 - 70, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y * 2)
            state.current(1)

        except Exception as e:
            print("Error occured in InsertPage in District Combobox section -", e)

        ##################################### MEET ENTRY ######################################################
        date_l2 = Label(frame, text="Date :", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        date_l2.place(x=INSERT_EX2 - 120 - 60, y=INSERT_HEAD_QUES_GAP_Y)
        date_entry_l2 = Entry(frame, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                              bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        date_entry_l2.insert(0, "dd/mm/yyyy")
        date_entry_l2.place(x=INSERT_EX2 - 70, y=INSERT_HEAD_QUES_GAP_Y)

        name_l2 = Label(frame, text="Name :", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        name_l2.place(x=INSERT_EX2 - 120 - 60, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y)
        name_entry_l2 = Entry(frame, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                              bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        name_entry_l2.insert(0, "name of person whom you meet")
        name_entry_l2.place(x=INSERT_EX2 - 70, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y)

        usn_l2 = Label(frame, text="USN :", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        usn_l2.place(x=INSERT_EX2 - 120 - 60, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y * 2)
        usn_entry_l2 = Entry(frame, width=30, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                             bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        usn_entry_l2.insert(0, "usn of person whom you meet")
        usn_entry_l2.place(x=INSERT_EX2 - 70, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y * 2)

        ########################## Buttons ##########################################################
        style1 = ttk.Style()
        style1.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                         borderwidth=-2, highlightthickness=-10, activebackground=SIGNPAGE_BG,
                         activeforeground=SIGNPAGE_BG)

        update_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        update_butt.config(image=update_butt_img)
        update_butt.place(x=525, y=480)

        add_more_butt = ttk.Button(frame, command=self.updatePopup)
        add_more_butt.config(image=add_more_img)
        add_more_butt.place(x=1200, y=580)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)

    @staticmethod
    def updatePopup():
        """
        Popup msg to show that data is updated
        """
        messagebox.showinfo("Update", message="Update Successfull ( you can insert new data :) ")


class SearchPage(Frame):
    """
    This page implements search facility for travel and meet history page
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global search_img_butt

        search_img_butt = PhotoImage(file="backgrounds/Ajna - artboards/search_butt.png")

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        label = Label(frame, text="SEARCH", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        label.place(x=610, y=HEAD_Y)

        #################################### TRAVEL SEARCH ################################################
        label1 = Label(frame, text="  TRAVEL SEARCH  ", font=("Arial", 20, "bold"), bg="pink", fg="#343434")
        label1.place(x=INSERT_EX1 - 15, y=INSERT_EY)

        key_l1 = Label(frame, text="Select Key : ", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        key_l1.place(x=INSERT_EX1 - 190, y=INSERT_HEAD_QUES_GAP_Y)
        key_lst = ["State", "District", "Date"]
        key_select = StringVar()

        combostyle = ttk.Style()
        combostyle.configure('ARD.TCombobox', background="#ffcc66", fieldbackground="#ffff99")

        travel = ttk.Combobox(frame, style="ARD.TCombobox", width=30, textvariable=key_select,
                              font=INPUT_FONT, state="readonly")
        travel['values'] = key_lst
        travel.place(x=INSERT_EX1 - 40, y=INSERT_HEAD_QUES_GAP_Y)
        travel.current(1)

        search = Label(frame, text="Search : ", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        search.place(x=INSERT_EX1 - 190, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y)
        search_entry = Entry(frame, width=25, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                             bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        search_entry.place(x=INSERT_EX1 - 40, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y)

        #################################### MEET SEARCH ##################################################
        label2 = Label(frame, text="  MEET SEARCH  ", font=("Arial", 20, "bold"), bg="pink", fg="#343434")
        label2.place(x=INSERT_EX2 - 15, y=INSERT_EY)
        key_l2 = Label(frame, text="Select Key : ", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        key_l2.place(x=INSERT_EX2 - 170, y=INSERT_HEAD_QUES_GAP_Y)
        key_lst1 = ["Name", "USN", "Date"]
        key_select1 = StringVar()

        meet = ttk.Combobox(frame, style="ARD.TCombobox", width=30, textvariable=key_select1,
                            font=INPUT_FONT, state="readonly")
        meet['values'] = key_lst1
        meet.place(x=INSERT_EX2 - 20, y=INSERT_HEAD_QUES_GAP_Y)
        meet.current(1)

        search1 = Label(frame, text="Search : ", font=QUES_PROMPT_FONT, bg=SIGNPAGE_BG)
        search1.place(x=INSERT_EX2 - 170, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y)
        search1_entry = Entry(frame, width=25, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                              bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        search1_entry.place(x=INSERT_EX2 - 20, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y)

        ##################################### Buttons #############################################
        style1 = ttk.Style()
        style1.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                         borderwidth=-2, highlightthickness=-10, activebackground=SIGNPAGE_BG,
                         activeforeground=SIGNPAGE_BG)

        search_butt = ttk.Button(frame, command=lambda: self.search_travel(frame, key_select.get(), search_entry.get()))
        search_butt.config(image=search_img_butt)
        search_butt.place(x=INSERT_EX1 + 260, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y - 15)

        search_butt1 = ttk.Button(frame,
                                  command=lambda: self.search_meet(frame, key_select1.get(), search1_entry.get()))
        search_butt1.config(image=search_img_butt)
        search_butt1.place(x=INSERT_EX2 + 260, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y - 15)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg)
        back_butt.place(x=75, y=630)

    @staticmethod
    def search_travel(frame, key, value):
        """
        This function used to popup the result to SearchPage frame when serach button clicks
        :param frame: to what we have to display
        :param key: to what reference we're searching like State, District, Date
        :param value: what we have to look for
        :return: nothing
        """

        # ["State", "District", "Date"]
        record = [
            ["23/12/2020", "Karnataka", "Bengaluru Urban"],
            ["07/01/2021", "Uttar Pradesh", "Mathura"],
            ["23/12/2020", "Karnataka", "Marathahalli"],
        ]

        new_lst = []
        indx = 0

        if key == "State":
            indx = 1
        elif key == "District":
            indx = 2
        elif key == "Date":
            indx = 0

        for i in range(len(record)):
            if record[i][indx] == value:
                new_lst.append(record[i])

        fr1 = Frame(frame, relief=RAISED, width=550, height=250, bg=SIGNPAGE_BG)
        fr1.place(x=INSERT_EX1 - 190, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y * 2)

        style = ttk.Style()
        style.configure("Treeview1", background="white", foreground="black", fieldbackground="white"
                        , font=("Arial Regular", 12), bd=0, highlightthickness=0)  # Modify the font of the body
        style.configure("mystyle.Treeview1.Heading", font=('Arial', 16, 'bold'),
                        background=TABLE_HEAD_BG, foreground=TABLE_HEAD_FG)  # Modify the font of the headings
        style.layout("mystyle.Treeview1", [('mystyle.Treeview1.treearea', {'sticky': 'nswe'})])  # Remove the borders
        style.map("Treeview1", background=[('selected', 'green')])

        my_tree_travel = ttk.Treeview(fr1, style="mystyle.Treeview1")
        my_tree_travel['columns'] = (" DATE ", " STATE ", " DISTRICT ")

        my_tree_travel.column("#0", width=0, stretch=NO)
        my_tree_travel.column("#1", anchor=CENTER, width=180, minwidth=50)
        my_tree_travel.column("#2", anchor=CENTER, width=180, minwidth=50)
        my_tree_travel.column("#3", anchor=CENTER, width=180, minwidth=50)

        my_tree_travel.heading("#1", text=" DATE ", anchor=CENTER)
        my_tree_travel.heading("#2", text=" STATE ", anchor=CENTER)
        my_tree_travel.heading("#3", text=" DISTRICT ", anchor=CENTER)

        my_tree_travel.tag_configure('oddrow', background="#9de892")
        my_tree_travel.tag_configure('evenrow', background="lightblue")

        count = 0
        for data in new_lst:
            if count % 2 == 0:
                my_tree_travel.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                                      tags=('evenrow',))
            else:
                my_tree_travel.insert(parent="", index="end", iid=count, text="", values=(data[0], data[1], data[2]),
                                      tags=('oddrow',))

            count += 1

        my_tree_travel.bind('<<TreeviewSelect>>')
        my_tree_travel.pack(side="left", fill="y")
        scrollbar1 = Scrollbar(fr1, orient='vertical')
        scrollbar1.configure(command=my_tree_travel.yview)
        scrollbar1.pack(side="right", fill="y", padx=5)
        my_tree_travel.config(yscrollcommand=scrollbar1.set)
        my_tree_travel.pack()

    @staticmethod
    def search_meet(frame, key, value):
        """
        This function used to popup the result to SearchPage frame when serach button clicks
        :param frame: to what we have to display
        :param key: to what reference we're searching like USN, Name, Date
        :param value: what we have to look for
        :return: nothing
        """
        frame2 = Frame(frame, relief=RAISED, width=550, height=250, bg=SIGNPAGE_BG)
        frame2.place(x=INSERT_EX2 - 170, y=INSERT_HEAD_QUES_GAP_Y + INSERT_QUES_GAP_Y * 2)

        style = ttk.Style()
        style.configure("Treeview1", background="white", foreground="black", fieldbackground="white"
                        , font=("Arial Regular", 12), bd=0, highlightthickness=0)  # Modify the font of the body
        style.configure("mystyle.Treeview1.Heading", font=('Arial', 16, 'bold'),
                        background=TABLE_HEAD_BG, foreground=TABLE_HEAD_FG)  # Modify the font of the headings
        style.layout("mystyle.Treeview1", [('mystyle.Treeview1.treearea', {'sticky': 'nswe'})])  # Remove the borders
        style.map("Treeview1", background=[('selected', 'green')])

        my_tree = ttk.Treeview(frame2, style="mystyle.Treeview1")
        my_tree['columns'] = (" DATE ", " USN ", " NAME ")

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("#1", anchor=CENTER, width=180, minwidth=50)
        my_tree.column("#2", anchor=CENTER, width=180, minwidth=50)
        my_tree.column("#3", anchor=CENTER, width=180, minwidth=50)

        my_tree.heading("#1", text=" DATE ", anchor=CENTER)
        my_tree.heading("#2", text=" USN ", anchor=CENTER)
        my_tree.heading("#3", text=" NAME ", anchor=CENTER)

        my_tree.bind('<<TreeviewSelect>>')
        my_tree.pack(side="left", fill="y")
        scrollbar2 = Scrollbar(frame2, orient='vertical')
        scrollbar2.configure(command=my_tree.yview)
        scrollbar2.pack(side="right", fill="y", padx=5)
        my_tree.config(yscrollcommand=scrollbar2.set)
        my_tree.pack()

def main():
    """
    This is the main function
    """
    app = Ajna()
    app.mainloop()


if __name__ == '__main__':
    main()
