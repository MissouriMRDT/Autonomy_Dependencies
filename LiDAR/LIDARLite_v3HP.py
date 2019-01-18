# python shell for the lidar

import ctypes


class LIDARLite_v3HP(ctypes.Structure):
    _fields_ = [("configuration", ctypes.c_uint8), ("lidarliteAddress", ctypes.c_uint8),
                ("newAddress", ctypes.c_uint8), ("disableDefault", ctypes.c_uint8),
                ("", ctypes.c_uint16), ("", ctypes.c_uint8), ("", ctypes.c_uint8), ("", ctypes.c_uint8),
                ("", ctypes.c_uint8), ("", ctypes.c_uint8), ("", ctypes.c_uint8), ("", ctypes.c_uint8),
                ("", ctypes.c_uint8)]
