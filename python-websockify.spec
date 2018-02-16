%global pkgname websockify
%global summary WSGI based adapter for the Websockets protocol
Name:           python-%{pkgname}
Version:        0.8.0
Release:        8%{?dist}
Summary:        %{summary}

License:        LGPLv3
URL:            https://github.com/kanaka/websockify
Source0:        https://github.com/kanaka/websockify/archive/v%{version}.tar.gz#/websockify-%{version}.tar.gz
BuildArch:      noarch

%description
Python WSGI based adapter for the Websockets protocol

%package -n python2-%{pkgname}
Summary:        %{summary} - Python 2 version
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires:       python2-setuptools

%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname}
Python WSGI based adapter for the Websockets protocol - Python 2 version

%package -n python3-%{pkgname}
Summary:        %{summary} - Python 3 version
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-setuptools

%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
Python WSGI based adapter for the Websockets protocol - Python 3 version

%package doc
Summary:        %{summary} - documentation

%description doc
Python WSGI based adapter for the Websockets protocol - documentation

%prep
%autosetup -n %{pkgname}-%{version}

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%py2_build
%py3_build

%install
%py2_install
rm %{buildroot}%{_bindir}/*
%py3_install

rm -Rf %{buildroot}/usr/share/websockify
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 444 docs/websockify.1 %{buildroot}%{_mandir}/man1/

%files -n python2-%{pkgname}
%license LICENSE.txt
%{python2_sitelib}/websockify/
%{python2_sitelib}/websockify-%{version}-py?.?.egg-info

%files -n python3-%{pkgname}
%license LICENSE.txt
%{_mandir}/man1/websockify.1*
%{python3_sitelib}/websockify/
%{python3_sitelib}/websockify-%{version}-py?.?.egg-info
%{_bindir}/websockify

%files doc
%license LICENSE.txt
%doc docs

%changelog
* Fri Feb 16 2018 2018 Lumír Balhar <lbalhar@redhat.com> - 0.8.0-8
- Fix directory ownership

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuild for Python 3.6

* Mon Aug 29 2016 Jan Beran <jberan@redhat.com> - 0.8.0-3
- Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 19 2016 Solly Ross <sross@redhat.com> - 0.8.0-1
- Update to release 0.8.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Pádraig Brady <pbrady@redhat.com> - 0.6.0-2
- Support big endian systems - rhbz#1216219

* Mon Mar 23 2015 Nikola Đipanov <ndipanov@redhat.com> - 0.6.0-1
- Update to release 0.6.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Nikola Đipanov <ndipanov@redhat.com> - 0.5.1-1
- Update to release 0.5.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Pádraig Brady <P@draigBrady.com> - 0.4.1-1
- Update to release 0.4.1

* Tue Mar 12 2013 Pádraig Brady <P@draigBrady.com> - 0.2.0-4
- Add runtime dependency on setuptools

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 31 2012 Pádraig Brady <P@draigBrady.com> - 0.2.0-2
- Remove hard dependency on numpy

* Mon Oct 22 2012 Nikola Đipanov <ndipanov@redhat.com> - 0.2.0-1
- Moving to the upstream version 0.2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 6 2012 Adam Young <ayoung@redhat.com> - 0.1.0-4
- Added Description
- Added Manpage

* Fri May 11 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.1.0-2
- spec cleanup

* Thu May 10 2012 Adam Young <ayoung@redhat.com> - 0.1.0-1
- Initial RPM release.

