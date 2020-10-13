FROM korekontrol/ubuntu-java-python3

EXPOSE 5000
WORKDIR /app
RUN pip3 install flask \
    && git clone https://github.com/coder-fly/douyin_device_register.git

CMD ["python3", "/app/douyin_device_register/app.py"]
