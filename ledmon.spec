#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ledmon
Version  : 0.90
Release  : 1
URL      : https://github.com/intel/ledmon/archive/v0.90.tar.gz
Source0  : https://github.com/intel/ledmon/archive/v0.90.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ledmon-bin = %{version}-%{release}
Requires: ledmon-license = %{version}-%{release}
Requires: ledmon-man = %{version}-%{release}
BuildRequires : sg3_utils-dev
BuildRequires : systemd-dev

%description
This package contains the Enclosure LED Utilities, version 0.90
All files in this package can be freely distributed and used according
to the terms of the GNU General Public License, version 2.
See http://www.gnu.org/ for details.

%package bin
Summary: bin components for the ledmon package.
Group: Binaries
Requires: ledmon-license = %{version}-%{release}
Requires: ledmon-man = %{version}-%{release}

%description bin
bin components for the ledmon package.


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
%setup -q -n ledmon-0.90

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550792474
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1550792474
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ledmon
cp COPYING %{buildroot}/usr/share/package-licenses/ledmon/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ledctl
/usr/bin/ledmon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ledmon/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/ledmon.conf.5.gz
/usr/share/man/man8/ledctl.8.gz
/usr/share/man/man8/ledmon.8.gz
