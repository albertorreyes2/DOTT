FROM python:3-alpine

WORKDIR /app

COPY ./DOTT/cidr_conver_api/python/requirements.txt
RUN pip3 install -r requirements.txt

pwd

COPY . .
CMD ["ash", "-c", "python api.py"]
# docker build -t pym .
# docker run -ti -p 8000:8000 pym