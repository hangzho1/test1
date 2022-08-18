FROM quay.io/centos/centos:stream8
WORKDIR /home

RUN dnf update -y && \
    dnf remove -y python36 && \    
dnf install -y git python39-pip curl wget numactl python39 python39-devel gcc && \
dnf --enablerepo=powertools install -y opencv && \
    pip3 install --upgrade pip && \
python3 -m pip3 install wheel tensorflow==2.8.2 neural-compressor==1.10.1 progress onnx tf2onnx onnxruntime sklearn setuptools
