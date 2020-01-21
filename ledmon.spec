#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ledmon
Version  : 0.93
Release  : 3
URL      : https://github.com/intel/ledmon/archive/0.93/ledmon-0.93.tar.gz
Source0  : https://github.com/intel/ledmon/archive/0.93/ledmon-0.93.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ledmon-bin = %{version}-%{release}
Requires: ledmon-license = %{version}-%{release}
Requires: ledmon-man = %{version}-%{release}
BuildRequires : sg3_utils-dev
BuildRequires : systemd-dev

%description
This package contains the Enclosure LED Utilities, version 0.93
All files in this package can be freely distributed and used according
to the terms of the GNU General Public License, version 2.
See http://www.gnu.org/ for details.

%package bin
Summary: bin components for the ledmon package.
Group: Binaries
Requires: ledmon-license = %{version}-%{release}

%description bin
bin components for the ledmon package.


%package doc
Summary: doc components for the ledmon package.
Group: Documentation
Requires: ledmon-man = %{version}-%{release}

%description doc
doc components for the ledmon package.


%package license
Summary: license components for the ledmon package.
Group: Default

%description license
license components for the ledmon package.


%package man
Summary: man components for the ledmon package.
Group: Default

%description man
man components for the ledmon package.


%prep
%setup -q -n ledmon-0.93
cd %{_builddir}/ledmon-0.93

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579637750
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1579637750
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ledmon
cp %{_builddir}/ledmon-0.93/COPYING %{buildroot}/usr/share/package-licenses/ledmon/74a8a6531a42e124df07ab5599aad63870fa0bd4
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ledctl
/usr/bin/ledmon

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ledmon/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ledmon/74a8a6531a42e124df07ab5599aad63870fa0bd4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/ledmon.conf.5.5
/usr/share/man/man8/ledctl.8.8
/usr/share/man/man8/ledmon.8.8
