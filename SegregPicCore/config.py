import sys

from colorama import init
from colorama import Fore, Back, Style
init()

__AUTHOR__ = "Kuczu https://github.com/Kuczu"
__VERSION__ = "0.1 BETA"
__LICENSE__ = "MIT"

IS_INTERRUPTED = False

WIDTH = ""
HEIGHT = ""

GOOD_FOLDER_NAME = ""
BAD_FOLDER_NAME = ""
UNRECOGNIZED_FOLDER_NAME = ""

PATH_SEPARATOR = ""
PATH = ""
MAIN_PATH = ""

# 0 - log
# 1 - success - unchangeable!
# 2 - warning
# 3 - error - unchangeable!
LOG_print_level = 0
SUCCESS_print_level = 1
WARNING_print_level = 2
ERROR_print_level = 3

PRINT_PERMITS = [True, True, True, True]
PRINT_OPTIONS = [Style.RESET_ALL, Fore.GREEN, Fore.YELLOW, Fore.RED]
LOG_TO_FILE_PERMITS = [True, True, True, True]

HANDLER_FILE_WITH_LOGS = ''
HANDLER_FILE_WITH_SUMMARY = ''

START_COMMANDS = sys.argv[1:]


def set_default_start_values(path):
    global WIDTH, HEIGHT, PATH, MAIN_PATH, PATH_SEPARATOR, GOOD_FOLDER_NAME, BAD_FOLDER_NAME, UNRECOGNIZED_FOLDER_NAME, \
        PRINT_PERMITS, LOG_TO_FILE_PERMITS
    WIDTH = 1920
    HEIGHT = 1080

    GOOD_FOLDER_NAME = "good"
    BAD_FOLDER_NAME = "bad"
    UNRECOGNIZED_FOLDER_NAME = "unrecognized"

    MAIN_PATH = path
    PATH = path

    PATH_SEPARATOR = "\\"

    PRINT_PERMITS = [True, True, True, True]
    LOG_TO_FILE_PERMITS = [True, True, True, True]


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


def set_print_option_for_log(value):
    global PRINT_PERMITS
    PRINT_PERMITS[0] = value


def set_print_option_for_warning(value):
    global PRINT_PERMITS
    PRINT_PERMITS[2] = value


def set_log_into_file_permits(value):
    global LOG_TO_FILE_PERMITS
    for i in range(len(LOG_TO_FILE_PERMITS)):
        LOG_TO_FILE_PERMITS[i] = value


def open_file_with_logs():
    print('log')
    # TODO


def open_file_with_summary():
    print('summary')
    # TODO


class FolderIsNotEmpty(Exception):
    pass
