FROM debian:stretch

ENV docker=TRUE

ADD ./digits/install/install1.sh ./
RUN ./install1.sh

ENV module=shotclock
ENV basemodule=shotclock

ADD ./digits/install/install2.sh ./
RUN ./install2.sh

ADD ./digits /home/digits/digits
RUN cd /home/digits/digits && rm IOPi && ln -s IOPiStub IOPi
RUN chown -R digits:digits /home/digits/digits


ADD ./digits/install/install3.sh ./
RUN ./install3.sh ${basemodule}

ADD ./digits/install/install4.sh ./
RUN ./install4.sh ${module}

EXPOSE 80

CMD service apache2 start && /bin/bash 
