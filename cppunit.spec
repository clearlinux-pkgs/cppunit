#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cppunit
Version  : 1.15.1
Release  : 23
URL      : https://dev-www.libreoffice.org/src/cppunit-1.15.1.tar.gz
Source0  : https://dev-www.libreoffice.org/src/cppunit-1.15.1.tar.gz
Summary  : The C++ Unit Test Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: cppunit-bin = %{version}-%{release}
Requires: cppunit-lib = %{version}-%{release}
Requires: cppunit-license = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : pkgconfig(cppunit)

%description
CppUnit --- The C++ Unit Test Library
-------------------------------------
http://www.freedesktop.org/wiki/Software/cppunit

%package bin
Summary: bin components for the cppunit package.
Group: Binaries
Requires: cppunit-license = %{version}-%{release}

%description bin
bin components for the cppunit package.


%package dev
Summary: dev components for the cppunit package.
Group: Development
Requires: cppunit-lib = %{version}-%{release}
Requires: cppunit-bin = %{version}-%{release}
Provides: cppunit-devel = %{version}-%{release}
Requires: cppunit = %{version}-%{release}

%description dev
dev components for the cppunit package.


%package doc
Summary: doc components for the cppunit package.
Group: Documentation

%description doc
doc components for the cppunit package.


%package lib
Summary: lib components for the cppunit package.
Group: Libraries
Requires: cppunit-license = %{version}-%{release}

%description lib
lib components for the cppunit package.


%package license
Summary: license components for the cppunit package.
Group: Default

%description license
license components for the cppunit package.


%prep
%setup -q -n cppunit-1.15.1
cd %{_builddir}/cppunit-1.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580323691
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static LDFLAGS="$LDFLAGS -ldl" --datadir=/usr/share/doc
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export GCC_IGNORE_WERROR=1 && make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1580323691
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cppunit
cp %{_builddir}/cppunit-1.15.1/COPYING %{buildroot}/usr/share/package-licenses/cppunit/0dfecfda4aed0dfbc3764e798a72b3b8ed9073c4
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/DllPlugInTester

%files dev
%defattr(-,root,root,-)
/usr/include/cppunit/AdditionalMessage.h
/usr/include/cppunit/Asserter.h
/usr/include/cppunit/BriefTestProgressListener.h
/usr/include/cppunit/CompilerOutputter.h
/usr/include/cppunit/Exception.h
/usr/include/cppunit/Message.h
/usr/include/cppunit/Outputter.h
/usr/include/cppunit/Portability.h
/usr/include/cppunit/Protector.h
/usr/include/cppunit/SourceLine.h
/usr/include/cppunit/SynchronizedObject.h
/usr/include/cppunit/Test.h
/usr/include/cppunit/TestAssert.h
/usr/include/cppunit/TestCaller.h
/usr/include/cppunit/TestCase.h
/usr/include/cppunit/TestComposite.h
/usr/include/cppunit/TestFailure.h
/usr/include/cppunit/TestFixture.h
/usr/include/cppunit/TestLeaf.h
/usr/include/cppunit/TestListener.h
/usr/include/cppunit/TestPath.h
/usr/include/cppunit/TestResult.h
/usr/include/cppunit/TestResultCollector.h
/usr/include/cppunit/TestRunner.h
/usr/include/cppunit/TestSuccessListener.h
/usr/include/cppunit/TestSuite.h
/usr/include/cppunit/TextOutputter.h
/usr/include/cppunit/TextTestProgressListener.h
/usr/include/cppunit/TextTestResult.h
/usr/include/cppunit/TextTestRunner.h
/usr/include/cppunit/XmlOutputter.h
/usr/include/cppunit/XmlOutputterHook.h
/usr/include/cppunit/config-auto.h
/usr/include/cppunit/config/CppUnitApi.h
/usr/include/cppunit/config/SelectDllLoader.h
/usr/include/cppunit/config/SourcePrefix.h
/usr/include/cppunit/config/config-bcb5.h
/usr/include/cppunit/config/config-evc4.h
/usr/include/cppunit/config/config-mac.h
/usr/include/cppunit/config/config-msvc6.h
/usr/include/cppunit/extensions/AutoRegisterSuite.h
/usr/include/cppunit/extensions/ExceptionTestCaseDecorator.h
/usr/include/cppunit/extensions/HelperMacros.h
/usr/include/cppunit/extensions/Orthodox.h
/usr/include/cppunit/extensions/RepeatedTest.h
/usr/include/cppunit/extensions/TestCaseDecorator.h
/usr/include/cppunit/extensions/TestDecorator.h
/usr/include/cppunit/extensions/TestFactory.h
/usr/include/cppunit/extensions/TestFactoryRegistry.h
/usr/include/cppunit/extensions/TestFixtureFactory.h
/usr/include/cppunit/extensions/TestNamer.h
/usr/include/cppunit/extensions/TestSetUp.h
/usr/include/cppunit/extensions/TestSuiteBuilderContext.h
/usr/include/cppunit/extensions/TestSuiteFactory.h
/usr/include/cppunit/extensions/TypeInfoHelper.h
/usr/include/cppunit/plugin/DynamicLibraryManager.h
/usr/include/cppunit/plugin/DynamicLibraryManagerException.h
/usr/include/cppunit/plugin/PlugInManager.h
/usr/include/cppunit/plugin/PlugInParameters.h
/usr/include/cppunit/plugin/TestPlugIn.h
/usr/include/cppunit/plugin/TestPlugInDefaultImpl.h
/usr/include/cppunit/portability/FloatingPoint.h
/usr/include/cppunit/portability/Stream.h
/usr/include/cppunit/tools/Algorithm.h
/usr/include/cppunit/tools/StringHelper.h
/usr/include/cppunit/tools/StringTools.h
/usr/include/cppunit/tools/XmlDocument.h
/usr/include/cppunit/tools/XmlElement.h
/usr/include/cppunit/ui/text/TestRunner.h
/usr/include/cppunit/ui/text/TextTestRunner.h
/usr/lib64/libcppunit.so
/usr/lib64/pkgconfig/cppunit.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/cppunit/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcppunit-1.15.so.1
/usr/lib64/libcppunit-1.15.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cppunit/0dfecfda4aed0dfbc3764e798a72b3b8ed9073c4
