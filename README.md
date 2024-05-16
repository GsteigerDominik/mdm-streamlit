# Docker Commands:
1. docker build -t dominikgsteiger/mdm-streamlit .
2. docker run --name mdm-streamlit -p 9000:8501 -d dominikgsteiger/mdm-streamlit
3. docker push dominikgsteiger/mdm-streamlit
# AZURE
1. az group create --name gsteidom-mdm-streamlit --location switzerlandnorth
2. az appservice plan create --name gsteidom-mdm-streamlit --resource-group gsteidom-mdm-streamlit --sku F1 --is-linux
3. az webapp create --resource-group gsteidom-mdm-streamlit --plan gsteidom-mdm-streamlit --name gsteidom-mdm-streamlit --deployment-container-image-name dominikgsteiger/mdm-streamlit:latest