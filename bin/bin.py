import subprocess

# Create and start the processes
proc1 = subprocess.Popen(['python', '/home/akash/Desktop/bin/ir.py'])
proc2 = subprocess.Popen(['python', 'arduino.py'])
proc3 = subprocess.Popen(['python', 'firebase_new.py'])
proc4 = subprocess.Popen(['python', '/home/akash/Desktop/bin/prediction_new.py'])
proc5 = subprocess.Popen(['python', 'humi_odour.py'])

# Wait for the processes to finish
proc1.wait()
proc2.wait()
proc3.wait()
proc4.wait()
proc5.wait()
