Name:           xrizer
Version:        %{?_version}
Release:        1%{?dist}
Summary:        A reimplementation of OpenVR on top of OpenXR.

License:        GNU General Public License v3.0
URL:            https://github.com/galister/motoc
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  gcc gcc-c++ make
BuildRequires:  cmake pkgconf-pkg-config
BuildRequires:  libX11-devel libXrandr-devel
BuildRequires:  libXinerama-devel libXcursor-devel
BuildRequires:  libXi-devel mesa-libGL-devel
BuildRequires:  libglvnd-devel vulkan-headers
BuildRequires:  vulkan-loader-devel jsoncpp-devel
BuildRequires:  libxcb-devel xcb-util-devel wayland-devel
BuildRequires:  libshaderc-devel glslc clang-devel

%description
xrizer is a reimplementation of OpenVR on top of OpenXR. This enables you to run OpenVR games through any OpenXR runtime without running SteamVR.

%prep
%autosetup -n %{name}-%{version}

%build
cargo xbuild --release

%install
install -Dpm0755 target/release/libxrizer.so %{buildroot}%{_libdir}/libxrizer.so

%files
%license LICENSE
%doc README.md
%{_libdir}/libxrizer.so

%changelog
* Fri Feb 13 2026 RedAzuki - %{version}-%{release}
- Initial Fedora RPM packaging
