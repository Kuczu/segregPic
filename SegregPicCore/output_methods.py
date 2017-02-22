from SegregPicCore import config


# 0 - log
# 1 - success
# 2 - warning
# 3 - error
def print_output(text, level):
    if config.PRINT_PERMITS[level]:
        try:
            print(config.PRINT_OPTIONS[level] + text)
            config.PRINT_OPTIONS[0]  # reset
        except (TypeError, UnicodeEncodeError):
            config.PRINT_OPTIONS[0]  # reset
            textp = text.encode("UTF-8")
            print(textp)

    # if config.LOG_TO_FILE_PERMITS[level]:
    #   log_to_file(text)


def log_to_file(text):
    print('LOGGED TO FILE')
    # TODO
