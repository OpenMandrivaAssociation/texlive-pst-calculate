Name:		texlive-pst-calculate
Version:	49817
Release:	1
Summary:	Support for floating point operations at LaTeX level
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-calculate
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calculate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calculate.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an interface to the LaTeX3 floating point
unit (part of expl3), mainly used for PSTricks related packages
to allow math expressions at LaTeX level. siunitx is used for
formatting the calculated number. The package also depends on
xkeyval and xparse.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-calculate
%doc %{_texmfdistdir}/doc/generic/pst-calculate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
