#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from urllib.request import urlretrieve
from sa import config
import os, zipfile, datetime
import shutil
import logging

class LoggerSetup(object):
    def __init__(self):
        self.current_date = datetime.date.today()
        logging.basicConfig(filename="log" + str(self.current_date) + ".log", level=logging.DEBUG)

    # def logwrite(self):
    #     logging.basicConfig()
class DownloadAchive(object):
    def __init__(self):
        self.url_arch = config.constants["git_arch"]  # урл на архив из констант
        # self.save_folder = config.constants["save_folder"]  #

    def download_acrh(self):
        destination = self.url_arch.rsplit('/', 1)[1]
        urlretrieve(self.url_arch, destination)


class UnzipArchive(object):
    def __init__(self):
        self.fzip = zipfile.ZipFile(config.constants["name_acrhive"])

    def unzip(self):
        self.fzip.extractall()


class BackUpServer(object):
    def __init__(self):
        self.current_date = datetime.date.today()
        self.zip_name = config.constants["path_to_save_backup"] + str(self.current_date)  # куда сохранять бэкап
        self.directory_name = config.constants["path_to_prj"]  # что сохранять в архив бэкапа

    def arch_server(self):
        return shutil.make_archive(self.zip_name, 'zip', self.directory_name)  # имя бэкапа в формате Backup2018-04-03


class RemoveFolder(object):
    def __init__(self):
        self.path_to_remove_folder = config.constants["path_to_prj"]

    def remove_f(self):
        shutil.rmtree(self.path_to_remove_folder, ignore_errors=False)
        # получается что удаляется и сама папка, если нет, то раскоментить нижнее
        # os.system("rm " + self.path_to_remove_folder + "/* -y")
#

a = DownloadAchive()
a.download_acrh()
b = UnzipArchive()
b.unzip()
c = BackUpServer()
c.arch_server()
d = RemoveFolder()
d.remove_f()
