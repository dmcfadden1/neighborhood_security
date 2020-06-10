FROM ubuntu:18.04

# Install prerequisites
RUN add-apt-repository -y ppa:alex-p/tesseract-ocr -y
RUN add-apt-repository ppa:alex-p/tesseract-ocr -y
RUN apt-get update -y
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y build-essential
RUN apt-get install -y cmake
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install -y libcurl3-dev
RUN apt-get install -y libleptonica-dev
RUN apt-get install -y liblog4cplus-dev
# RUN apt-get install -y libopencv-dev
RUN apt-get install -y libtesseract-dev
RUN apt-get install -y git
RUN apt-get install -y libssl1.0-dev
#RUN apt-get install -y node-gyp
RUN apt-get install -y nodejs
# RUN apt-get install -y npm
RUN apt-get install -y python
RUN apt-get install -y software-properties-common
RUN apt-get install -y beanstalkd
RUN apt-get install -y default-jdk
RUN apt-get install -y pkg-config
RUN apt-get install -y libgtk-3-dev
RUN apt-get install -y libavcodec-dev
RUN apt-get install -y libavformat-dev
RUN apt-get install -y libswscale-dev
RUN apt-get install -y libv4l-dev
RUN apt-get install -y libxvidcore-dev
RUN apt-get install -y libx264-dev
RUN apt-get install -y libjpeg-dev
RUN apt-get install -y libpng-dev
RUN apt-get install -y libtiff-dev
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y gfortran
RUN apt-get install -y openexr
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-numpy
RUN apt-get install -y libtbb2
RUN apt-get install -y libtbb-dev
RUN apt-get install -y libdc1394-22-dev
RUN apt install  -y tesseract-ocr -y

RUN mkdir ~/opencv_build && \
    cd ~/opencv_build && \
    git clone https://github.com/opencv/opencv.git && \
    git clone https://github.com/opencv/opencv_contrib.git

RUN cd ~/opencv_build/opencv && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON .. && \
    make -j8 && \
    make install && \
    pkg-config --modversion opencv4

# Copy all data
COPY /openalpr /openalpr
COPY /tag_reader_api /tag_reader_api

# Setup the build directory
RUN mkdir /openalpr/src/build

# Setup the compile environment
RUN cd /openalpr/src && \
    cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc && \
    make -j2 && \
    make install


RUN cp /openalpr/src/alpr /tag_reader_api/app/alpr

WORKDIR /tag_reader_api

RUN npm install --quiet
EXPOSE 8000
CMD ["node", "server.js"]
