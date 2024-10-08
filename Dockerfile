FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone -b 0.5/label https://github.com/DE32-3rd-team2/streamlit.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "src/t2_streamlit/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
