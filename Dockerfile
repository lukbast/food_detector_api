FROM python:3

WORKDIR /food_detector
COPY . /food_detector
RUN pip install  -r requirements.txt
EXPOSE 6000
ENV API_ADDR="34.133.180.162:8605"
CMD ["python", "./main.py"]
