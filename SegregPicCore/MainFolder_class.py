import os
import datetime

from PIL import Image

from SegregPicCore import SpecificFolder_class as SpecificFolder
from SegregPicCore import config


class MainFolder:
    def __init__(self, main_path, folder_name):
        self.__folder_full_path = main_path + config.PATH_SEPARATOR + folder_name
        self.__folder_name = folder_name

        self.__good_folder = SpecificFolder.SpecificFolder(self.__folder_full_path, config.GOOD_FOLDER_NAME)
        self.__bad_folder = SpecificFolder.SpecificFolder(self.__folder_full_path, config.BAD_FOLDER_NAME)
        self.__unrecognized_folder = SpecificFolder.SpecificFolder(self.__folder_full_path, config.UNRECOGNIZED_FOLDER_NAME)

        self.__list_of_folders = []
        self.__list_of_files = []

        self.__folder_stats = {}

    def cleanify(self):
        self.__get_folders_and_files_list(self.__folder_full_path)

        if self.__list_of_files:
            self.__recognize_files_and_move()

        while self.__list_of_folders:
            current_folder = self.__list_of_folders.pop()

            config.LOGGER.info_output(" PROCESSING: " + current_folder, False)

            self.__get_folders_and_files_list(current_folder)

            if self.__list_of_files:
                self.__recognize_files_and_move()

    def __get_folders_and_files_list(self, path):
        for entry in os.scandir(path):
            if not entry.is_file():
                if not (entry.name == config.GOOD_FOLDER_NAME or
                        entry.name == config.BAD_FOLDER_NAME or
                        entry.name == config.UNRECOGNIZED_FOLDER_NAME):
                    self.__list_of_folders.append(entry.path)

            if entry.is_file():
                self.__list_of_files.append(entry.path)

    def __recognize_files_and_move(self):
        for file in self.__list_of_files:
            fp = open(file, "rb")

            try:
                im = Image.open(fp)

                if im.size[0] >= config.WIDTH and im.size[1] >= config.HEIGHT:
                    im.close()
                    fp.close()
                    self.__good_folder.move_file(file)
                else:
                    im.close()
                    fp.close()
                    self.__bad_folder.move_file(file)
            except (IOError, OSError) as x:
                fp.close()

                config.LOGGER.warning_output(str(x))

                self.__unrecognized_folder.move_file(file)
                pass

        self.__list_of_files.clear()

    def save_folder_stats(self):
        if not config.WRITE_SUMMARY_TO_FILE:
            return

        file_name = "SegregPicSummary.txt"
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        file = open(self.__folder_full_path + config.PATH_SEPARATOR + file_name, 'x')

        message = "Processed date: " + date + '\n\n'

        stats = self.__good_folder.get_folder_stats()
        self.__folder_stats.update({'good': stats})

        message += "Matched files: " + str(stats['amount']) + '\n'
        message += "Matched files size: " + str(stats['size'] // 1024) + 'kB \n'

        stats = self.__bad_folder.get_folder_stats()
        self.__folder_stats.update({'bad': stats})

        message += "Not matched files: " + str(stats['amount']) + '\n'
        message += "Not matched files size: " + str(stats['size'] // 1024) + 'kB\n'

        stats = self.__unrecognized_folder.get_folder_stats()
        self.__folder_stats.update({'unrecognized': stats})

        message += "Unrecognized files: " + str(stats['amount']) + '\n'
        message += "Unrecognized files size: " + str(stats['size'] // 1024) + 'kB \n'

        file.write(message)

    def get_folder_stats(self):
        return self.__folder_stats
