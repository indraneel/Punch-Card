/*
 * Pin 13: built-in LED
       You can send a voltage to 13 to cause it to light up
       
 * Digital pins (hi/lo)
 
 Digital I/O
 pinMode(pin, INPUT/OUTPUT)
 digitalWrite(pin, value) // HIGH/LOW
 digitalRead(pin) // Returns HIGH/LOW, 1/0
 
 Analog I/O
 analogRead(pin) // returns 0-1023
 analogWrite(pin, val) // PWN output where val = 0 to 255
 
 Serial Communications
 * Receive and transmit data:
     Receive pin: 0
     Transmit pin: 1
   Communicate between devices and humans
   Key output functions:
     Serial.print();
     Serial.println();
     Serial.write();
     
 Getting Serial Data
   Reading data: can be blocking or non-blocking
   callbackSerial() - fills a buffer full of information without
     blocking
     
    method sig:
    int callbackSerial(char *buff)
    
  Swift's Stuff: BreakfastSerial
    Requires Firmata (API for interacting with an Arduino over Serial
    
  
 */

void setup(void) {
}

void loop(void) {
}


