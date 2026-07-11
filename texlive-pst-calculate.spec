%global tl_name pst-calculate
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	Support for floating point operations at LaTeX level
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-calculate
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calculate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calculate.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an interface to the LaTeX3 floating point unit
(part of expl3), mainly used for PSTricks related packages to allow math
expressions at LaTeX level. siunitx is used for formatting the
calculated number. The package also depends on xkeyval and xparse.

