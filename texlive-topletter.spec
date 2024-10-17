Name:		texlive-topletter
Version:	48182
Release:	2
Summary:	Letter class for the Politecnico di Torino
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/topletter
License:	apache2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topletter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topletter.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topletter.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class for typesetting letters
conforming to the official Corporate Image guidelines for the
Politecnico di Torino. The class can be used for letters
written in Italian and in English.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/topletter
%{_texmfdistdir}/tex/latex/topletter
%doc %{_texmfdistdir}/doc/latex/topletter

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
