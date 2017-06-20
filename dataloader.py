import pickle
import os, time, stat
from stat import * # ST_SIZE


# Speichert eine List mit Log-Files in ein file
def write_logfile_list_in_file(name, path):
    # Erstellt ein neues File Objekt
    file = File("", "", "", "", "")
    # File Infos werden in objekt file gespeichert
    st = os.stat(path)
    file.name = name
    file.path = path
    file.size = st[ST_SIZE]
    file.date = time.asctime(time.localtime(st[ST_MTIME]))

    # Überprüft ob file bereits existiert
    if os.path.isfile("log_files_list.txt"):
        # File mit liste laden
        with open("log_files_list.txt", "rb") as logfile_list_object_read:
            # Versucht liste mit files aus Datei zu lesen
            try:
                file_list = pickle.load(logfile_list_object_read)
                # Gibt dem neuen file eine id
                file1 = file_list[-1]
                file.id = file1.id + 1
            # Wenn file kene liste beinhaltet
            except (OSError, IOError, EOFError, AttributeError):
                # Gibt dem neuen file eine id
                file_list = []
                file.id = 1
    # Wenn File nicht existiert
    else:
        file_list = []
        file.id = 1
        open("log_files_list.txt", "wb")

    # Fügt neues file an list hinzu
    file_list.append(file)

    with open("log_files_list.txt", "wb") as logfile_list_object_write:
        # Schreibt Objekt in File
        pickle.dump(file_list, logfile_list_object_write)
        # file objekt schliessen
        logfile_list_object_write.close()

        return file.size, file.date, file.id


def read_logfile_list_from_file():
    if os.path.isfile("log_files_list.txt"):

        # Öffnet die Datei die die liste mit files beinhaltet
        with open("log_files_list.txt", "rb") as logfile_list_object:
            try:
                # Versucht Liste mit files aus datei zu lesen
                file_list = pickle.load(logfile_list_object)
                return file_list
            except (OSError, IOError, EOFError):
                pass
    else:
        open("log_files_list.txt", "wb")
    return list()


# Gibt den Logfile Inhalt zurück
def get_logfile_content(path):
    # Öffnet das das log file "read"
    with open(path, "rb") as logfile_object:
        # Gibt Fileinhalt zurück
        return logfile_object.read()


# Klasse File
class File:

    def __init__(self, id, path, name, date, size):
        self.id = id
        self.path = path
        self.name = name
        self.date = date
        self.size = size