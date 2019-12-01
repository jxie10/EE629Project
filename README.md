This is the project for EE629.  
[For more information please visit](https://sites.google.com/stevens.edu/jiajiangxie/)  
---
# **Smart Car with HC-SR04**  
Hardware:Rapberry Pi 3B+, HC-SR04, Assemble car kit, L298N motor driver, female-female Dupont line, male-female Dupont line  
1.Assemble the smart car.  
2.Autodrive: run ```Autodrive.py```. There is a HC-SR04 ultrasonic ranging sensor in the front of the smart car, so it 
can avoid barriers in front of the car. 
3.Manuallydrive: On the Raspberry Pi, use Python's bottle library to set up a web application service. Visit the remote control webpage index.html on the Raspberry Pi on a mobile browser to interact with the Manuallydrive.py program to control the operation of the car. By using the js click event, the button click condition in the webpage is detected and fed back to the index.py file, so as to realize the control of the car by clicking the button.  
How to drive: ```Manuallydrive.py, main.py, index.html``` should to be placed in the same file path. Run ```Manuallydrive.py```. Open http: // your raspberrypi's ip: 8080 on your mobile browser.  
Press up to move forward, down to move back, left to turn left, right to turn right and block to stop.  
