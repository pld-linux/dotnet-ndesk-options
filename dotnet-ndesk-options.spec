Summary:	C# Program Options Parsing library
Summary(pl.UTF-8):	Biblioteka C# do analizy opcji programu
Name:		dotnet-ndesk-options
Version:	0.2.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.ndesk.org/archive/ndesk-options/ndesk-options-%{version}.tar.gz
# Source0-md5:	2d139bbf4c8be5197128195a65d1c98b
Patch0:		%{name}-monodir.patch
URL:		http://www.ndesk.org/Options
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	mono-csharp >= 1.9
BuildRequires:	mono-monodoc >= 1.9
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	mono >= 1.9
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NDesk.Options is a program option parser for C#, inspired by
Getopt::Long.

%description -l pl.UTF-8
NDesk.Options to biblioteka C# do analizy opcji programu, inspirowana
Getopt::Long.

%package devel
Summary:	Development files for ndesk Options C# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki C# ndesk Options
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mono-devel >= 1.9

%description devel
Development files for ndesk Options C# library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki C# ndesk Options.

%prep
%setup -q -n ndesk-options-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%dir %{_prefix}/lib/ndesk-options
%{_prefix}/lib/ndesk-options/NDesk.Options.dll

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/ndesk-options/Options.cs
%{_prefix}/lib/monodoc/sources/ndesk-options-docs.*
%{_pkgconfigdir}/ndesk-options.pc
