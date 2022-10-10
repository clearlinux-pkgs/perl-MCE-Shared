#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MCE-Shared
Version  : 1.878
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-Shared-1.878.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-Shared-1.878.tar.gz
Summary  : 'MCE extension for sharing data supporting threads and processes'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-MCE-Shared-license = %{version}-%{release}
Requires: perl-MCE-Shared-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::FDPass)
BuildRequires : perl(MCE)
BuildRequires : perl(MCE::Flow)
BuildRequires : perl(MCE::Mutex)
BuildRequires : perl(MCE::Signal)
BuildRequires : perl(MCE::Util)

%description
## MCE::Shared for Perl
This document describes MCE::Shared version 1.878.
### Description

%package dev
Summary: dev components for the perl-MCE-Shared package.
Group: Development
Provides: perl-MCE-Shared-devel = %{version}-%{release}
Requires: perl-MCE-Shared = %{version}-%{release}

%description dev
dev components for the perl-MCE-Shared package.


%package license
Summary: license components for the perl-MCE-Shared package.
Group: Default

%description license
license components for the perl-MCE-Shared package.


%package perl
Summary: perl components for the perl-MCE-Shared package.
Group: Default
Requires: perl-MCE-Shared = %{version}-%{release}

%description perl
perl components for the perl-MCE-Shared package.


%prep
%setup -q -n MCE-Shared-1.878
cd %{_builddir}/MCE-Shared-1.878

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MCE-Shared
cp %{_builddir}/MCE-Shared-%{version}/Copying %{buildroot}/usr/share/package-licenses/perl-MCE-Shared/10a9a171b383cd4164956b76796943793854989d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MCE::Hobo.3
/usr/share/man/man3/MCE::Shared.3
/usr/share/man/man3/MCE::Shared::Array.3
/usr/share/man/man3/MCE::Shared::Base.3
/usr/share/man/man3/MCE::Shared::Cache.3
/usr/share/man/man3/MCE::Shared::Condvar.3
/usr/share/man/man3/MCE::Shared::Handle.3
/usr/share/man/man3/MCE::Shared::Hash.3
/usr/share/man/man3/MCE::Shared::Minidb.3
/usr/share/man/man3/MCE::Shared::Ordhash.3
/usr/share/man/man3/MCE::Shared::Queue.3
/usr/share/man/man3/MCE::Shared::Scalar.3
/usr/share/man/man3/MCE::Shared::Sequence.3
/usr/share/man/man3/MCE::Shared::Server.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MCE-Shared/10a9a171b383cd4164956b76796943793854989d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
