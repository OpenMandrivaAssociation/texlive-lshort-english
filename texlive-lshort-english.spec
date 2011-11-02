Name:		texlive-lshort-english
Version:	5.01
Release:	1
Summary:	A (Not So) Short Introduction to LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/english
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-english.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-english.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The document derives from a German introduction ('lkurz'),
which was translated and updated; it continues to be updated.
This translation has, in its turn, been translated into
Finnish, French, German, Italian, Japanese, Korean, Mongolian,
Persian (Farsi), Polish, Portuguese, Brazilian Portuguese,
Russian, Slovak, Slovenian, Spanish and Ukranian. Not all
translations are of the current English version, of course.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-english/CHANGES
%doc %{_texmfdistdir}/doc/latex/lshort-english/README
%doc %{_texmfdistdir}/doc/latex/lshort-english/lshort-5.01.src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-english/lshort.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
