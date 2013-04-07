/* Arduino Punchcard Reader
 * Uses LED lights to detect visible light.
 */

#define TOLERANCE 0.85
#define MAX 25000

#define N1 2
#define P1 3

#define N2 4
#define P2 5

#define N3 6
#define P3 7

#define N4 8
#define P4 9

#define SPEC_N 10
#define SPEC_P 11

unsigned int AMBIENT;
unsigned int DARKNESS;

void setup(void) {
  Serial.begin(9600);
  Serial.println("Loading...");
  
  // Take the average of the light and darkness readings
  unsigned int x = getReading(SPEC_N, SPEC_P);
  x += getReading(SPEC_N, SPEC_P);
  x += getReading(SPEC_N, SPEC_P);
  AMBIENT = x / 3;
  x = getReading(N1, P1);
  x += getReading(N1, P1);
  x += getReading(N1, P1);
  DARKNESS = x / 3;
  
  // Print it to output
  Serial.print("Ambient light: ");
  Serial.println(AMBIENT);
  Serial.print("Darkness: ");
  Serial.println(DARKNESS);
  Serial.println("Initialization done!");
  delay(3000);
}

void loop(void) {
  for(int i = 1; i < 6; i++) {
    Serial.print(getReading(i * 2, (i * 2) + 1));
    Serial.print("|");
  }
  Serial.println("");
  for(int i = 1; i < 6; i++) {
    Serial.print(getValue(i));
    Serial.print("|");
  }
  Serial.println("\n");
  delay(1000);
}

/**
 * @return True if we're going to stop reading input; false
 * otherwise.
 */
boolean inputOff() {
  // TODO
}

/**
 * Reads the bit corresponding to a certain slot.
 * @param row The row to read. Must be 1, 2, 3, 4, or 5; rows 1-4
 * correspond to normal input and row 5 is the "special" indicator.
 * @return '0' if the slot is in darkness; '1' if it is in light.
 */
char getValue(int row) {
  int pin = row * 2;
  unsigned int x = getReading(pin, pin + 1);
  // TODO Refine the tolerance. Perhaps hardcode some values
  return ((x / DARKNESS) > TOLERANCE) ? '0' : '1';
}

/**
 * Reads the brightness from the surrounding light.
 * @param negative The negative pin of the LED.
 * @param positive The positive pin.
 * @return An unsigned integer. The larger the number, the darker
 * the surroundings.
 */
unsigned int getReading(int negative, int positive) {
  unsigned int j;
  
    // Apply reverse voltage, charge up the pin and LED capacitance
  pinMode(negative,OUTPUT);
  pinMode(positive,OUTPUT);
  digitalWrite(negative,HIGH);
  digitalWrite(positive,LOW);
  
  // Turn off internal resistor
  pinMode(negative,INPUT);
  digitalWrite(negative,LOW);
  
  // Count how long it takes the diode to bleed back down
  // to a logic zero
  for (j = 0; j < MAX; j++) {
    if ( digitalRead(negative)==0) {
      break;
    }
  }
  return j;
}
