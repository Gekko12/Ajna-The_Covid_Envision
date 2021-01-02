"""
    Frontend program for GUI based implementation using tkinter
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

LABEL_FONT = ("Arial Regular", 18)
INPUT_FONT = ("Chilanka", 16)
HEADING_PAGE_FONT = ("Helvetica", 25, "bold")
CHECKBUTTON_FONT = ("Arial", 15)

(F_WIDTH, F_HEIGHT) = (1366, 768)  # frame width and height

MAINPAGE_BG = "#343434"

SIGNPAGE_BG = "white"
SIGNPAGE_INP_FG = "#2a12f0"
SIGNPAGE_INP_BG = "#ecf0f1"

(H_X1, H_X2, H_X3) = (208, 594, 980)  # X-axis coordinates of user Homepage for placing buttons
(H_Y1, H_Y2, H_Y3) = (75, 325, 570)

(E_X1, E_Y1, E_Y2, E_Y3, E_Y4) = (970, 147, 247, 347, 447)  # coordinates for daily entry page

(HEAD_X, HEAD_Y) = (550, 35)  # HEADING COORDINATES FOR DAILY ENTRIES ETC ...(X CAN BE VARIED UPON TEXT)


class Ajna(Tk):
    """
    Ajna class inherits tkinter.Frame()
    """

    def __init__(self):
        Tk.__init__(self)

        self.title("~~~ Ajna ~~~")
        self.geometry(str(F_WIDTH) + "x" + str(F_HEIGHT))  # another dimension for resolution 1400 × 1050
        # we can also put like self.geometry("1366x768")

        container = Frame(self)
        container.pack()

        self.frames = {}

        pages = (MainPage, SigninPage, RegisterPage, UserHomePage, DailyEntryPage, CovidCheckPage
                 , CovidSymptomsPage)

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

        global r_img, create_img, backimg1

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        r_img = PhotoImage(file="backgrounds/Ajna - artboards/createAcc.png")
        create_img = PhotoImage(file="backgrounds/Ajna - artboards/createButt.png")
        backimg1 = PhotoImage(file="backgrounds/Ajna - artboards/backButto.png")

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
        back_butt.config(image=backimg1)
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

        travelhist_butt = ttk.Button(frame)
        travelhist_butt.config(image=travelhist_img)
        travelhist_butt.place(x=H_X3, y=H_Y1)

        meethist_butt = ttk.Button(frame)
        meethist_butt.config(image=meethist_img)
        meethist_butt.place(x=H_X1, y=H_Y2)

        help_butt = ttk.Button(frame)
        help_butt.config(image=help_img)
        help_butt.place(x=H_X2, y=H_Y2)

        zone_butt = ttk.Button(frame)
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

        global covidaware_img, insert_img, search_img, reset_img, exit_img, backimg2

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        covidaware_img = PhotoImage(file="backgrounds/Ajna - artboards/covidAware_img.png")
        insert_img = PhotoImage(file="backgrounds/Ajna - artboards/insert_img.png")
        search_img = PhotoImage(file="backgrounds/Ajna - artboards/search_img.png")
        reset_img = PhotoImage(file="backgrounds/Ajna - artboards/reset_img.png")
        exit_img = PhotoImage(file="backgrounds/Ajna - artboards/exit_img.png")
        backimg2 = PhotoImage(file="backgrounds/Ajna - artboards/backButto.png")

        l1 = Label(frame, text="DAILY ENTRIES", font=HEADING_PAGE_FONT, bg=SIGNPAGE_BG)
        l1.place(x=HEAD_X, y=HEAD_Y)

        l2 = Label(frame, image=covidaware_img, bg=SIGNPAGE_BG)
        l2.place(x=50, y=130)

        style = ttk.Style()
        style.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground=SIGNPAGE_BG,
                        borderwidth=-2, highlightthickness=0, activebackground=SIGNPAGE_BG,
                        activeforeground=SIGNPAGE_BG)

        insert_butt = ttk.Button(frame)
        insert_butt.config(image=insert_img)
        insert_butt.place(x=E_X1, y=E_Y1)

        search_butt = ttk.Button(frame)
        search_butt.config(image=search_img)
        search_butt.place(x=E_X1, y=E_Y2)

        reset_butt = ttk.Button(frame)
        reset_butt.config(image=reset_img)
        reset_butt.place(x=E_X1, y=E_Y3)

        exit_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        exit_butt.config(image=exit_img)
        exit_butt.place(x=E_X1, y=E_Y4)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg2)
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

        global ques1_img, ques2_img, covid_symp_img, back_img, backimg3

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background=SIGNPAGE_BG)

        ques1_img = PhotoImage(file="backgrounds/Ajna - artboards/ques1_img.png")
        ques2_img = PhotoImage(file="backgrounds/Ajna - artboards/ques2_img.png")
        covid_symp_img = PhotoImage(file="backgrounds/Ajna - artboards/covid_symp_img.png")
        back_img = PhotoImage(file="backgrounds/Ajna - artboards/back_img.png")
        backimg3 = PhotoImage(file="backgrounds/Ajna - artboards/backButto.png")

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
        self_declare_butt.config(image=back_img)
        self_declare_butt.place(x=680, y=500)

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg3)
        back_butt.place(x=75, y=630)


class CovidSymptomsPage(Frame):
    """
    Displays Covid Symptoms msg only
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global covid_symp1_img, covid_symp2_img, covid_symp3_img, covid_symp4_img, covid_symp5_img, backimg4

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
        backimg4 = PhotoImage(file="backgrounds/Ajna - artboards/backButto.png")

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

        back_butt = ttk.Button(frame, command=lambda: controller.show_frame(UserHomePage))
        back_butt.config(image=backimg4)
        back_butt.place(x=75, y=630)


app = Ajna()
app.mainloop()
