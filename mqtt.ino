// This #include statement was automatically added by the Particle IDE.
#include <MQTT.h>
int i=0;
MQTT client("test.mosquitto.org",1883,callback);
void callback(char* topic, byte* payload, unsigned int length)
{
    i=1;
    digitalWrite(D7,HIGH);
    
}

void setup() {
    client.connect("ArgonDev");
    Particle.variable("Intruder",i);
    pinMode(D7,OUTPUT);
}

void loop() {

    client.subscribe("argonLOG");
    client.loop();
}