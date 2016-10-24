__AUTHOR__ = "Kuczu https://github.com/Kuczu"
__VERSION__ = "0.1 BETA"
__LICENSE__ = "MIT"

WIDTH = ""
HEIGHT = ""

GOOD_FOLDER_NAME = ""
BAD_FOLDER_NAME = ""
UNRECOGNIZED_FOLDER_NAME = ""

PATH_SEPARATOR = ""
PATH = ""
MAIN_PATH = ""


def set_default_start_values(path):
    global WIDTH, HEIGHT, PATH, MAIN_PATH, PATH_SEPARATOR, GOOD_FOLDER_NAME, BAD_FOLDER_NAME, UNRECOGNIZED_FOLDER_NAME
    WIDTH = 1920
    HEIGHT = 1080

    GOOD_FOLDER_NAME = "good"
    BAD_FOLDER_NAME = "bad"
    UNRECOGNIZED_FOLDER_NAME = "unrecognized"

    MAIN_PATH = path
    PATH = path

    PATH_SEPARATOR = "\\"


def set_width(width):
    global WIDTH
    WIDTH = width


def set_height(height):
    global HEIGHT
    HEIGHT = height


def set_path(path):
    global PATH
    PATH = path


def set_good_folder_name(name):
    global GOOD_FOLDER_NAME
    GOOD_FOLDER_NAME = name


def set_bad_folder_name(name):
    global BAD_FOLDER_NAME
    BAD_FOLDER_NAME = name


def set_unrecognized_folder_name(name):
    global UNRECOGNIZED_FOLDER_NAME
    UNRECOGNIZED_FOLDER_NAME = name
