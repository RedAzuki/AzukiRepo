ARG FEDORA_VERSION
FROM fedora:${FEDORA_VERSION}

RUN dnf -y update && dnf -y install \
    git \
    rpmdevtools rpmlint rpm-build \
    dotnet-sdk-8.0 dotnet-host

RUN useradd -m builder
USER builder
WORKDIR /home/builder
RUN rpmdev-setuptree
