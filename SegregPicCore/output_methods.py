from SegregPicCore import config

# TODO implement logger

# ##########################################

# INFO_print_level = 0
# SUCCESS_print_level = 1
# WARNING_print_level = 2
# ERROR_print_level = 3
PRINT_PROLOG = [
    "",
    "   SUCCESS!:",
    "   WARNING:",
    "   ERROR:"
]


def print_output(text, level, print_prologue=True):

    if config.PRINT_PERMITS[level]:
        if print_prologue:
            print(config.PRINT_OPTIONS[level] + PRINT_PROLOG[level])

        try:
            print(config.PRINT_OPTIONS[level] + text)
        except (TypeError, UnicodeEncodeError):
            config.PRINT_OPTIONS[0]  # reset
            textp = text.encode("UTF-8")
            print(textp)

        config.PRINT_OPTIONS[0]  # reset

    log_to_file(text, level, print_prologue)


def log_to_file(text, level, print_prologue):
    if config.WRITE_TO_FILE_PERMITS[level]:

        print('LOGGED TO FILE')

# ##########################################

# SINGLETON
class LoggerMetaclass(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(LoggerMetaclass, cls).__call__(*args, **kwargs)

        return cls.instance


class Logger(metaclass=LoggerMetaclass):
    def __init__(self, log_file_full_path, log_file_name):
        self.log_file_full_path = log_file_full_path
        self.log_file_name = log_file_name

        # self.file_handler = self.create_log_file(log_file_full_path, log_file_name)
        self.file_handler = None

        self.is_file_already_created = False

        self.PRINT_PROLOG = [
                                "",
                                "   SUCCESS!:",
                                "   WARNING:",
                                "   ERROR:"
                            ]

    def create_log_file(self):
        if self.is_file_already_created:
            raise FileIsAlreadyCreatedError("Log file is already created!")

        file = open(self.log_file_full_path + config.PATH_SEPARATOR + self.log_file_name, 'x')

        self.is_file_already_created = True

        return file

    def info_output(self, message, print_prologue=True):
        level = config.INFO_print_level
        self.output_method(message, level, print_prologue)

    def success_output(self, message, print_prologue=True):
        level = config.SUCCESS_print_level
        self.output_method(message, level, print_prologue)

    def warning_output(self, message, print_prologue=True):
        level = config.WARNING_print_level
        self.output_method(message, level, print_prologue)

    def error_output(self, message, print_prologue=True):
        level = config.ERROR_print_level
        self.output_method(message, level, print_prologue)

    def output_method(self, message, level, print_prologue):
        if config.PRINT_PERMITS[level]:
            self.print_stdout(message, level, print_prologue)

        if config.WRITE_TO_FILE_PERMITS[level]:
            self.write_to_file(message, level, print_prologue)

    def print_stdout(self, message, level, print_prologue):
        if print_prologue:
            print(config.PRINT_OPTIONS[level] + self.PRINT_PROLOG[level])

        try:
            print(config.PRINT_OPTIONS[level] + message)
        except (TypeError, UnicodeEncodeError):
            # config.PRINT_OPTIONS[0]  # reset
            textp = message.encode("UTF-8")
            print(textp)

        config.PRINT_OPTIONS[0]  # reset

    def write_to_file(self, message, level, print_prologue):
        if print_prologue:
            self.file_handler.write(self.PRINT_PROLOG[level] + '\n')

        self.file_handler.write(message + '\n')

    def close_file(self):
        self.file_handler.close()


class FileIsAlreadyCreatedError(Exception):
    pass
