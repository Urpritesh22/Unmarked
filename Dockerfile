
FROM python:3.12-slim

# for Setting the working directory..
WORKDIR /app

# to copy the requirements file
COPY requirements.txt .

# for  Installing the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# this will copy the application code
COPY . .


EXPOSE 5000

# this is for executing the app...
CMD ["python", "app1.py"]  
