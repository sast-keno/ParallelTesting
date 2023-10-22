# Paralleles Testen mit Selenium, Python und Docker

Im Rahmen meiner Bachelorarbeit mit dem Titel "Konzept für parallelisierte End-to-End-Tests
mit Selenium und Python zum Schutz gegen Regression mit integriertem Test-Reporting" wurde in Abschnitt 6.3 die Testdauer von fünf Testläufen gemessen. Das Repo enthält alle relevanten Dateien für die Testausführung. Darunter sind Python Dateien, die die Tests beinhalten und YAML-Datein, die zum hochfahren des Grids mit Docker erforderlich sind.

Im Folgenden wird beschrieben, wie jeder einzelne Testlauf gestartet werden kann. Testlauf 1 und 4 werden sequenziell ausgeführt, daher muss das Grid in diesen Fällen nicht hochgefahren werden.

## Testlauf 1:

Tests starten mit HTML-Report: 
```
pytest .\testlauf1.py --html=report.html
```

## Testlauf 2
Grid hochfahren: 
```
docker-compose -f docker-compose-testlauf2.yml up
```

Tests starten: 
```
pytest .\testlauf2und3.py --html=report.html -n 2
```

## Testlauf 3
Grid hochfahren: 
```
docker-compose -f docker-compose-testlauf3.yml up
```

Tests starten: 
```
pytest .\testlauf2und3.py --html=report.html -n 4
```

## Testlauf 4
Tests starten: 
```python
pytest .\testlauf4.py --html=report.html
```

## Testlauf 5
Grid hochfahren: 
```
docker-compose -f docker-compose-testlauf5.yml up
```

Tests starten: 
```
pytest .\testlauf5.py --html=report.html -n 4
```

----------

### Weiteres:
- Die gestarten Container lassen sich über folgenden Befehl herunterfahren und entfernen:

    ```python
    docker-compose -f <yaml-file> down
    ```

- Um den Titel des generierten Reports zu bestimmen, kann in der Datei "conftest.py" eine beliebiger Titel übergeben werden (Zeile 2).

- Das Grid Dashboard kann über ```http://localhost:4444``` eingesehen werden














