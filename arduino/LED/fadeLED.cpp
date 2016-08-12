  1 int brightness=2;
  2 int fadeAmount = 5;
  3 void setup(){
  4         pinMode(9, OUTPUT);
  5 }
  6 void loop(){
  7         analogWrite(9, brightness);
  8         brightness+=fadeAmount;
  9         if(brightness==0 || brightness==255){
 10                 fadeAmount-=5;
 11         }
 12         delay(30);
 13 }
