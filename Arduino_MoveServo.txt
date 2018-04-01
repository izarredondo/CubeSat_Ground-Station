/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep

 modified April 2017
 by Ben Christie and Izabella Arredondo
*/

#include <Servo.h>

Servo myservo1;
Servo myservo2;// create servo object to control a servo
// twelve servo objects can be created on most boards
String angles;
float pos1 = 0; 
float pos2 = 0;// variable to store the servo position

void setup() {
    Serial.begin(9600);
  Serial.println("setup");
 myservo1.attach(6);  // attaches the servo on pin 9 to the servo object
  myservo2.attach(5);
}

void loop() {
    //Serial.println("sweep");
    if (Serial.available()) {
      angles = Serial.readString();
      //angles += Serial.readString();
      
      Serial.println(angles);
    
    int commaIndex = angles.indexOf(',');
    int parenIndex = angles.indexOf(')');
    String firstPos = angles.substring(1, commaIndex);
    String secondPos = angles.substring(commaIndex+2,angles.length()-1);
    //String secondPos = angles.substring(commaIndex+2,parenIndex);
    Serial.println(angles);
    Serial.print("First Pos");
    Serial.println(firstPos);
    Serial.print("Second Pos");
    Serial.println(secondPos);
    char buffer[10];
    pos1 = firstPos.toFloat();
    pos2 = secondPos.toFloat();
    
       
  }

  angles = "";
  Serial.println(pos1);
  Serial.println(pos2);
  myservo1.write(pos1);              // tell servo to go to position in variable 'pos'
  myservo2.write(pos2);
  delay(500);
}

