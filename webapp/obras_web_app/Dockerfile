FROM node:12.2.0-alpine as builder
# RUN mkdir /usr/src/app
# WORKDIR /usr/src/app

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json

RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent

COPY . /app
RUN npm run build




FROM nginx:1.16.0-alpine
RUN apk add --no-cache jq
# RUN rm -rf /etc/nginx/conf.d
# COPY conf /etc/nginx
COPY --from=builder /app/build /usr/share/nginx/html
COPY docker-entrypoint.sh /
COPY generate_config_js.sh /
RUN chmod +x docker-entrypoint.sh generate_config_js.sh
 
ENTRYPOINT ["/docker-entrypoint.sh"]