Summary:	chrpath - change the rpath or runpath in binaries
Summary(pl):	chrpath - narzêdzie do zmiany rpath lub runpath w binariach
Name:		chrpath
Version:	0.9
Release:	1
Patch0:		%{name}-SEGV.patch
License:	GPL
Group:		Applications/Editors
Source0:	ftp://ftp.hungry.com/pub/hungry/chrpath/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chrpath changes, lists or removes the rpath or runpath setting in a
binary. The rpath, or runpath if it is present, is where the runtime
linker should look for the libraries needed for a program.

%description -l pl
chrpath zmienia, pokazuje lub usuwa ustawienia rpath lub runpath w
binariach. rpath lub runpath, je¶li jest ustawione, pokazuje miejsce,
w którym linker powinien szukaæ bibliotek wymaganych przez program.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
