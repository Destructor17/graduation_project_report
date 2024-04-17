FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y curl libfontconfig1 cpanminus
RUN curl -L -o install-tl-unx.tar.gz https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
RUN tar xzf install-tl-unx.tar.gz && mv install-tl-???????? install-tl
RUN cpanm Pod::Usage
RUN ./install-tl/install-tl --no-interaction
RUN apt-get install -y inotify-tools
# RUN /usr/local/texlive/????/bin/*/tlmgr install linguex

CMD [ "sh", "/build/graduation_project_report_common/docker/_build.sh"]
