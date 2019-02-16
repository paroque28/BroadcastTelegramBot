FROM python

WORKDIR /usr/src/app

# Copy requirements.txt first for better cache on later pushes
COPY ./requirements.txt /requirements.txt

# pip install python deps from requirements.txt on the resin.io build server
RUN pip install -r /requirements.txt
RUN git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive && cd python-telegram-bot && python setup.py install && cd .. && rm -rf python-telegram-bot
RUN mkdir ~/telegram
# This will copy all files in our root to the working  directory in the container
COPY . ./

# main.py will run when container starts up on the device
CMD ["python","-u","src/main.py"]
