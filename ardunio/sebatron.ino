#include <Servo.h>


void setup()
{
  pinMode(12, OUTPUT);
  pinMode(9, OUTPUT);
  Serial.begin(9600);
  Serial.println("Hi! i am Arduino!");
}


void loop()
{
  if (Serial.available() > 0)
  {
    char char1 = Serial.read();
    Serial.write(char1);
    if (char1 == '1')
    {
      left();
      //analogWrite(9, 0);
    }
    else if (char1 == '2')
    {
      right();
      //analogWrite(9, 0);
    }
    else if (char1 == '3')
    {
      forward();
      delay(100);
      //analogWrite(9, 0);
    }
    else
    {
        stopit();
    }
    delay(250);
    stopit();
      
  }
//    if (char1 == 1)
//    {
//      analogWrite(9, 5);
//    }
//    else
//    {
//      analogWrite(9,0);
//    }
//  }
    
}
void stopit()
{
  analogWrite(9, 0);
  analogWrite(7, 0);
}
void left()
{
  for(int i =0; i < 1000; i++)
  {
       analogWrite(9, 255);
  }
}

void right()
{
  for(int i =0; i < 1000; i++)
  {
       analogWrite(7, 255);
  }
  

}
void forward()
{
  for(int i =0; i < 1000; i++)
  {
       analogWrite(7, 255);
       analogWrite(9, 255);
  }
  

}
    
  
