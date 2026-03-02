const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.raw({ type: "application/octet-stream", limit: "10mb" }));

// =============================
// CONFIGURE AQUI
// =============================

const predictionKey = "SUA_PREDICTION_KEY";
const endpoint = "https://SEU-RECURSO.cognitiveservices.azure.com";
const projectId = "SEU_PROJECT_ID";
const iterationName = "Iteration1";

// =============================

app.post("/classificar", async (req, res) => {

    try {

        console.log("Recebendo imagem...");

        const response = await axios.post(
            `${endpoint}/customvision/v3.0/Prediction/${projectId}/classify/iterations/${iterationName}/image`,
            req.body,
            {
                headers: {
                    "Prediction-Key": predictionKey,
                    "Content-Type": "application/octet-stream"
                }
            }
        );

        console.log("Resposta recebida do Azure!");

        res.json(response.data);

    } catch (error) {

        console.log("ERRO NO AZURE:");
        console.log(error.response?.data || error.message);

        res.status(500).json({
            erro: error.response?.data || error.message
        });
    }
});

app.listen(3000, () => {
    console.log("Servidor rodando em http://localhost:3000");
});