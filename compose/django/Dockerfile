FROM python:3.5

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

#install geos
RUN cd ~ && wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
RUN cd ~ && tar xjf geos-3.4.2.tar.bz2
RUN cd ~/geos-3.4.2 && ./configure && make && make install

RUN pip install -r /requirements/production.txt \
    && groupadd -r django \
    && useradd -r -g django django

COPY . /app
RUN chown -R django /app

COPY ./compose/django/gunicorn.sh /gunicorn.sh
COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
