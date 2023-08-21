from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()

process = rwm.get_process_by_name("popcapgame1.exe")


# offset 5560
# StartPoiter 00400000
# EndPointer 00794000

# Read Pointer
baseAddress = 0x00400000 + 0x002A7A80
sun = process.get_pointer(baseAddress, offsets=[0x258, 0x768, 0x100, 0x4, 0x5560])
print("Address tổng Poiter Cộng lại: ", hex(sun))  # chuyển int hoặc long to hex

valueRead = process.read(sun)
print("value của Sun: ", valueRead)

valueHack = 99999999
valueWrite = process.write(sun, valueHack)
print("value Hack Sun: ", valueHack, valueWrite)

valueReadAfter = process.read(sun)
print("value của Sun sau khi Hack: ", valueReadAfter)

process.close()

# while 1:
#     valueRead = process.read(sun)
#     valueWrite = process.write(sun, 9999)
#     print(valueRead)
