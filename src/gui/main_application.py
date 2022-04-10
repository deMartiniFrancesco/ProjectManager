
from ..gui import *

# Modes: "System" (standard), "Dark", "Light"
set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
set_default_color_theme("blue")


class App(CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Project Manager")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        if sys.platform == "darwin":
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)

        # ============ create two frames ============

        # configure grid layout (1x2)
        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.frame_left = CTkFrame(master=self,
                                   width=180,
                                   corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = MainPage(self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.label_1 = CTkLabel(master=self.frame_left,
                                text="ProjectManager",
                                text_font=("Roboto Medium", -16),
                                )  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.new_project_button = CTkButton(master=self.frame_left,
                                            text="Nuovo Progetto",
                                            # <- custom tuple-color
                                            fg_color=("gray75", "gray30"),
                                            command=lambda: self.chose_frame(MainPageEnum.NEW_PROJECT))
        self.new_project_button.grid(row=2, column=0, pady=10, padx=20)

        self.sort_project_button = CTkButton(master=self.frame_left,
                                             text="Ordina Progetti",
                                             # <- custom tuple-color
                                             fg_color=("gray75", "gray30"),
                                             command=lambda: self.chose_frame(MainPageEnum.SORT_PROJECT))
        self.sort_project_button.grid(row=3, column=0, pady=10, padx=20)
        self.sort_project_button.config(state=tkinter.DISABLED)

        self.settings_button = CTkButton(master=self.frame_left,
                                         text="Settings",
                                         fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                         command=lambda: self.chose_frame(MainPageEnum.SETTINGS))
        self.settings_button.grid(
            row=9, column=0, pady=10, padx=20, sticky="w")

        self.switch_dark_mode = CTkSwitch(master=self.frame_left,
                                          text="Dark Mode",
                                          command=self.change_mode)
        self.switch_dark_mode.select()
        self.switch_dark_mode.grid(
            row=10, column=0, pady=10, padx=20, sticky="w")

    def change_right_frame(self, frame: CTkFrame):
        self.clear_frame_right()

        self.frame_right = frame

        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def chose_frame(self, page_type):
        match page_type:
            case MainPageEnum.NEW_PROJECT:
                self.change_right_frame(NewProjectPage(self))

            case MainPageEnum.SORT_PROJECT:
                # TODO sort project
                pass

            case MainPageEnum.SETTINGS:
                self.change_right_frame(SettingsPage(self, self))

            case _:
                self.change_right_frame(MainPage(self))

    def change_mode(self):
        if self.switch_dark_mode.get() == 1:
            set_appearance_mode("dark")
        else:
            set_appearance_mode("light")

    def clear_frame_right(self):
        self.frame_right.destroy()

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


    