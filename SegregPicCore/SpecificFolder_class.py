import os
import shutil
import uuid

from SegregPicCore import config
from SegregPicCore import output_methods as output


class SpecificFolder:
    def __init__(self, folder_path, specific_folder_name):
        self.__folder_full_path = folder_path + config.PATH_SEPARATOR + specific_folder_name
        self.__folder_name = specific_folder_name

        self.__unique_subfolder_name = ''
        self.__unique_subfolder_counter = 0

        self.__folder_size_bytes = 0
        self.__folder_amount = 0

        self.create_itself_folder()

    def create_itself_folder(self):
        try:
            os.makedirs(self.__folder_full_path)
        except OSError:
            config.LOGGER.warning_output("Folder: " + self.__folder_name + " already exists!")

    def move_file(self, image_path, image_destination = ''):
        try:
            image_destin = self.__folder_full_path + config.PATH_SEPARATOR + image_destination
            shutil.move(image_path, image_destin)
            self.update_folder_status(image_destin)

            config.LOGGER.info_output("     moved " + image_path + " to " + image_destin, False)

        except PermissionError as x:
            output.print_output(str(x), config.WARNING_print_level)
        except shutil.Error as x:
            string_exception = str(x)

            if string_exception[0] == 'D':  # stands for: Destination path ... already exists
                config.LOGGER.warning_output(string_exception)

                image_name = image_path.split(config.PATH_SEPARATOR)[-1]
                image_dest = self.get_path_to_unique_where_to_copy(image_name)
                self.move_file(image_path, image_dest)
            else:
                config.LOGGER.error_output(string_exception)

    def update_folder_status(self, image_full_path):
        # can raise OSError exception
        self.__folder_size_bytes += os.path.getsize(image_full_path)
        self.__folder_amount += 1

    def get_path_to_unique_where_to_copy(self, image_name):
        if self.__unique_subfolder_name == '':
            self.crate_unique_foldername()
            return self.__unique_subfolder_name
        elif not self.is_file_exists_in_given_folder(image_name, self.__unique_subfolder_name):
            return self.__unique_subfolder_name
        else:
            folder_name = self.get_subfolder_name_in_unique_where_to_copy(image_name)

            if folder_name == False:
                self.create_next_subfolder_in_unique()
                return self.__unique_subfolder_name + config.PATH_SEPARATOR + str(self.__unique_subfolder_counter - 1)
            else:
                return self.__unique_subfolder_name + config.PATH_SEPARATOR + folder_name

    def get_subfolder_name_in_unique_where_to_copy(self, image_name):
        for i in range(0, self.__unique_subfolder_counter):
            if not self.is_file_exists_in_given_folder(image_name, self.__unique_subfolder_name + config.PATH_SEPARATOR + str(i)):
                return str(i)

        return False

    def is_file_exists_in_given_folder(self, filename, folder_name):
        files_list = self.get_filename_list_from_given_folder(folder_name)

        return filename in files_list

    def get_filename_list_from_given_folder(self, folder_name):
        files_list = []
        full_path = self.__folder_full_path + config.PATH_SEPARATOR + folder_name

        for entry in os.scandir(full_path):
            if entry.is_file():
                files_list.append(entry.name)

        return files_list

    def crate_unique_foldername(self):
        unique_part = str(uuid.uuid4().hex)
        unique_destination_path = self.__folder_full_path + config.PATH_SEPARATOR + unique_part

        while os.path.exists(unique_destination_path):
            unique_part = str(uuid.uuid4().hex)
            unique_destination_path = self.__folder_full_path + config.PATH_SEPARATOR + unique_part

        os.makedirs(unique_destination_path)
        config.LOGGER.info_output('   Created unique folder: ' + unique_destination_path)

        self.__unique_subfolder_name = unique_part

    def create_next_subfolder_in_unique(self):
        full_path = self.__folder_full_path + config.PATH_SEPARATOR + self.__unique_subfolder_name + config.PATH_SEPARATOR + str(self.__unique_subfolder_counter)

        os.makedirs(full_path)
        self.__unique_subfolder_counter += 1
        config.LOGGER.info_output('   Created subfolder - folder: ' + full_path)
