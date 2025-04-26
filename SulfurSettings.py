import subprocess
from importlib.metadata import PackageNotFoundError
from VersionDATA.ai_renderer import call_file_path
call = call_file_path.Call()
file_path_settings_name_extra_device = call.settings_extra_debug()
file_path_settings_name_backup = call.settings_backup()

with open(file_path_settings_name_extra_device, "r", encoding="utf-8", errors="ignore") as file:
    lines = file.readlines()
    if len(lines) == 0:
        with open(file_path_settings_name_extra_device, "w", encoding="utf-8", errors="ignore") as file:
            file.write("no")

with open(file_path_settings_name_backup, "r", encoding="utf-8", errors="ignore") as file:
    lines = file.readlines()
    if len(lines) == 0:
        with open(file_path_settings_name_backup, "w", encoding="utf-8", errors="ignore") as file:
            file.write("yes")


def install(packages):
    package_string = ""

    if isinstance(packages, str):
        packages = [packages]

    for pkg in packages:
        try:
            if pkg == "pygame-ce":
                subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame-ce", "--upgrade"])
                print("pygame-ce installed successfully!")
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
                print(f"{pkg} installed successfully!")
        except (ModuleNotFoundError, PermissionError, TimeoutError, MemoryError) as error:
            print(f"An error occurred while installing {pkg}: {error}")
        except subprocess.CalledProcessError as error:
            print(f"Failed to install {pkg}. Error: {error}")

def print_verti_list(list):
    for item in list: print(item)

TOS = [
    "By using this application you agree to the Terms of Service listed in the project files.",
    "If you cannot find it, install a new version."
] #terms of service
print_verti_list(TOS)

print("-------SulfurAI Settings requires the extension PYGAME COMMUNITY EDITION.-------")
import os  ##Global and Importing functions and variables
import time,sys
try:
    import pygame
except ImportError:
    install("pygame-ce")
    import pygame


try:
    import pygame_gui
except ImportError:
    install("pygame_gui")
    import pygame_gui


supporting_text_ver = False

file_path_settings_name_ui_days_ago = call.settings_ui_days_ago()
file_path_settings_name_ui_days_apart = call.settings_ui_days_apart()

file_path_settings_name_ui_weeks_ago = call.settings_ui_weeks_ago()
file_path_settings_name_ui_weeks_apart = call.settings_ui_weeks_apart()

file_path_settings_name_ui_months_ago = call.settings_ui_months_ago()
file_path_settings_name_ui_months_apart = call.settings_ui_months_apart()

file_path_settings_name_ui_years_ago = call.settings_ui_years_ago()
file_path_settings_name_ui_years_apart = call.settings_ui_years_apart()
def attempt_quit_pygame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        managers = [
            manager,
            manager_dago,
            manager_dapart,
            manager_wago,
            manager_wapart,
            manager_mago,
            manager_mapart,
            manager_yago,
            manager_yapart,
        ]
        for m in managers:
            m.process_events(event)
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_object_id == '#main_text_entry':
                file_path = ""
                source_manager = event.ui_element.ui_manager


                if source_manager is manager:
                    file_path = file_path_input_limit
                elif source_manager is manager_dago:
                    file_path = file_path_settings_name_ui_days_ago
                elif source_manager is manager_dapart:
                    file_path = file_path_settings_name_ui_days_apart
                elif source_manager is manager_wago:
                    file_path = file_path_settings_name_ui_weeks_ago
                elif source_manager is manager_wapart:
                    file_path = file_path_settings_name_ui_weeks_apart
                elif source_manager is manager_mago:
                    file_path = file_path_settings_name_ui_months_ago
                elif source_manager is manager_mapart:
                    file_path = file_path_settings_name_ui_months_apart
                elif source_manager is manager_yago:
                    file_path = file_path_settings_name_ui_years_ago
                elif source_manager is manager_yapart:
                    file_path = file_path_settings_name_ui_years_apart


                try:
                    current_text = int(event.ui_element.get_text())
                except ValueError:
                    if source_manager is manager:
                        current_text = 50
                        print("Your input is not an integer. Auto set to 50.")
                    elif source_manager is not manager_yapart:
                        current_text = 5
                        print("Your input is not an integer. Auto set to 5.")
                    else:
                        current_text = 1
                        print("Your input is not an integer. Auto set to 1.")

                print(f"Input changed to {current_text}")

                # Save to the corresponding file
                with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
                    file.write(str(current_text))




