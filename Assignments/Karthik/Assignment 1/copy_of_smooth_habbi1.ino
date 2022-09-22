
void setup()
{
  
  
  pinMode(13,OUTPUT);

  pinMode(2,INPUT);
}

void loop()
{
  
  if((digitalRead(2))&& (analogRead(A0) < 412))
    tone(13,13,100); //play a tone if motion is dectected
  else
  	noTone(13);
}
  