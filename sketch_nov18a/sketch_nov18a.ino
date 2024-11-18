// Arduino code to control DC motor
int motorPin1 = 3;
int motorPin2 = 4;

void setup() {
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == 'F') {        // Forward
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
    } else if (command == 'B') { // Backward
      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, HIGH);
    } else if (command == 'S') { // Stop
      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, LOW);
    }
  }
}
