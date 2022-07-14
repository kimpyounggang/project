
#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>
#include <addons/TokenHelper.h>
#include <addons/RTDBHelper.h>
#define API_KEY "개인정보"
#define DATABASE_URL "개인정보"
#define USER_EMAIL "개인정보"
#define USER_PASSWORD "개인정보"
#define WIFI_SSID "와이파이"
#define WIFI_PASSWORD "와이파이비밀번호"

//Define Firebase Data object
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;


//-------------------------------------------------------
//*** Your variables***
int set_channel; // = value of V20 (Button "SET" from Blynk App)
unsigned long sendDataPrevMillis = 0;
unsigned long temp = 0;
unsigned long dust = 5;
unsigned long count = 0;
float sensor1,sensor2,sensor3,sensor4,sensor5,sensor6,sensor7,sensor8;
 //sensor9,sensor10,sensor11,sensor12,sensor13,sensor14,sensor15,sensor16;
//array of sensors related to channel 0,1,..7
//For example: "12467358" ==>Channel 0:Sensor1,...Channel 7: Sensor 8
int channel_select[8]; // 
//Declare position of each character in Received String Data
/*position of 'a': n1; position of 'b': n2 ; ==> temp
position of 'c': n3; position of 'd': n4 ; ==> humidity
 position of 'e': n5; position of 'f': n6 ; ==> light
position of 'g': n7; position of 'h': n8 ; ==> sound
position of 'i': n9; position of 'j': n10; ==> magnetic
position of 'k': n11; position of 'l': n12; ==> dust
 position of 'm': n13; position of 'n': n14; ==> smoke
 position of 'x': n15; position of 'y': n16; ==> flame */ 
int n1,n2,n3,n4,n5,n6,n7,n8,
 n9,n10,n11,n12,n13,n14,n15,n16;
//Declare String
String inputString; // Temporary input string received from Arduino Mega 2560
String value_out_string; // Data String received from Arduino Mega 2560
String sensor1_string,sensor2_string,sensor3_string,sensor4_string,
 sensor5_string,sensor6_string, sensor7_string,sensor8_string;
