Name: python-module-adns
Version: 1.1.0
Release: alt0.2.1

Summary: A Python module for the ADNS library
Group: Development/Python
License: GPL
Url: http://dustman.net/andy/python/adns-python

%setup_python_module adns-python

Source: %modulename-%version.tar.gz

Requires: libadns

Provides: adns-python = %version

BuildPreReq: libadns-devel

%description
%name is a Python module that interfaces to the adns asynchronous
resolver library.

%define python_libdir %_libdir/python%__python_version
%define python_site_packages_dir %python_libdir/site-packages
%define python_includedir %_includedir/python%__python_version

%prep
%setup -q -n %modulename-%version

%build
export CFLAGS="$RPM_OPT_FLAGS"
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --optimize=2

%files
%python_site_packages_dir
%doc README PKG-INFO

%changelog
* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.0-alt0.2.1
- Rebuilt with python-2.4.

* Mon Mar 07 2005 LAKostis <lakostis at altlinux.ru> 1.1.0-alt0.2
- First build for Sisyphus.

