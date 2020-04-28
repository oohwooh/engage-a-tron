FROM python:3.7-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt

COPY api ./api/
COPY bot ./bot/
COPY database ./database/
COPY run_all.sh ./run_all.sh
RUN chmod +x ./run_all.sh
RUN chmod +x ./api/prod_run.sh

EXPOSE 8000

CMD ["./run_all.sh"]
