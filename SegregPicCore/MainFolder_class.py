import os
import shutil
import uuid
from PIL import Image

from SegregPicCore import config
from SegregPicCore import console_param_parser as parser
from SegregPicCore import output_methods as output


class MainFolder:
    def __init__(self, main_path, folder_path):
        self.__folder_full_path = main_path + config.PATH_SEPARATOR + folder_path
        self.__folder_name = folder_path

        self.__unique_good_folder_name = ''
        self.__unique_good_counter = 0
        self.__unique_bad_folder_name = ''
        self.__unique_bad_counter = 0
        self.__unique_unrecognized_folder_name = ''
        self.__unique_unrecognized_counter = 0

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

        self.create_folders(self.__folder_full_path, [config.GOOD_FOLDER_NAME, config.BAD_FOLDER_NAME, config.UNRECOGNIZED_FOLDER_NAME])

        if self.__list_of_files:
            self.recognize_files_and_move()

        while self.__list_of_folders:
            current_folder = self.__list_of_folders.pop()

            output.print_output(" PROCESSING: " + current_folder, config.LOG_print_level)  # log

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
                    self.copy_file(file, config.GOOD_FOLDER_NAME)
                else:
                    im.close()
                    fp.close()
                    self.copy_file(file, config.BAD_FOLDER_NAME)
            except (IOError, OSError) as x:
                fp.close()

                output.print_output("     WARNING:", config.WARNING_print_level)  # warning
                output.print_output(str(x), config.WARNING_print_level)

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
                output.print_output("     moved " + image_path + " to " + full_dest_image, config.LOG_print_level)  # log
            except PermissionError as x:
                output.print_output("     WARNING:", config.WARNING_print_level)  # warning
                output.print_output(str(x), config.WARNING_print_level)
            except shutil.Error as x:
                string_exception = str(x)

                if string_exception[0] == 'D':  # stands for: Destination path ... already exists
                    output.print_output("     WARNING:", config.ERROR_print_level)  # warning
                    output.print_output(string_exception, config.ERROR_print_level)

                    if self.get_unique_foldername_from_dest_foldername(dest_folder) == '':
                        self.crate_unique_foldername(dest_folder)
                        full_dest_path += config.PATH_SEPARATOR + self.get_unique_foldername_from_dest_foldername(dest_folder)
                        shutil.move(image_path, full_dest_path)
                    else:
                        # TODO copy and find out or create next folder
                else:
                    output.print_output("     ERROR:", config.ERROR_print_level)  # error
                    output.print_output(string_exception, config.ERROR_print_level)

    def get_unique_foldername_from_dest_foldername(self, dest_foldername):
        if dest_foldername == config.GOOD_FOLDER_NAME:
            return self.__unique_good_folder_name
        elif dest_foldername == config.BAD_FOLDER_NAME:
            return self.__unique_bad_folder_name
        elif dest_foldername == config.UNRECOGNIZED_FOLDER_NAME:
            return self.__unique_unrecognized_folder_name

    def create_folders(self, path, folders_names):
        for folder_name in folders_names:
            try:
                self.create_empty_folder(path, folder_name)
            except config.FolderIsNotEmpty as x:
                output.print_output("     WARNING:", config.WARNING_print_level)  # warning
                output.print_output(str(x), config.WARNING_print_level)

    def create_empty_folder(self, path, folder_name):
        new_path = path + config.PATH_SEPARATOR + folder_name

        if not os.path.exists(new_path) and not os.listdir(path):
            os.makedirs(new_path)
        else:
            raise config.FolderIsNotEmpty('Folder' + new_path + " is not empty!")

    def crate_unique_foldername(self, destination_folder):
        destination_path = self.__folder_full_path + config.PATH_SEPARATOR + destination_folder

        unique_part = str(uuid.uuid4().hex)
        unique_destination_path = destination_path + config.PATH_SEPARATOR + unique_part

        while os.path.exists(unique_destination_path):
            unique_part = str(uuid.uuid4().hex)
            unique_destination_path = destination_path + config.PATH_SEPARATOR + unique_part

        os.makedirs(unique_destination_path)
        output.print_output('   Created unique folder: ' + unique_destination_path, config.LOG_print_level)

        if destination_folder == config.GOOD_FOLDER_NAME:
            self.__unique_good_folder_name = unique_part
        elif destination_folder == config.BAD_FOLDER_NAME:
            self.__unique_bad_folder_name = unique_part
        elif destination_folder == config.UNRECOGNIZED_FOLDER_NAME:
            self.__unique_unrecognized_folder_name = unique_part

    def get_filename_list_from_given_destination(self, destination):
        files_list = []

        for entry in os.scandir(destination):
            if not entry.is_file():
                files_list.append(entry)

        return files_list

    def get_destination_where_given_filename_is_unique(self, filename, destination, dest_folder):
        files_list = self.get_filename_list_from_given_destination(destination)

        if filename not in files_list:
            return ''

        for i in range(0, self.get_unique_counter_from_dest_foldername(dest_folder)):
            destination_to_check = destination + config.PATH_SEPARATOR + str(i)
            files_list = self.get_filename_list_from_given_destination(destination_to_check)

            if filename not in files_list:
                return str(i)

        #TODO CREATE FOLDER // add counter // return

    def get_unique_counter_from_dest_foldername(self, dest_foldername):
        if dest_foldername == config.GOOD_FOLDER_NAME:
            return self.__unique_good_counter
        elif dest_foldername == config.BAD_FOLDER_NAME:
            return self.__unique_bad_counter
        elif dest_foldername == config.UNRECOGNIZED_FOLDER_NAME:
            return self.__unique_unrecognized_counter_counter