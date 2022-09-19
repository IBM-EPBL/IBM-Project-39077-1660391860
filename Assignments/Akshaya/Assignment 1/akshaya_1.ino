// C++ code
//
#include<Servo.h>
Servo a;

void setup()
{
  pinMode(6, OUTPUT);
  a.attach(6);
}

void loop()
{
 double input = analogRead(A1);
 double t =(((input/1024)*5)-0.5)*100;
  if (analogRead(A0)&&(t>35)){
    a.write(180);
    
  }
  else{
	a.write(0);  
  }
}