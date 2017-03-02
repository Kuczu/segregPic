from SegregPicCore import config


def display_basic_info():
    print("Author: " + config.__AUTHOR__)
    print("Version: " + config.__VERSION__)
    print("License: " + config.__LICENSE__ + '\n')


def display_menu():
    display_config()
    display_helpers()


def display_config():
    print("Current config: ")
    print("  Path to clean: " + config.PATH)
    print("  Picture width: " + str(config.WIDTH))
    print("  Picture height: " + str(config.HEIGHT))
    print("  Folder for matching pics: " + config.PATH_SEPARATOR + config.GOOD_FOLDER_NAME)
    print("         not matching pics: " + config.PATH_SEPARATOR + config.BAD_FOLDER_NAME)
    print("        unrecognized files: " + config.PATH_SEPARATOR + config.UNRECOGNIZED_FOLDER_NAME + "\n")
    print("  Print info: " + str(config.PRINT_PERMITS[config.INFO_print_level]))
    print("    warnings: " + str(config.PRINT_PERMITS[config.WARNING_print_level]))
    display_file_section()
    display_summary_file_section()


def display_file_section():
    print()

    print("  Save logs into file: ")
    print("                 info: " + str(config.WRITE_TO_FILE_PERMITS[config.INFO_print_level]))
    print("              success: " + str(config.WRITE_TO_FILE_PERMITS[config.SUCCESS_print_level]))
    print("             warnings: " + str(config.WRITE_TO_FILE_PERMITS[config.WARNING_print_level]))
    print("               errors: " + str(config.WRITE_TO_FILE_PERMITS[config.ERROR_print_level]))

    if config.WRITE_TO_FILE_ENABLE:
        print("  log filename: " + config.LOG_FILENAME)
    else:
        print("  log filename: you have disabled logging to file")


def display_summary_file_section():
    print()
    print("  Save statistics file in each cleaned folder: " + str(config.WRITE_SUMMARY_TO_FILE))
    print()


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
    print("To change folders names usage: '-g FOLDER_NAME' to change name for matching pics folder")
    print("                             '-b FOLDER_NAME' to change name for not matching pics folder")
    print("                             '-u FOLDER_NAME' to change name for unrecognized files folder")
    print("To change print info: '-info t' to set true, '-info f' to set false")
    print("To change print warnings: '-warn t' to set true, '-warn f' to set false")
    print("To change saving all info into log file: '-infof t' to set true, '-infof f' to set false")
    print("To change saving all success into log file: '-succf t' to set true, '-succf f' to set false")
    print("To change saving all warnings into log file: '-warnf t' to set true, '-warnf f' to set false")
    print("To change saving all errors into log file: '-errf t' to set true, '-errf f' to set false")
    print("To change saving statistics file in each cleaned folder: '-statf t' to set true, '-statf f' to set false")
    display_helpers()
