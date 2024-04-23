import sqlite3
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
import random
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Notebook, Style
from time import sleep
import datetime
import os
import customtkinter as ctk

# from tabulate import tabulate #  This library is for Printing Documents with lines table creations
from prettytable import PrettyTable
import prettytable
from tkinter import filedialog

from tkcalendar import Calendar
import configparser  # This mudole is for creating config file in any settings
from serial import *
import tempfile
import win32api
import win32print
import smtplib  # for sending E-Mail
from email.mime.text import MIMEText as MMT
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageGrab, ImageFilter, ImageTk

# ============== Create a config file for saving personal settings =============


config_0 = configparser.ConfigParser()
config_0.read("config.ini")
Title = config_0.get("section_titles", "title")

# Title = "Space4 Software (Scale Controller V.1.0)"


"""
import usb.core
import usb.util

dev = usb.core.find(find_all = True)
busses = usb.busses()

if dev is None:
    raise ValueError('Device not found')

for bus in busses:
    devices = bus.devices
    for dev in devices:
        try:
            name = usb.util.get_string(dev.dev, 19, 1)
        except:
            continue
        dev.set_configuration()
        cfg = dev.get_active_configuration()
        interface_number = cfg[(0,0)].bInterfaceNumber
        alternate_setting = usb.control.get_interface(interface_number)
        print("Device Name:",_name)
        pirnt("Device:", dev.filename)
        print(" idVendor:", hex(dev.idVendor))
        print(" idProduct:", hex(dev.idProduct))
        for config in dev.configurations:
            print("    Configuration:", config.value)
            print("    Total length:", config.totalLength)
            print("    selfPowered:", config.selfPowered)
            print("    remoteWakeup:", config.remoteWakeup)
            print("    maxPower:", config.maxPower)

"""

"""
def calculate_scale():
    weight = float(weight_entry.get())
    scale = weight * 1.5
    scale_label.configure(text=f"Scale:{scale}")

"""


DEFAULTHCRBG = "#4B4B4B"  # 72959F
CTKLIGHT = "#EBEBEB"
CTKDARK = "#242424"
TKDARK = "#4B4B4B"
SaveExtensions = [
    ("choose a format", "*.*"),
    ("text", "*.TXT"),
    ("pdf", "*.PDF"),
    ("html", "*.HTML"),
]

# ============================== The main Roooooooooooooooooot ====================
root = ctk.CTk()
# root.geometry("1300x760+0+0")
root.iconbitmap("hcrIcon.ico")
root.title(Title)
root.state("zoomed")
# root.attributes("-alpha", 0.6)#For Transperincy
root.overrideredirect(True)

welcomeWin = Toplevel(root)
welcomeWin.overrideredirect(True)
welcomeWin.title(Title)
welcomeWin.geometry("1200x550+80+50")


def welcomeDest():
    welcomeWin.destroy()
    blur_overlay_welwin.destroy()


"""
imageLoad = Image.open("guicons/Loading1.gif")
LoadingImg = ImageTk.PhotoImage(imageLoad)
"""
Img4Logo = Image.open("guicons/Space4Img.png")
Img4_4Logo = Img4Logo.resize((200, 200))
S4LogoLargWelcome = ImageTk.PhotoImage(Img4_4Logo)
"""
SpinB = Spinbox(welcomeWin)
SpinB.pack()
"""
LogoLabel = Label(welcomeWin, image=S4LogoLargWelcome)
LogoLabel.pack()
welcomeLbl0 = Label(
    welcomeWin,
    text="Welcome to the scale controlling system",
    font=("Gilroy Extrabold", 30),
    fg="green",
)
welcomeLbl0.pack(fill=BOTH, expand=True)
welcomeLbl1 = Label(
    welcomeWin, text="Space4 Software engineering team", font=("Gilroy Light", 30)
)
welcomeLbl1.pack(fill=BOTH, expand=True)
welcomeLbl1 = Label(
    welcomeWin,
    text="Contact us:\n\tEmail: hcrgroup.info@gmail.com\nPhone & WhatsApp:\n\t+93795552579\n\t+93707386722\nWebsite:\twww.Space4.com",
    justify=LEFT,
)
welcomeLbl1.pack(fill=BOTH, expand=True)


# ============== This is the progress bar ====================
def animate():
    value = Progress_bar["value"]
    value += 1
    if value >= 1000:
        value = 0
    Progress_bar["value"] = value
    welcomeWin.after(100, animate)


Progress_bar = Progressbar(
    master=welcomeWin, mode="determinate", length=720, orient=HORIZONTAL
)
Progress_bar.pack()
DesProgress = Label(Progress_bar, text="wait...", width=180, font=("Arial", 5))
DesProgress.place(x=0, y=7)
animate()
# -------------------------------------------------------------

welcomeLbl1 = Label(
    welcomeWin, text="All rights reserved. Copyright C 2023", font=("Arial", 10)
)
welcomeLbl1.pack(fill=BOTH, expand=True)

welcomeWin.after(13000, welcomeDest)

FontMood_Var = "Bold"
FontStyle_Var = ("Arial", 13)


TRUCK_NUMBER = StringVar()
TRUCK_MODEL = StringVar()
EMPTY_WEIGHT = StringVar()
FULL_WEIGHT = StringVar()
PRICE_CHARGE = StringVar()
GOODS_TYPE = StringVar()
DRIVER_NAME = StringVar()
SERIAL_NUMBER = StringVar()
ORIGIN = StringVar()
DESTINATION = StringVar()
REG_DATE = StringVar()
MANUALDATE = StringVar()
REG_MOOD = StringVar()
ValueTransponder = IntVar()

THEMVARIABLE = StringVar()

DateNow = datetime.date.today()


# ===========================================
def send_email():
    from datetime import datetime
    from time import strftime

    nowTm = datetime.now()
    TimeNow = nowTm.strftime("%H:%M:%S")
    from prettytable import PrettyTable

    FPConn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
    FPCur1 = FPConn1.execute(
        "SELECT COUNT(SERIAL_NUMBER),SUM(FULL_WEIGHT-EMPTY_WEIGHT),SUM(PRICE_CHARGE) FROM ScaleTable"
    )
    fetching1 = FPCur1.fetchall()
    for Rw1 in fetching1:
        culumn1 = Rw1[0]
        culumn2 = Rw1[1]
        culumn3 = Rw1[2]
        culumn4 = DateNow
        culumn5 = TimeNow
        # >>>>>>>>>>> Naked Data Use in anywhere <<<<<<<<<<<
        DT0 = culumn1
        DT1 = culumn2
        DT2 = culumn3
        DT3 = culumn4
        DT4 = culumn5
        Field_names = (
            ["TRUCK_CYCLES", "TOTAL_TIRE", "TOTAL_PRICE", "REPORT_DATE", "REPORT_TIME"],
            [DT0, DT1, DT2, DT3, DT4],
        )

        MyT0 = PrettyTable(Field_names[0])
        MyT0.add_rows(Field_names[1:])
        MyT0.padding_width = 1

        f2S3 = str(MyT0)

    FPCur1.close()
    FPConn1.close()

    config = configparser.ConfigParser()
    config.read("Backup_Config.ini")
    SMADDR = config.get("section_mail", "SMADDR")
    SERVADDR = config.get("section_mail", "SERVADDR")
    SCLNAME = config.get("section_mail", "SCLNAME")
    SENDER = config.get("section_mail", "SENDER")
    SPASSWORD = config.get("section_mail", "SPASSWORD")
    RECEVER = config.get("section_mail", "RECEVER")

    smtpAddr = SMADDR
    servAddr = SERVADDR
    scaleName = SCLNAME
    sender_email = SENDER
    sender_password = SPASSWORD
    recipient_email = RECEVER

    message_text = MMT(f"{f2S3}\n\n\nSpace4 modern software engineering V.1.0")
    try:
        server = smtplib.SMTP(f"{smtpAddr}", servAddr)  # 587
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.ehlo
        message = f"Subject: Message from {scaleName}\n\n{message_text}"
        server.sendmail(sender_email, recipient_email, message)  # message or use it
        server.quit()
        messagebox.showinfo(Title, "Successfully reported.")

    except Exception as e:
        messagebox.showerror(Title, f"An error occurred: {str(e)}")


def VendorFunc():
    adminRoot = ctk.CTkToplevel(root)
    adminRoot.title(Title)
    adminRoot.iconbitmap("hcrIcon.ico")
    adminRoot.geometry("200x120+300+100")
    adminRoot.resizable(0, 0)
    adminRoot.overrideredirect(True)

    # ------this is for Blur other windows--------
    def close_new_window():
        adminRoot.destroy()
        blur_overlay.destroy()

    main_image = ImageTk.PhotoImage(ImageGrab.grab().filter(ImageFilter.BLUR))
    blur_overlay = Label(root, image=main_image)
    blur_overlay.place(x=0, y=0, relwidth=1, relheight=1)
    blur_overlay.image = main_image

    # -------------- To here--------------
    config_0.read("config.ini")
    PSS = config_0.get("section_ps", "PS1")
    VendorPassword = PSS

    def StartVendor():
        Venroot = ctk.CTkToplevel(adminRoot)
        Venroot.title(Title)
        Venroot.geometry("450x530+200+40")
        Venroot.iconbitmap("hcrIcon.ico")
        Venroot.resizable(0, 0)
        Venroot.overrideredirect(True)

        # ------this is for Blur other windows--------
        def close_new_window3():
            Venroot.destroy()
            blur_overlay.destroy()

        """
        main_image = ImageTk.PhotoImage(ImageGrab.grab().filter(ImageFilter.BLUR))
        blur_overlay3 = Label(root, image=main_image)
        blur_overlay3.place(x=0,y=0, relwidth=1, relheight=1)
        blur_overlay3.image = main_image
        #-------------- To here--------------
        """

        AppTitle_Var = StringVar()

        def Vdelete():
            VEntry1.delete(0, END)
            VEntry2.delete(0, END)
            VEntry2PASS.delete(0, END)
            VEntry3.delete(0, END)

        def Var_Save_Func():
            config1 = configparser.ConfigParser()
            if VEntry2.get() != "" or VEntry3.get() != "":
                SMADDR_Val = REntry0.get()
                SERVADDR_Val = REntry1.get()
                SCLNAME_Val = REntry2.get()
                SENDER_Val = VEntry2.get()
                SPASSWORD_Val = VEntry2PASS.get()
                RECEVER_Val = VEntry3.get()
                PORTS_Val = VEntry4.get()
                BAUDS_Val = VEntry5.get()

                try:
                    config1.add_section("section_mail")
                    messagebox.showinfo(Title, "mail saving successful")
                except:
                    messagebox.showinfo(Title, "mail saving successful")
                    pass
                config1.read("config.ini")
                config1.set("section_mail", "SMADDR", SMADDR_Val)
                config1.set("section_mail", "SERVADDR", SERVADDR_Val)
                config1.set("section_mail", "SCLNAME", SCLNAME_Val)
                config1.set("section_mail", "SENDER", SENDER_Val)
                config1.set("section_mail", "SPASSWORD", SPASSWORD_Val)
                config1.set("section_mail", "RECEVER", RECEVER_Val)
                config1.set("section_Saved_ports", "PORTS", PORTS_Val)
                config1.set("section_Saved_ports", "BAUDS", BAUDS_Val)

                with open("Backup_Config.ini", "w") as configfile1:
                    config1.write(configfile1)
                    REntry0.delete(0, END)
                    REntry1.delete(0, END)
                    REntry2.delete(0, END)
                    VEntry2.delete(0, END)
                    VEntry2PASS.delete(0, END)
                    VEntry3.delete(0, END)
                    VEntry4.delete(0, END)
                    VEntry5.delete(0, END)
            else:
                messagebox.showerror(Title, "Can't save empty fields!")

        def ReadConOnEntry():
            config1 = configparser.ConfigParser()
            config1.read("Backup_Config.ini")
            SMADDR = config1.get("section_mail", "SMADDR")
            SERVADDR = config1.get("section_mail", "SERVADDR")
            SCLNAME = config1.get("section_mail", "SCLNAME")
            SENDER = config1.get("section_mail", "SENDER")
            SPASSWORD = config1.get("section_mail", "SPASSWORD")
            RECEVER = config1.get("section_mail", "RECEVER")
            PORTS_Val = config1.get("section_Saved_ports", "PORTS")
            BAUDS_Val = config1.get("section_Saved_ports", "BAUDS")

            REntry0.insert(0, SMADDR)
            REntry1.insert(0, SERVADDR)
            REntry2.insert(0, SCLNAME)
            VEntry2.insert(0, SENDER)
            VEntry2PASS.insert(0, SPASSWORD)
            VEntry3.insert(0, RECEVER)
            VEntry4.insert(0, PORTS_Val)
            VEntry5.insert(0, BAUDS_Val)

        Vfrm2 = ctk.CTkFrame(Venroot)
        Vfrm2.grid(row=1, column=0, sticky=W, padx=20, pady=20)
        Vfrm3 = ctk.CTkFrame(Venroot)
        Vfrm3.grid(row=2, column=0, sticky=W, padx=20, pady=10)

        Vtitle1 = ctk.CTkLabel(
            Venroot,
            text="Vendor Settings",
            font=("Nexa Heavy", 13),
            text_color=("teal", "light yellow"),
        )
        Vtitle1.grid(row=0, column=0, padx=20, sticky=EW)

        VEntLabel1 = ctk.CTkLabel(Vfrm2, text="App title:")
        VEntLabel1.grid(row=0, column=0, padx=5, sticky=W)
        REntLabel0 = ctk.CTkLabel(Vfrm2, text="Host & Server:")
        REntLabel0.grid(row=1, column=0, padx=5, sticky=W)
        REntLabel1 = ctk.CTkLabel(Vfrm2, text="Scale Title:")
        REntLabel1.grid(row=2, column=0, padx=5, sticky=W)
        VEntLabel2 = ctk.CTkLabel(Vfrm2, text="Manager E-Mail:")
        VEntLabel2.grid(row=3, column=0, padx=5, sticky=W)
        VEntLabel2PASS = ctk.CTkLabel(Vfrm2, text="Password:")
        VEntLabel2PASS.grid(row=4, column=0, padx=5, sticky=W)
        VEntLabel3 = ctk.CTkLabel(Vfrm2, text="Admin E-Mail:")
        VEntLabel3.grid(row=5, column=0, padx=5, pady=10, sticky=W)
        VEntLabel4 = ctk.CTkLabel(Vfrm2, text="COM & BAUD:")
        VEntLabel4.grid(row=6, column=0, padx=5, pady=10, sticky=W)

        VEntry1 = ctk.CTkEntry(Vfrm2, placeholder_text="New App Title", state=DISABLED)
        VEntry1.grid(row=0, column=1, padx=5, pady=5, ipadx=70)

        RframeVal = ctk.CTkFrame(Vfrm2)
        RframeVal.grid(row=1, column=1, padx=5, pady=30)
        REntry0 = ctk.CTkEntry(RframeVal, placeholder_text="Host Address", width=200)
        REntry0.grid(row=0, column=0, padx=5, pady=5)
        REntry1 = ctk.CTkEntry(RframeVal, placeholder_text="Server", width=70)
        REntry1.grid(row=0, column=1, padx=5, pady=5)
        REntry2 = ctk.CTkEntry(Vfrm2, placeholder_text="Scale Name")
        REntry2.grid(row=2, column=1, padx=5, pady=5, ipadx=70)
        VEntry2 = ctk.CTkEntry(Vfrm2, placeholder_text="Sender email")
        VEntry2.grid(row=3, column=1, padx=5, pady=5, ipadx=70)
        VEntry2PASS = ctk.CTkEntry(Vfrm2, placeholder_text="Password", show="*")
        VEntry2PASS.grid(row=4, column=1, padx=5, pady=5, ipadx=70)
        VEntry3 = ctk.CTkEntry(Vfrm2, placeholder_text="Recever email")
        VEntry3.grid(row=5, column=1, padx=5, pady=20, ipadx=70)
        VFrameIn = ctk.CTkFrame(Vfrm2)
        VFrameIn.grid(row=6, column=1, pady=20)
        VEntry4 = ctk.CTkEntry(VFrameIn, placeholder_text="Port name", width=150)
        VEntry4.grid(row=0, column=0, padx=5)
        VEntry5 = ctk.CTkEntry(VFrameIn, placeholder_text="Buad Rate number", width=120)
        VEntry5.grid(row=0, column=1, padx=5)
        VButton1 = ctk.CTkButton(Vfrm3, text="Write", command=Var_Save_Func)
        VButton1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        VButton2 = ctk.CTkButton(Vfrm3, text="Clear", command=Vdelete)
        VButton2.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        VButton3 = ctk.CTkButton(
            Vfrm3, text="Read", text_color="yellow", width=95, command=ReadConOnEntry
        )
        VButton3.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        # =========== Check to save changes ============
        CheckE_0_1 = ctk.CTkCheckBox(
            Vfrm2,
            text="Save host & server changes",
            onvalue=1,
            offvalue=0,
            state=DISABLED,
        )
        CheckE_0_1.place(x=112, y=42)
        CheckE_0_2 = ctk.CTkCheckBox(
            Vfrm2,
            text="Save manager & admin email changes",
            onvalue=1,
            offvalue=0,
            state=DISABLED,
        )
        CheckE_0_2.place(x=112, y=110)
        CheckE_0_3 = ctk.CTkCheckBox(
            Vfrm2,
            text="Save indicator connection changes",
            onvalue=1,
            offvalue=0,
            state=DISABLED,
        )
        CheckE_0_3.place(x=112, y=306)

        VenrootExit = ctk.CTkButton(
            Venroot,
            image=AdminExitImg,
            text="",
            hover_color=(CTKLIGHT, CTKDARK),
            width=20,
            fg_color=(CTKLIGHT, CTKDARK),
            command=close_new_window3,
        )
        VenrootExit.place(x=415, y=0)

    def VendorOpen():
        if adminEnt1.get() == VendorPassword:
            StartVendor()
            adminRoot.withdraw()
        else:
            messagebox.showerror(Title, "Please type the correct password!")
            adminEnt1.focus()

    adminLabel1 = ctk.CTkLabel(adminRoot, text="Vendor Login")
    adminLabel1.pack(padx=10)
    adminEnt1 = ctk.CTkEntry(
        adminRoot, placeholder_text="Type Vendor Password", width=200, show="*"
    )
    adminEnt1.pack(padx=10, pady=10)
    adminLogin = ctk.CTkButton(adminRoot, text="Login", command=VendorOpen)
    adminLogin.pack(padx=10)

    adminRootExit = ctk.CTkButton(
        adminRoot,
        image=AdminExitImg,
        text="",
        hover_color=(CTKLIGHT, CTKDARK),
        width=20,
        fg_color=(CTKLIGHT, CTKDARK),
        command=close_new_window,
    )
    adminRootExit.place(x=165, y=0)


mygreen = "#d2ffd2"
myred = "#dd0505"
mylightblue = "light blue"
DEFAULTHCRBG = "#4B4B4B"  # 72959F
BGCOL1 = "#003A45"
BGCOL2 = "#2f2f2f"
FGCOL1 = "#FFFFFF"
FGCOL2 = "#6f7f3f"
FGCOL3 = "#ffffff"
FGCOL4 = "dark red"
BGCOL4 = "white"
BGGRAY = "#6f8f9f"
BGLIGHTBLUE = "light blue"
BGBLUE = "blue"
BGBLACK = "black"
BGYELLOW = "yellow"
BGGREEN = "green"
BGRED = "red"
BGLIGHTYELLOW = "light yellow"
BGDEFAULT = "DFDFDF"
BGORANGE = "orange"
BGLIGHTGREEN = "light green"
BGWHITE = "white"
BGLIGHTGRAY = "light gray"
BGDARKSKY = "#0F1F3F"
MODERNBACK = "#420052"
MODERNFORGROUND = "#8F49A6"
MODERNBACKBLUE = "#5D96A1"
MODERNFORGROUNDBLUE = "#454D9C"
MODERNLIGHTBLUE = "#5D96A1"
MODERNPINK = "#410070"
CTKDARK_ENT = "#2B2B2B"
DarkBlue = "#39003D"
MikroTik = "#7A949A"
DARKENTRY = "#343638"
GRAY_NEW = "#ADADAD"


