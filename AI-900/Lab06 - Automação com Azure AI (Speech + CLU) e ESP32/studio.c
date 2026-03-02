#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);
int ledPin = 2;

void handleRoot() {

  if (server.hasArg("action")) {
    String action = server.arg("action");

    if (action == "ligar") {
      digitalWrite(ledPin, HIGH);
    } 
    else if (action == "desligar") {
      digitalWrite(ledPin, LOW);
    }
  }

  // ===== HEADERS CORS =====
  server.sendHeader("Access-Control-Allow-Origin", "*");
  server.sendHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  server.sendHeader("Access-Control-Allow-Headers", "*");

  server.send(200, "text/plain", "OK");
}

void handleOptions() {
  server.sendHeader("Access-Control-Allow-Origin", "*");
  server.sendHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  server.sendHeader("Access-Control-Allow-Headers", "*");
  server.send(204);
}

void setup() {
  pinMode(ledPin, OUTPUT);
  
  WiFi.begin("SEU_WIFI", "SENHA");
  while (WiFi.status() != WL_CONNECTED) delay(500);

  server.on("/", handleRoot);
  server.onNotFound(handleRoot);
  server.on("/", HTTP_OPTIONS, handleOptions);

  server.begin();
}

void loop() {
  server.handleClient();
}