
 
// Include the Wire library for I2C
#include <Wire.h>
 
// LED on pin 13
const int led = 13; 
 
void setup() {
  // Join I2C bus as slave with address 9
  Wire.begin(0x9);
 
  
              
  Wire.onReceive(receiveEvent);
  
  // Setup pin 12 as output and turn LED off
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW); 
}
 
// Function that executes whenever data is received from master
void receiveEvent(int j) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    digitalWrite(led, c);
  }
}
void loop() {
  delay(100);
}
