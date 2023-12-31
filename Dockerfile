FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
ENV DJANGO_SETTINGS_MODULE=vinyls.DJANGO_SETTINGS_MODULE
EXPOSE 8000
CMD = ["python", "manage.py", "runserver", "0.0.0.0:8000"]