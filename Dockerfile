FROM gcr.io/google_appengine/python
LABEL maintainer qm28@georgetown.edu

# Create a virtualenv for the application dependencies.
RUN virtualenv -p python3 /env
ENV PATH /env/bin:$PATH

#Prevents Python from writing pyc files to disc (equivalent to python -B option)#
ENV PYTHONDONTWRITEBYTECODE 1
# So the logs can always write to container logs and not get buffered at first place
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt
ADD . /app

EXPOSE 8000
CMD gunicorn realestate.wsgi:application --bind 0.0.0.0:8000
#CMD gunicorn -b :8000 realestate.wsgi:application --timeout 90 
#CMD gunicorn realestate.wsgi:application --bind 0.0.0.0:8000



 
