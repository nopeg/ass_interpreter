import struct
import csv
import sys

# Словарь для преобразования команд
COMMANDS = {
    "LOAD_CONST": 201,
    "READ_MEM": 57,
    "WRITE_MEM": 27,
    "LOGIC_RSHIFT": 113,
}
