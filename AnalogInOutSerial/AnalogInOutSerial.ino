/*
Arduino sketch for reading analog signals from sensors.
@version: 1.0
*/

const int sensorOnePin = A0; 
const int sensorTwoPin = A1;

int sensorOneValue = 0;       
int sensorTwoValue = 0;


void setup() {

  Serial.begin(9600);
  /*Serial.print("SensorOne");
  Serial.print(",");
  Serial.println("Potentiometer");*/
  delay(5);

}

void loop() {

  sensorOneValue = analogRead(sensorOnePin);
  sensorTwoValue = analogRead(sensorTwoPin);
  
  Serial.print(sensorOneValue);
  Serial.print(",");
  Serial.println(sensorTwoValue);

}