# =================== Image files =======================
# SettingsImg = PhotoImage(file=r"guicons/SettingsImg.png")

AdminExitImg = ctk.CTkImage(dark_image=Image.open("guicons/ExitImg.png"))

SET1 = Image.open("guicons/BackupImg1.png")
SET2 = SET1.resize((40, 40))
SettingsImg = ImageTk.PhotoImage(SET2)

EDT1 = Image.open("guicons/EditImg.png")
EDT2 = EDT1.resize((40, 40))
EditImg = ImageTk.PhotoImage(EDT2)

PRNT1 = Image.open("guicons/PrintImg.png")
PRNT2 = PRNT1.resize((40, 40))
PrintImg = ImageTk.PhotoImage(PRNT2)

DTA1 = Image.open("guicons/DataImg.png")
DTA2 = DTA1.resize((40, 40))
DataImg = ImageTk.PhotoImage(DTA2)

EXT1 = Image.open("guicons/ExitImg.png")
EXT2 = EXT1.resize((20, 20))
ExitImg = ImageTk.PhotoImage(EXT2)

ActiveRadio1 = Image.open("guicons/RadioImage1.png")
ActiveRadio2 = ActiveRadio1.resize((25, 25))
RadioImage1 = ImageTk.PhotoImage(ActiveRadio2)

UnactiveRadio1 = Image.open("guicons/RadioActiveImage1.png")
UnactiveRadio2 = UnactiveRadio1.resize((25, 25))
RadioActiveImage1 = ImageTk.PhotoImage(UnactiveRadio2)

Minecart1 = Image.open("guicons/MinecartImgEmpty.png")
Minecart2 = Minecart1.resize((40, 40))
MinecartImgEmpty = ImageTk.PhotoImage(Minecart2)

Img0_1 = Image.open("guicons/RestordownImg.png")
Img0_2 = Img0_1.resize((20, 20))
RestordownImg = ImageTk.PhotoImage(Img0_2)

Img1_1 = Image.open("guicons/MinimizeImg.png")
Img_1_2 = Img1_1.resize((20, 20))
MinimizeImg = ImageTk.PhotoImage(Img_1_2)

TabImg1 = Image.open("guicons/TruckImg.png")
TabImg1_1 = TabImg1.resize((35, 35))
TruckImg = ImageTk.PhotoImage(TabImg1_1)

TabImg2 = Image.open("guicons/ReformationImg.png")
TabImg1_2 = TabImg2.resize((35, 35))
ReformationImg = ImageTk.PhotoImage(TabImg1_2)

TabImg3 = Image.open("guicons/ViewReportImg.png")
TabImg1_3 = TabImg3.resize((35, 35))
ViewReportImg = ImageTk.PhotoImage(TabImg1_3)

TabImg4 = Image.open("guicons/ManualImg.png")
TabImg1_4 = TabImg4.resize((35, 35))
ManualImg = ImageTk.PhotoImage(TabImg1_4)

TabImg5 = Image.open("guicons/Space4Img.png")
TabImg1_5 = TabImg5.resize((50, 50))
Space4TitleLogo = ImageTk.PhotoImage(TabImg1_5)

# ===================================
SPSign = PhotoImage(file=r"guicons/ShowPass.png")
DSPSign = PhotoImage(file=r"guicons/DontShowPass.png")
Locked = PhotoImage(file=r"guicons/Locked.png")
Login2 = PhotoImage(file=r"guicons/Login2.png")
Login1 = PhotoImage(file=r"guicons/Login1.png")


style = Style()
style.theme_use("default")
style.configure(
    "TNotebook.Tab",
    background="#222255",
    foreground="#ffffff",
    padding=[20, 6],
    tabmargins=[0, 0, 0, 0],
    font=("Gilroy Light", 10),
)
style.configure("TNotebook", background=DEFAULTHCRBG)
style.map(
    "TNotebook.Tab",
    background=[("selected", "#224499")],
    foreground=[("selected", "#ffff99")],
)
style.layout("cb.TNotebook.Tab", [("TNotebook.Tab", {"side": "left", "sticky": "ne"})])


style2 = ttk.Style()
style2.configure(
    "Treeview.Heading",
    background="#222233",
    foreground=BGWHITE,
    padding=[3, 4],
    tabmargins=[2, 5, 2, 0],
    font=("Arial", 8, "bold"),
)
style2.configure(
    "Treeview",
    background="#333333",
    foreground="#ffffff",
    font=("Bahnschrift SemiBold SemiConden", 10),
    rowheight=27,
    fieldbackground="#33333",
)
style2.map(
    "Treeview",
    background=[("selected", "#ffffff")],
    foreground=[("selected", "#000000")],
)
style2.layout(
    "cb.Treeview.Row",
    [
        ("Treeitme.row", {"sticky": "nsew"}),
        ("Treeitme.image", {"side": "right", "sticky": "w"}),
    ],
)


tabControl = ttk.Notebook(root)

tab1 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=20)
tab2 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=20)
tab3 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=20)
tab4 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=20)

tabControl.add(tab1, text="Cycle forming", image=TruckImg, compound=TOP)
tabControl.add(tab2, text="Reformation", image=ReformationImg, compound=TOP)
tabControl.add(tab3, text="View reports", image=ViewReportImg, compound=TOP)
tabControl.add(tab4, text="Manual", image=ManualImg, compound=TOP)

tabControl.grid(row=0, column=1, padx=40, sticky=W)


# ====================== Functions  =================
def Quit_1():
    AskYsNoMsg = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if AskYsNoMsg > 0:
        root.destroy()


# ====================================== MenuBar Options ==============================
def LightTheme():
    if THEMVARIABLE.get() == "LIGHT_THEM":
        ctk.set_appearance_mode("Light")


def DarkTheme():
    if THEMVARIABLE.get() == "DARK_THEM":
        ctk.set_appearance_mode("Dark")


# Readin Endicator Value ============================================
def val_trans_func():
    import serial
    import re

    conf_01 = configparser.ConfigParser()
    conf_01.read("Backup_Config.ini")

    COMS = conf_01.get("section_Saved_ports", "ports")
    PORTNO = conf_01.get("section_Saved_ports", "bauds")
    serRead = serial.Serial(COMS, PORTNO)

    def EndicatorValRef():
        serRead.write(
            b"R\r\n"
        )  # Set the 'R' or 'W' if this was an approperiate command for your indicator
        response = serRead.readline().decode().strip()
        time.sleep(0.1)
        serRead.open()
        weight_Read = float(response.strip())
        return response

    serRead.close()
    global weight_Read
    EndicatorValRef()


if ValueTransponder.get() > 100:
    val_trans_func()


def portChooseFunc():
    import serial
    import re

    def read_indicator_value():
        if PortChooser.get() == "COM1":
            ser = serial.Serial("COM1", 9600)

            def Val1():
                ser.write(
                    b"W\r\n"
                )  # Set the 'R' or 'W' if this was an approperiate command for your indicator
                response = ser.readline().decode().strip()
                # time.sleep(0.1)
                # ser.open()
                # weight = float(response.strip()) User the Weight into Label Configure which is showing the value
                return response

            CurrentWeight.after(100, Val1)
            ser.close()

        elif PortChooser.get() == "COM2":
            ser = serial.Serial("COM2", 9700)

            def Val2():
                ser.write(
                    b"R\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val2)
            ser.close()

        elif PortChooser.get() == "COM3":
            ser = serial.Serial("COM3", 19200)

            def Val3():
                ser.write(
                    b"R\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val3)
            ser.close()

        elif PortChooser.get() == "COM4":
            ser = serial.Serial("COM4", 38400)

            def Val4():
                ser.write(
                    b"R\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val4)
            ser.close()
        elif PortChooser.get() == "COM5":
            ser = serial.Serial("COM5", 57600)

            def Val5():
                ser.write(
                    b"R\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val5)
            ser.close()

        elif PortChooser.get() == "COM-6":
            ser = serial.Serial("COM-6", 56700)  # The tuple is Port and Baudrate

            def Val6():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val6)
            ser.close()

        elif PortChooser.get() == "COM7":
            ser = serial.Serial("COM7", 115200)

            def Val7():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val7)
            ser.close()

        elif PortChooser.get() == "COM8":
            ser = serial.Serial("COM8", 75)

            def Val8():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val8)
            ser.close()

        elif PortChooser.get() == "COM9":
            ser = serial.Serial("COM9", 110)

            def Val9():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val9)
            ser.close()

        elif PortChooser.get() == "COM10":
            ser = serial.Serial("COM10", 134)

            def Val10():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val10)
            ser.close()

        elif PortChooser.get() == "COM11":
            ser = serial.Serial("COM11", 150)

            def Val11():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val11)
            ser.close()

        elif PortChooser.get() == "COM12":
            ser = serial.Serial("COM12", 200)

            def Val12():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val12)
            ser.close()

        elif PortChooser.get() == "COM13":
            ser = serial.Serial("COM13", 300)

            def Val13():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val13)
            ser.close()

        elif PortChooser.get() == "COM14":
            ser = serial.Serial("COM14", 600)

            def Val14():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val14)
            ser.close()

        elif PortChooser.get() == "COM15":
            ser = serial.Serial("COM15", 1200)

            def Val15():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val15)
            ser.close()

        elif PortChooser.get() == "COM16":
            ser = serial.Serial("COM16", 1800)

            def Val16():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val16)
            ser.close()

        elif PortChooser.get() == "COM17":
            ser = serial.Serial("COM17", 2400)

            def Val17():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val17)
            ser.close()

        elif PortChooser.get() == "COM18":
            ser = serial.Serial("COM18", 4800)

            def Val18():
                ser.write(
                    b"W\r\n"
                )  # Replace the 'R' with the approperiate command for your indicator
                response = ser.readline().decode().strip()
                return response

            CurrentWeight.after(100, Val18)
            ser.close()
        else:
            messagebox.showerror(
                Title, "Port not selected !\nA port detected by system and uses now."
            )
            PortChooser.set("COM1")
            PortWin.withdraw()

    PortWin = ctk.CTkToplevel()
    PortWin.geometry("250x420")
    PortWin.title("Space4")
    PortWin.iconbitmap("hcrIcon.ico")
    PortWin.resizable(0, 0)
    PortWin.overrideredirect(True)

    # ------this is for Blur other windows--------
    def close_new_window1():
        PortWin.destroy()
        blur_overlay1.destroy()

    main_image = ImageTk.PhotoImage(ImageGrab.grab().filter(ImageFilter.BLUR))
    blur_overlay1 = Label(root, image=main_image)
    blur_overlay1.place(x=0, y=0, relwidth=1, relheight=1)
    blur_overlay1.image = main_image

    # -------------- To here--------------

    PORTVARIABLE = StringVar()

    def deleteScaneShow1():  # its just for cleaning the texts
        ScanShow1.delete("1.0", "end")
        ScanShow1.after(30000, deleteScaneShow1)

    target_port = "Port"
    baud_rates = [
        50,
        75,
        110,
        134,
        150,
        200,
        300,
        600,
        1200,
        1800,
        2400,
        4800,
        9600,
        19200,
        38400,
        57600,
        115200,
    ]

    def scan_baud_rates():
        for baud_rate in baud_rates:
            try:
                ser = serial.Serial(target_port, baud_rate, timeout=1)
                line1 = f"Connected at {baud_rate} baud\n"
                ScanShow1.configure(text_color="green", font=("Arial", 15, "bold"))
                ScanShow1.insert(0, line1)
                ser.close()
                SELECTED_COM = PortChooser.get()
            except serial.SerialException:
                line2 = f"Failed at {baud_rate} baud\n"
                ScanShow1.configure(text_color="red", font=("Consolas", 12))
                ScanShow1.insert(END, line2)

            except KeyboardInterrupt:
                line3 = "Scanning interrupted by user\n"
                ScanShow1.configure(text_color="yellow", font=("Arial", 15, "bold"))
                ScanShow1.insert(END, line3)
                break

    ScanShow1 = ctk.CTkTextbox(PortWin, width=230, height=230)
    ScanShow1.pack(pady=30)
    ScanShow1.after(30000, deleteScaneShow1)
    ScanButton1 = ctk.CTkButton(PortWin, text="Port Scan", command=scan_baud_rates)
    ScanButton1.pack()
    TruckModel_Mini = [
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "COM5",
        "COM-6",
        "COM7",
        "COM8",
        "COM9",
        "COM10",
        "COM11",
        "COM12",
        "COM13",
        "COM14",
        "COM15",
        "COM16",
        "COM17",
        "COM18",
    ]
    PORTVARIABLE.set("Choose the indicator serial port")

    PortChooser = ctk.CTkComboBox(
        PortWin, width=230, values=TruckModel_Mini, variable=PORTVARIABLE
    )
    PortChooser.pack(padx=10, pady=10)

    def PortWinWithdraw():
        PortWin.withdraw()

    def update_value_label():
        value = read_indicator_value()
        Value_string = value
        CurrentWeight.after(100, update_value_label)
        Ent4.delete(0, END)
        Ent4.insert(0, f"{value}")

        CurrentWeight.configure(text=f"{value} /Kg")
        if value != None:
            Btn_Data.configure(
                text="Truck\nDetected",
                font=("Arial", 12, "bold"),
                width=80,
                height=40,
                state=NORMAL,
            )
            PortConnectionLabel.configure(
                text_color=("green", "light green"), text="Connection successful"
            )
            PortWin.after(3000, PortWinWithdraw)
            while ValueTransponder < 500:
                Btn_Data.configure(
                    text="Truck not\nDetected",
                    font=("Arial", 12, "bold"),
                    width=80,
                    height=40,
                    state=DISABLED,
                )

        else:
            Btn_Data.configure(
                text="Truck not\nDetected",
                font=("Arial", 12, "bold"),
                width=80,
                height=40,
                state=DISABLED,
            )
            PortConnectionLabel.configure(
                text_color=("red", "orange"), text="Connection Failed"
            )

    update_value_button = ctk.CTkButton(
        PortWin, text="Update value", command=update_value_label
    )  # and switching the update value function
    update_value_button.pack()

    PortConnectionLabel = ctk.CTkLabel(PortWin, text="")
    PortConnectionLabel.pack(pady=20)

    PortWinExit = ctk.CTkButton(
        PortWin,
        image=AdminExitImg,
        text="",
        hover_color=(CTKLIGHT, CTKDARK),
        width=20,
        fg_color=(CTKLIGHT, CTKDARK),
        command=close_new_window1,
    )
    PortWinExit.place(x=215, y=0)


# ctk.set_default_color_theme("green")


# ===================== Calculator ====================


def Calculate():
    CalcRoot = ctk.CTkToplevel(root)
    CalcRoot.title("Space4 Calculator")
    CalcRoot.iconbitmap("hcrIcon.ico")
    CalcRoot.resizable(0, 0)
    CalcRoot.attributes("-alpha", 1.0)

    def btn_click(item):
        global expression
        expression = expression + str(item)
        input_text.set(expression)

    # 'bt_clear' function :This is used to clear
    # the input field
    def bt_clear():
        global expression
        expression = ""
        input_text.set("")

    # 'bt_equal':This method calculates the expression
    # present in input field
    def bt_equal():
        global expression
        result = str(
            eval(expression)
        )  # 'eval':This function is used to evaluates the string expression directly
        input_text.set(result)
        expression = ""

    # 'StringVar()' :It is used to get the instance of input field
    input_text = StringVar()

    # Let us creating a frame for the input field
    input_frame = ctk.CTkFrame(CalcRoot)
    input_frame.grid(row=0, column=0, padx=5, pady=5)

    input_field = ctk.CTkEntry(
        input_frame,
        font=("Courier New", 20, "bold"),
        textvariable=input_text,
        width=320,
        justify=RIGHT,
    )
    input_field.grid(row=0, column=0, ipady=12)
    # 'ipady' is internal padding to increase the height of input field

    # Let us creating another 'Frame' for the button below the 'input_frame'
    btns_frame = ctk.CTkFrame(CalcRoot)
    btns_frame.grid(row=1, column=0, pady=5)

    # first row
    clear = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="C",
        text_color=("orange", "red"),
        fg_color=("gray", "#555555"),
        width=245,
        height=50,
        cursor="hand1",
        command=lambda: bt_clear(),
    ).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
    divide = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="/",
        text_color=("light blue", "white"),
        fg_color=("gray", "#555555"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click("/"),
    ).grid(row=0, column=3, padx=1, pady=1)
    # second row
    seven = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="7",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(7),
    ).grid(row=1, column=0, padx=1, pady=1)
    eight = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="8",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(8),
    ).grid(row=1, column=1, padx=1, pady=1)
    nine = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="9",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(9),
    ).grid(row=1, column=2, padx=1, pady=1)
    multiply = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="*",
        text_color=("light blue", "white"),
        fg_color=("gray", "#555555"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click("*"),
    ).grid(row=1, column=3, padx=1, pady=1)

    # third row

    four = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="4",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(4),
    ).grid(row=2, column=0, padx=1, pady=1)
    five = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="5",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(5),
    ).grid(row=2, column=1, padx=1, pady=1)
    six = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="6",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(6),
    ).grid(row=2, column=2, padx=1, pady=1)
    minus = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="-",
        text_color=("light blue", "white"),
        fg_color=("gray", "#555555"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click("-"),
    ).grid(row=2, column=3, padx=1, pady=1)
    # fourth row
    one = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="1",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(1),
    ).grid(row=3, column=0, padx=1, pady=1)
    two = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="2",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(2),
    ).grid(row=3, column=1, padx=1, pady=1)
    three = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="3",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(3),
    ).grid(row=3, column=2, padx=1, pady=1)
    plus = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="+",
        text_color=("light blue", "white"),
        fg_color=("gray", "#555555"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click("+"),
    ).grid(row=3, column=3, padx=1, pady=1)

    # fourth row

    zero = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="0",
        text_color=(DarkBlue, "white"),
        fg_color=("light gray", "#333333"),
        width=160,
        height=50,
        cursor="hand2",
        command=lambda: btn_click(0),
    ).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
    point = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text=".",
        text_color=("light blue", "white"),
        fg_color=("gray", "#555555"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: btn_click("."),
    ).grid(row=4, column=2, padx=1, pady=1)
    equals = ctk.CTkButton(
        btns_frame,
        font=("Arial", 20, "bold"),
        border_width=1,
        text="=",
        text_color=("light blue", "white"),
        fg_color=("gray", "#555555"),
        width=80,
        height=50,
        cursor="hand2",
        command=lambda: bt_equal(),
    ).grid(row=4, column=3, padx=1, pady=1)


expression = ""


# +++++++++++++++++++++++++ SIDE Bar +++++++++++++++++++++++++++

DarkBlue = "#222255"
min_w = 40
max_w = 200
cur_width = min_w
expanded = False


def Expand_1():
    global cur_width, expanded
    cur_width += 10
    rep = frame.after(10, Expand_1)
    frame.config(width=cur_width)
    if cur_width >= max_w:
        expanded = True
        frame.after_cancel(rep)
        fill()


def Contract_1():
    global cur_width, expanded
    cur_width -= 10
    rep = frame.after(5, Contract_1)
    frame.config(width=cur_width)
    if cur_width <= min_w:
        expanded = False
        frame.after_cancel(rep)
        fill()


