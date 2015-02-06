%define upstream_name    Dist-Zilla-PluginBundle-CJM
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Get distribution version from its main_module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Hash::Merge::Simple)
BuildRequires:	perl(Module::Build::ModuleInfo)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Pod::Loom)
BuildRequires:	perl(autodie)
BuildArch:	noarch

%description
If included, this plugin will process each _.pm_ and _.pod_ file under
_lib_ or in the root directory through Pod::Loom.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

