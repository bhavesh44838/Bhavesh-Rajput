FROM nginx

WORKDIR /myapp

COPY . .

EXPOSE 80
