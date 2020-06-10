FROM python:3.6

RUN pip install torch==1.0.1
RUN git clone https://github.com/huggingface/torchMoji.git /var/src/torchMoji

RUN cd /var/src/torchMoji \
 && pip install -e . \
 && yes | python scripts/download_weights.py

RUN pip install smalld==0.1.2

COPY . /var/src/tweenie

CMD cd /var/src/tweenie && python tweenie.py
