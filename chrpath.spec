Summary:	chrpath - change the rpath or runpath in binaries
Summary(pl.UTF-8):	chrpath - narzędzie do zmiany rpath lub runpath w binariach
Name:		chrpath
Version:	0.16
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	https://alioth-archive.debian.org/releases/chrpath/chrpath/%{version}/%{name}-%{version}.tar.gz

# Source0-md5:	2bf8d1d1ee345fc8a7915576f5649982
Patch1:		%{name}-multilib.patch
URL:		https://alioth.debian.org/projects/chrpath/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_chrpath	1

%description
chrpath changes, lists or removes the rpath or runpath setting in a
binary. The rpath, or runpath if it is present, is where the runtime
linker should look for the libraries needed for a program.

%description -l pl.UTF-8
chrpath zmienia, pokazuje lub usuwa ustawienia rpath lub runpath w
binariach. rpath lub runpath, jeśli jest ustawione, pokazuje miejsce,
w którym linker powinien szukać bibliotek wymaganych przez program.

%prep
%setup -q
%ifarch %{x8664} ppc64 s390x sparc64
%patch -P1 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA=""

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/chrpath
%ifarch %{x8664} ppc64 s390x sparc64
%attr(755,root,root) %{_libdir}/libchrpath*.so
%endif
%{_mandir}/man1/chrpath.1*
