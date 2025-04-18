int lampu =7;
void setup() {
pinMode (lampu, OUTPUT);
}

void loop() {
digitalWrite(lampu, HIGH);
delay(1000);
digitalWrite(lampu, LOW);
delay(1000);
}