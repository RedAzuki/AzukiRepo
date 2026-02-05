Name:           motoc
Version:        %{?_version}
Release:        1%{?dist}
Summary:        Monado Tracking Origin Calibrator

License:        GNU General Public License v3.0
URL:            https://github.com/galister/motoc
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  gcc gcc-c++ make
BuildRequires:  openvr-devel
BuildRequires:  openxr-devel

%description
This tool allows users to calibrate devices of different tracking origins (tracking technologies) to work together.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release

%install
install -Dpm0755 target/release/motoc %{buildroot}%{_bindir}/motoc

%files
%license LICENSE
%doc README.md
%{_bindir}/motoc

%changelog
* Thu Feb 05 2026 RedAzuki - %{version}-%{release}
- Initial Fedora RPM packaging
