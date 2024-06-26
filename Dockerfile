FROM python:3.10.0

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501
CMD ["sh", "-c", "streamlit run --server.port 8501 /usr/app/app.py"]