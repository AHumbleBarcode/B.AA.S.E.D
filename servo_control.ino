#include <Servo.h>
int x1, x2, x3, y1, y2, y3;
int shoot = 0, shot_c =0;
int xpos = 80;
int ypos = 90;
int i = 0;
Servo X;
Servo Y;

const int Relay = 4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(Relay,OUTPUT);
  digitalWrite(Relay, HIGH);
  X.attach(10);
  Y.attach(11);
  X.write(xpos);
  Y.write(ypos);
  
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available()>6) {
    y1 = Serial.read() - '0';
    y2 = Serial.read() - '0';
    y3 = Serial.read() - '0';
    x1 = Serial.read() - '0';
    x2 = Serial.read() - '0';
    x3 = Serial.read() - '0';
    shoot = Serial.read() - '0';
    
    xpos = (100 * x1) + (10* x2) + x3 + 4;
    ypos = (100 * y1) + (10* y2) + y3 + 4;
    
    if (shoot != 0){
      shot_c ++;
    }else{
      digitalWrite(Relay, HIGH);
    }
  }

  if (shot_c > 4) {
    digitalWrite(Relay, LOW);
    shot_c = 0;
  }else {
    digitalWrite(Relay, HIGH);
  }
  
  X.write(xpos);
  Y.write(ypos);

  
}