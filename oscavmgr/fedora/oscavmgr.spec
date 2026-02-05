Name:           oscavmgr
Version:        %{?_version}
Release:        1%{?dist}
Summary:        A face tracking relay VRCFT replacement, among other things

License:        MIT License
URL:            https://github.com/wlx-team/wayvr
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  openssl-devel
BuildRequires:  gcc gcc-c++ make
BuildRequires:  openvr-devel
BuildRequires:  openxr-devel

%description
A face tracking relay VRCFT replacement, among other things

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release

%install
install -Dpm0755 target/release/oscavmgr %{buildroot}%{_bindir}/oscavmgr

%files
%license LICENSE.md
%doc README.md
%{_bindir}/oscavmgr

%changelog
* Thu Feb 05 2026 RedAzuki - %{version}-%{release}
- Initial Fedora RPM packaging
