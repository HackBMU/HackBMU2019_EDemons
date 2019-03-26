 int t=1;
 const int t1 = 13;
const int s = 12;
 long sd,td;
 
 
  void setup()
{
Serial.begin(9600);
pinMode(s,INPUT);
pinMode(t1,OUTPUT);
}

void loop()
{
  digitalWrite(t1, LOW);
  delayMicroseconds(2);

  digitalWrite(t1, HIGH);
  delayMicroseconds(10);

  
  digitalWrite(t1, LOW);

  sd=pulseIn(s, HIGH);

  td=sd/58.2;
  Serial.println(td);
  delay(50);

Serial.println("See It's working or not: ");
 Serial.println(t);
 t++;
 if(t==2)
 {
  Serial.print("et's see");
  }
 delay(1000);
}
