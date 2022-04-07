import io
import time
import datetime
start = time.time()
byte_list = []
with open("input.txt", "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        byte_list.append(byte)
file2 = io.open("encrypted.txt", "w")
key = 5
for byte in byte_list:
    int_value = ord(byte)
    int_value1 = int_value + key
    int_value2 = int_value * key
    int_value3 = int_value1 % int_value2
    int_value4 = int_value3 ^ key
    int_value5 = chr(int_value4)
    print(int_value5, file = file2, end = '')
file2.close()
end = time.time()
end_time = datetime.datetime.now()
print("Time of Execution", end - start)
print(end_time)


    
