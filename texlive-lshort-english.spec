Name:		texlive-lshort-english
Version:	58309
Release:	2
Summary:	A (Not So) Short Introduction to LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/english
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-english.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-english.doc.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/lshort-english

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
