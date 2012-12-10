Name:		biniax2
Version:	1.30
Release:	2
Summary:	Colour block logic game with original gameplay
License:	ZLib
Group:		Games/Puzzles
URL:		http://biniax.com
Source:		http://mordred.dir.bg/biniax/%{name}-%{version}-fullsrc.tar.gz
Source1:	%{name}-LICENSE
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel

%description
How to play Biniax :
The gaming field is a 5x7 grid filled partially with pairs of elements.
Every pair consists of two different elements combined of four possible.
You control the box with an element inside. You can move around the field
on empty spaces. You can also remove pairs of elements, if you have the
same element as the one of the pair. When you remove the pair your element
becomes the other one element of the pair and the score is increased;
The gaming field scrolls down slowly (increasing the speed with your progress)
and your goal is to stay as long as possible on the field. Remember, that if
you cannot take the pair in front of you, the scrolling will move your block
down!

%prep
%setup -q -c

%build
%make

%install
cp %{SOURCE1} LICENSE

%__cat > %{name}.sh <<EOF
#!/bin/sh
test -d "\$HOME/.%{name}" || {
  %__rm -rf "\$HOME/.%{name}"
  %__mkdir_p "\$HOME/.%{name}"
  %__ln_s %{_gamesdatadir}/%{name}/data "\$HOME/.%{name}/data"
}
cd "\$HOME/.%{name}"
exec %{name}.bin
EOF

%__mkdir_p %{buildroot}%{_datadir}/applications/
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Biniax-2
Comment=Colour logic game
Type=Application
Exec=%{name}
Icon=%{_datadir}/pixmaps/%{name}.png
Terminal=false
Categories=Game;LogicGame;
EOF

%__rm -f data/Thumbs.db

%__install -D %{name} %{buildroot}%{_gamesbindir}/%{name}.bin
%__install -D -m755 %{name}.sh %{buildroot}%{_gamesbindir}/%{name}
%__install -D data/graphics/element3.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}
cp -r data %{buildroot}%{_gamesdatadir}/%{name}/

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_gamesbindir}/%{name}*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_gamesdatadir}/%{name}



%changelog
* Sat Mar 24 2012 Andrey Bondrov <abondrov@mandriva.org> 1.30-1mdv2011.0
+ Revision: 786534
- imported package biniax2

