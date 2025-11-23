FROM nginx:alpine
WORKDIR /app
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
