## Gets distance of an object using Ultrasonic sensor.

An object is kept roughly 0.5 meters away from the Raspberry Pi.
The python script performs the following tasks:
1. Records a still image of the scene using either raspistill
2. Using the ultrasonic distance sensor, records 10 successive distance measurements between the Pi and the object
3. Calculates and prints the average of the 10 distance measurements onto the image using OpenCV

### Components:
Components:
1. Raspberry Pi
2. Breadboard
3. Distance sensor
4. Three 1kW resistors
5. Jumper wires
6. RPi Camera


### Setup:

<p align="left">
  <img alt="Setup1" src="https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/3179924fcb99b482ab1c41fe6a5b60bb5bc69015/Assignments/Assignment4/images/Connections.jpg" width="15%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Setup2" src="https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/3179924fcb99b482ab1c41fe6a5b60bb5bc69015/Assignments/Assignment4/images/Ping.jpg" width="16%">
</p>

### Result:
<p align="center">
  <img alt="Setup1" src="https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/32b53f6a14021d52bbbb76e52660a0ed9d10f886/Assignments/Assignment4/images/result.png" width="85%">
</p>

Connections timelapse video [here](https://youtu.be/_bE9GHTmR3U)
<p align="left">
  <img alt="Setup1" src="https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/5b34912f718fc3fb797c73e22b8020b76cccc295/Assignments/Assignment4/Ultrasonic/images/breadboard.jpg" width="65%">
</p>

**[Reference: UMCP, Mitchell](https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/a830aacf82cd3db6ce42b2e24de1cdf031a09cb1/Assignments/Assignment4/Ultrasonic/ENPM809T-04-upload.pdf)**

