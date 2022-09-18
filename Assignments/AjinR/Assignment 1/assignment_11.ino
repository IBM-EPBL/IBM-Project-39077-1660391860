#include <Servo.h>

Servo servoGarage;
Servo servoWindow;

void setup()
{
  
  servoGarage.attach(3);
  servoWindow.attach(5);

  
  pinMode(13,OUTPUT);
  pinMode(4,OUTPUT);
  
  
  pinMode(2,INPUT);
}

void loop()
{
  //door
  if(digitalRead(2))
    tone(13,8,100); //play a tone if motion is dectected
  else
  	noTone(13);
  
  
  
  //parking garage
  digitalWrite(4,1);
  delayMicroseconds(10);
  digitalWrite(4,0);
  float duration = pulseIn(A0,1); //get the duration
  float distance = (duration*0.343)/2;
  servoGarage.write(map(distance,400,2180,180,0));//rotate the servo
  
  //window
  if(analogRead(A1) > 412)/*open when luminocity > 412*/ servoWindow.write(180);
  else servoWindow.write(0);
  
  
  
}