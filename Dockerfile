FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /sswebsite
WORKDIR /sswebsite

# Copy and install requirements (using pipenv)
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /sswebsite/Pipfile
RUN pipenv install --skip-lock --system --dev

# Copy entrypoint script
COPY ./entrypoint.sh /sswebsite/entrypoint.sh

# Copy project
COPY . /sswebsite/

# Run entrypoint script
ENTRYPOINT ["/sswebsite/entrypoint.sh"]

