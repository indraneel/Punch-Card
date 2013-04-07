/* Arduino Punchcard Reader
 * Uses LED lights to detect visible light.
 */

#define TOLERANCE 0.6
#define MAX 31000

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
int VALS[5];
byte HALF_BYTE;
boolean CARD_ON, HALF_BYTE_READ;

void setup(void) {
  Serial.begin(9600);
  Serial.println("Loading...");
  
  // Init some constants yo
  CARD_ON = true;
  HALF_BYTE = 0;
  HALF_BYTE_READ = false;
  
  // Take the average of the light and darkness readings
  unsigned int x = getReading(SPEC_N, SPEC_P);
  x += getReading(SPEC_N, SPEC_P);
  x += getReading(SPEC_N, SPEC_P);
  AMBIENT = x / 3;
  x = getReading(N4, P4);
  x += getReading(N2, P2);
  x += getReading(N3, P3);
  DARKNESS = x / 3;
  
  // Print it to output
  Serial.print("Ambient light: ");
  Serial.println(AMBIENT);
  Serial.print("Darkness: ");
  Serial.println(DARKNESS);
  Serial.println("Initialization done!");
  
  for(int i = 2; i <= 10; i += 2) {
    digitalWrite(i, LOW);
    digitalWrite(i + 1, HIGH);
  }
  delay(1000);
    for(int i = 2; i <= 10; i += 2) {
    //digitalWrite(i, HIGH);
    digitalWrite(i + 1, LOW);
  }
  delay(1000);
}

void loop(void) {
  readerTest();
  /*
  //Serial.println(getValue(1));
  // TODO test this code!
  if(!CARD_ON) {
    CARD_ON = inputOn();
    return;
  }
  // Here, card is ON.
  boolean on = inputOn();
  if(!HALF_BYTE_READ && on) {
    // Reading the punch-card line
    for(int i = 4; i > 0; i--) {
      Serial.print(getValue(i));
    }
    Serial.print('\n');
    HALF_BYTE++;
    HALF_BYTE_READ = true; // Don't reread same line
  }
  else if(!on) {
    HALF_BYTE_READ = false; // Read card on input light on
  }
  
  // Test if the card has been fully read.
  if(HALF_BYTE % 8 == 0) {
    HALF_BYTE = 0;
    CARD_ON = false;
    delay(2000);
  }
  */
}

/**
 * Old loop code. Use this to test the input sensitivities of the
 * LEDs and write them to Serial.
 */
void readerTest(void) {
    for(int i = 1; i < 6; i++) {
    VALS[i - 1] = getReading(i * 2, (i * 2) + 1);
    Serial.print(VALS[i - 1]);
    Serial.print("|");
  }
  Serial.println("");
  for(int i = 1; i < 6; i++) {
    Serial.print(getValueFromUInt(VALS[i - 1]));
    Serial.print("|");
  }
  Serial.println("\n");
  delay(1000);
}

/**
 * When reading a punchcard, the special sensor is in darkness.
 * Every row begins with a light on the special sensor; this
 * signals that a half-byte has been found and it's time to read.
 * @return True if we're going to accept input; false otherwise.
 */
boolean inputOn(void) {
  return getValue(5) == '1';
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
  // TODO Refine the tolerance before the demo.
  return ((x / DARKNESS) > TOLERANCE) ? '0' : '1';
}

/**
 * Determines whether or not the input value corresponds to light
 * or darkness.
 * @param val The light reading.
 * @return '0' if it is darkness; '1' if it is light.
 */
char getValueFromUInt(unsigned int val) {
  return ((val / DARKNESS) > TOLERANCE) ? '0' : '1';
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
