FROM python:3.9

EXPOSE 80

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

# Assuming dependencies do not change, everything above will not have to be rerun when rebuilding the image
COPY . /app

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:80", "wsgi:app" ]