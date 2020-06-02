from smbus import SMBus
 
addr = 0x9 # bus address
bus_ = SMBus(1) # indicates /dev/ic2-1
 
i= 1
 
print ("Enter 1 for ON or 0 for OFF")
while i== 1:
 
    led= input(">>>>   ")
 
    if led== "1":
        bus_.write_byte(addr, 0x1) # switch it on
    elif led== "0":
        bus_.write_byte(addr, 0x0) # switch it on
    else:
        i= 0