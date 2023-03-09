FROM bvlc/caffe:gpu
# FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        libatlas-base-dev \
        git \
        vim \
        python-dev \
        python-pip \
        python-numpy \
        libopencv-dev \
        python-opencv \
        wget \
        sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG OPENPOSE_DIR=/root/openpose
ARG OPENPOSE_REPOSITORY_URL=https://github.com/CMU-Perceptual-Computing-Lab/openpose.git

RUN cd `dirname $OPENPOSE_DIR` \
  && git clone ${OPENPOSE_REPOSITORY_URL} \
  && cd $OPENPOSE_DIR \
  && sed -i -r -e '/hdf5/s/hdf5(_hl)?(:?_cpp)?\b/hdf5\1_cpp/g' \
       -e '/CAFFE_DIR.+lib/s#CAFFE_DIR\)/(:?build/)?lib#CAFFE_DIR)/build/lib#' \
       -e '/CAFFE_DIR.+include/s#\+= \$\(CAFFE_DIR\).*$#+= $(CAFFE_DIR)/build/include $(CAFFE_DIR)/include#' \
       scripts/ubuntu/Makefile.example \
  && sed -i -r -e '/CAFFE_DIR/s#:=.*$#:= /opt/caffe#' scripts/ubuntu/Makefile.config.Ubuntu16_cuda8_JetsonTX2 \
  && bash scripts/ubuntu/install_openpose_JetsonTX2_JetPack3.1.sh

WORKDIR ${OPENPOSE_DIR}
