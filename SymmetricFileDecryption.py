import datetime
import time
start = time.time()
byte_list = []
with open("encrypted.txt", "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        byte_list.append(byte)
file2 = open("decrypted.txt", "w")
key = 5
for byte in byte_list:
    value = ord(byte)
    value4 = value ^ key
    value1 = value4 - key
    value2 = value4 * key
    value3 = value1 % value2
    value5 = chr(value3)
    print(value5, file = file2, end = '')
file2.close()
end = time.time()
end_time = datetime.datetime.now()
print("Time of Execution", end - start)
print(end_time)

    
