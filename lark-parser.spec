#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lark-parser
Version  : 0.10.1
Release  : 27
URL      : https://files.pythonhosted.org/packages/0d/a5/60580c84bbc28f3952aec8f718e7311eb679a825f9c1d424d98a5542d7c0/lark-parser-0.10.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/a5/60580c84bbc28f3952aec8f718e7311eb679a825f9c1d424d98a5542d7c0/lark-parser-0.10.1.tar.gz
Summary  : a modern parsing library
Group    : Development/Tools
License  : MIT
Requires: lark-parser-license = %{version}-%{release}
Requires: lark-parser-python = %{version}-%{release}
Requires: lark-parser-python3 = %{version}-%{release}
Requires: regex
BuildRequires : buildreq-distutils3
BuildRequires : regex

%description
Lark is a modern general-purpose parsing library for Python.
        
        With Lark, you can parse any context-free grammar, efficiently, with very little code.

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
Provides: pypi(lark_parser)

%description python3
python3 components for the lark-parser package.


%prep
%setup -q -n lark-parser-0.10.1
cd %{_builddir}/lark-parser-0.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602720365
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lark-parser
cp %{_builddir}/lark-parser-0.10.1/LICENSE %{buildroot}/usr/share/package-licenses/lark-parser/af7225973c108376de2c312098b16c5a7a8828e6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lark-parser/af7225973c108376de2c312098b16c5a7a8828e6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
