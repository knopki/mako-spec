%global provider        github
%global provider_tld    com
%global project         emersion
%global repo            mako
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}

Name:           mako
Version:        1.1
Release:        1%{?dist}
Summary:        A lightweight notification daemon for Wayland.
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}.tar.gz

Requires:       systemd
Requires:       pango
Requires:       cairo
BuildRequires:  wayland-protocols-devel
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel

%description
%{summary}.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_bindir}/makoctl
%{_bindir}/mako

%changelog
* Sat Oct 20 2018 Sergey Korolev <korolev.srg@gmail.com> - 1.1-1
- Initial package
