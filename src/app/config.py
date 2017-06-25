
ENV="DEV"

if ENV == "DEV":
    HOST = "127.0.0.1"
    PORT = 3000
    DEBUG = True

elif ENV == "PROD":
    HOST = "0.0.0.0"
    PORT = 80
    DEBUG = False