FROM ubuntu:20.04
WORKDIR /home

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget curl llvm \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    libunwind8-dev \
    rsync 
# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

# install required package
RUN pip3 install numpy==1.19.5 \
          pandas==1.3.5 
RUN pip3 install https://github.com/intel/intel-extension-for-pytorch/releases/download/v1.10.0/intel_extension_for_pytorch-1.10.0+cpu-cp37-cp37m-linux_x86_64.whl
RUN pip3 install torch==1.10.0 \
          neural_compressor==1.10.1 \
          onnx==1.11.0 \
          onnxruntime==1.10.0 \
          tqdm==4.64.0 \
          protobuf==3.20.1
