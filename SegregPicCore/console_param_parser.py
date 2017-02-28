from SegregPicCore import config
import os
import re


def parse_command(commands):
    is_changed = False
    return_error_array = []

    i = 0
    while i < len(commands):
        if i + 1 < len(commands):
            if commands[i] == '-w':
                try:
                    val = int(commands[i + 1])
                    config.set_width(val)
                    is_changed = True
                except ValueError:
                    return_error_array.append("For " + commands[i] + " wrong argument: " + commands[i + 1] + " must be int")
                i += 2
            elif commands[i] == '-h':
                try:
                    val = int(commands[i + 1])
                    config.set_height(val)
                    is_changed = True
                except ValueError:
                    return_error_array.append("For " + commands[i] + " wrong argument: " + commands[i + 1] + " must be int")
                i += 2
            elif commands[i] == '-p':
                if os.path.exists(config.MAIN_PATH + config.PATH_SEPARATOR + commands[i + 1]):
                    config.set_path(commands[i + 1])
                    is_changed = True
                else:
                    return_error_array.append("For " + commands[i] + " wrong path: " + commands[i + 1] + " does not exist")
                i += 2
            elif commands[i] == '-pa':
                if os.path.exists(commands[i + 1]):
                    config.set_path(commands[i + 1])
                    is_changed = True
                else:
                    return_error_array.append("For " + commands[i] + " wrong path: " + commands[i + 1] + " does not exist")
                i += 2
            elif commands[i] == '-g':
                config.set_good_folder_name(commands[i + 1])
                is_changed = True
                i += 2
            elif commands[i] == '-b':
                config.set_bad_folder_name(commands[i + 1])
                is_changed = True
                i += 2
            elif commands[i] == '-b':
                config.set_unrecognized_folder_name(commands[i + 1])
                is_changed = True
                i += 2
            elif commands[i] == '-log':
                if commands[i + 1] == 't':
                    config.set_print_option_for_log(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_print_option_for_log(False)
                    is_changed = True
                else:
                    return_error_array.append(
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
                    return_error_array.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            elif commands[i] == '-sv':
                if commands[i + 1] == 't':
                    config.set_print_option_for_warning(True)
                    is_changed = True
                elif commands[i + 1] == 'f':
                    config.set_print_option_for_warning(False)
                    is_changed = True
                else:
                    return_error_array.append(
                        "For " + commands[i] + " must be 't' or 'f'")
                i += 2
            else:
                return_error_array.append("Unrecognized command: " + commands[i])
                i += 1
        else:
            if re.fullmatch("^-(w|h|g|b|u|pa|p)$", commands[i]) is not None:
                return_error_array.append("No argument for: " + commands[i])
                break
            else:
                return_error_array.append("Unrecognized command: " + commands[i])
                break

    return [return_error_array, is_changed]
