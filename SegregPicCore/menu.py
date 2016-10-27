from SegregPicCore import config
from SegregPicCore import console_param_parser as parser


def display_menu():
    print("Author: " + config.__AUTHOR__)
    print("Version: " + config.__VERSION__)
    print("License: " + config.__LICENSE__ + '\n')
    display_config()
    display_helpers()


def display_config():
    print("Current config: ")
    print("  Path to clean: " + config.PATH)
    print("  Picture width: " + str(config.WIDTH))
    print("  Picture height: " + str(config.HEIGHT))
    print("  Folder for matching pics: " + config.PATH_SEPARATOR + config.GOOD_FOLDER_NAME)
    print("             not matching pics: " + config.PATH_SEPARATOR + config.BAD_FOLDER_NAME)
    print("             unrecognized files: " + config.PATH_SEPARATOR + config.UNRECOGNIZED_FOLDER_NAME)
    print("  Print logs: " + str(config.PRINT_PERMITS[0]))
    print("  Print warnings: " + str(config.PRINT_PERMITS[2]))
    print("  Save all logs into file: " + str(config.LOG_TO_FILE_PERMITS[0]) + "\n")


def display_helpers():
    print("Type 'help' to list commands")
    print("Type 'config' to list commands")
    print("Type 'start' to start cleaning")
    print("Type 'q' to exit\n")


def display_help():
    print("To change pics size use: '-w (int)VALUE' to change width")
    print("                         '-h (int)VALUE' to change height")
    print("To change path use: '-p (relative)PATH' to change relative path (relative of segregPic.py location)")
    print("                    '-pa (absolute)PATH' to change absolute path")
    print("To change folders names use: '-g FOLDER_NAME' to change name for matching pics folder")
    print("                             '-b FOLDER_NAME' to change name for not matching pics folder")
    print("                             '-u FOLDER_NAME' to change name for unrecognized files folder")
    print("To change if print logs: '-log t' for set true, '-log t' for set false")
    print("To change if print warnings: '-warn t' for set true, '-warn t' for set false")
    print("To change if save all logs into file: '-sv t' for set true, '-sv t' for set false")
    display_helpers()


def get_prompt():
    command = input("> ")

    if command == 'q':
        return 0
    elif command == 'start':
        return 1
    elif command == 'help':
        return 2
    elif command == 'config':
        return 3
    else:
        error_list = parser.parse_command(command)[0]
        is_changed = parser.parse_command(command)[1]

        if not error_list:
            return 4
        else:
            print("Not every command was correct: ")

            for error in error_list:
                print(error)

            print()

            if is_changed:
                return -1
            else:
                return -2
