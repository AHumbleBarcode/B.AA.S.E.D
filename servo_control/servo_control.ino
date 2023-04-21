#include <Servo.h>
int x1;
int x2;
int x3;
int y1;
int y2;
int y3;
int xpos = 110;
int ypos = 90;
int i = 0;
  Servo X;
  Servo Y;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  X.attach(10);
  Y.attach(11);
  X.write(xpos);
  Y.write(ypos);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available()>5) {
    y1 = Serial.read() - '0';
    y2 = Serial.read() - '0';
    y3 = Serial.read() - '0';
    x1 = Serial.read() - '0';
    x2 = Serial.read() - '0';
    x3 = Serial.read() - '0';
    i++;
    xpos = (100 * x1) + (10* x2) + x3;
    ypos = (100 * y1) + (10* y2) + y3;
  }

  X.write(xpos);
  Y.write(ypos);

  
}
