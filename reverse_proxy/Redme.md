

### Build and Run

Para construir la imagen y levantar el contenedor ejecutar:

```
docker build -t reverseproxy:1.0.0 .

docker run -it --name proxy -p 80:80 --link=obras --link=ratings  --rm reverseproxy:1.0.0
```

### Test

```
CURL http://localhost/obras-catalog-service/obras

CURL http://localhost/ratings-service/1
```



### Referencias

* [How to install Nginx as a reverse proxy server with Docker](http://www.littlebigextra.com/install-nginx-reverse-proxy-server-docker/)

*[Use NGINX As A Reverse Proxy To Your Containerized Docker Applications](https://www.thepolyglotdeveloper.com/2017/03/nginx-reverse-proxy-containerized-docker-applications/)