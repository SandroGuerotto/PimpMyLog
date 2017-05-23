import pickle

# Speichert eine List mit Log-Files in ein file
def write_logfile_list_in_file(file_list):
    # Öffnet das File log_files.txt "write"
    logfile_list_object = open("log_files_list.txt", "w")
    # Schreibt Objekt in File
    pickle.dump(file_list, logfile_list_object)
    # file objekt schliessen
    logfile_list_object.close()


# Gibt eine Liste mit allen gespeicherten Log-Files zurück
def read_logfile_list_from_file():
    # Öffnet das file log_files.txt "read"
    logfile_list_object = open("log_files_list.txt", "r")
    # Ladet File Inhalt in Variable
    return pickle.load(logfile_list_object)


# Gibt den Logfile Inhalt zurück
def get_logfile_content(path):
    # Öffnet das das log file "read"
    logfile_object = open(path, "r")
    # Ladet File Inhalt in Variable
    return pickle.load(logfile_object)