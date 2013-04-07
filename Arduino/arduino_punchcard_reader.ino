// Uses LED lights to detect visible light.

#define TOLERANCE 3100
#define MAX 31000

#define N1 
#define P1 

#define N2 
#define P2 

#define N3 
#define P3 

#define N4 
#define P4 

// Measures the natural ambient light
unsigned int ambient;

void setup(void) {
  Serial.begin(9600);
  ambient = getReading();
}

void loop(void) {
}

boolean inputOff() {
}

char getValue(int pos, int neg) {
  unsigned int x = getReading(pos, neg);
  return (abs(x - ambient) < TOLERANCE) ? '0' : '1';
}

unsigned int getReading(int positive, int negative) {
  unsigned int j;
  
    // Apply reverse voltage, charge up the pin and LED capacitance
  pinMode(negative,OUTPUT);
  pinMode(positive,OUTPUT);
  digitalWrite(negative,HIGH);
  digitalWrite(positive,LOW);
  
  // Turn off internal resistor
  pinMode(negative,INPUT);
  digitalWrite(negative,LOW);
  
    // Count how long it takes the diode to bleed back down to a logic zero
  for (j = 0; j < 30000; j++) {
    if ( digitalRead(negative)==0) {
      break;
    }
  }
  
  return j;
}
