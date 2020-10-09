FROM ubuntu:16.04

# Install prerequisites
RUN apt-get -y update && apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
RUN apt-get install -y python python3-dev python3-numpy python3-pip curl npm
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs
COPY /tag_reader_api /tag_reader_api
WORKDIR /tag_reader_api
RUN npm install --quiet
EXPOSE 8000
CMD ["node", "server.js"]