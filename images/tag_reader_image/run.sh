#!/bin/#!/usr/bin/env bash

docker stop $(docker ps -q)
docker rm $(docker ps -a -q)
docker image rm $(docker images | grep -v ubuntu)
docker build .  -t tag_reader_image
docker run -d -p 4416:8000 tag_reader_image
