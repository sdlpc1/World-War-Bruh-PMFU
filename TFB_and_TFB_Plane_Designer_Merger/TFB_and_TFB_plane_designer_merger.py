import shutil
import os
import datetime

PULL_MOD_PATH = "B:/Program Files/SteamLibrary/steamapps/workshop/content/394360/"
MOD_PATH = "B:/chronosgithub/v3/hoi4/TheirFinestRats/TFB_and_TFB_Plane_Designer_Merger/build/"
MOD_FILES = "B:/chronosgithub/v3/hoi4/TheirFinestRats/TFB_and_TFB_Plane_Designer_Merger/mod_files/"
BACKUPS = "B:/chronosgithub/v3/hoi4/TheirFinestRats/TFB_and_TFB_Plane_Designer_Merger/backups/"

TFB = "2559317737"
TFB_PLANE_DESIGNER = "2897704040"

FILES_2_REMOVE = ["descriptor.mod", "thumbnail.png"]

MODS_COPY = [TFB, TFB_PLANE_DESIGNER]

MOD_FILES_TO_COPY = ["descriptor.mod", "thumbnail.png"]

shutil.rmtree(MOD_PATH)

os.mkdir(MOD_PATH)

for MOD in MODS_COPY:
    shutil.copytree(PULL_MOD_PATH + MOD, MOD_PATH, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)

for FILE in FILES_2_REMOVE:
    os.remove(MOD_PATH + FILE)

for MOD_FILE_COPY in MOD_FILES_TO_COPY:
    shutil.copy(MOD_FILES + MOD_FILE_COPY, MOD_PATH)

DATETIME = datetime.datetime.now()

DATETIMEFINAL = DATETIME.strftime("%Y-%m-%d-%H-%M-%S")

os.makedirs(BACKUPS + DATETIMEFINAL)

shutil.copytree(MOD_PATH, BACKUPS + DATETIMEFINAL, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)