def open_text_ver():
    pass # add text ver



verify = ["-------Checking for pygame.","-------Verifying..."]
print_verti_list(verify)
try:

    temp_init_pygame = 0
    pygame.init()
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720
    manager = pygame_gui.UIManager((1080, 720))
    manager_dago = pygame_gui.UIManager((1080, 720))
    manager_dapart = pygame_gui.UIManager((1080, 720))
    manager_wago = pygame_gui.UIManager((1080, 720))
    manager_wapart = pygame_gui.UIManager((1080, 720))
    manager_mago = pygame_gui.UIManager((1080, 720))
    manager_mapart = pygame_gui.UIManager((1080, 720))
    manager_yago = pygame_gui.UIManager((1080, 720))
    manager_yapart = pygame_gui.UIManager((1080, 720))
    text_input_input_settings = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((500, 350), (100, 50)), manager=manager,object_id='#main_text_entry')
    ui_dago = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 175), (100, 50)), manager=manager_dago, object_id='#main_text_entry')
    ui_dapart = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((825, 175), (100, 50)), manager=manager_dapart,object_id='#main_text_entry')

    ui_wago = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 260), (100, 50)), manager=manager_wago, object_id='#main_text_entry')
    ui_wapart = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((825, 260), (100, 50)), manager=manager_wapart,object_id='#main_text_entry')

    ui_mago = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 350), (100, 50)), manager=manager_mago,object_id='#main_text_entry')
    ui_mapart = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((850, 350), (100, 50)),manager=manager_mapart, object_id='#main_text_entry')

    ui_yago = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 425), (100, 50)), manager=manager_yago,object_id='#main_text_entry')
    ui_yapart = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((825, 425), (100, 50)),manager=manager_yapart, object_id='#main_text_entry')
    file_path_input_limit = call.input_limit()
    global limit_default


    def read_file_with_default(file_path, default_value):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                return ",".join(file.readlines())
        except (ValueError, FileNotFoundError):
            return default_value


    # Set default values
    default_limit = 50
    default_uda = default_wda = default_wdg = default_udg = default_mda = default_mdg = default_ydg = 5
    default_yda = 1

    # Read files
    limit_default = read_file_with_default(file_path_input_limit, default_limit)
    udg = read_file_with_default(file_path_settings_name_ui_days_ago, default_udg)
    uda = read_file_with_default(file_path_settings_name_ui_days_apart, default_uda)
    wdg = read_file_with_default(file_path_settings_name_ui_weeks_ago, default_wdg)
    wda = read_file_with_default(file_path_settings_name_ui_weeks_apart, default_wda)
    mdg = read_file_with_default(file_path_settings_name_ui_months_ago, default_mdg)
    mda = read_file_with_default(file_path_settings_name_ui_months_apart, default_mda)
    ydg = read_file_with_default(file_path_settings_name_ui_years_ago, default_ydg)
    yda = read_file_with_default(file_path_settings_name_ui_years_apart, default_yda)



    app_open = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    text_input_input_settings.set_text(str(limit_default))
    ui_dago.set_text(str(udg))
    ui_dapart.set_text(str(uda))
    ui_wago.set_text(str(wdg))
    ui_wapart.set_text(str(wda))

    ui_mago.set_text(str(mdg))
    ui_mapart.set_text(str(mda))
    ui_yago.set_text(str(ydg))
    ui_yapart.set_text(str(yda))
    dt = 0
    clock = pygame.time.Clock()

    class Button:
        def __init__(self, image_path, position, scale=1.0):
            self.image = pygame.image.load(image_path).convert_alpha()
            original_width = self.image.get_width()
            original_height = self.image.get_height()
            new_width = int(original_width * scale)
            new_height = int(original_height * scale)
            self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
            self.rect = self.image.get_rect(topleft=position)
            self.pressed = False
            self.touched = False

        def draw(self, window):
            window.blit(self.image, self.rect)

        def draw_x_y(self, window, x, y):
            window.blit(self.image, (x, y))

        def x_y(self):
            return self.rect.x, self.rect.y

        def is_pressed(self):
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()[0]

            if self.rect.collidepoint(mouse_pos):
                if mouse_pressed and not self.pressed:  # study
                    self.pressed = True
                    return True

            if not mouse_pressed:
                self.pressed = False

            return False

        def is_touched(self):
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                self.touched = True

                return True
            return False

        def set_alpha(self, alpha):
            self.image.set_alpha(alpha)

        def rotate(self, degrees):
            self.image = pygame.transform.rotate(self.image, degrees)

    extra_debug_settings_button = Button("DATA/settings/images/ex_dbg_button.jpeg",(250,200),.15)
    extra_debug_settings_screen = Button("DATA/settings/images/ex_dbg_screen.jpeg", (55, 50), .6)
    extra_debug_settings_x = Button("DATA/settings/images/ex_dbg_x.jpeg", (900, 0), .25)
    extra_debug_settings_off = Button("DATA/settings/images/ex_dbg_off.jpeg", (425, 150), .15)
    extra_debug_settings_on = Button("DATA/settings/images/ex_dbg_on.jpeg", (425, 150), .15)

    extra_backup_settings_screen = Button("DATA/settings/images/ex_dbg_screen_backup.jpeg", (55, 50), .6)
    extra_backup_settings_button = Button("DATA/settings/images/ex_backup_button.jpeg", (500, 200), .15)
    extra_backup_settings_x = Button("DATA/settings/images/ex_dbg_x.jpeg", (900, 0), .25)
    extra_backup_settings_off = Button("DATA/settings/images/ex_dbg_off.jpeg", (425, 200), .15)
    extra_backup_settings_on = Button("DATA/settings/images/ex_dbg_on.jpeg", (425, 200), .15)

    extra_input_settings_screen = Button("DATA/settings/images/ex_input_screen.jpeg", (55, 50), .6)
    extra_input_settings_button = Button("DATA/settings/images/ex_input_button.jpeg", (750, 200), .15)
    extra_input_settings_x = Button("DATA/settings/images/ex_dbg_x.jpeg", (900, 0), .25)
    extra_input_settings_processLimit_off = Button("DATA/settings/images/ex_dbg_off.jpeg", (620, 190), .15)
    extra_input_settings_processLimit_on = Button("DATA/settings/images/ex_dbg_on.jpeg", (620, 190), .15)

    extra_user_insight_screen = Button("DATA/settings/images/ex_user_insight_screen.jpeg", (55, 50), .6)
    extra_user_insight_button = Button("DATA/settings/images/ex_user_insight.jpeg", (250, 350), .15)
    extra_user_insight_x = Button("DATA/settings/images/ex_dbg_x.jpeg", (900, 0), .25)
    extra_user_insight_off = Button("DATA/settings/images/ex_dbg_off.jpeg", (620, 190), .15)
    extra_user_insight_on = Button("DATA/settings/images/ex_dbg_on.jpeg", (620, 190), .15)



    ####################SPRITES
    backdrop = pygame.image.load("DATA/settings/images/backdrop.png")
    backdrop = pygame.transform.smoothscale(backdrop,(SCREEN_WIDTH+ 42,SCREEN_HEIGHT + 25))

    mouseHitbox = pygame.image.load("DATA/settings/images/mousehitbox.jpeg")
    mouseHitbox.set_alpha(0)
    show_settings_screen = False
    show_backup_screen = False
    show_input_screen = False
    show_ui_screen = False

    while app_open:
        if temp_init_pygame == 0:
            print("-------Pygame initiated succesfully.")
            temp_init_pygame = 1
        layers = {
            "backdrop":backdrop,
            "mouseHitbox":mouseHitbox,

        }
        for layer_name, layer_surface in layers.items():
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if layer_name == "backdrop": screen.blit(backdrop,(-25,-10))
            elif layer_name == "mouseHitbox": screen.blit(mouseHitbox,(mouse_x,mouse_y))
        extra_debug_settings_button.draw(screen)
        extra_backup_settings_button.draw(screen)
        extra_input_settings_button.draw(screen)
        extra_user_insight_button.draw(screen)
        ##########exdg button
        if extra_debug_settings_button.is_touched():
            extra_debug_settings_button.set_alpha(200)
        else:
            extra_debug_settings_button.set_alpha(255)
        if extra_debug_settings_button.is_pressed():
                show_settings_screen = True
        ######backup button
        if extra_backup_settings_button.is_touched():
            extra_backup_settings_button.set_alpha(200)
        else:
            extra_backup_settings_button.set_alpha(255)
        if extra_backup_settings_button.is_pressed():
                show_backup_screen = True

        ######input button
        if extra_input_settings_button.is_touched():
            extra_input_settings_button.set_alpha(200)
        else:
            extra_input_settings_button.set_alpha(255)
        if extra_input_settings_button.is_pressed():
            show_input_screen = True

        ######ui button
        if extra_user_insight_button.is_touched():
            extra_user_insight_button.set_alpha(200)
        else:
            extra_user_insight_button.set_alpha(255)
        if extra_user_insight_button.is_pressed():
            show_ui_screen = True

        ##########exdg screen
        if show_settings_screen:
            with open(file_path_settings_name_extra_device, "r", encoding="utf-8", errors="ignore") as file:
                extra_debug = file.readlines()
            # Replace this with your actual settings screen drawing logic
            extra_debug_settings_screen.draw(screen)
            extra_debug_settings_x.draw(screen)
            if "no" in extra_debug:
                extra_debug_settings_off.draw(screen)
                if extra_debug_settings_off.is_touched(): extra_debug_settings_off.set_alpha(200)
                else:  extra_debug_settings_off.set_alpha(255)
                if extra_debug_settings_off.is_pressed():
                    with open(file_path_settings_name_extra_device, "w", encoding="utf-8", errors="ignore") as file:
                        file.write("yes")

            else:
                if "yes" in extra_debug:
                    extra_debug_settings_on.draw(screen)
                    if extra_debug_settings_on.is_touched():
                        extra_debug_settings_on.set_alpha(200)
                    else:
                        extra_debug_settings_on.set_alpha(255)
                    if extra_debug_settings_on.is_pressed():
                        with open(file_path_settings_name_extra_device, "w", encoding="utf-8", errors="ignore") as file:
                            file.write("no")
            if extra_debug_settings_x.is_touched():
                extra_debug_settings_x.set_alpha(200)
            else:
                extra_debug_settings_x.set_alpha(255)
            if extra_debug_settings_x.is_pressed():
                show_settings_screen = False
        ##########backup screen
        if show_backup_screen:
            with open(file_path_settings_name_backup, "r", encoding="utf-8", errors="ignore") as file:
                allow_backup_td = file.readlines()
            # Replace this with your actual settings screen drawing logic
            extra_backup_settings_screen.draw(screen)
            extra_backup_settings_x.draw(screen)
            if "no" in allow_backup_td:
                extra_backup_settings_off.draw(screen)
                if extra_backup_settings_off.is_touched():
                    extra_backup_settings_off.set_alpha(200)
                else:
                    extra_backup_settings_off.set_alpha(255)
                if extra_backup_settings_off.is_pressed():
                    with open(file_path_settings_name_backup, "w", encoding="utf-8", errors="ignore") as file:
                        file.write("yes")

            else:
                if "yes" in allow_backup_td:
                    extra_backup_settings_on.draw(screen)
                    if extra_backup_settings_on.is_touched():
                        extra_backup_settings_on.set_alpha(200)
                    else:
                        extra_backup_settings_on.set_alpha(255)
                    if extra_backup_settings_on.is_pressed():
                        with open(file_path_settings_name_backup, "w", encoding="utf-8", errors="ignore") as file:
                            file.write("no")
            if extra_backup_settings_x.is_touched():
                extra_backup_settings_x.set_alpha(200)
            else:
                extra_backup_settings_x.set_alpha(255)
            if extra_backup_settings_x.is_pressed():
                show_backup_screen = False



        ##########input screen
        if show_input_screen:

            file_path_settings_name_input_process_limit = call.settings_input_process_limit()
            with open(file_path_settings_name_input_process_limit, "r", encoding="utf-8", errors="ignore") as file:
                limit_process_input = file.readlines()

            extra_input_settings_screen.draw(screen)
            extra_input_settings_x.draw(screen)
            manager.draw_ui(screen)
            if "no" in limit_process_input:
                extra_input_settings_processLimit_off.draw(screen)
                if extra_input_settings_processLimit_off.is_touched():
                    extra_input_settings_processLimit_off.set_alpha(200)
                else:
                    extra_input_settings_processLimit_off.set_alpha(255)
                if extra_input_settings_processLimit_off.is_pressed():
                    with open(file_path_settings_name_input_process_limit, "w", encoding="utf-8", errors="ignore") as file:
                        file.write("yes")

            else:
                if "yes" in limit_process_input:
                    extra_input_settings_processLimit_on.draw(screen)
                    if extra_input_settings_processLimit_on.is_touched():
                        extra_input_settings_processLimit_on.set_alpha(200)
                    else:
                        extra_input_settings_processLimit_on.set_alpha(255)
                    if extra_input_settings_processLimit_on.is_pressed():
                        with open(file_path_settings_name_input_process_limit, "w", encoding="utf-8", errors="ignore") as file:
                            file.write("no")
            if extra_input_settings_x.is_touched():
                extra_input_settings_x.set_alpha(200)
            else:
                extra_input_settings_x.set_alpha(255)
            if extra_input_settings_x.is_pressed():
                show_input_screen = False
            manager.update(0)

        ##########ui screen
        if show_ui_screen:




            extra_user_insight_screen.draw(screen)
            extra_user_insight_x.draw(screen)

            manager_dago.draw_ui(screen)
            manager_dapart.draw_ui(screen)
            manager_wago.draw_ui(screen)
            manager_wapart.draw_ui(screen)
            manager_mago.draw_ui(screen)
            manager_mapart.draw_ui(screen)
            manager_yago.draw_ui(screen)
            manager_yapart.draw_ui(screen)

            if extra_user_insight_x.is_touched():
                extra_user_insight_x.set_alpha(200)
            else:
                extra_user_insight_x.set_alpha(255)
            if extra_user_insight_x.is_pressed():
                show_ui_screen = False
            manager_dago.update(0)
            manager_dapart.update(0)
            manager_wago.update(0)
            manager_wapart.update(0)
            manager_mago.update(0)
            manager_mapart.update(0)
            manager_yago.update(0)
            manager_yapart.update(0)


            ##########

        if sum([show_backup_screen, show_settings_screen, show_input_screen,show_ui_screen]) > 1:
            show_backup_screen = False
            show_settings_screen = False
            show_input_screen = False
            show_ui_screen = False




        attempt_quit_pygame()
        pygame.display.update()

        dt = clock.tick(120) / 1000

except (ModuleNotFoundError) as error:
    if error == "ModuleNotFoundError":
        print("The extension module PYGAME was not found. To install it, go to program files/python. Open python terminal and run pip install pygame.")
        print("Attempting to open the settings tweaker in python...")
        if supporting_text_ver: open_text_ver()
        else: print("This version does not support text tweaker.")





