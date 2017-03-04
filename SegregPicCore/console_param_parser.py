from SegregPicCore import config
import os
import re


def parse_command(commands):
    is_changed = False
    return_error_list = []

    i = 0
    while i < len(commands):
        if i + 1 < len(commands):
            if commands[i] == '-w':
                try:
                    val = int(commands[i + 1])
                    config.set_width(val)
                    is_changed = True
                except ValueError:
                    return_error_list.append("For " + commands[i] + " wrong argument: " + commands[i + 1] + " must be int")
                i += 2
            elif commands[i] == '-h':
                try:
                    val = int(commands[i + 1])
                    config.set_height(val)
                    is_changed = True
                except ValueError:
                    return_error_list.append("For " + commands[i] + " wrong argument: " + commands[i + 1] + " must be int")
                i += 2
            elif commands[i] == '-p':
                if os.path.exists(config.MAIN_PATH + config.PATH_SEPARATOR + commands[i + 1]):
                    config.set_path(config.MAIN_PATH + config.PATH_SEPARATOR + commands[i + 1])
                    is_changed = True
                else:
                    return_error_list.append("For " + commands[i] + " wrong path: " + commands[i + 1] + " does not exist")
                i += 2
            elif commands[i] == '-pa':
                if os.path.exists(commands[i + 1]):
                    config.set_path(commands[i + 1])
                    is_changed = True
                else:
                    return_error_list.append("For " + commands[i] + " wrong path: " + commands[i + 1] + " does not exist")
                i += 2
            elif commands[i] == '-g':
                config.set_good_folder_name(commands[i + 1])
                is_changed = True
                i += 2
            elif commands[i] == '-b':
                config.set_bad_folder_name(commands[i + 1])
                is_changed = True
                i += 2
            elif commands[i] == '-u':
                config.set_unrecognized_folder_name(commands[i + 1])
                is_changed = True
                i += 2
            elif commands[i] == '-info':
                if commands[i + 1] == 't':
                    config.set_print_option_for_info(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_print_option_for_info(False)
                    is_changed = True
                else:
                    return_error_list.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            elif commands[i] == '-warn':
                if commands[i + 1] == 't':
                    config.set_print_option_for_warning(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_print_option_for_warning(False)
                    is_changed = True
                else:
                    return_error_list.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            elif commands[i] == '-infof':
                if commands[i + 1] == 't':
                    config.set_info_save_to_file_permit(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_info_save_to_file_permit(False)
                    is_changed = True
                else:
                    return_error_list.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            elif commands[i] == '-succf':
                if commands[i + 1] == 't':
                    config.set_succ_save_to_file_permit(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_succ_save_to_file_permit(False)
                    is_changed = True
                else:
                    return_error_list.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            elif commands[i] == '-warnf':
                if commands[i + 1] == 't':
                    config.set_warning_save_to_file_permit(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_warning_save_to_file_permit(False)
                    is_changed = True
                else:
                    return_error_list.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            elif commands[i] == '-errf':
                if commands[i + 1] == 't':
                    config.set_error_save_to_file_permit(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_error_save_to_file_permit(False)
                    is_changed = True
                else:
                    return_error_list.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            elif commands[i] == '-statf':
                if commands[i + 1] == 't':
                    config.set_save_statistic_file_permit(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_save_statistic_file_permit(False)
                    is_changed = True
                else:
                    return_error_list.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            else:
                return_error_list.append("Unrecognized command: " + commands[i])
                i += 1
        else:
            if re.fullmatch("^-(w|h|g|b|u|pa|p|info|warn|infof|succf|warnf|errf|statf)$", commands[i]) is not None:
                return_error_list.append("No argument for: " + commands[i])
                break
            else:
                return_error_list.append("Unrecognized command: " + commands[i])
                break

    return [return_error_list, is_changed]


def get_prompt():
    command = input("> ").split(' ')

    if command[0] == 'q':
        return 0
    elif command[0] == 'start':
        return check_start_options()
    elif command[0] == 'help':
        return 2
    elif command[0] == 'config':
        return 3
    else:
        return parse_commands(command)


def check_start_options():
    if config.PATH == config.MAIN_PATH:
        print("Change Path to clean!")
        return -2

    return 1


def parse_commands(command_list):
    x = parse_command(command_list)
    error_list = x[0]
    is_changed = x[1]

    if not error_list:
        return 4
    else:
        print("Not every command or argument was correct: ")

        for error in error_list:
            print(error)

        print()

        if is_changed:
            return -1
        else:
            return -2
