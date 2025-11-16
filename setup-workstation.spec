Name:           setup-workstation
Version:        2025.11.1
Release:        1%{?dist}
Summary:        Ansible-based Workstation Setup

License:        MIT
URL:            https://github.com/c4t3l/setup-workstation
Source0:        %{url}/archive/%{version}/setup-workstation-%{version}.tar.gz

BuildRequires:  ansible
Requires:       ansible
Requires:       ansible-collection-community-general

BuildArch:      noarch

%description
KDE-based workstation setup and initial configuration.

%prep
%autosetup


%build
# Nothing to build


%install
install -D -p -m 0644 -t %{buildroot}/opt/setup-workstation default.yml
install -D -p -m 0644 -t %{buildroot}/opt/setup-workstation hosts
install -D -p -m 0755 -t %{buildroot}/opt/setup-workstation/vars vars/*
cp -prv roles %{buildroot}/opt/setup-workstation/.


%check
ansible-playbook --check --inventory hosts default.yml 

%files
%license LICENSE
%doc README.md
/opt/setup-workstation/



%changelog
* Sat Nov 15 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.1
- Initial build
