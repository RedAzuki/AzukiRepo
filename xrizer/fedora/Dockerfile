ARG FEDORA_VERSION
FROM fedora:${FEDORA_VERSION}

RUN dnf -y update && dnf -y install \
    git \
    rpmdevtools rpmlint rpm-build \
    rust cargo rust-packaging \
    cmake make gcc gcc-c++ pkgconf-pkg-config \
    libX11-devel libXrandr-devel libXinerama-devel \
    libXcursor-devel libXi-devel mesa-libGL-devel \
    libglvnd-devel vulkan-headers \
    vulkan-loader-devel jsoncpp-devel \
    libxcb-devel xcb-util-devel wayland-devel \
    libshaderc-devel glslc clang-devel

RUN useradd -m builder
USER builder
WORKDIR /home/builder
RUN rpmdev-setuptree
