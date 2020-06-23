FROM python:3.6

COPY requirements.txt .
RUN pip install -rrequirements.txt

RUN git clone https://github.com/huggingface/torchMoji.git /var/src/torchMoji \
 && cd /var/src/torchMoji \
 && pip install -e . \
 && yes | python scripts/download_weights.py

COPY . /var/src/tweenie

CMD cd /var/src/tweenie && python tweenie.py
