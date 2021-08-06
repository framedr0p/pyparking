#include <WiFi.h>
#define ledPin 5      // LED
#define echoPin 6     // Echo HC-SR04
#define trigerPin 7   // Trigger HC-SR04

long id;              // ID des Sensors
long id1000;          // abgewandelte ID des Sensors wenn freier PP
long distancelimit;   // ab welchem Abstand gilt der Parkplatz als frei
long duration;        // vom Sensor gemessene Dauer
long distance;        // aus Dauer errechnete Entfernung

String  request;
IPAddress staticIP709_10.10.0.99(10.10.0.99);
IPAddress gateway709_10.10.0.99(10.10.0.254);
IPAddress subnet709_10.10.0.99(255.255.255.0);

WiFiClient client;

String myurl = "/";
String line="";
String IotClientSendWithAnswer(String IPcache, String monmessagecache) {
line="";
client.print(String("GET ") + myurl +monmessagecache + " HTTP/1.1\r\n" +
          "Host: " + IPcache + "\r\n" +
         "Connection: close\r\n\r\n");
unsigned long timeout = millis();
while (client.available() == 0) {
if (millis() - timeout > 5000) {
client.stop();
return "Client Timeout!";
}
}
while(client.available()) {line += client.readStringUntil('\r');}
return line;
}

void setup()
{
id = 101;               // ID des Sensors
id1000 = 1101;          // ID des Sonsors wenn PP frei
distancelimit = 100000; // ab welchem Abstand gilt der Parkplatz als frei
request = "";

pinMode(echoPin, INPUT); 
pinMode(trigPin, OUTPUT);

Serial.begin(9600);

  WiFi.disconnect();
  delay(3000);
  Serial.println("START");
  WiFi.begin("HOME","8QU5TCD2V7DSBP4MZNZQV");     // WiFi Zugangsdaten
  while ((!(WiFi.status() == WL_CONNECTED))){
    delay(300);
    Serial.print("..");

  }
  Serial.println("Connected");
  WiFi.config(staticIP709_10.10.0.99, gateway709_10.10.0.99, subnet709_10.10.0.99);
  Serial.println("Your IP is");
  Serial.println((WiFi.localIP()));

}

void loop()
{
  // Sensor wird von HIGH Puls ausgelöst, der länger als 10 Microsekunden dauert
  // vorher ein kurzer LOW Puls, für sauberen HIGH Puls
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Signal vom Sensor einlesen:
  // duration = Zeit in Mikrosekunden für Senden eines Pings
  // bis zum Empfangen des Echos von einem Objekt
  duration = pulseIn(echoPin, HIGH);

  // Formel: distance = 1/2 * duration / Schallgeschwindigkeit
  // Schallgeschwindigkeit ca 323m/s
  // durch 2, da duration die Zeit für hin und zurück ist
  distance = duration * 0.034 / 2;

  // Entkommentieren, falls gemessener Abstand auf Serial Monitor ausgegeben werden soll
  // Serial.print("Abstand: ");
  // Serial.println(distance);

  if (client.connect("10.10.0.98", 80)) {
    if (distance <= distancelimit) {    // falls Abstand zu klein -> Parkplatz belegt
      request = id;
    }
    // sonst ist der Parkplatz frei
    else if (distance > distancelimit) {
      request = id1000;
    }
    // sende den Request an den Controller
    Serial.println((IotClientSendWithAnswer("10.10.0.98",request)));
  }
  delay(100);
}