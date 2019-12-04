# coding=utf-8
import os


def is_file(location_file):
    """
    Metodo che dato un percorso, restituisce True se si riferisce ad un file.
    :param location_file: percorso del file
    :return: True se è un file, False altrimenti
    """
    return os.path.isfile(location_file)


def read(location_file, mode="r"):
    """
    Metodo che dato il percorso di un file, ritorna il contenuto del file.
    :param location_file: percorso di un file
    :param mode: modo di lettura
    :return: una lista di stringhe, una per riga, del file, False se non esiste il file
    """
    if is_file(location_file):
        return_file = []
        with open(location_file, mode) as _file:
            return_file.extend(_file)
            _file.close()

        return return_file
    return False
