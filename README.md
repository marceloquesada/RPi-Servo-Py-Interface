# RPyServo

## Installation

To install the package, simply run:
<pre>$ pip install RpyServo </pre>

Now, pigpio is required for this package, if it does not install automatically along with the package, simply run:
<pre>$ pip install pigpio </pre>

## Description

A Python library to simplify the use of servos in RaspberryPi.

This inferface was created to simplify the pigpio interace, it is quite simple at the moment, but it manages the pigpio initialization and fixes the arbitrary servo angles of 500-2500 to 0-1000.

This is still a work in progress, so feel free to contribute!

## Use:

To import the library use:

<prep>import RpyServo</prep>

### Servo_motor class:

The only class in the project currently is the <prep>Servo_motor()</prep> class, below there is an example of the Servo_motor() initialization:

<prep>my_servo = Servo_motor([servo gpio port])</prep>

##### set_angle:

This functions sets the angle of the servo, the angles go from 0 to 1000, being 0 the angle 0 and 1000 the angle 180. This is an example of how to use this function:

<prep>my_servo.set_angle([Desired angle])</prep>

##### get_angle:

This function reads the angle from the servo, being 1000 the angle 180 and 0 being 0. This is an example of how to use this function:

<prep>angle = my_servo.get_angle()</prep>