//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
void setup()
{
  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();
  Serial.printf("Firebase Client v%s\n\n", FIREBASE_CLIENT_VERSION);
  config.api_key = API_KEY;
  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;
  config.database_url = DATABASE_URL;
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
  Firebase.setDoubleDigits(5);
}
//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
void loop()
{ // LOOP BEGIN
 if (Firebase.ready() && (millis() - sendDataPrevMillis > 15000 || sendDataPrevMillis == 0))
  {
    sendDataPrevMillis = millis();

  while (Serial.available() > 0) 
 { char inChar = Serial.read();
 if (inChar != '\n'){inputString+=inChar;} 
 else {value_out_string=inputString;inputString="";}
 }
 
// Find the positions of characters used for splitting data string
for(int i=0;i<value_out_string.length();i++)
 {
// Temperature 
 if (value_out_string.charAt(i)=='a'){n1=i; }
 else if (value_out_string.charAt(i)=='b'){n2=i; }
// Humidity 
else if (value_out_string.charAt(i)=='c'){n3=i; }
else if (value_out_string.charAt(i)=='d'){n4=i; }
// Light 
else if (value_out_string.charAt(i)=='e'){n5=i; }
else if (value_out_string.charAt(i)=='f'){n6=i; }
// Sound 
else if (value_out_string.charAt(i)=='g'){n7=i; }
else if (value_out_string.charAt(i)=='h'){n8=i; }
// Magnetic 
else if (value_out_string.charAt(i)=='i'){n9=i; }
else if (value_out_string.charAt(i)=='j'){n10=i;}
// Dust 
else if (value_out_string.charAt(i)=='k'){n11=i;}
else if (value_out_string.charAt(i)=='l'){n12=i;}
// Smoke
else if (value_out_string.charAt(i)=='m'){n13=i;}
else if (value_out_string.charAt(i)=='n'){n14=i;}
// Flame
else if (value_out_string.charAt(i)=='x'){n15=i;}
else if (value_out_string.charAt(i)=='y'){n16=i;}
}
// Split data string
sensor1_string=value_out_string.substring(n1+1,n2-1);
sensor2_string=value_out_string.substring(n3+1,n4-1);
sensor3_string=value_out_string.substring(n5+1,n6-1);
sensor4_string=value_out_string.substring(n7+1,n8-1);
sensor5_string=value_out_string.substring(n9+1,n10-1);
sensor6_string=value_out_string.substring(n11+1,n12-1);
sensor7_string=value_out_string.substring(n13+1,n14-1);
sensor8_string=value_out_string.substring(n15+1,n16-1);
// Convert strings to float numbers
sensor1=sensor1_string.toFloat(); sensor2=sensor2_string.toFloat();
sensor3=sensor3_string.toFloat(); sensor4=sensor4_string.toFloat();
sensor5=sensor5_string.toFloat(); sensor6=sensor6_string.toFloat();
sensor7=sensor7_string.toFloat(); sensor8=sensor8_string.toFloat(); 
// Send data to the Widgets over the Virtual Pin

    Serial.printf("Set bool... %s\n", Firebase.setBool(fbdo, "/test/bool", count % 2 == 0) ? "ok" : fbdo.errorReason().c_str());

    Serial.printf("Get bool... %s\n", Firebase.getBool(fbdo, "/test/bool") ? fbdo.to<bool>() ? "true" : "false" : fbdo.errorReason().c_str());

    bool bVal;
    Serial.printf("Get bool ref... %s\n", Firebase.getBool(fbdo, "/test/bool", &bVal) ? bVal ? "true" : "false" : fbdo.errorReason().c_str());

    Serial.printf("Set int... %s\n", Firebase.setFloat(fbdo, "/sensors/sensor1", sensor1) ? "ok" : fbdo.errorReason().c_str());
    Serial.printf("Get int... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor1") ? String(fbdo.to<float>()).c_str() : fbdo.errorReason().c_str());

    int iVal = 0;
    Serial.printf("Get int ref... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor1", &iVal) ? String(iVal).c_str() : fbdo.errorReason().c_str());

    Serial.printf("Set temp... %s\n", Firebase.setFloat(fbdo, "/sensors/sensor2", sensor2) ? "ok" : fbdo.errorReason().c_str());
    Serial.printf("Get temp... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor2") ? String(fbdo.to<float>()).c_str() : fbdo.errorReason().c_str());

    Serial.printf("Set dust... %s\n", Firebase.setFloat(fbdo, "/sensors/sensor3", sensor3) ? "ok" : fbdo.errorReason().c_str());
    Serial.printf("Get dust... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor3") ? String(fbdo.to<float>()).c_str() : fbdo.errorReason().c_str());

    Serial.printf("Set dust... %s\n", Firebase.setFloat(fbdo, "/sensors/sensor4", sensor4) ? "ok" : fbdo.errorReason().c_str());
    Serial.printf("Get dust... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor4") ? String(fbdo.to<float>()).c_str() : fbdo.errorReason().c_str());

    Serial.printf("Set dust... %s\n", Firebase.setFloat(fbdo, "/sensors/sensor5", sensor5) ? "ok" : fbdo.errorReason().c_str());
    Serial.printf("Get dust... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor4") ? String(fbdo.to<float>()).c_str() : fbdo.errorReason().c_str());

    Serial.printf("Set dust... %s\n", Firebase.setFloat(fbdo, "/sensors/sensor6", sensor6) ? "ok" : fbdo.errorReason().c_str());
    Serial.printf("Get dust... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor6") ? String(fbdo.to<float>()).c_str() : fbdo.errorReason().c_str());

    Serial.printf("Set dust... %s\n", Firebase.setFloat(fbdo, "/sensors/sensor7", sensor7) ? "ok" : fbdo.errorReason().c_str());
    Serial.printf("Get dust... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor7") ? String(fbdo.to<float>()).c_str() : fbdo.errorReason().c_str());

    Serial.printf("Set dust... %s\n", Firebase.setFloat(fbdo, "/sensors/sensor8", sensor8) ? "ok" : fbdo.errorReason().c_str());
    Serial.printf("Get dust... %s\n", Firebase.getFloat(fbdo, "/sensors/sensor8") ? String(fbdo.to<float>()).c_str() : fbdo.errorReason().c_str());

    Serial.println();

    count++;


}

    

    
 }
