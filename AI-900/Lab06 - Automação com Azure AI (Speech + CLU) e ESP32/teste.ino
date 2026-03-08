#include <WiFi.h>
#include <WebServer.h>

// ===== CONFIGURAÇÕES =====
const char* ssid = "SEU_WIFI";
const char* password = "SENHA";

WebServer server(80);
int ledPin = 2;

// ===== FUNÇÃO PRINCIPAL =====
void handleRoot() {

  if (server.hasArg("action")) {
    String action = server.arg("action");

    if (action == "ligar") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED LIGADO");
    } 
    else if (action == "desligar") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED DESLIGADO");
    }
  }

  // ===== HEADERS CORS =====
  server.sendHeader("Access-Control-Allow-Origin", "*");
  server.sendHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  server.sendHeader("Access-Control-Allow-Headers", "*");

  server.send(200, "text/plain", "OK");
}

// ===== TRATAMENTO DE PREFLIGHT (CORS) =====
void handleOptions() {
  server.sendHeader("Access-Control-Allow-Origin", "*");
  server.sendHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  server.sendHeader("Access-Control-Allow-Headers", "*");
  server.send(204);
}

// ===== CONEXÃO WIFI =====
void conectarWiFi() {
  Serial.println("\nConectando ao WiFi...");
  WiFi.begin(ssid, password);

  int tentativas = 0;

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    tentativas++;

    if (tentativas > 20) {
      Serial.println("\nFalha ao conectar. Reiniciando ESP...");
      ESP.restart();
    }
  }

  Serial.println("\nWiFi Conectado!");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());
}

// ===== SETUP =====
void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  conectarWiFi();

  // Rotas do servidor
  server.on("/", handleRoot);
  server.on("/", HTTP_OPTIONS, handleOptions);
  server.onNotFound(handleRoot);

  server.begin();
  Serial.println("Servidor HTTP iniciado");
}

// ===== LOOP =====
void loop() {
  // Reconexão automática se cair o WiFi
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi desconectado. Reconectando...");
    conectarWiFi();
  }
  Serial.println(WiFi.localIP());

  server.handleClient();
}