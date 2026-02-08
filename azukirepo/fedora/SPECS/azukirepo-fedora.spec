Name:           azukirepo-fedora
Version:        1.0
Release:        1
Summary:        AzukiRepo DNF repository configuration
License:        MIT
URL:            https://repo.redazuki.com/

BuildArch:      noarch

Source0:        azukirepo.repo
Source1:        RPM-GPG-KEY-azukirepo

Requires:       dnf
Requires(post): rpm

%description
Installs the RedAzuki RPM repository configuration and GPG key.

%prep
# nothing

%build
# nothing

%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
install -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/azukirepo.repo

mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-azukirepo

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/azukirepo.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-azukirepo

%changelog
* Sun Feb 08 2026 RedAzuki - 1.0-1
- Initial repo release package
