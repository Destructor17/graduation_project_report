FROM miktex/miktex:essential
RUN apt-get update -y
RUN apt-get install -y make
RUN apt-get install -y python3
USER root
ENTRYPOINT [ "/bin/sh", "-c" ]
