import subprocess
from importlib.metadata import PackageNotFoundError
from DATA.ai_renderer import call_file_path
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


def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except (ModuleNotFoundError, PermissionError, PackageNotFoundError, TimeoutError, MemoryError) as error:
        print(f"An error occurred while installing {package}: {error}")

def print_verti_list(list):
    for item in list: print(item)

TOS = [
    "By using this application you agree to the Terms of Service listed in the project files.",
    "If you cannot find it, install a new version."
] #terms of service
print_verti_list(TOS)

print("-------SulfurAI Settings requires the extension PYGAME.-------")
import os  ##Global and Importing functions and variables
import time
try:
    import pygame
except ImportError:
    install("pygame")
import sys

supporting_text_ver = False

def attempt_quit_pygame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close the game
            sys.exit()

def open_text_ver():
    pass # add text ver



verify = ["-------Checking for pygame.","-------Verifying..."]
print_verti_list(verify)
try:
    temp_init_pygame = 0
    pygame.init()
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720
    app_open = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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



    ####################SPRITES
    backdrop = pygame.image.load("DATA/settings/images/backdrop.png")
    backdrop = pygame.transform.smoothscale(backdrop,(SCREEN_WIDTH+ 42,SCREEN_HEIGHT + 25))

    mouseHitbox = pygame.image.load("DATA/settings/images/mousehitbox.jpeg")
    mouseHitbox.set_alpha(0)
    show_settings_screen = False
    show_backup_screen = False

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

        if show_backup_screen and show_settings_screen:
            show_backup_screen = False
            show_settings_screen = False


        attempt_quit_pygame()
        pygame.display.update()
        dt = clock.tick(120) / 1000

except (ModuleNotFoundError) as error:
    if error == "ModuleNotFoundError":
        print("The extension module PYGAME was not found. To install it, go to program files/python. Open python terminal and run pip install pygame.")
        print("Attempting to open the settings tweaker in python...")
        if supporting_text_ver: open_text_ver()
        else: print("This version does not support text tweaker.")


