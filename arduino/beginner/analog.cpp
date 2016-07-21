const unsigned int LED_PIN = 13;
const unsigned int BAUD_RATE = 9600;
void setup(){
	pinMode(LED_PIN, OUTPUT);
	pinMode(12, OUTPUT);
	digitalWrite(12, HIGH);
	Serial.begin(BAUD_RATE);
}
void loop(){
	int anoVal = analogRead(A1);
	// 因為電壓最高就是1024，而他對應到5V  其他的數字就按比例去算
	//加了光敏電阻，光愈亮光敏電阻的電阻愈小
	Serial.println(anoVal);
	if (anoVal>=1000){
		digitalWrite(LED_PIN, HIGH);
	}
	else{
		digitalWrite(LED_PIN, LOW);
	}
	delay(10);
}