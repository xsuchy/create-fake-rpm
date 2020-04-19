Name:           create-fake-rpm
Version:        1
Release:        0%{?dist}
License:        GPLv2+
Summary:        Generate fake (S)RPM
BuildArch:      noarch
# Sources can be obtained by
# git clone git://github.com/xsuchy/create-fake-rpm.git
# cd create-fake-rpm
# tito build --tgz
Source0:        %{name}-%{version}.tar.gz
URL:            https://github.com/xsuchy/create-fake-rpm

Requires:       rpm-build
BuildRequires:  asciidoc
BuildRequires:  libxslt

%description
Tool to generate an (s)rpm with faked provides.

%prep
%setup -q

%build
a2x -d manpage -f manpage create-fake-rpm.1.asciidoc
sed -i 's|^TEMPLATEDIR=.*|TEMPLATEDIR=%{_datadir}/%{name}/|' create-fake-rpm

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m755 create-fake-rpm %{buildroot}%{_bindir}
install -m644 create-fake-rpm.1 %{buildroot}/%{_mandir}/man1/
cp -a template/template.spec %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/create-fake-rpm
%doc %{_mandir}/man1/create-fake-rpm.1*
%{_datadir}/%{name}

%changelog

