##  Calculate moving average of the raw accelerometer data

Load ADXL327 3-axis accelerometer  sensor data with Python/NumPy and plot/analyze data with Matplotlib

### Steps:
1. Load the data from text file [imudata.txt](https://github.com/kavyadevd/ENPM809T-AutonomousRobot/blob/48ee22a0d03f7cf8c07e14e9acf4f9fce1a0def4/Assignments/Assignment1/imudata.txt) into Python/NumPy.
2. Plot the raw data for the 5th column of the file, corresponding to the pitch angle of the
accelerometer as configured with the vehicle. The 5th column begins with values [6, 3, 10, 9, 8,
…]. The x-axis of the plot should begin with 0, 1, 2, … ; the y-axis should be in units of degrees.
3. Label the axes then add a title and legend to the plot.
4. Write your own function (i.e. do not use any built-in functionalities) to calculate a moving
average of the raw accelerometer data.
5. Plot the averaged data on top of the raw data on the same plot.
6. Calculate the mean and standard deviation of the averaged data and include this information
on the plot. 