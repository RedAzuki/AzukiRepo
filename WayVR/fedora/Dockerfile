ARG FEDORA_VERSION
FROM fedora:${FEDORA_VERSION}

RUN dnf -y update && dnf -y install \
    git \
    rpmdevtools rpmlint rpm-build \
    rust cargo rust-packaging \
    gcc gcc-c++ make \
    pkgconf-pkg-config \
    cmake \
    python3 \
    clang \
    openssl-devel \
    spirv-tools-devel \
    glslang-devel \
    libshaderc-devel \
    jq curl tar gzip xz findutils which \
    libxkbcommon libxkbcommon-devel \
    fontconfig fontconfig-devel \
    dbus dbus-devel \
    alsa-lib alsa-lib-devel \
    wayland-devel \
    libX11-devel libXext-devel libXrandr-devel libxkbcommon-x11-devel \
    pipewire-devel \
    openvr-devel openxr-devel

RUN useradd -m builder
USER builder
WORKDIR /home/builder
RUN rpmdev-setuptree
