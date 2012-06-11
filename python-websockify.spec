Name:           python-websockify
Version:        0.1.0
Release:        4%{?dist}
Summary:        WSGI based adapter for the Websockets protocol

License:        LGPLv3
URL:            https://github.com/kanaka/websockify
Source0:        https://github.com/downloads/kanaka/websockify/websockify-%{version}.tar.gz
Patch0:		websockify-0.1.1-manpage.patch
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       numpy
%description
Python WSGI based adapter for the Websockets protocol

%prep
%setup -q -n websockify-%{version}
%patch0 -p1

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

install websockify.py %{buildroot}/%{python_sitelib}
install websocket.py %{buildroot}/%{python_sitelib}
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 444 docs/websockify.1 %{buildroot}%{_mandir}/man1/


%files
%doc LICENSE.txt docs
%{_mandir}/man1/websockify.1*
%{python_sitelib}/websockify.py*
%{python_sitelib}/websocket.py*
%{python_sitelib}/websockify-%{version}-py?.?.egg-info
%{_bindir}/websockify



%changelog
* Wed Jun 6 2012  - Adam Young <ayoung@redhat.com> - 0.1.0-4
- Added Description
- Added Manpage

* Fri May 11 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.1.0-2
- spec cleanup

* Thu May 10 2012 Adam Young <ayoung@redhat.com> - 0.1.0-1
- Initial RPM release.
