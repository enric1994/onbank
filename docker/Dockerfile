
# Select a base image:

FROM python:3.7

# Install OS packages (from requirements_os.txt):

ADD docker/requirements_os.txt .
RUN apt update -y && apt install -y $(cat requirements_os.txt|grep -v '#')


# Install Python packages (from requirements.txt):

ADD docker/requirements.txt .
RUN pip install -r requirements.txt