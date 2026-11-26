1.  -python: nie sprawdza
    -go: strukturalne dopasowanie 
    sprawdzane przez kompilator
    -java: klauzula 'implements' sprawdzana
    przez kompilator

2. go i java: wykryją błąd na etapie kompilacji

3. java wymaga bezpośredniego 'implements',
go nie wymaga 'implements' ale wykryje
źle wywołaną metode przy kompilacji,
python wywoła błąd dopiero gdy
program spróbuje użyć metody z błędem