def fill():
    if expanded:
        FileBtn.config(text="  External Devices", image=HomeImg, command=portChooseFunc)
        SetBtn.config(text="  Vendor Settings", image=SettingsImg, command=VendorFunc)
        ViewBtn.config(text="  Bill View", image=DataImg)
        LogoLable.config(image=S4LogoLarg)
        DevName.config(
            text="Space4 Software", font=("Gilroy Light", 13), bg=DarkBlue, fg="white"
        )
        WindowBtn.config(
            text="  Window",
            image=WindowImg,
        )
        ToolBtn.config(text="  Calculator", image=ToolImg, command=Calculate)
        AboutBtn.config(text="  About", image=AboutImg)
        ThemRadioBtn_1.config(text="Light   ")
        ThemRadioBtn_2.config(text="Dark    ")
        ThemSeprator0.config(text="________________________________", fg="white")
        ThemSeprator1.config(text="________________________________", fg="white")
        ThemSeprator2.config(text="________________________________", fg="white")

    else:
        FileBtn.config(text="", image=HomeImg)
        SetBtn.config(text="", image=SettingsImg)
        ViewBtn.config(text="", image=DataImg)
        LogoLable.config(image=S4Logo)
        DevName.config(text="", bg=DarkBlue)
        WindowBtn.config(text="", image=WindowImg)
        ToolBtn.config(text="", image=ToolImg)
        AboutBtn.config(text="", image=AboutImg)
        ThemRadioBtn_1.config(text="")
        ThemRadioBtn_2.config(text="")
        ThemSeprator0.config(text="")
        ThemSeprator1.config(text="")
        ThemSeprator2.config(text="")


def MEnter1(event):
    FileBtn.config(fg="orange", font=("Nexa Heavy", 10))


def MLeave1(event):
    FileBtn.config(fg="light yellow", font=("Gilroy Light", 9))


def MEnter2(event):
    SetBtn.config(fg="orange", font=("Nexa Heavy", 10))


def MLeave2(event):
    SetBtn.config(fg="light yellow", font=("Gilroy Light", 9))


def MEnter3(event):
    ViewBtn.config(fg="orange", font=("Nexa Heavy", 11))


def MLeave3(event):
    ViewBtn.config(fg="light yellow", font=("Gilroy Light", 9))


def MEnter4(event):
    WindowBtn.config(fg="orange", font=("Nexa Heavy", 11))


def MLeave4(event):
    WindowBtn.config(fg="light yellow", font=("Gilroy Light", 9))


def MEnter5(event):
    ToolBtn.config(fg="orange", font=("Nexa Heavy", 11))


def MLeave5(event):
    ToolBtn.config(fg="light yellow", font=("Gilroy Light", 9))


def MEnter6(event):
    AboutBtn.config(fg="orange", font=("Nexa Heavy", 11))


def MLeave6(event):
    AboutBtn.config(fg="light yellow", font=("Gilroy Light", 9))


hm1 = Image.open("guicons/HomeImg.png")
hm2 = hm1.resize((25, 25))
HomeImg = ImageTk.PhotoImage(hm2)

Img1 = Image.open("guicons/SettingsImg.png")
Img1_1 = Img1.resize((25, 25))
SettingsImg = ImageTk.PhotoImage(Img1_1)

Img2 = Image.open("guicons/DataImg.png")
Img2_2 = Img2.resize((25, 25))
DataImg = ImageTk.PhotoImage(Img2_2)

Img3 = Image.open("guicons/Space4RoundImg.png")
Img3_3 = Img3.resize((25, 25))
S4Logo = ImageTk.PhotoImage(Img3_3)

Img4 = Image.open("guicons/Space4Img.png")
Img4_4 = Img4.resize((100, 100))
S4LogoLarg = ImageTk.PhotoImage(Img4_4)

Img5 = Image.open("guicons/WindowImg.png")
Img5_5 = Img5.resize((25, 25))
WindowImg = ImageTk.PhotoImage(Img5_5)

Img6 = Image.open("guicons/ToolImg.png")
Img6_6 = Img6.resize((25, 25))
ToolImg = ImageTk.PhotoImage(Img6_6)

Img7 = Image.open("guicons/AboutImg.png")
Img7_7 = Img7.resize((25, 25))
AboutImg = ImageTk.PhotoImage(Img7_7)

Img8 = Image.open("guicons/ThemRadioOff.png")
Img8_8 = Img8.resize((25, 25))
ThemRadioOff = ImageTk.PhotoImage(Img8_8)

Img9 = Image.open("guicons/ThemRadioON.png")
Img9_9 = Img9.resize((25, 25))
ThemRadioON = ImageTk.PhotoImage(Img9_9)


root.update()
frame = Frame(root, bg=DarkBlue, width=40, height=750)
frame.place(x=0, y=0)

LogoLable = Label(frame, image=S4Logo, bd=0, bg=DarkBlue)
LogoLable.grid(row=0, column=0, padx=5, pady=5)
DevName = Label(frame, text="", bg=DarkBlue, font=("Arial Black", 12))
DevName.grid(row=1, column=0)
ThemSeprator0 = Label(frame, bg=DarkBlue, bd=0, text="")
ThemSeprator0.grid(row=2, column=0)

FileBtn = Button(
    frame,
    image=HomeImg,
    bg=DarkBlue,
    activebackground=DarkBlue,
    bd=0,
    fg="white",
    relief="flat",
    compound=LEFT,
    font=("Gilroy Light", 9),
)
FileBtn.grid(row=3, column=0, pady=5, padx=5, sticky=W)
SetBtn = Button(
    frame,
    image=SettingsImg,
    bg=DarkBlue,
    activebackground=DarkBlue,
    bd=0,
    fg="white",
    relief="flat",
    compound=LEFT,
    font=("Gilroy Light", 9),
)
SetBtn.grid(row=4, column=0, pady=5, padx=5, sticky=W)
ViewBtn = Button(
    frame,
    image=DataImg,
    bg=DarkBlue,
    activebackground=DarkBlue,
    bd=0,
    fg="white",
    relief="flat",
    compound=LEFT,
    font=("Gilroy Light", 9),
)
ViewBtn.grid(row=5, column=0, pady=5, padx=5, sticky=W)
WindowBtn = Button(
    frame,
    image=WindowImg,
    bg=DarkBlue,
    activebackground=DarkBlue,
    bd=0,
    fg="white",
    relief="flat",
    compound=LEFT,
    font=("Gilroy Light", 9),
)
WindowBtn.grid(row=6, column=0, pady=5, padx=5, sticky=W)
ToolBtn = Button(
    frame,
    image=ToolImg,
    bg=DarkBlue,
    activebackground=DarkBlue,
    bd=0,
    fg="white",
    relief="flat",
    compound=LEFT,
    font=("Gilroy Light", 9),
)
ToolBtn.grid(row=7, column=0, pady=5, padx=5, sticky=W)
AboutBtn = Button(
    frame,
    image=AboutImg,
    bg=DarkBlue,
    activebackground=DarkBlue,
    bd=0,
    fg="white",
    relief="flat",
    compound=LEFT,
    font=("Gilroy Light", 9),
)
AboutBtn.grid(row=8, column=0, pady=5, padx=5, sticky=W)

ThemFrame1 = Frame(frame, bg=DarkBlue, bd=1)
ThemFrame1.grid(row=9, column=0, padx=0, pady=20)
ThemSeprator1 = Label(ThemFrame1, bg=DarkBlue, bd=0, text="")
ThemSeprator1.grid(row=0, column=0)

ThemRadioBtn_1 = Radiobutton(
    ThemFrame1,
    compound=RIGHT,
    wraplength=False,
    indicatoron=False,
    image=ThemRadioOff,
    selectimage=ThemRadioON,
    bd=0,
    selectcolor=DarkBlue,
    text="",
    activebackground=DarkBlue,
    bg=DarkBlue,
    fg=BGWHITE,
    variable=THEMVARIABLE,
    value="LIGHT_THEM",
    command=LightTheme,
)
ThemRadioBtn_1.grid(row=1, column=0, padx=5, pady=0, sticky=W)

ThemRadioBtn_2 = Radiobutton(
    ThemFrame1,
    compound=RIGHT,
    wraplength=False,
    indicatoron=False,
    image=ThemRadioOff,
    selectimage=ThemRadioON,
    bd=0,
    selectcolor=DarkBlue,
    text="",
    activebackground=DarkBlue,
    bg=DarkBlue,
    fg=BGWHITE,
    variable=THEMVARIABLE,
    value="DARK_THEM",
    command=DarkTheme,
)
ThemRadioBtn_2.grid(row=2, column=0, padx=5, pady=0, sticky=W)

ThemSeprator2 = Label(ThemFrame1, bg=DarkBlue, bd=0, text="")
ThemSeprator2.grid(row=3, column=0)

FileBtn.bind("<Enter>", MEnter1)
FileBtn.bind("<Leave>", MLeave1)
SetBtn.bind("<Enter>", MEnter2)
SetBtn.bind("<Leave>", MLeave2)
ViewBtn.bind("<Enter>", MEnter3)
ViewBtn.bind("<Leave>", MLeave3)
WindowBtn.bind("<Enter>", MEnter4)
WindowBtn.bind("<Leave>", MLeave4)
ToolBtn.bind("<Enter>", MEnter5)
ToolBtn.bind("<Leave>", MLeave5)
AboutBtn.bind("<Enter>", MEnter6)
AboutBtn.bind("<Leave>", MLeave6)

frame.bind("<Enter>", lambda e: Expand_1())
frame.bind("<Leave>", lambda e: Contract_1())

frame.grid_propagate(False)


# ============================= Database Part ==========================


with sqlite3.connect("DataBaseDir/ExtraScale.db") as db:
    cur = db.cursor()
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS RegTruck(
    TRUCK_NUMBER INTEGER PRIMARY KEY NOT NULL,
    TRUCK_MODEL TEXT NOT NULL,
    EMPTY_WEIGHT INTEGER NOT NULL,
    DRIVER_NAME TEXT NOT NULL,
    REG_DATE DATE,
    REG_TIME TIME,
    REG_MOOD TEXT NOT NULL,
    TIME_ID DATETIME);
    """
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS ScaleTable(
    TRUCK_NUMBER INTEGER NOT NULL,
    TRUCK_MODEL TEXT NOT NULL,
    EMPTY_WEIGHT INTEGER NOT NULL,
    FULL_WEIGHT INTEGER NOT NULL,
    PRICE_CHARGE INTEGER NOT NULL,
    GOODS_TYPE TEXT NOT NULL,
    DRIVER_NAME TEXT NOT NULL,
    SERIAL_NUMBER INTEGER PRIMARY KEY AUTOINCREMENT,
    ORIGIN TEXT NOT NULL,
    DESTINATION TEXT NOT NULL,
    REG_DATE DATE,
    REG_TIME TIME,
    REG_MOOD TEXT NOT NULL,
    TIME_ID DATETIME);
    """
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS GraphTable1(
    G_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    G_Sun INTEGER NOT NULL,
    G_Mon INTEGER NOT NULL,
    G_Tue INTEGER NOT NULL,
    G_Wed INTEGER NOT NULL,
    G_Thu INTEGER NOT NULL,
    G_Fri INTEGER NOT NULL,
    G_Sat INTEGER NOT NULL);
    """
    )


# BACKUP DATABASE DataBaseDir/ExtraScale.db TO DISK = 'C:User/Desktop/FlanFolder/'

"""
def submit():
    DateNow = datetime.date.today()
    conn1 = sqlite3.connect('DataBaseDir/ExtraScale.db')
    cur1 = conn1.cursor()
    if Ent1.get() == "" or Ent3.get() == "" or Ent4.get() == "" or Ent6.get() == "" or Ent7.get() == "" or Ent8.get() == "":
        messagebox.showwarning("Ooh","Please fill the entries befor saving file!")
    else:
        cur1.execute(f"insert into ScaleTable (TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,\
            GOODS_TYPE,DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE)\
            values ('{TRUCK_NUMBER.get()}','{TRUCK_MODEL.get()}','{EMPTY_WEIGHT.get()}',\
            '{FULL_WEIGHT.get()}','{PRICE_CHARGE.get()}','{GOODS_TYPE.get()}','{DRIVER_NAME.get()}',\
            '{SERIAL_NUMBER.get()}','{ORIGIN.get()}','{DESTINATION.get()}','{DateNow}')")

    conn1.commit()
    conn1.close()
