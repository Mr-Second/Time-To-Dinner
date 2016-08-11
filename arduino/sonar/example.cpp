// Ultrasonic - Library for HR-SC04 Ultrasonic Ranging Module.
// Rev.4 (06/2012)
// J.Rodrigo ( www.jrodrigo.net )
// more info at http://www.ardublog.com
// Wiki: https://github.com/JRodrigoTech/Ultrasonic-HC-SR04/wiki/Plug-&-Play

#include <Ultrasonic.h>

Ultrasonic ultrasonic(5,6); // (Trig PIN,Echo PIN)

void setup() {
	Serial.begin(9600);
	pinMode(4, OUTPUT); // VCC pin
	pinMode(7, OUTPUT); // GND ping
	digitalWrite(4, HIGH); // VCC +5V mode  
	digitalWrite(7, LOW);  // GND mode
}

void loop()
{ 
	int range = ultrasonic.Ranging(CM);
	if (assurePassing(range))
	{
		digitalWrite(13, HIGH);
	}
	else{
		digitalWrite(13, LOW);
	}
	Serial.print(range); // CM or INC
	Serial.println(" cm" );
	// the Signal of Serial (0 and 1) will duplicate to BlueTooth module, so we can 
}
bool assurePassing(int range){
	int ConsistCount=3;
	while(ConsistCount){
		if(range<30){
			ConsistCount--;
		}
		else{
			return false;
		}
		delay(500);
	}
	return true;
}