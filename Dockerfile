FROM ubuntu 

# Installing packages
RUN apt-get update 
RUN apt-get install -y python3-pip

# Setting up work directory
WORKDIR /

# Copying the requirements.txt file
COPY ./requirements.txt requirements.txt

# Installing project dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copying all the files and folders in the working directory container directory
COPY ./app.py app.py
ADD ./src src

# Setting up entry point, environment variables, and start command
ENTRYPOINT [ "python3" ]
RUN python3 -m nltk.downloader stopwords
CMD [ "app.py" ]