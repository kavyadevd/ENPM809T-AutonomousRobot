## Gets distance of an object using Ultrasonic sensor.

An object is kept roughly 0.5 meters away from the Raspberry Pi.
The python script performs the following tasks:
1. Records a still image of the scene using either raspistill
2. Using the ultrasonic distance sensor, records 10 successive distance measurements between the Pi and the object
3. Calculates and prints the average of the 10 distance measurements onto the image using OpenCV

### Setup:

<p align="center">
  <img alt="Setup1" src="https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/3179924fcb99b482ab1c41fe6a5b60bb5bc69015/Assignments/Assignment4/images/Connections.jpg" width="15%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Setup2" src="https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/3179924fcb99b482ab1c41fe6a5b60bb5bc69015/Assignments/Assignment4/images/Ping.jpg" width="16%">
</p>

### Result:
<p align="center">
  <img alt="Setup1" src="https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/32b53f6a14021d52bbbb76e52660a0ed9d10f886/Assignments/Assignment4/images/result.png" width="85%">
</p>


