import os
from PIL import Image

from SegregPicCore import SpecificFolder_class as SpecificFolder
from SegregPicCore import config
from SegregPicCore import output_methods as output


class MainFolder:
    def __init__(self, main_path, folder_name):
        self.__folder_full_path = main_path + config.PATH_SEPARATOR + folder_name
        self.__folder_name = folder_name

        self.__good_folder = SpecificFolder.SpecificFolder(self.__folder_full_path, config.GOOD_FOLDER_NAME)
        self.__bad_folder = SpecificFolder.SpecificFolder(self.__folder_full_path, config.BAD_FOLDER_NAME)
        self.__unrecognized_folder = SpecificFolder.SpecificFolder(self.__folder_full_path, config.UNRECOGNIZED_FOLDER_NAME)

        self.__list_of_folders = []
        self.__list_of_files = []

    def cleanify(self):
        self.get_folders_and_files_list(self.__folder_full_path)

        if self.__list_of_files:
            self.recognize_files_and_move()

        while self.__list_of_folders:
            current_folder = self.__list_of_folders.pop()

            output.print_output(" PROCESSING: " + current_folder, config.INFO_print_level, False)  # log

            self.get_folders_and_files_list(current_folder)

            if self.__list_of_files:
                self.recognize_files_and_move()

    def get_folders_and_files_list(self, path):
        for entry in os.scandir(path):
            if not entry.is_file():
                if not (entry.name == config.GOOD_FOLDER_NAME or
                        entry.name == config.BAD_FOLDER_NAME or
                        entry.name == config.UNRECOGNIZED_FOLDER_NAME):
                    self.__list_of_folders.append(entry.path)

            if entry.is_file():
                self.__list_of_files.append(entry.path)

    def recognize_files_and_move(self):
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

                # output.print_output("     WARNING:", config.WARNING_print_level)  # warning
                output.print_output(str(x), config.WARNING_print_level)

                self.__unrecognized_folder.move_file(file)
                pass

        self.__list_of_files.clear()

    # def get_filename_list_from_given_destination(self, destination):
    #     files_list = []
    #
    #     for entry in os.scandir(destination):
    #         if not entry.is_file():
    #             files_list.append(entry)
    #
    #     return files_list
