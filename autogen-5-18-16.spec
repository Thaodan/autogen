Summary:    AutoGen - The Automated Program Generator
Name:       autogen
Version:    5.18.16
Vendor:     Bruce Korb http://www.gnu.org/software/autogen
Release:    1
License:    GPL
Source:     ftp://ftp.gnu.org/gnu/autogen/rel5.18.16/autogen-5.18.16.tar.gz
BuildRoot:  %{_tmppath}/%{name}-root
BuildRequires:  pkgconfig(guile-2.2)
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	make
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(lib)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl(warnings)

%description
AutoGen is a tool designed for generating program files that contain
repetitive text with varied substitutions.  Its goal is to simplify the
maintenance of programs that contain large amounts of repetitious text.
This is especially valuable if there are several blocks of such text
that must be kept synchronized in parallel tables.

Some parts are released under different licensing:

libopts LGPL  This is a tear-off, redistributable option processing library
autofsm BSD   This is a template for producing finite state machine programs

The Copyright itself is privately held by Bruce Korb.
Copyright (C) 1992-2018 by Bruce Korb.  All rights reserved.  Licensed under GPL, version 2 or later.
%prep
%setup -q -n %{name}-%{version}/%{name}-%{version}
chmod -R +rw *

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-format-overflow -Wno-format-truncation -Wno-implicit-fallthrough"
%configure --disable-static --disable-dependency-tracking
%{make_build}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}
rm -f ${RPM_BUILD_ROOT}/usr/lib/libopts.la
rm -f ${RPM_BUILD_ROOT}/usr/share/info/dir

%post
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc NEWS COPYING TODO README THANKS AUTHORS
%{_datadir}/aclocal/*
%{_includedir}/autoopts
%{_datadir}/autogen
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_infodir}/*
%{_bindir}/*
%{_libdir}/libopts.so*
%{_libdir}/autogen
%{_libdir}/pkgconfig/*.pc


%changelog
* Sun Aug 26 2018 Bruce Korb,,, <bkorb@> Regenerated
* Sun May  6 2012 Install only existing files to doc directory.
- Omit NOTES and VERSION.
* Fri Dec 31 2004 Bruce Korb <bkorb@gnu.org> Restored the file list
* Wed Oct 27 2004 Ed Swierk <eswierk@users.sf.net> fixed up for Fedora
* Tue Dec 16 2003 Richard Zidlicky <rz@linux-m68k.org> 5.5.7pre5-5
- fix %%doc
- add post/pre scriptlets
- change default prefix
* Sat Mar 15 2003 Bruce Korb <bkorb@gnu.org>
- Rework as a template to automatically produce a properly configured RPM
* Fri Aug 9 2002 Bruce Korb <bkorb@gnu.org>
- Pull stuff from Thomas Steudten's version of this file
