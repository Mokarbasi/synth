// Arduino Code (ADC for Amplitude and Frequency Pots)
// Converts Pots inputs to digital and to Raspberry Pi

const int AMP_POT_PIN = A0;  // Amplitude pot on A0
const int FREQ_POT_PIN = A1; // Frequency pot on A1

void setup() {
  Serial.begin(9600);  // Initialize serial (9600 baud)
}

void loop() {
  int ampValue = analogRead(AMP_POT_PIN);    // Read amplitude pot (0-1023)
  int freqValue = analogRead(FREQ_POT_PIN);  // Read frequency pot (0-1023)

  // Send values as "ampValue,freqValue" over serial
  Serial.print(ampValue);
  Serial.print(",");
  Serial.println(freqValue);

  delay(20);  // Small delay to avoid flooding serial
}