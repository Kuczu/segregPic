import os
import shutil
from PIL import Image

from SegregPicCore import config
from SegregPicCore import output_methods as output


class MainFolder:
    def __init__(self, main_path, folder_path):
        self.__folder_full_path = main_path + config.PATH_SEPARATOR + folder_path
        self.__folder_name = folder_path

        self.__good_amount = 0
        self.__good_size = 0

        self.__bad_amount = 0
        self.__bad_size = 0

        self.__unrecognized_amount = 0
        self.__unrecognized_size = 0

        self.__list_of_folders = []
        self.__list_of_files = []

    def cleanify(self):
        self.get_folders_and_files_list(self.__folder_full_path)

        # self.create_empty_folder(self.__folder_full_path, "good")
        # self.create_empty_folder(self.__folder_full_path, "bad")
        # self.create_empty_folder(self.__folder_full_path, "unrecognized")

        self.create_empty_folder(self.__folder_full_path, config.GOOD_FOLDER_NAME)
        self.create_empty_folder(self.__folder_full_path, config.BAD_FOLDER_NAME)
        self.create_empty_folder(self.__folder_full_path, config.UNRECOGNIZED_FOLDER_NAME)

        if self.__list_of_files:
            self.recognize_files_and_move()

        while self.__list_of_folders:
            current_folder = self.__list_of_folders.pop()

            # print(" PROCESSING: " + current_folder)
            output.print_output(" PROCESSING: " + current_folder, 0)  # log

            self.get_folders_and_files_list(current_folder)

            if self.__list_of_files:
                self.recognize_files_and_move()

    def get_folders_and_files_list(self, path):
        for entry in os.scandir(path):
            if not entry.is_file():
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
                    self.copy_file(file, config.GOOD_FOLDER_NAME)
                else:
                    im.close()
                    fp.close()
                    self.copy_file(file, config.BAD_FOLDER_NAME)
            except (IOError, OSError) as x:
                fp.close()

                # print("     WARNING:")
                # print(x)
                output.print_output("     WARNING:", 2)  # warning
                output.print_output(str(x), 2)

                self.copy_file(file, config.UNRECOGNIZED_FOLDER_NAME)
                pass

        self.__list_of_files.clear()

    def copy_file(self, image_path, dest_folder):
        image_name = image_path.split(config.PATH_SEPARATOR)[-1]
        full_dest_path = self.__folder_full_path + config.PATH_SEPARATOR + dest_folder
        full_dest_image = full_dest_path + config.PATH_SEPARATOR + image_name

        if not image_path == full_dest_image:
            try:
                shutil.move(image_path, full_dest_path)
                # print("     moved " + image_path + " to " + full_dest_image)
                output.print_output("     moved " + image_path + " to " + full_dest_image, 0)  # log
            except PermissionError as x:
                # print("     WARNING:")
                # print(x)
                output.print_output("     WARNING:", 2)  # warning
                output.print_output(str(x), 2)
            except shutil.Error as x:
                # print("     ERROR:")
                # print(x)
                output.print_output("     ERROR:", 3)  # error
                output.print_output(str(x), 3)

    def create_empty_folder(self, path, folder_name):
        new_path = path + config.PATH_SEPARATOR + folder_name

        if not os.path.exists(new_path):
            os.makedirs(new_path)
