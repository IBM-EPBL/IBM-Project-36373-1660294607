ASSIGNMENT 1 - HOME AUTOMATION

// C++ code
//
void setup()
{
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(11,OUTPUT);
}

void loop()
{
  // Getting the data from the Temperature sensor
  double a = analogRead(A0);
  
  // Converting Analog value to Digital Value 
  double Conv = (((a/1024)*5)-0.5)*100;
  Serial.println("The Temperature is :");
  Serial.println(Conv);
  Serial.println("**********");
  delay(1000);
  if(Conv>30)
  {
    	digitalWrite(9,HIGH);
  }
  else
  {
    	digitalWrite(8,HIGH);
  }
  
  // Getting the data from Gas Sensor
  int gas = analogRead(A3);
  Serial.println("Tha value is: ");
  Serial.println(gas);
  int thres = 50;
  if (gas > thres)
  {
    	digitalWrite(11,HIGH);
  }
}

