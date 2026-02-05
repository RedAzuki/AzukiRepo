ARG FEDORA_VERSION
FROM fedora:${FEDORA_VERSION}

RUN dnf -y update && dnf -y install \
    git \
    rpmdevtools rpmlint rpm-build \
    rust cargo rust-packaging \
    gcc gcc-c++ make \
    openssl-devel \
    openvr-devel openxr-devel

RUN useradd -m builder
USER builder
WORKDIR /home/builder
RUN rpmdev-setuptree
