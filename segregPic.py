# TODO: warning before start
# TODO: add about

import os

from SegregPicCore import config
from SegregPicCore import menu
from SegregPicCore import MainFolder_class
from SegregPicCore import console_param_parser as parser


def get_folders_list(path):
    folder_list = []

    for entry in os.scandir(path):
        if not entry.is_file():
            folder_list.append(entry.name)

    return folder_list


def run_segreg():
    folder_list = get_folders_list(config.PATH)

    list_of_folder_objects = []

    for item in folder_list:
        print("Start processing: " + item)  # TODO make log
        list_of_folder_objects.append(MainFolder_class.MainFolder(config.PATH, item))
        list_of_folder_objects[-1].cleanify()


def start():
    config.create_logger_instance()
    run_segreg()


def prepare():
    config.set_default_start_values(os.getcwd() + "\\test")
    config.set_log_filename()

    menu.display_basic_info()

    parser.parse_commands(config.START_COMMANDS)

    menu.display_menu()


def main():
    prepare()

    while not config.IS_INTERRUPTED:
        command = parser.get_prompt()

        # add return variable as return code
        if command == 0:
            break
        elif command == 1:
            start()
        elif command == 2:
            menu.display_help()
            continue
        elif command == 3:
            menu.display_config()
            continue
        elif command == 4:
            print("Configuration change was successful!")
            menu.display_config()
            continue
        elif command == -1:
            print("Configuration PARTLY change was successful!")
            menu.display_config()
            continue
        elif command == -2:
            menu.display_config()
            continue

        break


if __name__ == "__main__":
    main()
