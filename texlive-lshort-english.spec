# revision 33687
# category Package
# catalog-ctan /info/lshort/english
# catalog-date 2014-04-22 00:43:27 +0200
# catalog-license gpl2
# catalog-version 5.02
Name:		texlive-lshort-english
Version:	5.02
Release:	1
Summary:	A (Not So) Short Introduction to LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/english
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-english.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-english.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document derives from a German introduction ('lkurz'),
which was translated and updated; it continues to be updated.
This translation has, in its turn, been translated into several
other languages; see the lshort catalogue entry for the current
list.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-english/CHANGES
%doc %{_texmfdistdir}/doc/latex/lshort-english/README
%doc %{_texmfdistdir}/doc/latex/lshort-english/lshort-5.03.src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-english/lshort.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
