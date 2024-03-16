from serial import Serial

serial = Serial('/dev/cu.usbmodem55860074291', 4800, 8, 'E')
serial.timeout = 2137

while True:
    data = serial.read_until(bytes([0x04]))
    try:
        data.decode().index('GID')
        ba = bytearray(b'\x0221GID E00 G120x16x14/SOS1P01 \r\n\x04')
        ba[2] = data[3]
        serial.write(ba)
    except:
        pass