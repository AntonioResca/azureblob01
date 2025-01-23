# azureblob01
Esempio di accesso a  blob storage di Azure in python

step 0:
se non l'hai già fatto, installa azcli 

step 1:
cd <tua dir>
clona il repository
cd azureblob01
python3 -m venv venv
az login

per avere la connection string vai sul portale Azure
home>il tuo resource group>il tuo storage account>Security + networking>Access keys
copia la connection string della key1

aggiungi la definizione di "AZURE_STORAGE_CONNECTION_STRING" nel tuo local.settings.json

vedi la documentazione su:
https://learn.microsoft.com/en-us/python/api/overview/azure/storage-blob-readme?view=azure-python
