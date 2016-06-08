Summary:	Wrapper library for DNS name resolving or DNS faking
Summary(pl.UTF-8):	Biblioteka obudowująca do rozwiązywania lub fałszowania nazw DNS
Name:		resolv_wrapper
Version:	1.1.4
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://www.samba.org/ftp/cwrap/%{name}-%{version}.tar.gz
# Source0-md5:	bb4f8b1a02817ecb0781215eed830d12
URL:		https://cwrap.org/resolv_wrapper.html
BuildRequires:	cmake >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
resolv_wrapper makes it possible on most UNIX platforms to contact
your own DNS implmentation in your test environment. It requires
socket_wrapper to be able to contact the server. Alternatively, the
wrapper is able to fake DNS queries and return valid responses to your
application.

%description -l pl.UTF-8
resolv_wrapper umożliwia kontaktowanie się z własną implementacją DNS
w środowisku testowym na większości platform uniksowych. Wymaga
socket_wrappera w celu połączenia się z serwerem. Alternatywnie
pozwala sfałszować zapytanai DNS i zwracać aplikacji poprawne
odpowiedzi.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libresolv_wrapper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libresolv_wrapper.so.0
%attr(755,root,root) %{_libdir}/libresolv_wrapper.so
%{_pkgconfigdir}/resolv_wrapper.pc
%{_libdir}/cmake/resolv_wrapper
%{_mandir}/man1/resolv_wrapper.1*
