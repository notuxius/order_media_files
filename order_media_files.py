#!/bin/env python3

import os
import shutil
from os.path import expanduser

img_exts = [
    "png",
    "gif",
    "jpg",
    "jpeg",
    "webp",
    "svg",
    "tif",
    "tiff",
    "bmp",
    "psd",
    "xcf",
    "ico",
]

vid_exts = [
    "mkv",
    "mp4",
    "webm",
    "m4v",
    "mov",
    "hevc",
    "wmv",
    "vob",
    "flv",
    "avi",
    "3gp",
    "ogg",
]

# curr_folder = os.path.dirname(os.path.realpath(__file__))
home_folder = expanduser("~")
docs_folder = os.path.join(home_folder, "Documents")
chrome_download_folder = os.path.join(docs_folder, "chrome_download")

imgs_folder = os.path.join(docs_folder, "_IMAGES")
vids_folder = os.path.join(docs_folder, "_VIDEOS")


def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def list_media(folder, exts):
    media_files = []

    for ext in exts:
        media_files += [file for file in os.listdir(folder) if file.endswith(ext)]

    return media_files


def move_files(files, src_folder, dst_folder):
    for file in files:
        try:
            shutil.move(os.path.join(src_folder, file), dst_folder)

        except shutil.Error as e:
            print(e)
            print((os.path.join(src_folder, file)))
            # print("Removing the existing file")
            # os.remove(os.path.join(src_folder, file))


for src_folder in (docs_folder, chrome_download_folder):
    try:
        imgs = []
        vids = []

        imgs += list_media(src_folder, img_exts)
        vids += list_media(src_folder, vid_exts)

        media_files = {imgs_folder: imgs, vids_folder: vids}

        for media_folder in media_files:
            if media_files[media_folder]:
                create_folder_if_not_exists(media_folder)

                move_files(
                    media_files[media_folder],
                    src_folder,
                    media_folder,
                )

    # if no source folder
    except FileNotFoundError:
        pass
