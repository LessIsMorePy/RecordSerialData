# RecordSerialData

Using Pyserial as main modulo record data from a serial port into the text file and watch at the same time the data in your console. 

The script can generate a text file per day.

# Flowchart

|Serial Port (RS232, UART)| => |PC| => |Text file store| => |See the data in your console|

# Step by step

1. In the script you should establish your serial port and your basics configurations for serial comunication, i.e.

 s = serial.Serial(port = 'COM4', 
                  baudrate = 9600, 
                  bytesize = 8, 
                  parity = serial.PARITY_NONE,
                  stopbits = 1)
                  
2. Then, you can change the file name in the next line.   

 archivo = open('Log-'+strftime("%d-%m-%y")+'.txt', 'a')   
 
The name of the output file it will be "Log-23-02-18.txt", depending on the date in your computer.

In this case, the current line it allows to create a new text file every day. All the data that pass for the serial comunicaction it will store in the text file, even if there are special characters or if you restart the script.
