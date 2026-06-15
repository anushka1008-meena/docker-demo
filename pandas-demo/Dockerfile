FROM python:slim

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY 1st.py .

CMD ["python","1st.py"]