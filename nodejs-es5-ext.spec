%{?scl:%scl_package nodejs-es5-ext}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename es5-ext
%global enable_tests 0
# tests disabled until we have the npm(tad) test suite

Name:		%{?scl_prefix}nodejs-es5-ext
Version:	0.10.12
Release:	2%{?dist}
Summary:	ECMAScript 5 extensions and ES6 shims

License:	MIT
URL:		https://github.com/medikoo/es5-ext.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tad)
%endif

Requires:	%{?scl_prefix}nodejs

%description
ECMAScript 5 extensions and ES6 shims

%prep
%setup -q -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js array/ boolean/ date/ error/ function/ \
	iterable/ math/ number/ object reg-exp string   \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{__nodejs} -e 'require("./")'
%{__nodejs} %{nodejs_sitelib}/tad/bin/tad
%else
echo "Tests are disabled..."
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.12-2
- Rebuild for rhscl

* Thu Jul 14 2016 Jared Smith <jsmith@fedoraproject.org> - 0.10.12-1
- Update to upstream 0.10.12 version

* Wed Feb 17 2016 Jared Smith <jsmith@fedoraproject.org> - 0.10.11-1
- Update to upstream 0.10.11 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Jared Smith <jsmith@fedoraproject.org> - 0.10.10-1
- Update to upstream 0.10.10 release

* Tue Nov 10 2015 Jared Smith <jsmith@fedoraproject.org> - 0.10.8-1
- Initial packaging
