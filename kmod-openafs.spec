Name:		kmod-openafs
Version:	1.6.22.3
Release:	1.SL610%{?dist}
Summary:	Pull in OpenAFS kernel modules

BuildArch:      noarch

Group:		System Environment/Kernel
License:	GPL

Requires:	kmod-openafs-754
#Requires:	kmod-openafs-642
#Requires:	kmod-openafs-573
#Requires:	kmod-openafs-504
#Requires:	kmod-openafs-431
#Requires:	kmod-openafs-358
#Requires:	kmod-openafs-279
#Requires:	kmod-openafs-220
#Requires:	kmod-openafs-131
#Requires:	kmod-openafs-71

Provides:       openafs-kernel = %{version}-%{release}

%description
Pull in kernel modules for the current SL release, and (maybe) the previous one.

%files

%changelog
* Mon Jun 15 2016 Kevin M. Hill <kevinh@fnal.gov> = 1.6.18-1.SL68
- Update to current afs version
* Mon Jun 13 2016 Kevin M. Hill <kevinh@fnal.gov> = 1.6.17-1.SL68
- Updated for SL 6.8 
* Mon Jul 27 2015 Pat Riehecky <riehecky@fnal.gov> - 1.6.13-1.SL67
- Updated for SL 6.7
* Mon Oct 20 2014 Pat Riehecky <riehecky@fnal.gov> - 1.6.10-1.SL66
- Updated for SL 6.6
* Mon Nov 25 2013 Pat Riehecky <riehecky@fnal.gov> - 1.6.5.1-1.SL65
- Updated for SL 6.5
* Wed Apr 24 2013 Pat Riehecky <riehecky@fnal.gov> - 1.6.2-5.SL64
- Had a minor flip flop with version numbers.... no actual code changes
  just a build change
* Mon Feb 25 2013 Stephan Wiesand <stephan wiesand desy de> - 1.6.2-4.SL64
- SL64 build, to go out with the -358 kernel
* Mon Feb 25 2013 Stephan Wiesand <stephan wiesand desy de> - 1.6.2-3.SL63
- only require kmods for the current and previous SL releases, not all
* Sat Dec 22 2012 Stephan Wiesand <stephan wiesand desy de> - 1.6.2-2.SL63
- adapted to kmod-openafs-<nnn> instead of _<nnn>
* Thu Dec 13 2012 Stephan Wiesand <stephan wiesand desy de> - 1.6.2-1.SL63
- Initial build
