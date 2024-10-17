Name:		texlive-tie
Version:	70015
Release:	1
Summary:	Allow multiple web change files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/web/tie
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tie.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-tie.bin

%description
Tie was originally developed to allow web programmers to apply
more than one change file to their source. The program may also
be used to create a new version of a .web file that
incorporates existing changes.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/tie.1*
%doc %{_texmfdistdir}/doc/man/man1/tie.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
