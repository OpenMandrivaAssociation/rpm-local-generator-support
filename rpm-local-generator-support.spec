Summary: RPM local_generator support
Name: rpm-local-generator-support
Version: 1
Release: 1

# It is not really clear if the one empty file shipped by this package is even
# copyrightable. But let's go with GPLv2+ which is the license used by RPM,
# where this file should ideally come from or be replaced by different
# implementation.
#
# The license was discussed in this thread:
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/X6RUQK5R6KIMVIQ6FQPNVGTJJXSNRD4V/
License: GPLv2+
URL: https://src.fedoraproject.org/rpms/rpm-local-generator-support
Source1: README.md
BuildArch: noarch

%description
local_generator.attr file enabling RPM dependency generator to be used on .spec
files, which ships them.

%prep

%build

%install
install %{SOURCE1} %{basename %{SOURCE1}}

install -d %{buildroot}%{_fileattrsdir}
touch %{buildroot}%{_fileattrsdir}/local_generator.attr

%files
%doc README.md
%{_fileattrsdir}/local_generator.attr