"""


def submit():
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur1 = conn.cursor()
    selected_item = MiniTree1.selection()[0]
    for selected_item in MiniTree1.selection():
        from datetime import datetime
        from time import strftime

        nowTm = datetime.now()
        TimeNow = nowTm.strftime("%H:%M:%S")

        cur1.execute(
            "SELECT * FROM RegTruck WHERE TRUCK_NUMBER=?",
            (MiniTree1.set(selected_item, "#1"),),
        )

        fetch1 = cur1.fetchall()
        for Row in fetch1:
            Row0 = Row[0]
            Row1 = Row[1]
            Row2 = Row[2]
            Row3 = Row[3]
            Row4 = Row[4]
            Row5 = Row[5]
            Row6 = Row[6]

            # if FULL_WEIGHT.get() == '' or PRICE_CHARGE.get() == '' or GOODS_TYPE.get() == ''or ORIGIN.get()==''or DESTINATION.get()=='':
            if (
                PRICE_CHARGE.get() == ""
                or GOODS_TYPE.get() == ""
                or ORIGIN.get() == ""
                or DESTINATION.get() == ""
            ):
                messagebox.showinfo(Title, "Fill the empty fields please!")
            else:
                import serial
                from datetime import datetime
                from time import strftime

                nowTm = datetime.now()
                TimeNow = nowTm.strftime("%H:%M:%S")

                conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
                cur = conn.cursor()
                cur.execute(
                    f"insert into ScaleTable (TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,\
                    GOODS_TYPE,DRIVER_NAME,ORIGIN,DESTINATION,REG_DATE,REG_TIME,REG_MOOD,TIME_ID) values ('{Row0}','{Row1}','{Row2}',\
                    '{ValueTransponder.get()}','{PRICE_CHARGE.get()}','{GOODS_TYPE.get()}','{Row3}',\
                    '{ORIGIN.get()}','{DESTINATION.get()}','{Row4}','{Row5}','{Row6}','{nowTm}')"
                )

                conn.commit()
    conn.commit()

    def PrintFast():
        TimeNow = nowTm.strftime("%H:%M:%S")
        from prettytable import PrettyTable

        selected_item = MiniTree1.selection()[0]
        for selected_item in MiniTree1.selection():
            bill_file = tempfile.mktemp(".txt")

            FPConn2 = sqlite3.connect("DataBaseDir/ExtraScale.db")
            FPCur2 = FPConn2.execute(
                "SELECT MAX(SERIAL_NUMBER),MAX(REG_DATE) FROM ScaleTable"
            )
            fetching1 = FPCur2.fetchall()
            for Rw1 in fetching1:
                culumn1 = Rw1[0]
                culumn2 = Rw1[1]
                culumn3 = TimeNow

                # >>>>>>>>>>> Naked Data Use in anywhere <<<<<<<<<<<
                DT1 = Ent4.get()
                DT2 = Ent5.get()
                DT3 = Ent6.get()
                DT4 = culumn1
                DT5 = Ent9.get()
                DT6 = Ent10.get()
                DT7 = culumn2
                DT8 = culumn3

                Field_names = (
                    [
                        "FULL_W",
                        "PRICE",
                        "GOODS",
                        "SERIAL_NO",
                        "ORIGIN",
                        "DEST",
                        "DATE",
                        "TIME",
                    ],
                    [DT1, DT2, DT3, DT4, DT5, DT6, DT7, DT8],
                )

                MyT0 = PrettyTable(Field_names[0])
                MyT0.add_rows(Field_names[1:])
                MyT0.padding_width = 1

                f2S3 = str(MyT0)

                FPConn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
                FPCur1 = FPConn1.execute(
                    "SELECT TRUCK_NUMBER AS TRUCK_NO,TRUCK_MODEL,EMPTY_WEIGHT AS EMPTY_WT,DRIVER_NAME,REG_DATE,REG_TIME AS R_TIME FROM RegTruck  WHERE TRUCK_NUMBER=?",
                    (MiniTree1.set(selected_item, "#1"),),
                )
                MyT1 = prettytable.from_db_cursor(FPCur1)
                MyT1.padding_width = 1
                file2Save2 = str(MyT1)
                open(bill_file, "w").writelines("\n\n\n\n\n\n\n\n\n")
                open(bill_file, "a").writelines(file2Save2)
                open(bill_file, "a").writelines("\n")
                open(bill_file, "a").writelines(f2S3)

            FPCur2.close()
            FPConn2.close()

            FPCur1.close()
            FPConn1.close()

            win32api.ShellExecute(
                0,
                "print",
                bill_file,
                '/d:"%s"' % win32print.GetDefaultPrinter(),
                ".",
                0,
            )
            # chp = open(bill_file, "r")
            # print(chp)
            Ent4.delete(0, END)
            Ent5.delete(0, END)
            Ent6.delete(0, END)
            Ent9.delete(0, END)
            Ent10.delete(0, END)
            Ent5.focus()
            Ref1()

    # PrintFast()

    def PrintFast1():  # This function prints data without prettyTable
        TimeNow = nowTm.strftime("%H:%M:%S")
        selected_item = MiniTree1.selection()[0]
        for selected_item in MiniTree1.selection():
            bill_file = tempfile.mktemp(".txt")

            FPConn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
            FPCur1 = FPConn1.execute(
                "SELECT MAX(SERIAL_NUMBER),MAX(REG_DATE) FROM ScaleTable"
            )
            fetching1 = FPCur1.fetchall()
            for Rw2 in fetching1:
                culumn1 = Rw2[0]
                culumn2 = Rw2[1]
                culumn3 = TimeNow

                # >>>>>>>>>>> Naked Data Use in anywhere <<<<<<<<<<<
                DT1 = Ent4.get()  # Full Weight
                DT2 = Ent5.get()  # Price Charge
                DT3 = Ent6.get()  # Goods Type
                DT4 = culumn1  # Serial No
                DT5 = Ent9.get()  # Origin
                DT6 = Ent10.get()  # Distination
                DT7 = culumn2  # Date
                DT8 = culumn3  # Bill Time Current

                FPConn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
                FPCur1 = FPConn1.execute(
                    "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,DRIVER_NAME,REG_DATE,REG_TIME FROM RegTruck  WHERE TRUCK_NUMBER=?",
                    (MiniTree1.set(selected_item, "#1"),),
                )
                fetching1 = FPCur1.fetchall()
                for Rw1 in fetching1:
                    culumn1_1 = Rw1[0]
                    culumn2_2 = Rw1[1]
                    culumn3_3 = Rw1[2]
                    culumn4_4 = Rw1[3]
                    culumn5_5 = Rw1[4]
                    culumn6_6 = Rw1[5]

                    DT9 = culumn1_1  # Truck No
                    DT10 = culumn2_2  # Truck Model
                    DT11 = culumn3_3  # Empty Weight
                    DT12 = culumn4_4  # Driver Name
                    DT13 = culumn5_5  # Reg Date
                    DT14 = culumn6_6  # Reg Time
                    DT15 = int(DT1) - int(DT11)  # Net Weight

                    open(bill_file, "w").writelines("\n\n\n\n\n\n")
                    open(bill_file, "a").writelines(str(DT13))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT8))  # Or use DT14
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT4))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT9))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT12))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT10))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT3))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT11))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT1))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT15))
                    open(bill_file, "a").writelines("\n")
                    open(bill_file, "a").writelines(str(DT2))

            FPCur1.close()
            FPConn1.close()

            win32api.ShellExecute(
                0,
                "print",
                bill_file,
                '/d:"%s"' % win32print.GetDefaultPrinter(),
                ".",
                0,
            )
            # chp = open(bill_file, "r")
            # print(chp)

            Ent4.delete(0, END)
            Ent5.delete(0, END)
            Ent6.delete(0, END)
            Ent9.delete(0, END)
            Ent10.delete(0, END)
            Ent5.focus()
            Ref1()

    PrintFast1()


def ClearEntry1():
    Ent4.delete(0, END)
    Ent5.delete(0, END)
    Ent6.delete(0, END)
    Ent9.delete(0, END)
    Ent10.delete(0, END)
    Ent5.focus()


def Ref1():
    Tree1.delete(*Tree1.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute(
        """SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
    DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable"""
    )

    fetch = cur.fetchall()
    for data in fetch:
        Tree1.insert("", "end", values=(data))
    cur.close()
    conn.close()
    MiniRef1()


def MiniRef1():
    MiniTree1.delete(*MiniTree1.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute(
        """SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,DRIVER_NAME,REG_DATE FROM RegTruck """
    )
    fetch = cur.fetchall()
    for data in fetch:
        MiniTree1.insert("", "end", values=(data))
    cur.close()
    conn.close()


# ============ Mini Root For Empty Trucks Reg ==============
def MiniRootFunc():
    Miniroot = ctk.CTkToplevel()
    Miniroot.iconbitmap("hcrIcon.ico")
    Miniroot.title("HCR-BLUE")
    Miniroot.geometry("370x340+400+50")
    Miniroot.resizable(0, 0)
    Miniroot.attributes("-alpha", 0.9)
    Miniroot.overrideredirect(True)

    # ------this is for Blur other windows--------
    def close_new_window2():
        Miniroot.destroy()
        blur_overlay2.destroy()

    main_image = ImageTk.PhotoImage(ImageGrab.grab().filter(ImageFilter.BLUR))
    blur_overlay2 = Label(root, image=main_image)
    blur_overlay2.place(x=0, y=0, relwidth=1, relheight=1)
    blur_overlay2.image = main_image

    # -------------- To here--------------
    # ========== Variables ============
    TRUCK_NUMBER_MINI = StringVar()
    TRUCK_MODEL_MINI = StringVar()
    DRIVER_NAME_MINI = StringVar()

    # ====== Functions =============

    def MiniSubmit():
        import datetime

        DateNow = datetime.date.today()
        conn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
        cur1 = conn1.cursor()
        if (
            MiniEntry1.get() == ""
            or MiniEntry2.get() == ""
            or MiniEntry3.get() == ""
            or MiniEntry4.get() == ""
        ):
            messagebox.showwarning("Ooh", "Please fill the entries befor saving file!")
        else:
            from datetime import datetime
            from time import strftime

            nowTm = datetime.now()
            TimeNow = nowTm.strftime("%H:%M:%S")

            cur1.execute(
                f"insert into RegTruck (TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,\
                DRIVER_NAME,REG_DATE,REG_TIME,REG_MOOD,TIME_ID)\
                values ('{TRUCK_NUMBER_MINI.get()}','{TRUCK_MODEL_MINI.get()}','{MiniEntry4.get()}',\
                '{DRIVER_NAME_MINI.get()}',\
                '{DateNow}','{TimeNow}','Auto','{nowTm}')"
            )

        conn1.commit()
        conn1.close()

        MiniEntry1.delete(0, END)
        MiniEntry2.set("Choose Truck Model")
        MiniEntry3.delete(0, END)
        MiniEntry4.delete(0, END)
        MiniEntry1.focus()
        Ref1()
        MiniRef1()

    def MiniClearFunc():
        MiniEntry1.delete(0, END)
        MiniEntry2.set("Choose Truck Model")
        MiniEntry3.delete(0, END)
        MiniEntry4.delete(0, END)
        MiniEntry1.focus()

    # ==================== Mini Frames ================
    MiniFrame0 = ctk.CTkLabel(
        Miniroot,
        text="Truck Registeration",
        font=("Arial", 20, "bold"),
        text_color=("green", "light blue"),
    )
    MiniFrame0.grid(row=0, column=0, padx=50, pady=20)

    MiniFrame1 = ctk.CTkFrame(Miniroot)
    MiniFrame1.grid(row=1, column=0)

    MiniFrameBot = ctk.CTkFrame(Miniroot)
    MiniFrameBot.grid(row=2, column=0)

    MiniFrameInfo = ctk.CTkLabel(Miniroot, text="HCR-BLUE", font=("Arial", 9, "bold"))
    MiniFrameInfo.grid(row=3, column=0)

    # ============= Wedgets =====================

    MiniLabel1 = ctk.CTkLabel(MiniFrame1, text="Truck Number:")
    MiniLabel1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    MiniEntry1 = ctk.CTkEntry(
        MiniFrame1,
        width=250,
        font=("Arial", 15, "bold"),
        height=35,
        corner_radius=7,
        textvariable=TRUCK_NUMBER_MINI,
    )
    MiniEntry1.grid(row=0, column=1)
    MiniEntry1.focus()

    MiniLabel2 = ctk.CTkLabel(MiniFrame1, text="Truck Model:")
    MiniLabel2.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    TruckModel_Mini = ["Actrus", "Hino", "Mazda", "Kamaz"]
    TRUCK_MODEL_MINI.set("Choose Truck Model")
    MiniEntry2 = ctk.CTkComboBox(
        MiniFrame1,
        width=250,
        font=("Arial", 15, "bold"),
        height=35,
        values=TruckModel_Mini,
        corner_radius=10,
        variable=TRUCK_MODEL_MINI,
    )
    MiniEntry2.grid(row=1, column=1)

    MiniLabel3 = ctk.CTkLabel(MiniFrame1, text="Driver Name:")
    MiniLabel3.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    MiniEntry3 = ctk.CTkEntry(
        MiniFrame1,
        width=250,
        font=("Arial", 15, "bold"),
        height=35,
        corner_radius=7,
        textvariable=DRIVER_NAME_MINI,
    )
    MiniEntry3.grid(row=2, column=1)

    MiniLabel4 = ctk.CTkLabel(MiniFrame1, text="Empty Weight:")
    MiniLabel4.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    MiniEntry4 = ctk.CTkEntry(
        MiniFrame1,
        width=250,
        font=("Arial", 15, "bold"),
        height=35,
        corner_radius=7,
        textvariable=ValueTransponder,
    )
    MiniEntry4.grid(row=3, column=1)

    MiniSaveBut = ctk.CTkButton(MiniFrameBot, text="Save", command=MiniSubmit)
    MiniSaveBut.grid(row=0, column=0, padx=20, pady=10)
    MiniClearBut = ctk.CTkButton(
        MiniFrameBot, text="Clear", fg_color=("blue", "red"), command=MiniClearFunc
    )
    MiniClearBut.grid(row=0, column=1, padx=10, pady=10)

    MinirootExit = ctk.CTkButton(
        Miniroot,
        image=AdminExitImg,
        text="",
        hover_color=(CTKLIGHT, CTKDARK),
        width=20,
        fg_color=(CTKLIGHT, CTKDARK),
        command=close_new_window2,
    )
    MinirootExit.place(x=335, y=0)


# =============================== MainFrames of Weight Calculation are 3 (Top Middle and Bottom) ============================

MainFrameTop = ctk.CTkFrame(tab1)
MainFrameTop.grid(row=0, column=0, sticky=W, pady=10, padx=10)
MainFrameMid = ctk.CTkFrame(tab1)
MainFrameMid.grid(row=1, column=0, sticky=W, ipady=5)
MainFrameBot = ctk.CTkFrame(tab1, border_width=0)
MainFrameBot.grid(row=2, column=0, sticky=W, pady=10)
# ====================== Tab 2 Frames  ==========================
InMainFrameTab2 = ctk.CTkFrame(tab2)
InMainFrameTab2.grid(row=0, column=0, sticky=W, pady=5, padx=10)
InMainFrameTab2Mid = ctk.CTkFrame(tab2, fg_color=MODERNBACKBLUE)
InMainFrameTab2Mid.grid(row=1, column=0, sticky=W, pady=5, padx=10)
InMainFrameTab2Bot = ctk.CTkFrame(tab2)
InMainFrameTab2Bot.grid(row=2, column=0, sticky=W, pady=5, padx=10)


# ====================== Inner Frames of Label & Entries ==========================
InMainFrameTop = ctk.CTkFrame(MainFrameTop)
InMainFrameTop.grid(row=0, column=0, pady=5)
InMainFrameMidLeft = ctk.CTkFrame(MainFrameMid, border_width=2, corner_radius=10)
InMainFrameMidLeft.grid(row=0, column=0, padx=10, sticky=W)
InMainFrameMidRIGHT = ctk.CTkFrame(MainFrameMid, corner_radius=10)
InMainFrameMidRIGHT.grid(row=0, column=1, padx=10, sticky=W)
InMainFrameMid = ctk.CTkFrame(MainFrameMid)
InMainFrameMid.grid(row=0, column=2)
InMainFrameBot = ctk.CTkFrame(MainFrameBot)
InMainFrameBot.grid(row=0, column=0)
# ===================== Date, Time, Developer Labels =========================================

clocklbl = ctk.CTkLabel(tab1)
clocklbl.place(x=800, y=20)
datelbl = ctk.CTkLabel(tab1)
datelbl.place(x=1000, y=20)
developlbl = ctk.CTkLabel(
    tab1,
    justify="left",
    text="  Created By: Space4 software engineering team. \n  Contacts:____________________\n  Mail: hcrgroup.info@gmail.com \n  Phone & WhatsApp: 0795552579  ",
    text_color=BGBLACK,
    fg_color="Silver",
)
developlbl.place(x=100, y=5)
CurrentWeightLabelName = ctk.CTkLabel(
    tab1, text="Current Weight: ", font=("Arial", 20, "bold"), height=60
)
CurrentWeightLabelName.place(x=395, y=5)
CurFrame1 = ctk.CTkFrame(tab1, border_color="green", border_width=2, height=65)
CurFrame1.place(x=550, y=4)
CurrentWeight = ctk.CTkLabel(
    CurFrame1,
    textvariable=ValueTransponder,
    justify="left",
    font=("Consolas", 25, "bold"),
    text="---------/Kg",
)
CurrentWeight.place(x=5, y=15)

# ======================= Buttons Frame & Developer Info ===========================

Btn_Data = ctk.CTkButton(
    InMainFrameTop,
    text="Truck not\nDetected",
    font=("Arial", 12, "bold"),
    width=80,
    height=40,
    command=MiniRootFunc,
    state=DISABLED,
)
Btn_Data.grid(row=0, column=0, sticky=W, padx=1)
Btn_Exit = Button(
    root,
    image=ExitImg,
    fg="black",
    activebackground=TKDARK,
    compound=LEFT,
    bd=0,
    bg="#4B4B4B",
    command=Quit_1,
    takefocus=False,
)
Btn_Exit.place(x=1190, y=10)
"""
Btn_RestorDown = Button(root,image=RestordownImg,fg="black",activebackground="#4B4B4B",compound=LEFT,bd=0,bg="#4B4B4B",takefocus=False)
Btn_RestorDown.place(x=1150, y=10)
Btn_Minimize = Button(root,image=MinimizeImg,fg="black",activebackground="#4B4B4B",compound=LEFT,bd=0,bg="#4B4B4B",takefocus=False)
Btn_Minimize.place(x=1110, y=10)
"""
Space4LogoTitle = Label(root, bg="#4B4B4B", image=Space4TitleLogo)
Space4LogoTitle.place(x=700, y=1)
Space4Title = Label(
    root, bg="#4B4B4B", text="Space4 Software", font=("Gilroy Light", 5), fg="white"
)
Space4Title.place(x=697, y=52)
# ==================================================


# ======================= Label & Entries ===========================


LBL_4 = ctk.CTkLabel(InMainFrameMid, text="Full Weight / Kg:", font=FontStyle_Var)
LBL_4.grid(row=0, column=0, sticky=W, padx=10, pady=5)
LBL_5 = ctk.CTkLabel(InMainFrameMid, text="Price Charge/ Af:", font=FontStyle_Var)
LBL_5.grid(row=1, column=0, sticky=W, padx=10, pady=5)
LBL_6 = ctk.CTkLabel(InMainFrameMid, text="Goods Type:", font=FontStyle_Var)
LBL_6.grid(row=2, column=0, sticky=W, padx=10, pady=5)

LBL_8 = ctk.CTkLabel(InMainFrameMid, text="Serial No:", font=FontStyle_Var)
LBL_8.grid(row=3, column=0, sticky=W, padx=10, pady=5)

LBL_9 = ctk.CTkLabel(InMainFrameMid, text="Origin:", font=FontStyle_Var)
LBL_9.grid(row=0, column=2, sticky=W, padx=10, pady=5)
LBL_10 = ctk.CTkLabel(InMainFrameMid, text="Destination:", font=FontStyle_Var)
LBL_10.grid(row=1, column=2, sticky=W, padx=10, pady=5)
LBL_12 = ctk.CTkLabel(InMainFrameMid, text="Actions:", font=FontStyle_Var)
LBL_12.grid(row=3, column=2, sticky=W, padx=10, pady=5)


Ent4 = ctk.CTkEntry(
    InMainFrameMid,
    width=180,
    font=("Arial", 15, "bold"),
    height=35,
    takefocus=0,
    corner_radius=7,
    textvariable=ValueTransponder,
)
Ent4.grid(row=0, column=1, padx=10, sticky=W)
Ent5 = ctk.CTkEntry(
    InMainFrameMid,
    width=180,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=PRICE_CHARGE,
)
Ent5.grid(row=1, column=1, padx=10, sticky=W)
Ent5.focus()
Ent6 = ctk.CTkEntry(
    InMainFrameMid,
    width=180,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=GOODS_TYPE,
)
Ent6.grid(row=2, column=1, padx=10, sticky=W)
Ent8 = ctk.CTkEntry(
    InMainFrameMid,
    width=180,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    border_width=0,
    state=DISABLED,
)
Ent8.grid(row=3, column=1, padx=10, sticky=W)
Ent9 = ctk.CTkEntry(
    InMainFrameMid,
    width=180,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=ORIGIN,
)
Ent9.grid(row=0, column=3, padx=10, sticky=W)
Ent10 = ctk.CTkEntry(
    InMainFrameMid,
    width=180,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=DESTINATION,
)
Ent10.grid(row=1, column=3, padx=10, sticky=W)


InMidMainFrame = ctk.CTkFrame(
    InMainFrameMid, border_color=BGGRAY, border_width=1, corner_radius=7
)
InMidMainFrame.grid(row=3, column=3, padx=10, sticky=W)
Btn_Save = ctk.CTkButton(
    InMidMainFrame,
    text="Save",
    font=("Arial", 11, "bold"),
    width=30,
    fg_color=BGGREEN,
    text_color=BGYELLOW,
    command=submit,
)
Btn_Save.grid(row=0, column=0, padx=7, pady=5, sticky=W)
Btn_Clear = ctk.CTkButton(
    InMidMainFrame,
    text="Clear",
    font=("Arial", 11, "bold"),
    width=30,
    text_color=BGYELLOW,
    command=ClearEntry1,
)
Btn_Clear.grid(row=0, column=1, padx=7, pady=5, sticky=W)
Btn_Refresh = ctk.CTkButton(
    InMidMainFrame,
    text="Refresh",
    font=("Arial", 11, "bold"),
    width=30,
    text_color=BGLIGHTGREEN,
    command=Ref1,
)
Btn_Refresh.grid(row=0, column=2, padx=7, pady=5, sticky=W)

# Ent10.bind("<Return>", submit)

# ============== Find & select Truck Number to insert info =======================
"""
def RedLightImg1Func():
    SignLight.configure(image=RedLightImg1)
    SignLight.after(1000,GreenLightImg1Func)

def GreenLightImg1Func():
    SignLight.configure(image=GreenLightImg1)
    SignLight.after(1000,RedLightImg1Func)

"""


def ClearFinder():
    Rgd_TrucksFounderEntry.delete(0, END)
    # SignLight.after(1000, RedLightImg1Func)


SEARCH_TRNO = StringVar()


def FindTruckNoFunc():
    if SEARCH_TRNO.get() != "":
        MiniTree1.delete(*MiniTree1.get_children())
        conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
        cur = conn.execute(
            "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,DRIVER_NAME,REG_DATE FROM RegTruck WHERE TRUCK_NUMBER LIKE?",
            ("%" + str(SEARCH_TRNO.get()) + "%",),
        )
        fetch = cur.fetchall()
        for data1 in fetch:
            MiniTree1.insert("", "end", values=(data1))

    else:
        messagebox.showerror("Ooops", "Search Entry Can't be empty!!!")


Rgd_TrucksFounderLabel = ctk.CTkLabel(InMainFrameMidLeft, text="Find Truck Number:")
Rgd_TrucksFounderLabel.grid(row=0, column=0, padx=10, pady=10, sticky=W)

Rgd_TrucksFounderEntry = ctk.CTkEntry(
    InMainFrameMidLeft,
    height=30,
    textvariable=SEARCH_TRNO,
    corner_radius=10,
    font=("Arial", 27, "bold"),
    border_color="teal",
)
Rgd_TrucksFounderEntry.grid(row=1, column=0, padx=10, pady=10, sticky=W)

Rgd_TrucksFounderBtnFind = ctk.CTkButton(
    InMainFrameMidLeft, text="Find Truck", command=FindTruckNoFunc, border_color="teal"
)
Rgd_TrucksFounderBtnFind.grid(row=2, column=0, padx=10, pady=10)


SignLight = ctk.CTkLabel(InMainFrameMidLeft, text="")
SignLight.place(x=280, y=110)


# ================== The TreeView ============================== MiniTree1 =====================

MiniTruckTree1 = ctk.CTkFrame(InMainFrameMidRIGHT)
MiniTruckTree1.grid(row=0, column=1, sticky=W)
MiniScrolbarXtree1 = ctk.CTkScrollbar(InMainFrameMidRIGHT, orientation=HORIZONTAL)
MiniScrolbarYtree1 = ctk.CTkScrollbar(InMainFrameMidRIGHT, orientation=VERTICAL)
MiniTree1 = ttk.Treeview(
    MiniTruckTree1,
    columns=("TRUCK_NUMBER", "TRUCK_MODEL", "EMPTY_WEIGHT", "DRIVER_NAME", "REG_DATE"),
    selectmode="browse",
    height=5,
    yscrollcommand=MiniScrolbarYtree1.set,
    xscrollcommand=MiniScrolbarXtree1.set,
)
MiniScrolbarXtree1.configure(command=MiniTree1.xview)
MiniScrolbarXtree1.grid(row=1, column=1, ipadx=65, sticky=W)
# =====setting headings for the columns


MiniTree1.heading("TRUCK_NUMBER", text="Truck No", anchor=W)
MiniTree1.heading("TRUCK_MODEL", text="Truck Model", anchor=W)
MiniTree1.heading("EMPTY_WEIGHT", text="Empty Weight", anchor=W)
MiniTree1.heading("DRIVER_NAME", text="Driver Name", anchor=W)
MiniTree1.heading("REG_DATE", text="Date", anchor=W)

# setting width of the columns
MiniTree1.column("#0", stretch=NO, minwidth=0, width=0)
MiniTree1.column("#1", stretch=NO, minwidth=0, width=50)
MiniTree1.column("#2", stretch=NO, minwidth=0, width=80)
MiniTree1.column("#3", stretch=NO, minwidth=0, width=80)
MiniTree1.column("#4", stretch=NO, minwidth=0, width=80)
MiniTree1.column("#5", stretch=NO, minwidth=0, width=70)

MiniTree1.grid(sticky=SW)


MiniTree1.delete(*MiniTree1.get_children())
Miniconn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
Minicur1 = Miniconn1.execute(
    "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,DRIVER_NAME,REG_DATE FROM RegTruck"
)

fetch1 = Minicur1.fetchall()
for data1 in fetch1:
    MiniTree1.insert("", "end", values=(data1))
Minicur1.close()
Miniconn1.close()


# ================== The TreeView ============================== Tree1 =====================
MiniWinTree1 = ctk.CTkFrame(MainFrameBot, border_width=0)
MiniWinTree1.grid(row=0, column=0, padx=18, sticky=W)
ScrolbarXtree1 = ctk.CTkScrollbar(MainFrameBot, orientation=HORIZONTAL)
ScrolbarYtree1 = ctk.CTkScrollbar(MainFrameBot, orientation=VERTICAL)
Tree1 = ttk.Treeview(
    MiniWinTree1,
    columns=(
        "TRUCK_NUMBER",
        "TRUCK_MODEL",
        "EMPTY_WEIGHT",
        "FULL_WEIGHT",
        "PRICE_CHARGE",
        "GOODS_TYPE",
        "DRIVER_NAME",
        "SERIAL_NUMBER",
        "ORIGIN",
        "DESTINATION",
        "REG_DATE",
    ),
    selectmode="browse",
    height=13,
    yscrollcommand=ScrolbarYtree1.set,
    xscrollcommand=ScrolbarXtree1.set,
)
ScrolbarYtree1.configure(command=Tree1.yview)
ScrolbarYtree1.grid(row=0, column=1, ipady=90, sticky=W)
ScrolbarXtree1.configure(command=Tree1.xview)
ScrolbarXtree1.grid(row=1, column=0, ipadx=477, sticky=W)
# =====setting headings for the columns

Tree1.heading("TRUCK_NUMBER", text="Truck No", anchor=W)
Tree1.heading("TRUCK_MODEL", text="Truck Model", anchor=W)
Tree1.heading("EMPTY_WEIGHT", text="Empty Weight", anchor=W)
Tree1.heading("FULL_WEIGHT", text="Full Weight", anchor=W)
Tree1.heading("PRICE_CHARGE", text="Price Charge", anchor=W)
Tree1.heading("GOODS_TYPE", text="Goods Type", anchor=W)
Tree1.heading("DRIVER_NAME", text="Driver Name", anchor=W)
Tree1.heading("SERIAL_NUMBER", text="Serial No", anchor=W)
Tree1.heading("ORIGIN", text="Origin", anchor=W)
Tree1.heading("DESTINATION", text="Destination", anchor=W)
Tree1.heading("REG_DATE", text="Date", anchor=W)

# setting width of the columns
Tree1.column("#0", stretch=NO, minwidth=0, width=0)
Tree1.column("#1", stretch=NO, minwidth=0, width=60)
Tree1.column("#2", stretch=NO, minwidth=0, width=110)
Tree1.column("#3", stretch=NO, minwidth=0, width=110)
Tree1.column("#4", stretch=NO, minwidth=0, width=110)
Tree1.column("#5", stretch=NO, minwidth=0, width=110)
Tree1.column("#6", stretch=NO, minwidth=0, width=100)
Tree1.column("#7", stretch=NO, minwidth=0, width=120)
Tree1.column("#8", stretch=NO, minwidth=0, width=80)
Tree1.column("#9", stretch=NO, minwidth=0, width=120)
Tree1.column("#10", stretch=NO, minwidth=0, width=110)
Tree1.column("#11", stretch=NO, minwidth=0, width=100)

Tree1.grid()

Tree1.delete(*Tree1.get_children())
conn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
cur1 = conn1.execute(
    "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
    DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable"
)

fetch1 = cur1.fetchall()
for data1 in fetch1:
    Tree1.insert("", "end", values=(data1))
cur1.close()
conn1.close()


"""
ID
TRUCK_NUMBER
TRUCK_MODEL
EMPTY_WEIGHT
FULL_WEIGHT
PRICE_CHARGE
GOODS_TYPE
DRIVER_NAME
SERIAL_NUMBER
ORIGIN
DESTINATION
REG_DATE
"""


def timshow1():
    from time import strftime

    string = strftime("%H:%M : %S %p")
    stringdate = strftime("%Y-%m-%d - %a")
    clocklbl.configure(text=string, font=("Arial", 20))
    datelbl.configure(text=stringdate, font=("Humnst777 Blk BT", 20))

    clocklbl.after(1000, timshow1)


timshow1()


# ============================================= tab 2 ==================================================
# ============================================= tab 2 ==================================================
# ============================================= tab 2 ==================================================
# ============================================= tab 2 ==================================================
# ============================================= tab 2 ==================================================
# ============================================= tab 2 ==================================================


TRUCK_NUMBER_1 = StringVar()
TRUCK_MODEL_1 = StringVar()
EMPTY_WEIGHT_1 = StringVar()
FULL_WEIGHT_1 = StringVar()
PRICE_CHARGE_1 = StringVar()
GOODS_TYPE_1 = StringVar()
DRIVER_NAME_1 = StringVar()
BILL_NUMBER_1 = StringVar()
ORIGIN_1 = StringVar()
DESTINATION_1 = StringVar()
MANUALDATE_1 = StringVar()
SEARCH = StringVar()
SEARCH_2 = StringVar()
"""

