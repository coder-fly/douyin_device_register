FROM korekontrol/ubuntu-java-python3

EXPOSE 5000
WORKDIR /app/douyin
COPY  ./nativates/* /app/douyin/nativate/
COPY ./app.py /app/douyin
RUN pip3 install flask

CMD ["python3", "/app/douyin/app.py"]
