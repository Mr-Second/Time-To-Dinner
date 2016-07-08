// int led = 13;
// void setup(){
// 	pinMode(led, OUTPUT);
// }

// void loop(){
// 	digitalWrite(led, HIGH);
// 	delay(1000);
// 	digitalWrite(led, LOW);
// 	delay(1000);
// }
// void setup(){
// 	Serial.begin(9600);
// }
// void loop(){
// 	int anoVal = analogRead(A0);
// 	Serial.println(anoVal);
// 	delay(10);
// }
const unsigned int LED_PIN = 13;
const unsigned int BAUD_RATE = 9600;
void setup(){
	pinode(LED_PIN, OUTPUT);
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