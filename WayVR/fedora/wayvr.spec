Name:           wayvr
Version:        %{?_version}
Release:        1%{?dist}
Summary:        A lightweight OpenXR/OpenVR overlay for Wayland and X11 desktops.

License:        GPL-3.0-or-later
URL:            https://github.com/wlx-team/wayvr
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  pkgconf-pkg-config
BuildRequires:  python3
BuildRequires:  clang
BuildRequires:  openssl-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  glslang-devel
BuildRequires:  libshaderc-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  fontconfig-devel
BuildRequires:  dbus-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  wayland-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  pipewire-devel
BuildRequires:  openvr-devel
BuildRequires:  openxr-devel

%description
A lightweight OpenXR/OpenVR overlay for Wayland and X11 desktops.
This build enables all supported features (Wayland, X11, PipeWire, OpenVR, OpenXR, OSC).

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="${RUSTFLAGS:-} -C link-args=-Wl,-rpath,\$ORIGIN/../%{_lib}/%{name}"
cargo build --release --all-features

%install
install -Dpm0755 target/release/wayvr %{buildroot}%{_bindir}/wayvr
install -Dpm0755 target/release/wayvrctl %{buildroot}%{_bindir}/wayvrctl
mkdir -p %{buildroot}%{_libdir}/%{name}
install -Dpm0755 target/release/build/ovr_overlay_sys-*/out/libopenvr_api.so %{buildroot}%{_libdir}/%{name}/libopenvr_api.so

%files
%license LICENSE
%doc README.md
%{_bindir}/wayvr
%{_bindir}/wayvrctl
%dir %{_libdir}/%{name}
%{_libdir}/wayvr/libopenvr_api.so

%changelog
* Sun Feb 03 2026 RedAzuki - %{version}-%{release}
- Initial Fedora RPM packaging (all features)
