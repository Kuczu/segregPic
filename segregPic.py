# TODO: v1.1 generate starting console parameters
# TODO: v1.1 add about info
# TODO: v1.1 add copy file with all folders from PATH to specified folder
# TODO: v1.1 clear empty cleared folders
# TODO: v1.1 delete only bad pics?

import os
import sys

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

    stats = {'good': {'size': 0, 'amount': 0},
             'bad': {'size': 0, 'amount': 0},
             'unrecognized': {'size': 0, 'amount': 0}}

    for item in folder_list:
        config.LOGGER.info_output("Start processing: " + item, False)
        list_of_folder_objects.append(MainFolder_class.MainFolder(config.PATH, item))
        list_of_folder_objects[-1].cleanify()
        list_of_folder_objects[-1].save_folder_stats()

        if config.WRITE_TO_FILE_ENABLE or config.PRINT_PERMITS[config.INFO_print_level]:
            stat = list_of_folder_objects[-1].get_folder_stats()

            stats['good']['size'] += stat['good']['size']
            stats['good']['amount'] += stat['good']['amount']

            stats['bad']['size'] += stat['bad']['size']
            stats['bad']['amount'] += stat['bad']['amount']

            stats['unrecognized']['size'] += stat['unrecognized']['size']
            stats['unrecognized']['amount'] += stat['unrecognized']['amount']

    message = ''
    if config.WRITE_TO_FILE_ENABLE:
        message += "\n\nMatched files: " + str(stats['good']['amount']) + '\n'
        message += "Matched files size: " + str(stats['good']['size'] // 1024) + 'kB \n'

        message += "Not Matched files: " + str(stats['bad']['amount']) + '\n'
        message += "Not Matched files size: " + str(stats['bad']['size'] // 1024) + 'kB \n'

        message += "Unrecognized files: " + str(stats['unrecognized']['amount']) + '\n'
        message += "Unrecognized files size: " + str(stats['unrecognized']['size'] // 1024) + 'kB \n'

        config.LOGGER.write_to_file(message, 0, False)

    print(message)


def confirm():
    print("ARE YOU SURE YOU WANT TO START?")
    print("Type 'y' to start something else to interrupt")

    command = input(">  ").split(' ')[0]

    if not command == "y":
        sys.exit("Interrupted")


def start():
    confirm()
    config.create_logger_instance()
    run_segreg()


def prepare():
    config.set_default_start_values(os.getcwd())
    config.set_log_filename()

    menu.display_basic_info()

    parser.parse_commands(config.START_COMMANDS)

    menu.display_menu()


def main():
    prepare()

    while True:
        command = parser.get_prompt()

        # add return variable as return code
        if command == 0:
            sys.exit()
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

    config.LOGGER.close_file()

if __name__ == "__main__":
    main()