def TruckNoFunc():
    if EditCheckBox_1.get() > 0:
        Tab2Ent1.configure(state=NORMAL)
    else:
        Tab2Ent1.configure(state=DISABLED)

def TruckModFunc():
    if EditCheckBox_2.get() > 0:
        Tab2Ent2.configure(state=NORMAL)
    else:
        Tab2Ent2.configure(state=DISABLED)

def EmptyWeightFunc():
    if EditCheckBox_3.get() > 0:
        Tab2Ent3.configure(state=NORMAL)
    else:
        Tab2Ent3.configure(state=DISABLED)

def FullWeightFunc():
    if EditCheckBox_4.get() > 0:
        Tab2Ent4.configure(state=NORMAL)
    else:
        Tab2Ent4.configure(state=DISABLED)

def GoodsTypeFunc():
    if EditCheckBox_5.get() > 0:
        Tab2Ent6.configure(state=NORMAL)
    else:
        Tab2Ent6.configure(state=DISABLED)

def CustomerNameFunc():
    if EditCheckBox_6.get() > 0:
        Tab2Ent7.configure(state=NORMAL)
    else:
        Tab2Ent7.configure(state=DISABLED)

def BillNoFunc():
    if EditCheckBox_7.get() > 0:
        Tab2Ent8.configure(state=NORMAL)
    else:
        Tab2Ent8.configure(state=DISABLED)

def OriginFunc():
    if EditCheckBox_8.get() > 0:
        Tab2Ent9.configure(state=NORMAL)
    else:
        Tab2Ent9.configure(state=DISABLED)

def DestinationFunc():
    if EditCheckBox_9.get() > 0:
        Tab2Ent10.configure(state=NORMAL)
    else:
        Tab2Ent10.configure(state=DISABLED)

def DateFunc():
    if EditCheckBox_10.get() > 0:
        Tab2Ent11.configure(state=NORMAL)
    else:
        Tab2Ent11.configure(state=DISABLED)

"""


def Ref2():
    Tree2.delete(*Tree2.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute(
        """SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
    DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable """
    )

    fetch = cur.fetchall()
    for data in fetch:
        Tree2.insert("", "end", values=(data))
    cur.close()
    conn.close()


def DeleteRecord2():
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.cursor()
    messageDelete = messagebox.askyesno(
        "Confirmation", "Are you sure you want to permanently delete this record?"
    )
    if messageDelete > 0:
        selected_item = Tree2.selection()[0]
        for selected_item in Tree2.selection():
            cur.execute(
                "DELETE FROM ScaleTable WHERE SERIAL_NUMBER=?",
                (Tree2.set(selected_item, "SERIAL_NUMBER"),),
            )
        conn.commit()
        Tree2.delete(selected_item)
    conn.close()


def EditUPFunc():
    passget = StringVar()
    logwin = Toplevel(root)
    logwin.title("Space4 Software Login")
    logwin.geometry("330x173+500+80")
    logwin.iconbitmap("hcrIcon.ico")
    logwin.resizable(0, 0)
    logwin.overrideredirect(True)

    # ------this is for Blur other windows--------
    def close_new_window3():
        logwin.destroy()
        blur_overlay3.destroy()

    main_image3 = ImageTk.PhotoImage(ImageGrab.grab().filter(ImageFilter.BLUR))
    blur_overlay3 = Label(root, image=main_image3)
    blur_overlay3.place(x=0, y=0, relwidth=1, relheight=1)
    blur_overlay3.image = main_image3

    def log_in():
        config_0.read("config.ini")
        APSS = config_0.get("section_ps", "ADMPS")
        password1 = APSS
        if passwordEntry.get() == "":
            messagebox.showwarning(
                "Space4 Software password(Error)", "Insert your Password first!"
            )
            passwordEntry.focus()
        elif len(passwordEntry.get()) < 4:
            messagebox.showwarning(
                "Space4 Software password(Error)", "Use more than 4 characters!"
            )
            passwordEntry.focus()
        elif passwordEntry.get() != password1:
            messagebox.showerror("Space4 Software", "Password Wrong!!!")
            passwordEntry.focus()

        elif passget.get() == password1:
            Tab2Btn_Save.configure(state=NORMAL, fg_color=BGGREEN, text_color=BGYELLOW)
            passwordEntry.delete(0, END)
            logwin.bind("<FocusOut>")
            messagebox.showinfo("Space4 Software", "Now you can edit any record!")

            logwin.destroy()
            close_new_window3()

            def EditingFunction():
                conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
                cur1 = conn.cursor()
                cur2 = conn.cursor()
                cur3 = conn.cursor()
                cur4 = conn.cursor()
                cur5 = conn.cursor()
                cur6 = conn.cursor()
                cur7 = conn.cursor()
                cur8 = conn.cursor()
                cur9 = conn.cursor()
                cur10 = conn.cursor()
                cur11 = conn.cursor()
                cur12 = conn.cursor()

                selected_item = Tree2.selection()[0]
                for selected_item in Tree2.selection():
                    cur1.execute(
                        "SELECT TRUCK_NUMBER FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur2.execute(
                        "SELECT TRUCK_MODEL FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur3.execute(
                        "SELECT EMPTY_WEIGHT FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur4.execute(
                        "SELECT FULL_WEIGHT FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur5.execute(
                        "SELECT PRICE_CHARGE FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur6.execute(
                        "SELECT GOODS_TYPE FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur7.execute(
                        "SELECT DRIVER_NAME FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur8.execute(
                        "SELECT SERIAL_NUMBER FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur9.execute(
                        "SELECT ORIGIN FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur10.execute(
                        "SELECT DESTINATION FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    cur11.execute(
                        "SELECT REG_DATE FROM ScaleTable WHERE SERIAL_NUMBER=?",
                        (Tree2.set(selected_item, "#8"),),
                    )
                    fetch1 = cur1.fetchall()
                    fetch2 = cur2.fetchall()
                    fetch3 = cur3.fetchall()
                    fetch4 = cur4.fetchall()
                    fetch5 = cur5.fetchall()
                    fetch6 = cur6.fetchall()
                    fetch7 = cur7.fetchall()
                    fetch8 = cur8.fetchall()
                    fetch9 = cur9.fetchall()
                    fetch10 = cur10.fetchall()
                    fetch11 = cur11.fetchall()

                    conn.commit()
                    if Tab2Ent1.get() == "":
                        Tab2Ent1.insert(0, fetch1)
                    else:
                        messagebox.showerror("Oooops", "There is a file on EDIT!")

                    if Tab2Ent2.get() != "":
                        Tab2Ent2.set(fetch2)

                    if Tab2Ent3.get() == "":
                        Tab2Ent3.insert(0, fetch3)

                    if Tab2Ent4.get() == "":
                        Tab2Ent4.insert(0, fetch4)

                    if Tab2Ent5.get() == "":
                        Tab2Ent5.insert(0, fetch5)

                    if Tab2Ent6.get() == "":
                        Tab2Ent6.insert(0, fetch6)

                    if Tab2Ent7.get() == "":
                        Tab2Ent7.insert(0, fetch7)

                    if Tab2Ent8.get() == "":
                        Tab2Ent8.insert(0, fetch8)

                    if Tab2Ent9.get() == "":
                        Tab2Ent9.insert(0, fetch9)

                    if Tab2Ent10.get() == "":
                        Tab2Ent10.insert(0, fetch10)

                    if Tab2Ent11.get() == "":
                        Tab2Ent11.insert(0, fetch11)

                cur1.close()
                cur2.close()
                cur3.close()
                cur4.close()
                cur5.close()
                cur6.close()
                cur7.close()
                cur8.close()
                cur9.close()
                cur10.close()
                cur11.close()
                conn.close()
                Tab2Ent1.focus()

            Tab2Btn_Update.configure(command=EditingFunction)

    def hidemypass():
        if passwordEntry.get() == "":
            SPB.configure(image=DSPSign)
        else:
            passwordEntry.configure(show="*")
            SPB.configure(image=DSPSign, command=showmypass)

    def showmypass():
        if passwordEntry.get() == "":
            SPB.configure(image=DSPSign)
        else:
            passwordEntry.configure(show="")
            SPB.configure(image=SPSign, command=hidemypass)

    def LoginFocusIn(event):
        logButton.config(image=Login2)

    def LoginFocusOut(event):
        logButton.config(image=Login1)

    def highlighting0(event):
        forgetPassSet.config(fg="teal")

    def highlighting1(event):
        forgetPassSet.config(fg="blue")

    LogFTop = Frame(logwin)
    LogFTop.grid(row=0, column=0, pady=20)
    LogFM = Frame(logwin)
    LogFM.grid(row=1, column=0, sticky=W)
    LogFBot = Frame(logwin)
    LogFBot.grid(row=2, column=0)
    showFrm = Frame(LogFM)
    showFrm.grid(row=0, column=2)

    HeaderLbl = Label(
        LogFTop,
        text="     Insert your Password to access edit mode     ",
        bg="#2f5c7c",
        fg="light yellow",
        font=("Arial", 10, "bold"),
    )
    HeaderLbl.grid(row=0, column=0, pady=5)
    passwordlabel = Label(LogFM, text="Password:", font=("Arial", 10, "bold"))
    passwordlabel.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    passwordEntry = ctk.CTkEntry(
        LogFM,
        show="*",
        width=200,
        font=("Cascadia Code", 12),
        text_color="black",
        corner_radius=10,
        border_width=2,
        fg_color=("white", "white"),
        textvariable=passget,
    )
    passwordEntry.grid(row=0, column=1)
    passwordEntry.focus()

    SPB = Button(showFrm, image=DSPSign, bd=0, command=showmypass, takefocus=False)
    SPB.grid(row=0, column=0, padx=10)

    # logButton = ctk.CTkButton(LogFBot,image=UnLocked,text="Login",compound=RIGHT,fg_color=("green","white"),width=100,font=FontStyle_Var, command=log_in)
    logButton = Button(
        LogFBot,
        image=Login1,
        compound=RIGHT,
        bd=0,
        width=100,
        font=FontStyle_Var,
        command=log_in,
    )
    logButton.grid(
        row=0, column=0, pady=5
    )  # the comopound can place the image to left,right,center,up and down sides...........................

    CreatorLabel = ctk.CTkLabel(
        LogFBot,
        text="Secured By: HCR-BLUE",
        font=("Arial", 8),
        text_color=("blue", "black"),
    )
    CreatorLabel.grid(
        row=1,
        column=0,
        pady=2,
    )

    MinirootExit3 = Button(
        logwin,
        image=ExitImg,
        bd=0,
        activebackground=BGLIGHTGRAY,
        width=20,
        command=close_new_window3,
    )
    MinirootExit3.place(x=300, y=0)

    # >>>>>>> Refreshing >>>>>>>>>>>>>>>>>
    logButton.bind("<Enter>", LoginFocusIn)
    logButton.bind("<Leave>", LoginFocusOut)
    logButton.bind("<FocusIn>", LoginFocusIn)
    logButton.bind("<FocusOut>", LoginFocusOut)


def UpdateFunction():
    if (
        Tab2Ent1.get() == ""
        or Tab2Ent2.get() == ""
        or Tab2Ent3.get() == ""
        or Tab2Ent4.get() == ""
        or Tab2Ent5.get() == ""
        or Tab2Ent6.get() == ""
        or Tab2Ent7.get() == ""
        or Tab2Ent9.get() == ""
        or Tab2Ent10.get() == ""
        or Tab2Ent11.get() == ""
    ):
        messagebox.showerror("Warning!!!", "Please fill the Entries First!")
    else:
        if (
            Tab2Ent1.get() != ""
            or Tab2Ent2.get() != ""
            or Tab2Ent3.get() != ""
            or Tab2Ent4.get() != ""
            or Tab2Ent5.get() == ""
            or Tab2Ent6.get() != ""
            or Tab2Ent7.get() != ""
            or Tab2Ent9.get() != ""
            or Tab2Ent10.get() != ""
            or Tab2Ent11.get() != ""
        ):
            dt1 = TRUCK_NUMBER_1.get()
            dt2 = TRUCK_MODEL_1.get()
            dt3 = EMPTY_WEIGHT_1.get()
            dt4 = FULL_WEIGHT_1.get()
            dt5 = PRICE_CHARGE_1.get()
            dt6 = GOODS_TYPE_1.get()
            dt7 = DRIVER_NAME_1.get()
            dt9 = ORIGIN_1.get()
            dt10 = DESTINATION_1.get()
            dt11 = MANUALDATE_1.get()

            for selected_item in Tree2.selection():
                conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
                cur = conn.cursor()
                cur.execute(
                    "UPDATE ScaleTable SET TRUCK_NUMBER=?,TRUCK_MODEL=?,EMPTY_WEIGHT=?,FULL_WEIGHT=?,PRICE_CHARGE=?,GOODS_TYPE=?,DRIVER_NAME=?,ORIGIN=?,DESTINATION=?,REG_DATE=? WHERE SERIAL_NUMBER=?",
                    (
                        dt1,
                        dt2,
                        dt3,
                        dt4,
                        dt5,
                        dt6,
                        dt7,
                        dt9,
                        dt10,
                        dt11,
                        Tree2.set(selected_item, "#8"),
                    ),
                )
                conn.commit()
                conn.close()

                Tab2Ent1.delete(0, END)
                Tab2Ent2.set("Choose Truck Model")
                Tab2Ent3.delete(0, END)
                Tab2Ent4.delete(0, END)
                Tab2Ent5.delete(0, END)
                Tab2Ent6.delete(0, END)
                Tab2Ent7.delete(0, END)
                Tab2Ent9.delete(0, END)
                Tab2Ent10.delete(0, END)
                Tab2Ent11.delete(0, END)
                Tab2Ent1.focus()
                Ref2()

        else:
            messagebox.showinfo("ooops", "Can't Update The records!!!")


def ClearEntry2():
    Tab2Ent1.delete(0, END)
    Tab2Ent2.set("Choose Truck Model")
    Tab2Ent3.delete(0, END)
    Tab2Ent4.delete(0, END)
    Tab2Ent5.delete(0, END)
    Tab2Ent6.delete(0, END)
    Tab2Ent7.delete(0, END)
    Tab2Ent9.delete(0, END)
    Tab2Ent10.delete(0, END)
    Tab2Ent11.delete(0, END)
    Tab2Ent1.focus()


def ExportSelectedFile():
    conn2 = sqlite3.connect("DataBaseDir/ExtraScale.db")
    selected_item2 = Tree2.selection()[0]
    for selected_item2 in Tree2.selection():
        cur2 = conn2.execute(
            "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
            DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable  WHERE SERIAL_NUMBER=?",
            (Tree2.set(selected_item2, "SERIAL_NUMBER"),),
        )

        MyTable = prettytable.from_db_cursor(cur2)
        cur2 = conn2.cursor()
        rows = cur2.fetchall()

        for row in rows:
            MyTable.add_row(row)
        cur2.close()
        conn2.close()

        # =========Save Part ===============

        filesave = filedialog.asksaveasfile(
            mode="w",
            title="Export single record",
            filetypes=SaveExtensions,
            defaultextension=SaveExtensions,
        )
        if filesave is None:
            return
        file2Save = str(MyTable)
        filesave.write(file2Save)
        filesave.close()
        messagebox.showinfo(
            "HCR-BLUE", "Please choose font\n< Consolas >\n and then print out!"
        )


"""

