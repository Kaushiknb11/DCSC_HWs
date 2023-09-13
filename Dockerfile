FROM python:3.9.1


WORKDIR /app
COPY pipeline.py pipeline_copy.py
#COPY laptopData.csv source.csv


RUN pip install pandas
RUN pip install numpy


ENTRYPOINT [ "python", "pipeline_copy.py" ]

