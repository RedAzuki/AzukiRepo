Name:           vrcadvert
Version:        %{?_version}
Release:        1%{?dist}
Summary:        Advertise your OSC app via OSCQuery. To be used with VRChat.

License:        The Unlicense
URL:            https://github.com/galister/VrcAdvert
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  dotnet-sdk-8.0
BuildRequires:  dotnet-host

%global __brp_strip_lto %{nil}
%global __brp_strip_comment_note %{nil}
%global debug_package %{nil}

%description
Advertise your OSC app via OSCQuery. To be used with VRChat.
This is meant to be used with an OSC app that's not OSCQuery-ready.

%prep
%autosetup -n %{name}-%{version}

%build
dotnet publish -r linux-x64 --self-contained true -p:PublishSingleFile=true -p:PublishTrimmed=true

%install
install -Dpm0755 bin/Release/net8.0/linux-x64/publish/VrcAdvert %{buildroot}%{_bindir}/VrcAdvert

%files
%license LICENSE
%doc README.md
%{_bindir}/VrcAdvert

%changelog
* Thu Feb 05 2026 RedAzuki - %{version}-%{release}
- Initial Fedora RPM packaging
