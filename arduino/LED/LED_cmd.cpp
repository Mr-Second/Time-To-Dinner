const unsigned int LED_PIN = 13;
const unsigned int BAUD_RATE = 9600;
void setup(){
	pinMode(LED_PIN, OUTPUT);
	Serial.begin(BAUD_RATE);
}
void loop(){
	if(Serial.available()>0){
		int com = Serial.read();

		if (com == '1')
		{
			digitalWrite(LED_PIN, HIGH);
		}
		else if(com=='2'){
			digitalWrite(LED_PIN, LOW);
		}
		else{
			Serial.println("fuck");
		}
	}
}