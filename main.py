import os
import shutil

downloads_dir = r"C:\Users\Sai Vignesh\Downloads"
os.chdir(downloads_dir)

file_loc = {r"C:\Users\Sai Vignesh\Pictures": ["jpg", "png", "jpeg", "jfif", "pjpeg", "pjp", "gif", "svg",
                                               "apng", "avif", "webp"],
            r"C:\Users\Sai Vignesh\Videos": ["mp4", "mov", "avi", "wmv", "avchd", "webm", "flv", "amv", "mpg", "mp2",
                                             "mpeg", "mpe", "mpv", "m4v"],
            r"C:\Users\Sai Vignesh\Music": ["mp3", "m4v", "wav", "m4b", "m4p", "mmf", "ogg", "oga", "mogg", "raw", "wma",
                                            "webm"],
            r"C:\Users\Sai Vignesh\Documents": ["pdf", "docx", "doc", "txt"]}

def get_dir(extension):
    for dir, extensions in file_loc.items():
        if extension in extensions:
            return dir
    return ""

def file_organizer():
    for file in os.listdir():
        if os.path.isfile(os.path.join(downloads_dir, file)):
            file_ext = file.split(".")[-1]
            dir = get_dir(file_ext)
            if dir != "":
                file_path = os.path.join(downloads_dir, file)
                destination_path = os.path.join(dir, file)
                if os.path.isfile(destination_path):
                    pass
                else:
                    shutil.move(os.path.join(downloads_dir, file), dir)

if __name__ == "__main__":
    file_organizer()
