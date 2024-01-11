%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-cpio
Version:        0.1
Release:        29%{?dist}
Summary:        A Python module for accessing cpio archives

License:        LGPLv2+
URL:            http://developer.berlios.de/projects/python-cpio/
Source0:        http://download.berlios.de/python-cpio/python-cpio-0.1.tar.bz2
Patch0:         cpioarchive_supports_2_3.patch
Patch1:         cpioarchive_bytes_str_compatibility.patch

BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-devel
%endif
BuildRequires:  python3-devel

%global _description\
This is a Python module for accessing cpio archives.

%description %_description

%if %{with python2}
%package -n python2-cpio
Summary: %summary
%{?python_provide:%python_provide python2-cpio}

%description -n python2-cpio %_description
%endif

%package -n python3-cpio
Summary:	A Python module for accessing cpio archives

%description -n python3-cpio
This is a Python module for accessing cpio archives.

%prep
%setup -q
%patch0
%patch1

%build
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%if %{with python2}
%py2_install
%endif
%py3_install

%if %{with python2}
%files -n python2-cpio
%license COPYING.lib
%doc AUTHORS ChangeLog README TODO
%{python2_sitelib}/cpioarchive.py*
%{python2_sitelib}/*.egg-info
%endif

%files -n python3-cpio
%license COPYING.lib
%doc AUTHORS ChangeLog README TODO
%{python3_sitelib}/cpioarchive.py*
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/*.egg-info


%changelog
* Mon Nov 12 2018 Watson Yuuma Sato <wsato@redhat.com> - 0.1-29
- Fix for python3 compatibility - bytes to str (rhbz#1638499)

* Wed Jul 04 2018 Lumír Balhar <lbalhar@redhat.com> - 0.1-28
- Python 2 subpackage disabled by default

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-26
- Python 2 binary package renamed to python2-cpio
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-23
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-22
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug 14 2015 José Matos <jamatos@fedoraproject.org> - 0.1-19
- Add python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 8 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1-10
- Update for new python guidelines
- Fix spec so that EPEL-6 will build

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1-7
- Rebuild for Python 2.6

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1-6
- fix license tag

* Tue Apr  1 2008 José Matos <jamatos[AT]fc.up.pt> - 0.1-5
- Add egg-info for F9+.

* Tue Aug 28 2007 José Matos <jamatos[AT]fc.up.pt> - 0.1-4
- License fix, rebuild for devel (F8).

* Tue Dec 12 2006 José Matos <jamatos[AT]fc.up.pt> - 0.1-3
- Rebuild for python 2.5.

* Mon Sep 11 2006 José Matos <jamatos[AT]fc.up.pt> - 0.1-2
- Rebuild for FC6.

* Tue Jan  3 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1-1
- Initial RPM release
