#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10,11);

int writePin = 2;
int readPin = 3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  BTSerial.begin(9600);
  pinMode(writePin, OUTPUT);
  pinMode(readPin, INPUT); 
}

void loop() {
  // put your main code here, to run repeatedly:
  int button = digitalRead(readPin);

  if (button == HIGH) {
    BTSerial.write(1);
  }
}
