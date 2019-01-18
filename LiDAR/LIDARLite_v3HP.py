# python shell for the lidar

import ctypes

"""
!!!!!!variable names list!!!!!!:
uint8_t * dataBytes (POINTER)
uint16_t numberOfReadings
VOID FXN: configure
    uint8_t sigCountMax
    uint8_t acqConfigReg
    uint8_t refCountMax
    uint8_t thresholdBypass
VOID FXN: LIDARLite_v3HP::setI2Caddr
    uint8_t dataBytes[2];
VOID FXN: LIDARLite_v3HP::takeRange
    uit8_t dataByte
VOID FXN: LIDARLite_v3HP::waitForBusy
    uint16_t busyCounter
    uint8_t busyFlag
uint8_t FXN: LIDARLite_v3HP::getBusyFlag
    uint8_t busyFlag
uint16_t FXN: LIDARLite_v3HP::readDistance
    uint16_t distance
    uint8_t dataBytes[2]
VOID FXN: LIDARLite_v3HP::write
    int nackCatcher
VOID FXN: LIDARLite_v3HP::read
    uint16_t i
    int nackCatcher = 0
VOID FXn: LIDARLite_v3HP::correlationRecordToSerial
    uint16_t i = 0
    uint8_t dataBytes[2]
    int16_t correlationValue = 0
"""

class LIDARLite_v3HP(ctypes.Structure):
    _fields_ = [("configuration", ctypes.c_uint8), ("lidarliteAddress", ctypes.c_uint8),
                ("regAddr", ctypes.c_uint8), ("disableDefault", ctypes.c_uint8),
                ("numBytes", ctypes.c_uint16), ("numberOfReadings", ctypes.c_uint16)]
