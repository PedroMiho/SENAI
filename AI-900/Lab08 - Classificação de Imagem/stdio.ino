#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "iPhone de Pedro";
const char* password = "12348765";

WebServer server(80);

// Pinos dos LEDs
int ledAmarelo = 14;
int ledVermelho = 27;
int ledVerde = 26;

// =========================
// Função que recebe a cor
// =========================
void handleCor() {

  if (server.hasArg("valor")) {

    String valor = server.arg("valor");

    // Desliga todos os LEDs
    digitalWrite(ledAmarelo, LOW);
    digitalWrite(ledVermelho, LOW);
    digitalWrite(ledVerde, LOW);

    if (valor == "amarelo") {
      digitalWrite(ledAmarelo, HIGH);
      Serial.println("LED Amarelo acionado");
    }
    else if (valor == "vermelho") {
      digitalWrite(ledVermelho, HIGH);
      Serial.println("LED Vermelho acionado");
    }
    else if (valor == "verde") {
      digitalWrite(ledVerde, HIGH);
      Serial.println("LED Verde acionado");
    }

    server.send(200, "text/plain", "LED " + valor + " acionado");
  }
  else {
    server.send(400, "text/plain", "Parametro nao recebido");
  }
}

// =========================
// Setup
// =========================
void setup() {

  Serial.begin(115200);
  delay(1000);

  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  pinMode(ledVerde, OUTPUT);

  Serial.println("Conectando ao WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi conectado!");
  Serial.print("IP do ESP32: ");
  Serial.println(WiFi.localIP());

  server.on("/cor", handleCor);
  server.begin();
}
// =========================
// Loop
// =========================
void loop() {
  server.handleClient();
}