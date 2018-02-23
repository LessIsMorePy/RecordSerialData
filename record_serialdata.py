'''
Name: record_serialdata.py
Python 3.5

Description:
This script allows to recive data from port serial 
and store all data captured in a text file using 
the function "save_data".

Created on 17 ene. 2018

@author: Luis Antonio V R
'''
# Pyserial
import serial

# Time
from time import strftime


def save_data(data):
    '''
        Save and print the captured data.
        
        parameters:
        data: Data from port serial  
    '''    
   
    # Build text file 
    archivo = open('Log-'+strftime("%d-%m-%y")+'.txt', 'a')
    
    # Save read data
    data = data
   
    try:
        archivo.write(str(data.decode().strip()) + '\n')
        print(data.decode().strip())
        
    except UnicodeDecodeError:
        
        archivo.write(str(data) + '\n')
        print(data)
    
    archivo.close()

# Serial configuration
s = serial.Serial(port = 'COM4', 
                  baudrate = 9600, 
                  bytesize = 8, 
                  parity = serial.PARITY_NONE,
                  stopbits = 1)

# Clean Buffer
s.flushInput()
s.setDTR()

# State port
print("Port: " + s.name)
print("State: ", s.isOpen())
 
# Do while the port is open
while s.isOpen():
   
    # Read
    serial_data = s.readline()
    # Store
    save_data(serial_data) 
