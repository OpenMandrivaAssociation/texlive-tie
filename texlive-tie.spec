%global tl_name tie
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Allow multiple web change files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/web/tie
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kpathsea)
Requires:	texlive(tie.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Tie was originally developed to allow web programmers to apply more than
one change file to their source. The program may also be used to create
a new version of a .web file that incorporates existing changes.

