# revision 23089
# category TLCore
# catalog-ctan /web/tie
# catalog-date 2009-11-10 08:50:14 +0100
# catalog-license other-free
# catalog-version 2.4
Name:		texlive-tie
Version:	2.4
Release:	1
Summary:	Allow multiple web change files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/web/tie
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tie.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tie.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-tie.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Tie was originally developed to allow web programmers to apply
more than one change file to their source. The program may also
be used to create a new version of a web file that incorporates
existing changes.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/tie.1*
%doc %{_texmfdir}/doc/man/man1/tie.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
