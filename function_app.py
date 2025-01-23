import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import logging
import json
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="getblob")
def getblob(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Parametri dello storage account
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = "mycontainer"
    try:
        # Creazione del client del servizio blob
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        # Recupera la lista dei blob
        blob_list = []
        for blob in container_client.list_blobs():
            blob_list.append({
                "name": blob.name,
                "size": blob.size,
                "last_modified": blob.last_modified.isoformat() if blob.last_modified else None
            })

        # Ritorna il JSON con i blob
        return func.HttpResponse(
            body=json.dumps({"blobs": blob_list}, indent=4),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        logging.error(f"Errore durante l'elaborazione: {str(e)}")
        return func.HttpResponse(
            body=json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )