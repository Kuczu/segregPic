import os
import sys
import uuid
import datetime

from SegregPicCore import output_methods

from colorama import init
from colorama import Fore, Back, Style
init()  # colorama init

__AUTHOR__ = "Kuczu https://github.com/Kuczu"
__VERSION__ = "1.0"
__LICENSE__ = "MIT"

WIDTH = ""
HEIGHT = ""

GOOD_FOLDER_NAME = ""
BAD_FOLDER_NAME = ""
UNRECOGNIZED_FOLDER_NAME = ""

LOG_FILENAME = ""

PATH_SEPARATOR = ""
PATH = ""
MAIN_PATH = ""

INFO_print_level = 0
SUCCESS_print_level = 1
WARNING_print_level = 2
ERROR_print_level = 3

PRINT_PERMITS = [True, True, True, True]
PRINT_OPTIONS = [Style.RESET_ALL, Fore.GREEN, Fore.YELLOW, Fore.RED]

WRITE_TO_FILE_ENABLE = True
WRITE_TO_FILE_PERMITS = [True, True, True, True]

WRITE_SUMMARY_TO_FILE = True

START_COMMANDS = sys.argv[1:]

LOGGER = None


def set_default_start_values(path):
    global WIDTH, HEIGHT, PATH, MAIN_PATH, PATH_SEPARATOR, GOOD_FOLDER_NAME, BAD_FOLDER_NAME, UNRECOGNIZED_FOLDER_NAME, \
        WRITE_TO_FILE_ENABLE, PRINT_PERMITS, WRITE_TO_FILE_PERMITS
    WIDTH = 1920
    HEIGHT = 1080

    GOOD_FOLDER_NAME = "good"
    BAD_FOLDER_NAME = "bad"
    UNRECOGNIZED_FOLDER_NAME = "unrecognized"

    MAIN_PATH = path
    PATH = path

    PATH_SEPARATOR = "\\"

    PRINT_PERMITS = [True, True, True, True]

    WRITE_TO_FILE_ENABLE = True
    WRITE_TO_FILE_PERMITS = [True, True, True, True]


def create_logger_instance():
    global LOGGER
    LOGGER = output_methods.Logger(PATH, LOG_FILENAME)


def set_width(width):
    global WIDTH
    WIDTH = width


def set_height(height):
    global HEIGHT
    HEIGHT = height


def set_path(path):
    global PATH
    PATH = path

    set_log_filename()


def set_good_folder_name(name):
    global GOOD_FOLDER_NAME
    GOOD_FOLDER_NAME = name


def set_bad_folder_name(name):
    global BAD_FOLDER_NAME
    BAD_FOLDER_NAME = name


def set_unrecognized_folder_name(name):
    global UNRECOGNIZED_FOLDER_NAME
    UNRECOGNIZED_FOLDER_NAME = name


def set_print_option_for_info(value):
    global PRINT_PERMITS
    PRINT_PERMITS[0] = value


def set_print_option_for_warning(value):
    global PRINT_PERMITS
    PRINT_PERMITS[2] = value


def set_info_save_to_file_permit(value):
    global WRITE_TO_FILE_PERMITS
    WRITE_TO_FILE_PERMITS[0] = value
    _check_save_to_file_enable()


def set_succ_save_to_file_permit(value):
    global WRITE_TO_FILE_PERMITS
    WRITE_TO_FILE_PERMITS[1] = value
    _check_save_to_file_enable()


def set_warning_save_to_file_permit(value):
    global WRITE_TO_FILE_PERMITS
    WRITE_TO_FILE_PERMITS[2] = value
    _check_save_to_file_enable()


def set_error_save_to_file_permit(value):
    global WRITE_TO_FILE_PERMITS
    WRITE_TO_FILE_PERMITS[3] = value
    _check_save_to_file_enable()


def _check_save_to_file_enable():
    global WRITE_TO_FILE_ENABLE
    WRITE_TO_FILE_ENABLE = True in WRITE_TO_FILE_PERMITS


def set_save_statistic_file_permit(value):
    global WRITE_SUMMARY_TO_FILE
    WRITE_SUMMARY_TO_FILE = value


def _generate_unique_log_filename():
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = "SegregPicSummary_" + date
    unique_part = ""
    extension = ".txt"

    full_destination = PATH + PATH_SEPARATOR + filename

    unique_destination_path = full_destination + extension

    while os.path.exists(unique_destination_path):
        unique_part = "__" + str(uuid.uuid4().hex)
        unique_destination_path = full_destination + unique_part + extension

    return filename + unique_part + extension


def set_log_filename():
    global LOG_FILENAME
    LOG_FILENAME = _generate_unique_log_filename()
