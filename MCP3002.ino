// Arduino code to test the MCP3002 ADC chip.
// Code outputs an analog signal with PWM to the
// ADC which outputs a digital signal to the 
// Arduino using SPI.
//
// Pins:
// MCP3002  | Arduino Pin  |  Name
//     Vdd  |  5V
//     Gnd  |  Gnd
//     CH0  |  3
//     CLK  |  13             SCK
//     Din  |  11             MOSI
//     Dout |  12             MISO
//     CS'  |  10             SS

// Global variables for pin numbers
const int clk = 13;
const int din = 11;
const int dout = 12;
const int cs = 10;

void setup() {

  // Serial setup
  Serial.begin(9600);

  // Set pin modes
  pinMode(clk, OUTPUT);
  pinMode(din, OUTPUT);
  pinMode(dout, INPUT);
  pinMode(cs, OUTPUT);

  // Set beginning pin outputs
  digitalWrite(clk, LOW);
  digitalWrite(din, LOW);
  digitalWrite(cs, HIGH);

  // Generate 50% duty cycle PWM for testing only
  pinMode(3, OUTPUT);
  analogWrite(3, 127);
  

}

int readADC(byte settings) {
  // Create variable for return value
  int data = 0;

  digitalWrite(cs, LOW);

  // Send setup data to ADC
  for (int i = 3; i >= 0; i++) {
    //digitalWrite(din, (settings & (1 << i)) ? HIGH : LOW);
    digitalWrite(din, settings & (1 << i));
    digitalWrite(clk, HIGH);
    digitalWrite(clk, LOW);
  }

  // Ignore null bit
  digitalWrite(clk, HIGH);
  digitalWrite(clk, LOW);

  // Read 10 bits of data from ADC
  for (int i = 0; i < 10; i++) {
    digitalWrite(clk, HIGH);
    data = (data << 1) | digitalRead(dout);
    digitalWrite(clk, LOW);
  }

  digitalWrite(cs, HIGH);

  return data;
  
}

void loop() {

  // create data variable to store data from ADC
  int data = 0;

  // Send data to MCP3002 for setup and store digital signal in data variable
  // First bit high indicates start
  // Second bit high indicates single ended mode
  // Third bit low indicates channel 0
  // Fourth bit high indicates MSB first
  data = readADC(0xD);

  // Print data and wait 1 second
  Serial.println(data);
  delay(1000);

}