def SearchRec():

    if SEARCH_2.get() !="":
        Tree2.delete(*Tree2.get_children())
        conn = sqlite3.connect('DataBaseDir/ExtraScale.db')
        cur  = conn.execute("SELECT ID,TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
            DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE TRUCK_NUMBER LIKE?",('%'+ str(SEARCH.get())+'%',))
        fetch = cur.fetchall()
        for data in fetch:
            Tree2.insert('','end', values=(data))
    else:
        messagebox.showerror("oooops","Type something first!!!")
"""


def searchRadio():
    if SEARCH_2.get() == "TRUCK_N1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE TRUCK_NUMBER LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )
        pass
    elif SEARCH_2.get() == "TRUCK_1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE TRUCK_MODEL LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )
        pass
    elif SEARCH_2.get() == "EMPTY_W1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE EMPTY_WEIGHT LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )
        pass
    elif SEARCH_2.get() == "FULL_W1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE FULL_WEIGHT LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )

    elif SEARCH_2.get() == "PRICE_CH":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE PRICE_CHARGE LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )

        pass
    elif SEARCH_2.get() == "GOODS1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE GOODS_TYPE LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )
        pass
    elif SEARCH_2.get() == "CUSTOMER1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE DRIVER_NAME LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )
        pass
    elif SEARCH_2.get() == "BILL_N1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE SERIAL_NUMBER LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )
        pass
    elif SEARCH_2.get() == "O1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE ORIGIN LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )

        pass
    elif SEARCH_2.get() == "DESTIN1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE DESTINATION LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )

        pass
    elif SEARCH_2.get() == "MANUA1":
        if SEARCH.get() != "":
            Tree2.delete(*Tree2.get_children())
            conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
            cur = conn.execute(
                "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
                DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable WHERE REG_DATE LIKE?",
                ("%" + str(SEARCH.get()) + "%",),
            )
            fetch = cur.fetchall()
            for data in fetch:
                Tree2.insert("", "end", values=(data))
        else:
            messagebox.showerror(
                "oooops", "Type something first and then search on it!"
            )

    else:
        messagebox.showerror(
            "Ooooops", "You have to choose type of search\nSearch By Type"
        )


RadioBtn_1 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Truck No",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="TRUCK_N1",
)
RadioBtn_1.grid(row=0, column=0, padx=0, pady=5, sticky=W)

RadioBtn_2 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Truck Model",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="TRUCK_1",
)
RadioBtn_2.grid(row=1, column=0, padx=0, pady=5, sticky=W)

RadioBtn_3 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Empty Weight",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="EMPTY_W1",
)
RadioBtn_3.grid(row=0, column=1, padx=5, pady=5, sticky=W)

RadioBtn_4 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Full Weight",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="FULL_W1",
)
RadioBtn_4.grid(row=1, column=1, padx=5, pady=5, sticky=W)

RadioBtn_5 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Price Charge",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="PRICE_CH",
)
RadioBtn_5.grid(row=0, column=2, padx=5, pady=5, sticky=W)

RadioBtn_6 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Goods Type",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="GOODS1",
)
RadioBtn_6.grid(row=1, column=2, padx=5, pady=5, sticky=W)

RadioBtn_7 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Driver Name",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="CUSTOMER1",
)
RadioBtn_7.grid(row=0, column=3, padx=5, pady=5, sticky=W)

RadioBtn_8 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Serial No",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="BILL_N1",
)
RadioBtn_8.grid(row=1, column=3, padx=5, pady=5, sticky=W)

RadioBtn_9 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Origin",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="O1",
)
RadioBtn_9.grid(row=0, column=4, padx=5, pady=5, sticky=W)

RadioBtn_10 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Destination",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="DESTIN1",
)
RadioBtn_10.grid(row=1, column=4, padx=5, pady=5, sticky=W)

RadioBtn_11 = Radiobutton(
    master=InMainFrameTab2Mid,
    compound=LEFT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=MODERNBACKBLUE,
    text="Date ",
    activebackground=MODERNBACKBLUE,
    bg=MODERNBACKBLUE,
    fg=BGDARKSKY,
    font=("Arial", 10),
    variable=SEARCH_2,
    value="MANUA1",
)
RadioBtn_11.grid(row=0, column=4, padx=5, pady=5, sticky=W)


SearchLabel = ctk.CTkLabel(
    InMainFrameTab2Mid, text="Search:", compound=RIGHT, font=("Arial", 15, "bold")
)
SearchLabel.grid(row=0, column=5, padx=20)

SearchEntry = ctk.CTkEntry(InMainFrameTab2Mid, width=250, textvariable=SEARCH)
SearchEntry.grid(row=0, column=6, padx=10)
# ================= Search Button ==============
SearchBtn1 = ctk.CTkButton(
    InMainFrameTab2Mid,
    text="Search",
    fg_color="dark red",
    font=("Arial", 14, "bold"),
    command=searchRadio,
)
SearchBtn1.grid(row=0, column=7, padx=10)

"""
EditCheckBox_1 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Truck No",onvalue=1,state=DISABLED,offvalue=0,command=TruckNoFunc)
EditCheckBox_1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
EditCheckBox_2 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Truck Model",onvalue=1,state=DISABLED,offvalue=0,command=TruckModFunc)
EditCheckBox_2.grid(row=1,column=0,padx=10,pady=5,sticky=W)
EditCheckBox_3 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Empty Weight",onvalue=1,state=DISABLED,offvalue=0,command=EmptyWeightFunc)
EditCheckBox_3.grid(row=0,column=1,padx=10,pady=5,sticky=W)
EditCheckBox_4 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Full Weight",onvalue=1,state=DISABLED,offvalue=0,command=FullWeightFunc)
EditCheckBox_4.grid(row=1,column=1,padx=10,pady=5,sticky=W)
EditCheckBox_5 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Goods Type",onvalue=1,state=DISABLED,offvalue=0,command=GoodsTypeFunc)
EditCheckBox_5.grid(row=0,column=2,padx=10,pady=5,sticky=W)
EditCheckBox_6 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Driver Name",onvalue=1,state=DISABLED,offvalue=0,command=CustomerNameFunc)
EditCheckBox_6.grid(row=1,column=2,padx=10,pady=5,sticky=W)
EditCheckBox_7 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Serial No",onvalue=1,state=DISABLED,offvalue=0,command=BillNoFunc)
EditCheckBox_7.grid(row=0,column=3,padx=10,pady=5,sticky=W)
EditCheckBox_8 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Origin",onvalue=1,state=DISABLED,offvalue=0,command=OriginFunc)
EditCheckBox_8.grid(row=1,column=3,padx=10,pady=5,sticky=W)
EditCheckBox_9 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Destination",onvalue=1,state=DISABLED,offvalue=0,command=DestinationFunc)
EditCheckBox_9.grid(row=0,column=4,padx=10,pady=5,sticky=W)
EditCheckBox_10 = ctk.CTkCheckBox(InMainFrameTab2Mid,text="Date",onvalue=1,state=DISABLED,offvalue=0,command=DateFunc)
EditCheckBox_10.grid(row=1,column=4,padx=10,pady=5,sticky=W)
"""

Tab2_LBL_1 = ctk.CTkLabel(InMainFrameTab2, text="Truck No:", font=("Arial", 13, "bold"))
Tab2_LBL_1.grid(row=0, column=0, sticky=W, padx=10, pady=5)
Tab2_LBL_2 = ctk.CTkLabel(
    InMainFrameTab2, text="Truck Model:", font=("Arial", 13, "bold")
)
Tab2_LBL_2.grid(row=1, column=0, sticky=W, padx=10, pady=5)
Tab2_LBL_3 = ctk.CTkLabel(
    InMainFrameTab2, text="Empty Weight / Kg:", font=("Arial", 13, "bold")
)
Tab2_LBL_3.grid(row=2, column=0, sticky=W, padx=10, pady=5)
Tab2_LBL_4 = ctk.CTkLabel(
    InMainFrameTab2, text="Full Weight / Kg:", font=("Arial", 13, "bold")
)
Tab2_LBL_4.grid(row=3, column=0, sticky=W, padx=10, pady=5)

Tab2_LBL_5 = ctk.CTkLabel(
    InMainFrameTab2, text="Price Charge/ Kg:", font=("Arial", 13, "bold")
)
Tab2_LBL_5.grid(row=0, column=2, sticky=W, padx=10, pady=5)
Tab2_LBL_6 = ctk.CTkLabel(
    InMainFrameTab2, text="Goods Type:", font=("Arial", 13, "bold")
)
Tab2_LBL_6.grid(row=1, column=2, sticky=W, padx=10, pady=5)
Tab2_LBL_7 = ctk.CTkLabel(
    InMainFrameTab2, text="Driver Name:", font=("Arial", 13, "bold")
)
Tab2_LBL_7.grid(row=2, column=2, sticky=W, padx=10, pady=5)
Tab2_LBL_8 = ctk.CTkLabel(
    InMainFrameTab2, text="Serial No:", font=("Arial", 13, "bold")
)
Tab2_LBL_8.grid(row=3, column=2, sticky=W, padx=10, pady=5)

Tab2_LBL_9 = ctk.CTkLabel(InMainFrameTab2, text="Origin:", font=("Arial", 13, "bold"))
Tab2_LBL_9.grid(row=0, column=4, sticky=W, padx=10, pady=5)
Tab2_LBL_10 = ctk.CTkLabel(
    InMainFrameTab2, text="Destination:", font=("Arial", 13, "bold")
)
Tab2_LBL_10.grid(row=1, column=4, sticky=W, padx=10, pady=5)
Tab2_LBL_11 = ctk.CTkLabel(InMainFrameTab2, text="Date", font=("Arial", 13, "bold"))
Tab2_LBL_11.grid(row=2, column=4, sticky=W, padx=10, pady=5)
Tab2_LBL_12 = ctk.CTkLabel(InMainFrameTab2, text="Actions:", font=("Arial", 13, "bold"))
Tab2_LBL_12.grid(row=3, column=4, sticky=W, padx=10, pady=5)


Tab2Ent1 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=TRUCK_NUMBER_1,
)
Tab2Ent1.grid(row=0, column=1, padx=10, sticky=W)
Tab2Ent1.focus()

TruckModel_1 = ["Actrus", "Hino", "Mazda", "Kamaz"]
TRUCK_MODEL_1.set("Choose Truck Model")
Tab2Ent2 = ctk.CTkComboBox(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    values=TruckModel_1,
    corner_radius=10,
    variable=TRUCK_MODEL_1,
)
Tab2Ent2.grid(row=1, column=1, padx=10, sticky=W)
Tab2Ent3 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=EMPTY_WEIGHT_1,
)
Tab2Ent3.grid(row=2, column=1, padx=10, sticky=W)
Tab2Ent4 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=FULL_WEIGHT_1,
)
Tab2Ent4.grid(row=3, column=1, padx=10, sticky=W)

Tab2Ent5 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=PRICE_CHARGE_1,
)
Tab2Ent5.grid(row=0, column=3, padx=10, sticky=W)
Tab2Ent6 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=GOODS_TYPE_1,
)
Tab2Ent6.grid(row=1, column=3, padx=10, sticky=W)
Tab2Ent7 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=DRIVER_NAME_1,
)
Tab2Ent7.grid(row=2, column=3, padx=10, sticky=W)
Tab2Ent8 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    border_width=0,
    corner_radius=7,
    state=DISABLED,
)
Tab2Ent8.grid(row=3, column=3, padx=10, sticky=W)

Tab2Ent9 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=ORIGIN_1,
)
Tab2Ent9.grid(row=0, column=5, padx=10, sticky=W)
Tab2Ent10 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=DESTINATION_1,
)
Tab2Ent10.grid(row=1, column=5, padx=10, sticky=W)
Tab2Ent11 = ctk.CTkEntry(
    InMainFrameTab2,
    width=250,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=MANUALDATE_1,
)
Tab2Ent11.grid(row=2, column=5, padx=10, sticky=W)
Tab2InMidMainFrame = ctk.CTkFrame(
    InMainFrameTab2, border_color=BGGRAY, border_width=1, corner_radius=7
)
Tab2InMidMainFrame.grid(row=3, column=5, padx=10, sticky=W)
Tab2Btn_Save = ctk.CTkButton(
    Tab2InMidMainFrame,
    text=" Save ",
    font=("Arial", 15, "bold"),
    width=30,
    fg_color=BGGRAY,
    text_color=BGYELLOW,
    command=UpdateFunction,
    state=DISABLED,
)
Tab2Btn_Save.grid(row=0, column=0, padx=5, pady=5, sticky=W)
Tab2Btn_Clear = ctk.CTkButton(
    Tab2InMidMainFrame,
    text="Clear",
    font=("Arial", 13, "bold"),
    width=30,
    text_color=BGYELLOW,
    command=ClearEntry2,
)
Tab2Btn_Clear.grid(row=0, column=1, padx=5, pady=5, sticky=W)
Tab2Btn_Update = ctk.CTkButton(
    Tab2InMidMainFrame,
    text="Edit",
    font=("Arial", 13, "bold"),
    width=30,
    command=EditUPFunc,
)
Tab2Btn_Update.grid(row=0, column=2, padx=5, pady=5, sticky=W)
Tab2Btn_Refresh = ctk.CTkButton(
    Tab2InMidMainFrame,
    text="Refresh",
    font=("Arial", 13, "bold"),
    width=30,
    text_color=BGLIGHTGREEN,
    command=Ref2,
)
Tab2Btn_Refresh.grid(row=0, column=3, padx=5, pady=5, sticky=W)


MiniWinTree2 = ctk.CTkFrame(InMainFrameTab2Bot)
MiniWinTree2.grid(row=0, column=0, padx=5, sticky=W)
ScrolbarXtree2 = ctk.CTkScrollbar(InMainFrameTab2Bot, orientation=HORIZONTAL)
ScrolbarYtree2 = ctk.CTkScrollbar(InMainFrameTab2Bot, orientation=VERTICAL)
Tree2 = ttk.Treeview(
    MiniWinTree2,
    columns=(
        "TRUCK_NUMBER",
        "TRUCK_MODEL",
        "EMPTY_WEIGHT",
        "FULL_WEIGHT",
        "PRICE_CHARGE",
        "GOODS_TYPE",
        "DRIVER_NAME",
        "SERIAL_NUMBER",
        "ORIGIN",
        "DESTINATION",
        "REG_DATE",
    ),
    selectmode="extended",
    height=13,
    yscrollcommand=ScrolbarYtree2.set,
    xscrollcommand=ScrolbarXtree2.set,
)
ScrolbarYtree2.configure(command=Tree2.yview)
ScrolbarYtree2.grid(row=0, column=1, ipady=90, sticky=W)
ScrolbarXtree2.configure(command=Tree2.xview)
ScrolbarXtree2.grid(row=1, column=0, ipadx=470, sticky=W)
# =====setting headings for the columns


Tree2.heading("TRUCK_NUMBER", text="Truck No", anchor=W)
Tree2.heading("TRUCK_MODEL", text="Truck Model", anchor=W)
Tree2.heading("EMPTY_WEIGHT", text="Empty Weight", anchor=W)
Tree2.heading("FULL_WEIGHT", text="Full Weight", anchor=W)
Tree2.heading("PRICE_CHARGE", text="Price Charge", anchor=W)
Tree2.heading("GOODS_TYPE", text="Goods Type", anchor=W)
Tree2.heading("DRIVER_NAME", text="Driver Name", anchor=W)
Tree2.heading("SERIAL_NUMBER", text="Serial No", anchor=W)
Tree2.heading("ORIGIN", text="Origin", anchor=W)
Tree2.heading("DESTINATION", text="Destination", anchor=W)
Tree2.heading("REG_DATE", text="Date", anchor=W)

# setting width of the columns
Tree2.column("#0", stretch=NO, minwidth=0, width=0)
Tree2.column("#1", stretch=NO, minwidth=0, width=60)
Tree2.column("#2", stretch=NO, minwidth=0, width=110)
Tree2.column("#3", stretch=NO, minwidth=0, width=110)
Tree2.column("#4", stretch=NO, minwidth=0, width=110)
Tree2.column("#5", stretch=NO, minwidth=0, width=110)
Tree2.column("#6", stretch=NO, minwidth=0, width=100)
Tree2.column("#7", stretch=NO, minwidth=0, width=120)
Tree2.column("#8", stretch=NO, minwidth=0, width=80)
Tree2.column("#9", stretch=NO, minwidth=0, width=120)
Tree2.column("#10", stretch=NO, minwidth=0, width=110)
Tree2.column("#11", stretch=NO, minwidth=0, width=100)


Tree2.grid()


Tree2.delete(*Tree2.get_children())
conn2 = sqlite3.connect("DataBaseDir/ExtraScale.db")
cur2 = conn2.execute(
    "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
    DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable"
)

fetch1 = cur2.fetchall()
for data2 in fetch1:
    Tree2.insert("", "end", values=(data2))
cur2.close()
conn2.close()


def RightClickFunc(event):
    try:
        selectedRow = Tree2.selection()[0]
        RCMenu = Menu(Tree2, tearoff=0)
        RCMenu.add_command(label="Delete", command=DeleteRecord2)
        RCMenu.add_command(label="Refresh", command=Ref2)
        RCMenu.add_command(label="Print", command=ExportSelectedFile)

        try:
            RCMenu.tk_popup(event.x_root, event.y_root)
        finally:
            RCMenu.grab_release()
    except:
        messagebox.showinfo("Ooops", "Choose a record first!")


Tree2.bind("<Button-3>", RightClickFunc)


# ============================================= tab 3 ===================N==============================
# ============================================= tab 3 =================W===E============================
# ============================================= tab 3 ===================S==============================
# ============================================= tab 3 ==================================================
# ============================================= tab 3 ==================================================
# ============================================= tab 3 ==================================================


def PreVeiw2Print():
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    selected_item = TreeDTree2.selection()[0]
    for selected_item in TreeDTree2.selection():
        cur = conn.execute(
            "SELECT TRUCK_NUMBER,TRUCK_MODEL,SUM(EMPTY_WEIGHT-FULL_WEIGHT) AS NET_WEIGHT,PRICE_CHARGE,\
            DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable  WHERE TRUCK_NUMBER=?",
            (TreeDTree2.set(selected_item, "#1"),),
        )

        MyTable1 = prettytable.from_db_cursor(cur)
        cur = conn.cursor()
        rows = cur.fetchall()

        for row in rows:
            MyTable1.add_row(row)

        cur.close()
        conn.close()

        # =========Save Part ===============
        filesave = filedialog.asksaveasfile(
            mode="w",
            title="Export single record",
            filetypes=SaveExtensions,
            defaultextension=SaveExtensions,
        )
        if filesave is None:
            return
        file2Save = str(MyTable1)
        filesave.write(file2Save)
        BillEditor.insert(END, file2Save)
        filesave.close()


"""
def ShowbeforPrint1():
    conn = sqlite3.connect('DataBaseDir/ExtraScale.db')
    selected_item = TreeDTree2.selection()[0]
    for selected_item in TreeDTree2.selection():
        cur = conn.execute("SELECT TRUCK_NUMBER AS PLATE_NO,TRUCK_MODEL,SUM(FULL_WEIGHT-EMPTY_WEIGHT) AS NET_WEIGHT,PRICE_CHARGE AS PRICE,\
            DRIVER_NAME,SERIAL_NUMBER AS BILL_NO,ORIGIN,DESTINATION,REG_DATE AS _DATE FROM ScaleTable  WHERE TRUCK_NUMBER=?",(TreeDTree2.set(selected_item, "#1"),))

        MyTable1 = prettytable.from_db_cursor(cur)
        cur = conn.cursor()
        rows = cur.fetchall()

        file2Save = (str(MyTable1))
        BillEditor.insert(END,"\n\n\n\t\t\t\t   Space4 modern Software Engineer team\n\t\t\t\t____________________________________________\n\t\
            Do not lose this bill till expiration cycle!\n\t\t  _______________________________________________________________________\n\n\n")
        BillEditor.insert(END, file2Save)
        cur.close()
        conn.close()
"""


def ShowbeforPrint():
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    selected_item = TreeDTree2.selection()[0]
    for selected_item in TreeDTree2.selection():
        cur1 = conn.execute(
            "SELECT TRUCK_NUMBER AS PLATE_NO,TRUCK_MODEL,SUM((FULL_WEIGHT)-(EMPTY_WEIGHT)) AS NET_WEIGHT,PRICE_CHARGE AS PRICE\
            FROM ScaleTable  WHERE SERIAL_NUMBER=?",
            (TreeDTree2.set(selected_item, "#4"),),
        )

        MyTable1 = prettytable.from_db_cursor(cur1)
        cur1 = conn.cursor()
        rows = cur1.fetchall()

        file2Save = str(MyTable1)
        BillEditor.insert(
            END,
            "\n\nSpace4 modern Software Engineering.\n______________________________________________\n\n",
        )
        BillEditor.insert(END, file2Save)

        cur1.close()

        cur2 = conn.execute(
            "SELECT DRIVER_NAME,SERIAL_NUMBER AS SERIAL_NO,ORIGIN,DESTINATION\
            FROM ScaleTable  WHERE SERIAL_NUMBER=?",
            (TreeDTree2.set(selected_item, "#4"),),
        )

        MyTable2 = prettytable.from_db_cursor(cur2)
        cur2 = conn.cursor()
        rows2 = cur2.fetchall()

        file2Save2 = str(MyTable2)
        BillEditor.insert(END, "\n")
        BillEditor.insert(END, file2Save2)
        cur2.close()

        cur3 = conn.execute(
            "SELECT REG_DATE FROM ScaleTable  WHERE SERIAL_NUMBER=?",
            (TreeDTree2.set(selected_item, "#4"),),
        )
        MyTable3 = prettytable.from_db_cursor(cur3)
        cur3 = conn.cursor()
        rows3 = cur3.fetchall()

        file2Save3 = str(MyTable3)
        BillEditor.insert(END, "\n")
        BillEditor.insert(END, file2Save3)
        BillEditor.insert(END, "\n")
        BillEditor.insert(END, ("Bill_Exportation_Date:", DateNow))
        BillEditor.insert(END, "\n")
        cur3.close()

        conn.close()


def RefTotal5():
    TreeDTree2.delete(*TreeDTree2.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute(
        """SELECT TRUCK_NUMBER,TRUCK_MODEL,DRIVER_NAME,SERIAL_NUMBER,REG_DATE,REG_MOOD FROM ScaleTable"""
    )
    fetch = cur.fetchall()
    for data in fetch:
        TreeDTree2.insert("", "end", values=(data))
    cur.close()
    conn.close()
    InRef1()
    InRef2()
    InRef3()
    InRef4()
    InRef5()
    InRef6()


def InRef1():
    TreeDTree2.delete(*TreeDTree2.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute(
        """SELECT TRUCK_NUMBER,TRUCK_MODEL,DRIVER_NAME,SERIAL_NUMBER,REG_DATE,REG_MOOD FROM ScaleTable"""
    )
    fetch = cur.fetchall()
    for data in fetch:
        TreeDTree2.insert("", "end", values=(data))
    cur.close()
    conn.close()


def InRef2():
    CaclTree.delete(*CaclTree.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute("""SELECT COUNT(TRUCK_NUMBER) FROM RegTruck""")
    fetch = cur.fetchall()
    for data in fetch:
        CaclTree.insert("", "end", values=(data))
    cur.close()
    conn.close()


def InRef3():
    CaclTree1.delete(*CaclTree1.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute("""SELECT SUM(FULL_WEIGHT-EMPTY_WEIGHT) FROM ScaleTable""")
    fetch = cur.fetchall()
    for data in fetch:
        CaclTree1.insert("", "end", values=(data))
    cur.close()
    conn.close()


def InRef4():
    CaclTree2.delete(*CaclTree2.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute("""SELECT SUM(PRICE_CHARGE) FROM ScaleTable""")
    fetch = cur.fetchall()
    for data in fetch:
        CaclTree2.insert("", "end", values=(data))
    cur.close()
    conn.close()


def InRef5():
    CaclTree3.delete(*CaclTree3.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute("""SELECT COUNT(SERIAL_NUMBER) FROM ScaleTable""")
    fetch = cur.fetchall()
    for data in fetch:
        CaclTree3.insert("", "end", values=(data))
    cur.close()
    conn.close()


def InRef6():
    TreeDTree.delete(*TreeDTree.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute(
        """SELECT TRUCK_NUMBER,TRUCK_MODEL,DRIVER_NAME,REG_DATE,REG_MOOD FROM RegTruck"""
    )
    fetch = cur.fetchall()
    for data in fetch:
        TreeDTree.insert("", "end", values=(data))
    cur.close()
    conn.close()


def BillEditorClear():
    BillEditor.delete("1.0", "end")


def Tab3SearchFunc():
    if Tab3BtnEntry.get() != "":
        TreeDTree2.delete(*TreeDTree2.get_children())
        conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
        cur = conn.execute(
            "SELECT TRUCK_NUMBER,TRUCK_MODEL,DRIVER_NAME,SERIAL_NUMBER,REG_DATE,REG_MOOD FROM ScaleTable\
            WHERE TRUCK_NUMBER LIKE?",
            ("%" + str(Tab3BtnEntry.get()) + "%",),
        )
        fetch = cur.fetchall()
        for data in fetch:
            TreeDTree2.insert("", "end", values=(data))
            ATruckCycleFunc()


def ATruckCycleFunc():
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute(
        "SELECT COUNT(TRUCK_NUMBER) FROM ScaleTable WHERE TRUCK_NUMBER LIKE?",
        ("%" + str(Tab3BtnEntry.get()) + "%",),
    )
    fetch = cur.fetchall()
    for dataA in fetch:
        Tab3LblTtlShow.configure(text=f"{dataA[0]}", font=("Arial", 15, "bold"))


Tab3FrameLeft = ctk.CTkFrame(tab3)
Tab3FrameLeft.grid(row=0, column=0, sticky=W)

Tab3FrameInLeft = ctk.CTkFrame(
    Tab3FrameLeft, border_width=2, corner_radius=10, border_color="teal"
)
Tab3FrameInLeft.grid(row=0, column=0, padx=5, pady=5, sticky=NW)


# ========== Buttons Left ===============
FrameBtn1 = ctk.CTkFrame(Tab3FrameInLeft, width=210)
FrameBtn1.grid(row=0, column=0, pady=10, padx=10, sticky=W)
FrameAdminView2 = ctk.CTkFrame(Tab3FrameInLeft, width=210)
FrameAdminView2.grid(row=1, column=0, padx=10, pady=10, sticky=W)
FrameBillGen3 = ctk.CTkFrame(Tab3FrameLeft, width=210)
FrameBillGen3.grid(row=0, column=1, padx=10, sticky=NW)
FrameBillGen3Btn = ctk.CTkFrame(FrameBillGen3, width=210)
FrameBillGen3Btn.grid(row=1, column=0, pady=5, sticky=NW)


# ============= Calcuations TreeViews ================
Tab3FrameInRight = ctk.CTkFrame(FrameBtn1)
Tab3FrameInRight.grid(row=0, column=0, pady=5, padx=10, sticky=W)
Tab3FrameInRightUpTitle = ctk.CTkLabel(Tab3FrameInRight, text="Registered Trucks")
Tab3FrameInRightUpTitle.grid(row=0, column=0)

CalcTreeV = ctk.CTkFrame(Tab3FrameInRight)
CalcTreeV.grid(row=1, column=0, padx=10, sticky=W)
CaclTree = ttk.Treeview(CalcTreeV, columns=("TR_QUITE"), selectmode="browse", height=1)
CaclTree.heading("TR_QUITE", text="Trucks Quantity", anchor=W)
CaclTree.column("#0", stretch=NO, minwidth=0, width=0)
CaclTree.column("#1", stretch=NO, minwidth=0, width=100)
CaclTree.grid()
CaclTree.delete(*CaclTree.get_children())
CalcConn = sqlite3.connect("DataBaseDir/ExtraScale.db")
CalcCur = CalcConn.execute("SELECT COUNT(TRUCK_NUMBER) FROM RegTruck")
fetch1 = CalcCur.fetchall()
for data1 in fetch1:
    CaclTree.insert("", "end", values=(data1))
CalcCur.close()
CalcConn.close()


Tab3FrameInRightUpTitle1 = ctk.CTkLabel(Tab3FrameInRight, text="Passed Weight")
Tab3FrameInRightUpTitle1.grid(row=0, column=1)

CalcTreeV1 = ctk.CTkFrame(Tab3FrameInRight)
CalcTreeV1.grid(row=1, column=1, padx=10, sticky=W)
CaclTree1 = ttk.Treeview(
    CalcTreeV1, columns=("PS_WEIGHT"), selectmode="browse", height=1
)
CaclTree1.heading("PS_WEIGHT", text="Total Weight /Kg", anchor=W)
CaclTree1.column("#0", stretch=NO, minwidth=0, width=0)
CaclTree1.column("#1", stretch=NO, minwidth=0, width=100)
CaclTree1.grid()
CaclTree1.delete(*CaclTree1.get_children())
CalcConn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
CalcCur1 = CalcConn1.execute("SELECT SUM(FULL_WEIGHT-EMPTY_WEIGHT) FROM ScaleTable")
fetch11 = CalcCur1.fetchall()
for data11 in fetch11:
    CaclTree1.insert("", "end", values=(data11))
CalcCur1.close()
CalcConn1.close()


Tab3FrameInRightUpTitle2 = ctk.CTkLabel(Tab3FrameInRight, text="Price Charged")
Tab3FrameInRightUpTitle2.grid(row=0, column=2)

CalcTreeV2 = ctk.CTkFrame(Tab3FrameInRight)
CalcTreeV2.grid(row=1, column=2, padx=10, sticky=W)
CaclTree2 = ttk.Treeview(
    CalcTreeV2, columns=("PC_CHARGE"), selectmode="browse", height=1
)
CaclTree2.heading("PC_CHARGE", text="Total Price /Afs", anchor=W)
CaclTree2.column("#0", stretch=NO, minwidth=0, width=0)
CaclTree2.column("#1", stretch=NO, minwidth=0, width=100)
CaclTree2.grid()
CaclTree2.delete(*CaclTree2.get_children())
CalcConn2 = sqlite3.connect("DataBaseDir/ExtraScale.db")
CalcCur2 = CalcConn2.execute("SELECT SUM(PRICE_CHARGE) FROM ScaleTable")
fetch12 = CalcCur2.fetchall()
for data12 in fetch12:
    CaclTree2.insert("", "end", values=(data12))
CalcCur2.close()
CalcConn2.close()


Tab3FrameInRightUpTitle3 = ctk.CTkLabel(Tab3FrameInRight, text="Total Passed")
Tab3FrameInRightUpTitle3.grid(row=0, column=3)

CalcTreeV3 = ctk.CTkFrame(Tab3FrameInRight)
CalcTreeV3.grid(row=1, column=3, padx=10, sticky=W)
CaclTree3 = ttk.Treeview(CalcTreeV3, columns=("PASSED"), selectmode="browse", height=1)
CaclTree3.heading("PASSED", text="Passed Time", anchor=W)
CaclTree3.column("#0", stretch=NO, minwidth=0, width=0)
CaclTree3.column("#1", stretch=NO, minwidth=0, width=100)
CaclTree3.grid()
CaclTree3.delete(*CaclTree3.get_children())
CalcConn3 = sqlite3.connect("DataBaseDir/ExtraScale.db")
CalcCur3 = CalcConn3.execute("SELECT COUNT(SERIAL_NUMBER) FROM ScaleTable")
fetch13 = CalcCur3.fetchall()
for data3 in fetch13:
    CaclTree3.insert("", "end", values=(data3))
CalcCur3.close()
CalcConn3.close()


# ----------- Frame 2------------
TreeDLabel = ctk.CTkLabel(
    FrameAdminView2, text="Registered trucks", font=("Arial Black", 13)
)
TreeDLabel.grid(row=0, column=0)

TreeDFrame = ctk.CTkFrame(FrameAdminView2)
TreeDFrame.grid(row=1, column=0, padx=10, sticky=W)
TreeDTree = ttk.Treeview(
    TreeDFrame, columns=("L1", "L2", "L3", "L4", "L5"), selectmode="browse", height=7
)
TreeDTree.heading("L1", text="Truck No", anchor=W)
TreeDTree.heading("L2", text="Truck Model", anchor=W)
TreeDTree.heading("L3", text="Driver name", anchor=W)
TreeDTree.heading("L4", text="Registered Date", anchor=W)
TreeDTree.heading("L5", text="Reg Mood", anchor=W)

TreeDTree.column("#0", stretch=NO, minwidth=0, width=0)
TreeDTree.column("#1", stretch=NO, minwidth=0, width=90)
TreeDTree.column("#2", stretch=NO, minwidth=0, width=100)
TreeDTree.column("#3", stretch=NO, minwidth=0, width=100)
TreeDTree.column("#4", stretch=NO, minwidth=0, width=100)
TreeDTree.column("#5", stretch=NO, minwidth=0, width=80)
TreeDTree.grid()
TreeDTree.delete(*TreeDTree.get_children())
TreeDconn = sqlite3.connect("DataBaseDir/ExtraScale.db")
TreeDcur = TreeDconn.execute(
    "SELECT TRUCK_NUMBER,TRUCK_MODEL,DRIVER_NAME,REG_DATE,REG_MOOD FROM RegTruck"
)
fetchD1 = TreeDcur.fetchall()
for dataD1 in fetchD1:
    TreeDTree.insert("", "end", values=(dataD1))
TreeDcur.close()
TreeDconn.close()


TreeDLabel2 = ctk.CTkLabel(
    FrameAdminView2, text="Passed Weights", font=("Arial Black", 13)
)
TreeDLabel2.grid(row=2, column=0)

TreeDFrame2 = ctk.CTkFrame(FrameAdminView2)
TreeDFrame2.grid(row=3, column=0, padx=10, sticky=W)
TreeDTree2 = ttk.Treeview(
    TreeDFrame2,
    columns=("L2", "L3", "L4", "L5", "L6", "L7"),
    selectmode="browse",
    height=7,
)

TreeDTree2.heading("L2", text="Truck No", anchor=W)
TreeDTree2.heading("L3", text="Truck Model", anchor=W)
TreeDTree2.heading("L4", text="Driver name", anchor=W)
TreeDTree2.heading("L5", text="Serial No", anchor=W)
TreeDTree2.heading("L6", text="Reg Date", anchor=W)
TreeDTree2.heading("L7", text="Reg Mood", anchor=W)

TreeDTree2.column("#0", stretch=NO, minwidth=0, width=0)
TreeDTree2.column("#1", stretch=NO, minwidth=0, width=80)
TreeDTree2.column("#2", stretch=NO, minwidth=0, width=80)
TreeDTree2.column("#3", stretch=NO, minwidth=0, width=80)
TreeDTree2.column("#4", stretch=NO, minwidth=0, width=80)
TreeDTree2.column("#5", stretch=NO, minwidth=0, width=80)
TreeDTree2.column("#6", stretch=NO, minwidth=0, width=80)

TreeDTree2.grid()
TreeDTree2.delete(*TreeDTree2.get_children())
TreeDconn2 = sqlite3.connect("DataBaseDir/ExtraScale.db")
TreeDcur2 = TreeDconn2.execute(
    "SELECT TRUCK_NUMBER,TRUCK_MODEL,DRIVER_NAME,SERIAL_NUMBER,REG_DATE,REG_MOOD FROM ScaleTable"
)
fetchD2 = TreeDcur2.fetchall()
for dataD2 in fetchD2:
    TreeDTree2.insert("", "end", values=(dataD2))
TreeDcur2.close()
TreeDconn2.close()


# ------- Bill Generator --------

BillEditor = ctk.CTkTextbox(FrameBillGen3, width=600, height=200, font=("Consolas", 15))
BillEditor.grid(row=0, column=0)

GenBtnSave = ctk.CTkButton(
    FrameBillGen3Btn, text="Save truck cycles", width=100, command=PreVeiw2Print
)
GenBtnSave.grid(row=0, column=0, padx=5, pady=0)
GenBtnClear = ctk.CTkButton(
    FrameBillGen3Btn,
    text="Clear",
    width=100,
    fg_color=("orange"),
    text_color=("black"),
    command=BillEditorClear,
)
GenBtnClear.grid(row=0, column=1, padx=5, pady=0)
GenBtnBillW = ctk.CTkButton(
    FrameBillGen3Btn, text="Bill View", width=100, command=ShowbeforPrint
)
GenBtnBillW.grid(row=0, column=2, padx=5, pady=0)
GenBtnRef = ctk.CTkButton(
    FrameBillGen3Btn,
    text="Refresh",
    width=100,
    fg_color=("green", "dark green"),
    command=RefTotal5,
)
GenBtnRef.grid(row=0, column=3, padx=5, pady=0)
GenBtnPrint = ctk.CTkButton(
    FrameBillGen3Btn,
    text="Send reports",
    width=100,
    text_color="yellow",
    command=send_email,
)
GenBtnPrint.grid(row=0, column=4, padx=5, pady=0)

Tab3BtnFrame = ctk.CTkFrame(FrameBillGen3)
Tab3BtnFrame.grid(row=2, column=0, sticky=W, padx=5, pady=5, ipadx=20)
TXTV = StringVar()
Tab3Btnlabel = ctk.CTkLabel(Tab3BtnFrame, text="Search in bills")
Tab3Btnlabel.grid(row=0, column=0, sticky=W, padx=10, pady=5)
Tab3BtnEntry = ctk.CTkEntry(
    Tab3BtnFrame, width=150, placeholder_text="Type a truck number"
)
Tab3BtnEntry.grid(row=0, column=1, sticky=W, padx=10, pady=5)
Tab3Btn1 = ctk.CTkButton(Tab3BtnFrame, text="Search", command=Tab3SearchFunc)
Tab3Btn1.grid(row=0, column=2, sticky=W, padx=10, pady=5)
Tab3LblTtlShowTit = ctk.CTkLabel(Tab3BtnFrame, text="| Cycles: ")
Tab3LblTtlShowTit.grid(row=0, column=3, sticky=W, padx=10, pady=5)
Tab3LblTtlShow = ctk.CTkLabel(Tab3BtnFrame, text="")
Tab3LblTtlShow.grid(row=0, column=4, sticky=W, padx=10, pady=5)

# =========== Graph parts =============
GraphFrame1 = ctk.CTkFrame(FrameBillGen3)
GraphFrame1.grid(row=3, column=0)
WaitingLabel = ctk.CTkLabel(
    GraphFrame1, text="Calculating the incomes\nPlease wait a few seconds..."
)
WaitingLabel.grid(row=0, column=0)

# this is my real problem
FromDate1 = "2023-09-12"  # i can add entry for this, date instead
ToDate1 = "2023-09-18"


def saveMonthlyFunc():
    connGraph = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cursor_Graph = connGraph.cursor()
    curG1 = cursor_Graph.execute(
        "SELECT SUM(PRICE_CHARGE) FROM ScaleTable WHERE REG_DATE BETWEEN DATE('now','-7 day') AND DATE('now')"
    )

    result_G1 = curG1.fetchone()[0]
    result_Graph1 = str(result_G1)

    print(result_Graph1, "\t from database")
    config2 = configparser.ConfigParser()
    config2.read("config.ini")
    try:
        config2.add_section("section_months")
    except:
        """"""
    config2.set("section_months", "Jan", result_Graph1)

    with open("Backup_Config_graph.ini", "w") as configfile1:
        config2.write(configfile1)

    cursor_Graph.close()
    connGraph.close()


saveMonthlyFunc()


configGraphGet = configparser.ConfigParser()
configGraphGet.read("Backup_Config_graph.ini")
dtgGet1 = configGraphGet.get("section_months", "Jan")
print(dtgGet1, "\t from config")
income_per_month = {
    "Sun": 500,
    "Mon": 1000,
    "Tue": 2000,
    "Wed": 3000,
    "Thu": 4000,
    "Fri": 5000,
    "Sat": 6000,
}


def plot_income_graph():
    WaitingLabel.destroy()
    months = list(income_per_month.keys())
    income = list(income_per_month.values())
    fig = Figure(figsize=(8, 4), dpi=80)
    plot = fig.add_subplot(111)
    plot.bar(months, income)  # use (plot,bar)(hist,pie not working with this options)
    plot.set_xlabel("Months")
    plot.set_ylabel(f"Income from: {DateNow}")  # Need to set the year

    canvas = FigureCanvasTkAgg(fig, master=GraphFrame1)
    canvas.draw()
    canvas.get_tk_widget().pack(anchor=W)


GraphFrame1.after(2000, plot_income_graph)


# ============================================= tab 4 ==================================================
# ============================================= tab 4 ==================================================
# ============================================= tab 4 ==================================================
# ============================================= tab 4 ==================================================
# ============================================= tab 4 ==================================================
# ============================================= tab 4 ==================================================


# =============================== MainFrames of Weight Calculation are 3 (Top Middle and Bottom) ============================


TRUCK_NUMBER_4 = StringVar()
TRUCK_MODEL_4 = StringVar()
EMPTY_WEIGHT_4 = StringVar()
FULL_WEIGHT_4 = StringVar()
PRICE_CHARGE_4 = StringVar()
GOODS_TYPE_4 = StringVar()
DRIVER_NAME_4 = StringVar()
BILL_NUMBER_4 = StringVar()
ORIGIN_4 = StringVar()
DESTINATION_4 = StringVar()
REG_DATE_4 = StringVar()


def Ref4():
    Tree4.delete(*Tree4.get_children())
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.execute(
        """SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
    DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable """
    )

    fetch = cur.fetchall()
    for data in fetch:
        Tree4.insert("", "end", values=(data))
    cur.close()
    conn.close()


def DeleteRecord4():
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur = conn.cursor()
    messageDelete = messagebox.askyesno(
        "Confirmation", "Do you want to permanently delete this record?"
    )
    if messageDelete > 0:
        selected_item = Tree4.selection()[0]
        for selected_item in Tree4.selection():
            cur.execute(
                "DELETE FROM ScaleTable WHERE SERIAL_NUMBER=?",
                (Tree4.set(selected_item, "SERIAL_NUMBER"),),
            )
        conn.commit()
        Tree4.delete(selected_item)
    conn.close()


"""

def EditingFunction4():
    conn = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur1=conn.cursor()
    cur3=conn.cursor()
    cur4=conn.cursor()
    cur5=conn.cursor()
    cur6=conn.cursor()
    cur7=conn.cursor()
    cur8=conn.cursor()
    cur9=conn.cursor()
    cur10=conn.cursor()
    cur11=conn.cursor()

    selected_item = Tree4.selection()[0]
    for selected_item in Tree4.selection():
        cur1.execute("SELECT TRUCK_NUMBER FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur3.execute("SELECT EMPTY_WEIGHT FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur4.execute("SELECT FULL_WEIGHT FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur5.execute("SELECT PRICE_CHARGE FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur6.execute("SELECT GOODS_TYPE FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur7.execute("SELECT DRIVER_NAME FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur8.execute("SELECT SERIAL_NUMBER FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur9.execute("SELECT ORIGIN FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur10.execute("SELECT DESTINATION FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        cur11.execute("SELECT REG_DATE FROM ScaleTable WHERE ID=?",(Tree4.set(selected_item, "#1"),))
        fetch1 = cur1.fetchall()
        fetch3 = cur3.fetchall()
        fetch4 = cur4.fetchall()
        fetch5 = cur5.fetchall()
        fetch6 = cur6.fetchall()
        fetch7 = cur7.fetchall()
        fetch8 = cur8.fetchall()
        fetch9 = cur9.fetchall()
        fetch10 = cur10.fetchall()
        fetch11 = cur11.fetchall()

        conn.commit()
        if T4Ent1.get() == "":
            T4Ent1.insert(0,fetch1)
        else:
            messagebox.showerror("Oooops","You just clicked on edit!!!")
        if T4Ent3.get() == "":
            T4Ent3.insert(0,fetch3)
        
        if T4Ent4.get() == "":
            T4Ent4.insert(0,fetch4)

        if T4Ent5.get() == "":
            T4Ent5.insert(0,fetch5)
        
        if T4Ent6.get() == "":
            T4Ent6.insert(0,fetch6)
        
        if T4Ent7.get() == "":
            T4Ent7.insert(0,fetch7)
        
        if T4Ent8.get() == "":
            T4Ent8.insert(0,fetch8)
        
        if T4Ent9.get() == "":
            T4Ent9.insert(0,fetch9)
        
        if T4Ent10.get() == "":
            T4Ent10.insert(0,fetch10)
        
        if T4Ent11.get() == "":
            T4Ent11.insert(0,fetch11)
        

    cur1.close()
    cur3.close()
    cur4.close()
    cur5.close()
    cur6.close()
    cur7.close()
    cur8.close()
    cur9.close()
    cur10.close()
    cur11.close()
    conn.close()
    T4Ent1.focus()


"""


def submit4():
    messagebox.showinfo(
        Title, "Remember Dear User!!!\nManual data registration has no guarantee !!!"
    )
    DateNow = datetime.date.today()
    conn1 = sqlite3.connect("DataBaseDir/ExtraScale.db")
    cur1 = conn1.cursor()
    if (
        T4Ent1.get() == ""
        or T4Ent2.get() == ""
        or T4Ent3.get() == ""
        or T4Ent4.get() == ""
        or T4Ent5.get() == ""
        or T4Ent6.get() == ""
        or T4Ent7.get() == ""
        or T4Ent9.get() == ""
        or T4Ent10.get() == ""
        or T4Ent11.get() == ""
    ):
        messagebox.showerror("Warning!!!", "Please fill the Entries First!")
    else:
        cur1.execute(
            f"insert into ScaleTable (TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,\
            GOODS_TYPE,DRIVER_NAME,ORIGIN,DESTINATION,REG_DATE,REG_MOOD)\
            values ('{TRUCK_NUMBER_4.get()}','{TRUCK_MODEL_4.get()}','{EMPTY_WEIGHT_4.get()}',\
            '{FULL_WEIGHT_4.get()}','{PRICE_CHARGE_4.get()}','{GOODS_TYPE_4.get()}','{DRIVER_NAME_4.get()}',\
            '{ORIGIN_4.get()}','{DESTINATION_4.get()}','{REG_DATE_4.get()}','Manual')"
        )

    conn1.commit()
    conn1.close()

    T4Ent1.delete(0, END)
    T4Ent2.set("Choose Truck Model")
    T4Ent3.delete(0, END)
    T4Ent4.delete(0, END)
    T4Ent5.delete(0, END)
    T4Ent6.delete(0, END)
    T4Ent7.delete(0, END)
    T4Ent9.delete(0, END)
    T4Ent10.delete(0, END)
    T4Ent11.delete(0, END)
    T4Ent1.focus()
    Ref4()


def ClearEntry4():
    T4Ent1.delete(0, END)
    T4Ent2.set("Choose Truck Model")
    T4Ent3.delete(0, END)
    T4Ent4.delete(0, END)
    T4Ent5.delete(0, END)
    T4Ent6.delete(0, END)
    T4Ent7.delete(0, END)
    T4Ent9.delete(0, END)
    T4Ent10.delete(0, END)
    T4Ent11.delete(0, END)
    T4Ent1.focus()


def ExportSelectedFile4():
    conn2 = sqlite3.connect("DataBaseDir/ExtraScale.db")
    selected_item2 = Tree4.selection()[0]
    for selected_item2 in Tree4.selection():
        cur2 = conn2.execute(
            "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
            DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE,REG_MOOD FROM ScaleTable  WHERE SERIAL_NUMBER=?",
            (Tree4.set(selected_item2, "SERIAL_NUMBER"),),
        )

        MyTable = prettytable.from_db_cursor(cur2)
        cur2 = conn2.cursor()
        rows = cur2.fetchall()

        for row in rows:
            MyTable.add_row(row)
        cur2.close()
        conn2.close()

        # =========Save Part ===============
        filesave = filedialog.asksaveasfile(
            mode="w",
            title="Export single record",
            filetypes=SaveExtensions,
            defaultextension=SaveExtensions,
        )
        if filesave is None:
            return
        file2Save = str(MyTable)
        filesave.write(file2Save)
        filesave.close()
        messagebox.showinfo(
            "HCR-BLUE", "Please choose font\n< Consolas >\n in your text viewer"
        )


# ====================== Tab 4 Frames  ==========================
MainFrameMidTab4 = ctk.CTkFrame(tab4)
MainFrameMidTab4.grid(row=0, column=0, sticky=W, ipady=20)
MainFrameBotTab4 = ctk.CTkFrame(tab4)
MainFrameBotTab4.grid(row=1, column=0, padx=5, sticky=W, pady=10)


# ====================== Inner Frames of Label & Entries ==========================
InMainFrameMidTab4 = ctk.CTkFrame(MainFrameMidTab4)
InMainFrameMidTab4.grid(row=0, column=0, pady=20)
InMainFrameBotTab4 = ctk.CTkFrame(MainFrameBotTab4)
InMainFrameBotTab4.grid(row=0, column=0)
# ===================== Date, Time, Developer Labels =========================================

clocklblTab4 = ctk.CTkLabel(tab4)
clocklblTab4.place(x=490, y=190)
datelblTab4 = ctk.CTkLabel(tab4)
datelblTab4.place(x=650, y=190)


# ======================= Label & Entries ===========================

T4LBL_1 = ctk.CTkLabel(InMainFrameMidTab4, text="Truck No:", font=("Arial", 13, "bold"))
T4LBL_1.grid(row=0, column=0, sticky=W, padx=10, pady=5)
T4LBL_2 = ctk.CTkLabel(
    InMainFrameMidTab4, text="Truck Model:", font=("Arial", 13, "bold")
)
T4LBL_2.grid(row=1, column=0, sticky=W, padx=10, pady=5)
T4LBL_3 = ctk.CTkLabel(
    InMainFrameMidTab4, text="Empty Weight / Kg:", font=("Arial", 13, "bold")
)
T4LBL_3.grid(row=2, column=0, sticky=W, padx=10, pady=5)
T4LBL_4 = ctk.CTkLabel(
    InMainFrameMidTab4, text="Full Weight / Kg:", font=("Arial", 13, "bold")
)
T4LBL_4.grid(row=3, column=0, sticky=W, padx=10, pady=5)

T4LBL_5 = ctk.CTkLabel(
    InMainFrameMidTab4, text="Price Charge/ Af:", font=("Arial", 13, "bold")
)
T4LBL_5.grid(row=0, column=2, sticky=W, padx=10, pady=5)
T4LBL_6 = ctk.CTkLabel(
    InMainFrameMidTab4, text="Goods Type:", font=("Arial", 13, "bold")
)
T4LBL_6.grid(row=1, column=2, sticky=W, padx=10, pady=5)
T4LBL_7 = ctk.CTkLabel(
    InMainFrameMidTab4, text="Driver Name:", font=("Arial", 13, "bold")
)
T4LBL_7.grid(row=2, column=2, sticky=W, padx=10, pady=5)
T4LBL_8 = ctk.CTkLabel(
    InMainFrameMidTab4, text="Serial No:", font=("Arial", 13, "bold")
)
T4LBL_8.grid(row=3, column=2, sticky=W, padx=10, pady=5)

T4LBL_9 = ctk.CTkLabel(InMainFrameMidTab4, text="Origin:", font=("Arial", 13, "bold"))
T4LBL_9.grid(row=0, column=4, sticky=W, padx=10, pady=5)
T4LBL_10 = ctk.CTkLabel(
    InMainFrameMidTab4, text="Destination:", font=("Arial", 13, "bold")
)
T4LBL_10.grid(row=1, column=4, sticky=W, padx=10, pady=5)
T4LBL_11 = ctk.CTkLabel(InMainFrameMidTab4, text="Date", font=("Arial", 13, "bold"))
T4LBL_11.grid(row=2, column=4, sticky=W, padx=10, pady=5)
T4LBL_12 = ctk.CTkLabel(InMainFrameMidTab4, text="Actions:", font=("Arial", 13, "bold"))
T4LBL_12.grid(row=3, column=4, sticky=W, padx=10, pady=5)


T4Ent1 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=TRUCK_NUMBER_4,
)
T4Ent1.grid(row=0, column=1, padx=10, sticky=W)
T4Ent1.focus()

TruckModel = ["Actrus", "Hino", "Mazda", "Kamaz"]
TRUCK_MODEL_4.set("Choose Truck Model")
T4Ent2 = ctk.CTkComboBox(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    values=TruckModel,
    corner_radius=10,
    variable=TRUCK_MODEL_4,
)
T4Ent2.grid(row=1, column=1, padx=10, sticky=W)
T4Ent3 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=EMPTY_WEIGHT_4,
)
T4Ent3.grid(row=2, column=1, padx=10, sticky=W)
T4Ent4 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=FULL_WEIGHT_4,
)
T4Ent4.grid(row=3, column=1, padx=10, sticky=W)

T4Ent5 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=PRICE_CHARGE_4,
)
T4Ent5.grid(row=0, column=3, padx=10, sticky=W)
T4Ent6 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=GOODS_TYPE_4,
)
T4Ent6.grid(row=1, column=3, padx=10, sticky=W)
T4Ent7 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=DRIVER_NAME_4,
)
T4Ent7.grid(row=2, column=3, padx=10, sticky=W)
T4Ent8 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    state=DISABLED,
)
T4Ent8.grid(row=3, column=3, padx=10, sticky=W)

T4Ent9 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=ORIGIN_4,
)
T4Ent9.grid(row=0, column=5, padx=10, sticky=W)
T4Ent10 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=DESTINATION_4,
)
T4Ent10.grid(row=1, column=5, padx=10, sticky=W)
T4Ent11 = ctk.CTkEntry(
    InMainFrameMidTab4,
    width=249,
    font=("Arial", 15, "bold"),
    height=35,
    corner_radius=7,
    textvariable=REG_DATE_4,
)
T4Ent11.grid(row=2, column=5, padx=10, sticky=W)
T4InMidMainFrame = ctk.CTkFrame(
    InMainFrameMidTab4, border_color=BGGRAY, border_width=0, corner_radius=7
)
T4InMidMainFrame.grid(row=3, column=5, padx=10, sticky=W)
T4Btn_Save = ctk.CTkButton(
    T4InMidMainFrame,
    text="   Save   ",
    font=("Arial", 15, "bold"),
    width=30,
    fg_color=BGGREEN,
    text_color=BGYELLOW,
    command=submit4,
)
T4Btn_Save.grid(row=0, column=0, padx=8, pady=5, sticky=W)
T4Btn_Clear = ctk.CTkButton(
    T4InMidMainFrame,
    text=" Clear ",
    font=("Arial", 13, "bold"),
    width=30,
    text_color=BGYELLOW,
    command=ClearEntry4,
)
T4Btn_Clear.grid(row=0, column=1, padx=8, pady=5, sticky=W)
T4Btn_Refresh = ctk.CTkButton(
    T4InMidMainFrame,
    text=" Refresh ",
    font=("Arial", 13, "bold"),
    width=30,
    command=Ref4,
)
T4Btn_Refresh.grid(row=0, column=2, padx=8, pady=5, sticky=W)


MiniWinTree4 = ctk.CTkFrame(MainFrameBotTab4)
MiniWinTree4.grid(row=0, column=0, padx=5, sticky=W)
ScrolbarXtree1 = ctk.CTkScrollbar(MainFrameBotTab4, orientation=HORIZONTAL)
ScrolbarYtree1 = ctk.CTkScrollbar(MainFrameBotTab4, orientation=VERTICAL)
Tree4 = ttk.Treeview(
    MiniWinTree4,
    columns=(
        "TRUCK_NUMBER",
        "TRUCK_MODEL",
        "EMPTY_WEIGHT",
        "FULL_WEIGHT",
        "PRICE_CHARGE",
        "GOODS_TYPE",
        "DRIVER_NAME",
        "SERIAL_NUMBER",
        "ORIGIN",
        "DESTINATION",
        "REG_DATE",
    ),
    selectmode="extended",
    height=13,
    yscrollcommand=ScrolbarYtree1.set,
    xscrollcommand=ScrolbarXtree1.set,
)
ScrolbarYtree1.configure(command=Tree4.yview)
ScrolbarYtree1.grid(row=0, column=1, ipady=90, sticky=W)
ScrolbarXtree1.configure(command=Tree4.xview)
ScrolbarXtree1.grid(row=1, column=0, ipadx=470, sticky=W)
# =====setting headings for the columns


Tree4.heading("TRUCK_NUMBER", text="Truck No", anchor=W)
Tree4.heading("TRUCK_MODEL", text="Truck Model", anchor=W)
Tree4.heading("EMPTY_WEIGHT", text="Empty Weight", anchor=W)
Tree4.heading("FULL_WEIGHT", text="Full Weight", anchor=W)
Tree4.heading("PRICE_CHARGE", text="Price Charge", anchor=W)
Tree4.heading("GOODS_TYPE", text="Goods Type", anchor=W)
Tree4.heading("DRIVER_NAME", text="Driver Name", anchor=W)
Tree4.heading("SERIAL_NUMBER", text="Serial No", anchor=W)
Tree4.heading("ORIGIN", text="Origin", anchor=W)
Tree4.heading("DESTINATION", text="Destination", anchor=W)
Tree4.heading("REG_DATE", text="Date", anchor=W)

# setting width of the columns
Tree4.column("#0", stretch=NO, minwidth=0, width=0)
Tree4.column("#1", stretch=NO, minwidth=0, width=60)
Tree4.column("#2", stretch=NO, minwidth=0, width=110)
Tree4.column("#3", stretch=NO, minwidth=0, width=110)
Tree4.column("#4", stretch=NO, minwidth=0, width=110)
Tree4.column("#5", stretch=NO, minwidth=0, width=110)
Tree4.column("#6", stretch=NO, minwidth=0, width=100)
Tree4.column("#7", stretch=NO, minwidth=0, width=120)
Tree4.column("#8", stretch=NO, minwidth=0, width=80)
Tree4.column("#9", stretch=NO, minwidth=0, width=120)
Tree4.column("#10", stretch=NO, minwidth=0, width=110)
Tree4.column("#11", stretch=NO, minwidth=0, width=100)


Tree4.grid()


Tree4.delete(*Tree4.get_children())
conn3 = sqlite3.connect("DataBaseDir/ExtraScale.db")
cur3 = conn3.execute(
    "SELECT TRUCK_NUMBER,TRUCK_MODEL,EMPTY_WEIGHT,FULL_WEIGHT,PRICE_CHARGE,GOODS_TYPE,\
    DRIVER_NAME,SERIAL_NUMBER,ORIGIN,DESTINATION,REG_DATE FROM ScaleTable"
)

fetch1 = cur3.fetchall()
for data1 in fetch1:
    Tree4.insert("", "end", values=(data1))
cur3.close()
conn3.close()


def RightClickFunc4(event):
    try:
        selectedRow4 = Tree4.selection()[0]
        RCMenu4 = Menu(Tree4, tearoff=0)
        RCMenu4.add_command(label="Delete", command=DeleteRecord4)
        RCMenu4.add_command(label="Refresh", command=Ref4)
        RCMenu4.add_command(label="Print", command=ExportSelectedFile4)

        try:
            RCMenu4.tk_popup(event.x_root, event.y_root)
        finally:
            RCMenu4.grab_release()
    except:
        messagebox.showinfo("Ooops", "Choose a record first!")


Tree4.bind("<Button-3>", RightClickFunc4)


def timshow():
    from time import strftime

    string = strftime(" %H:%M : %S %p")
    stringdate = strftime("%Y-%m-%d - %a")
    clocklblTab4.configure(text=string, font=("Arial", 20))
    datelblTab4.configure(text=stringdate, font=("Humnst777 Blk BT", 20))

    clocklblTab4.after(1000, timshow)


timshow()


# ============== Welcomed window Blur background =========================
# ============== the other option of this event is near the root window =========
main_image_welwin = ImageTk.PhotoImage(ImageGrab.grab().filter(ImageFilter.BLUR))
blur_overlay_welwin = Label(root, image=main_image_welwin)
blur_overlay_welwin.place(x=0, y=0, relwidth=1, relheight=1)
blur_overlay_welwin.image = main_image_welwin


root.mainloop()
