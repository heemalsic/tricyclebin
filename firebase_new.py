#! /usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		Hologlyph Bots (HB) Theme (eYRC 2023-24)
*        		===============================================
*
*  This script is to implement Task 2B of Hologlyph Bots (HB) Theme (eYRC 2023-24).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''


# Team ID:		[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:		feedback.py
# Functions:
#			[ Comma separated list of functions in this file ]
# Nodes:		Add your publishing and subscribing node


################### IMPORT MODULES #######################

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Float32
import firebase_admin
from firebase_admin import credentials, firestore

class firebase(Node):
    def __init__(self):
        super().__init__('firebase')
        self.subscriber1 = self.create_subscription(Float32,"/ult1", self.ult1, 10)
        self.subscriber2 = self.create_subscription(Float32,'/ult2', self.ult2, 10)
        self.subscriber3 = self.create_subscription(Float32,'/ult3', self.ult3, 10)
        self.dist1=25.0
        self.dist2=50.0
        self.dist3=75.0
        self.cred = credentials.Certificate(r"/home/akash/Desktop/firebase.json")
        firebase_admin.initialize_app(self.cred)
        #self.subscriber1

    def ult1(self,msg):
        self.dist1=msg.data
        self.pid1()
    def ult2(self,msg):
        self.dist2=msg.data
        self.pid2()
    def ult3(self,msg):
        self.dist3=msg.data
        self.pid3()
        
    def pid1(self):
        db = firestore.client()
        doc_ref = db.collection('distance_data').document('sensor_data_1')
        doc_ref.set({'distance': self.dist1})
        print(self.dist1,self.dist2,self.dist3)
        #time.sleep(1)
    def pid2(self):
        db = firestore.client()
        doc_ref = db.collection('distance_data').document('sensor_data_2')
        doc_ref.set({'distance': self.dist2})
    def pid3(self):
        db = firestore.client()
        doc_ref = db.collection('distance_data').document('sensor_data_3')
        doc_ref.set({'distance': self.dist3})





def main(args=None):
    rclpy.init(args=args)
    
    fire = firebase()
       
    # Main loop
    

        # Spin once to process callbacks
    while(rclpy.ok):
        # fire.pid1()
        # fire.pid2()
        # fire.pid3()
        rclpy.spin_once(fire)
    
    # Destroy the node and shut down ROS
    fire.destroy_node()
    rclpy.shutdown()

# Entry point of the script
if __name__ == '__main__':
    main()
