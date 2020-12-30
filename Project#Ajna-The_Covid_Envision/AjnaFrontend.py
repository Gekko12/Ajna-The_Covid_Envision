"""
    Frontend program for GUI based implementation using tkinter
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

INPUT_FONT = ("Arial Regular", 18)
(F_WIDTH, F_HEIGHT) = (1366, 768)  # frame width and height
SIGNPAGE_BG = "white"
SIGNPAGE_INP_FG = "#2a12f0"
SIGNPAGE_INP_BG = "#ecf0f1"


class Ajna(Tk):
    """
    Ajna class inherits tkinter.Frame()
    """

    def __init__(self):
        Tk.__init__(self)

        self.title("    Ajna    ")
        self.geometry(str(F_WIDTH) + "x" + str(F_HEIGHT))  # another dimension for resolution 1400 × 1050
        # we can also put like self.geometry("1366x768")

        container = Frame(self)
        container.pack()

        self.frames = {}

        pages = (MainPage, SigninPage)

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
        signup
        login
    Label -
        tagline (img)
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global tagLine, signin, register

        frame = Frame(self, relief=RAISED, width=F_WIDTH, height=F_HEIGHT)  # as a option for resolution 1400 × 1050
        frame.pack()
        frame.pack_propagate(0)
        frame.config(background="#343434")

        tagLine = PhotoImage(file="backgrounds/Ajna - artboards/tag.png")
        signin = PhotoImage(file="backgrounds/Ajna - artboards/signIn.png")
        register = PhotoImage(file="backgrounds/Ajna - artboards/register.png")

        Label(frame, image=tagLine, bg="#343434").pack(fill="both", side="top")

        style = ttk.Style()
        style.configure("TButton", padding=0, relief=FLAT, background="#343434", foreground="#343434",
                        borderwidth=-2, highlightthickness=0, activebackground="#343434", activeforeground="#343434")

        sign_butt = ttk.Button(frame, command=lambda: controller.show_frame(SigninPage))
        sign_butt.config(image=signin)
        sign_butt.pack(pady=15)

        register_butt = ttk.Button(frame)  # , command=lambda :RegisterPage)
        register_butt.config(image=register)
        register_butt.pack(pady=2)


class SigninPage(Frame):
    """
    Sign in page which have sign in credentials to input
    Buttons -
        forgot_passwd
        sign_in
    Entry -
        username
        passwd
    Label -
        signimg
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
        frame1.pack()
        frame1.config(background=SIGNPAGE_BG)

        l1 = Label(frame1, text="Username :", width=10, font=INPUT_FONT, bg=SIGNPAGE_BG)
        # l1.pack(side="left" ,pady=15)
        l1.grid(row=0, column=10, sticky="w", pady=75, columnspan=2)

        username = Entry(frame1, width=20, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                         bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        username.grid(row=0, column=12, sticky="w", pady=45)
        # username.insert(0, "Enter USN")

        l2 = Label(frame1, text="Password :", width=10, font=INPUT_FONT, bg=SIGNPAGE_BG)
        l2.grid(row=1, column=10, sticky="w", pady=2, columnspan=2)

        passwd = Entry(frame1, width=20, bd=3, font=INPUT_FONT, cursor="arrow", justify="left",
                       bg=SIGNPAGE_INP_BG, fg=SIGNPAGE_INP_FG, selectborderwidth=-5)
        passwd.grid(row=1, column=12, sticky="w", pady=2)
        passwd.config(show="*")

        frame2 = Frame(frame, width=F_WIDTH, height=F_HEIGHT - 100)
        frame2.pack()
        frame2.config(background=SIGNPAGE_BG)

        forgotimg = PhotoImage(file="backgrounds/Ajna - artboards/forgotpwd.png")
        logimg = PhotoImage(file="backgrounds/Ajna - artboards/loginimg.png")
        backimg = PhotoImage(file="backgrounds/Ajna - artboards/backButto.png")

        style = ttk.Style()
        style.configure("TButton", padding=0, background=SIGNPAGE_BG, foreground="#343434",
                        borderwidth=-2, highlightthickness=0, activebackground="#343434", activeforeground="#343434")

        forgot_butt = ttk.Button(frame2, command=self.popup_passwd)
        forgot_butt.config(image=forgotimg)
        forgot_butt.grid(pady=15)

        login_butt = ttk.Button(frame2)
        login_butt.config(image=logimg)
        login_butt.grid(pady=2)

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


app = Ajna()
app.mainloop()
