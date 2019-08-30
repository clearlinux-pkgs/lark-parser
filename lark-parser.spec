#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lark-parser
Version  : 0.7.4
Release  : 9
URL      : https://files.pythonhosted.org/packages/db/e3/0fd07ef281655418b6f76a26958635aac7a65845b2ec52dd553093f3789b/lark-parser-0.7.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/db/e3/0fd07ef281655418b6f76a26958635aac7a65845b2ec52dd553093f3789b/lark-parser-0.7.4.tar.gz
Summary  : a modern parsing library
Group    : Development/Tools
License  : MIT
Requires: lark-parser-license = %{version}-%{release}
Requires: lark-parser-python = %{version}-%{release}
Requires: lark-parser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Lark - a modern parsing library for Python
Parse any context-free grammar, FAST and EASY!

%package license
Summary: license components for the lark-parser package.
Group: Default

%description license
license components for the lark-parser package.


%package python
Summary: python components for the lark-parser package.
Group: Default
Requires: lark-parser-python3 = %{version}-%{release}

%description python
python components for the lark-parser package.


%package python3
Summary: python3 components for the lark-parser package.
Group: Default
Requires: python3-core

%description python3
python3 components for the lark-parser package.


%prep
%setup -q -n lark-parser-0.7.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567181696
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lark-parser
cp LICENSE %{buildroot}/usr/share/package-licenses/lark-parser/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lark-parser/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
