# TODO: output colors
# TODO: summary info
# TODO: save summary info
# TODO: warning before start
# TODO: add about

import os

from SegregPicCore import config
from SegregPicCore import menu
from SegregPicCore import MainFolder_class


def get_folders_list(path):
    folder_list = []

    for entry in os.scandir(path):
        if not entry.is_file():
            folder_list.append(entry.name)

    return folder_list


def start():
    folder_list = get_folders_list(config.PATH)

    list_of_folder_objects = []

    for item in folder_list:
        print("Start processing: " + item)
        list_of_folder_objects.append(MainFolder_class.MainFolder(config.PATH, item))
        list_of_folder_objects[-1].cleanify()


def main():
    config.set_default_start_values(os.getcwd() + "\\test")

    menu.parse_commands(config.START_COMMANDS)

    menu.display_menu()

    while not config.IS_INTERRUPTED:
        command = menu.get_prompt()

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
            print("configuration change was successful!")
            menu.display_config()
            continue
        elif command == -1:
            print("configuration PARTLY change was successful!")
            menu.display_config()
            continue
        elif command == -2:
            menu.display_config()
            continue

        break


if __name__ == "__main__":
    main()
