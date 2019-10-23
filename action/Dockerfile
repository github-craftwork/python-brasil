FROM python:3.7.5

RUN pip install os
RUN pip install json
RUN pip install requests

COPY . .

CMD ["python", "./action/run.py"]
