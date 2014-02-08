# revision 26689
# category TLCore
# catalog-ctan /web/tie
# catalog-date 2012-04-27 12:20:53 +0200
# catalog-license other-free
# catalog-version 2.4
Name:		texlive-tie
Version:	2.4
Release:	4
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

%description
Tie was originally developed to allow web programmers to apply
more than one change file to their source. The program may also
be used to create a new version of a web file that incorporates
existing changes.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/tie.1*
%doc %{_texmfdir}/doc/man/man1/tie.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4-3
+ Revision: 812925
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4-2
+ Revision: 756862
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4-1
+ Revision: 719741
- texlive-tie
- texlive-tie
- texlive-tie

