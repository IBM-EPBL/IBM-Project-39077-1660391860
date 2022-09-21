#include<Servo.h>

Servo servo;
void setup()
{
  servo.attach(3);
  
  pinMode(13,OUTPUT);
  pinMode(5,OUTPUT);
}

void loop()
{
  //open the window if temp is high
  double input = analogRead(A1);
  double t = (((input/1024)*5)-0.5)*100;
  if(t > 32) servo.write(180);
  else servo.write(0);
  
  
  
  //open windows
  int temp  = analogRead(A0);
  if(temp > 552)digitalWrite(13,1);
  else digitalWrite(13,0);
  
  //turn fan
  if(temp > 40) analogWrite(5,255);
  
  
}