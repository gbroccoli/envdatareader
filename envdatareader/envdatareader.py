import ctypes
import platform
from os.path import abspath


class EnvDataReader:
    def __init__(self, file_path=".env"):
        if platform.system() == 'Windows':
            lib_extension = '.dll'
        else:
            lib_extension = '.so'

        lib_filename = abspath(f'libs/envdatareader{lib_extension}')
        self._lib = ctypes.CDLL(lib_filename)

        self._lib.EnvDataReader_new.restype = ctypes.c_void_p
        self._lib.EnvDataReader_new.argtypes = [ctypes.c_char_p]
        self._lib.EnvDataReader_load_variables.argtypes = [ctypes.c_void_p]
        self._lib.EnvDataReader_get_value.restype = ctypes.c_char_p
        self._lib.EnvDataReader_get_value.argtypes = [
            ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
        self._lib.EnvDataReader_delete.argtypes = [ctypes.c_void_p]

        self._file_path = file_path.encode('utf-8')
        self._reader = self._lib.EnvDataReader_new(self._file_path)
        self._load_variables()

    def get_value(self, key: str, default_val="") -> str:
        key = key.encode('utf-8')
        default_val = default_val.encode('utf-8')
        value = self._lib.EnvDataReader_get_value(
            self._reader, key, default_val)
        return value.decode('utf-8')

    def _load_variables(self):
        self._lib.EnvDataReader_load_variables(self._reader)

    def __del__(self):
        if hasattr(self, '_reader'):
            self._lib.EnvDataReader_delete(self._reader)
