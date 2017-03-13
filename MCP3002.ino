// Arduino code to test the MCP3002 ADC chip.
// Code outputs an analog signal with PWM to the
// ADC which outputs a digital signal to the 
// Arduino using SPI.
// Pins:
// MCP3002 <-> Arduino
//     Vdd  |  5V
//     CH0  |  D3
//     CLK  |  D13
//     Din  |  D11
//     Dout |  D12
//     CS'  |  D10

#include <SPI.h>

int data = 0;

void setup() {
  // Begin serial for data output
  Serial.begin(9600);

  // Set pin 3 to OUTPUT for PWM
  pinMode(3, OUTPUT);

  // SPI setup
  SPI.beginTransaction(SPISettings(100000, MSBFIRST, SPI_MODE0));

}

void loop() {
  // Output 50% duty cycle PWM signal on pin D3
  analogWrite(3, 127);

  // Send data to MCP3002 for setup and receive digital signal
  // First bit high indicates start
  // Second bit high indicates single ended mode
  // Third bit low indicates channel 0
  // Fourth bit high indicates MSB first
  data = SPI.transfer(0xD);

  // Print data
  Serial.print(data);
  

}
