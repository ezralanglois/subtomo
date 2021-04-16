# docker build --rm -t ezralanglois/subtomo -f ./docker/Dockerfile  ./


FROM centos:7
ENV PATH="/opt/EMAN2/bin:/opt/EMAN2/extlib/bin:${PATH}"
ENV PYTHONPATH="/opt/EMAN2/lib:/opt/EMAN2/bin"
ENV GIT_SSL_NO_VERIFY false
WORKDIR /tmp
COPY ./docker/requirements.sh /tmp/requirements.sh
COPY ./scripts /opt/scripts
RUN bash /tmp/requirements.sh
RUN rm -frv /tmp/*

CMD ["/opt/scripts/version.py"]
ENTRYPOINT ["python"]
