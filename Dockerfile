 #Using the base image with python 3.9
FROM python:3.9

# Copy local directory to /app in container
COPY . /app/

#Set our working directory as app
WORKDIR /app 

RUN pip install -r requirements.txt

# Expose port and run the application when the container is started
EXPOSE 9999:9999
ENTRYPOINT python flask_api.py 9999
# CMD ["flask_api.py"]