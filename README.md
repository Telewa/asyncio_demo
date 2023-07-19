# Asyncio Demo

Demo of how to run something in parallel using asyncio. In this case, we are downloading a bunch of files from the internet in parallel.

### requirements:
```
python==3.11
aiofile==3.8.7
aiohttp==3.8.5
structlog==23.1.0
```

### instructions
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Sample output:

```
(.venv) ➜  ~/Documents/asyncio_demo git:(master) python main.py                                              
2023-07-20 02:40:43 [info     ] Download                       filename=Carlsen.zip state=start url=https://www.pgnmentor.com/players/Carlsen.zip
2023-07-20 02:40:43 [info     ] Download                       filename=Kramnik.zip state=start url=https://www.pgnmentor.com/players/Kramnik.zip
2023-07-20 02:40:43 [info     ] Download                       filename=So.zip state=start url=https://www.pgnmentor.com/players/So.zip
2023-07-20 02:40:43 [info     ] Download                       filename=GrunfeldFianchetto.zip state=start url=https://www.pgnmentor.com/openings/GrunfeldFianchetto.zip
2023-07-20 02:40:43 [info     ] Download                       filename=KIDClassical.zip state=start url=https://www.pgnmentor.com/openings/KIDClassical.zip
2023-07-20 02:40:43 [info     ] Download                       filename=NimzoSaemisch.zip state=start url=https://www.pgnmentor.com/openings/NimzoSaemisch.zip
2023-07-20 02:40:43 [info     ] Download                       filename=DutchClassical.zip state=start url=https://www.pgnmentor.com/openings/DutchClassical.zip
2023-07-20 02:40:45 [info     ] Download                       action=fetch status=success url=https://www.pgnmentor.com/openings/GrunfeldFianchetto.zip
2023-07-20 02:40:45 [info     ] Download                       action=fetch status=success url=https://www.pgnmentor.com/openings/DutchClassical.zip
2023-07-20 02:40:45 [info     ] Download                       action=fetch status=success url=https://www.pgnmentor.com/players/So.zip
2023-07-20 02:40:45 [info     ] Download                       action=fetch status=success url=https://www.pgnmentor.com/players/Carlsen.zip
2023-07-20 02:40:45 [info     ] Download                       action=fetch status=success url=https://www.pgnmentor.com/players/Kramnik.zip
2023-07-20 02:40:45 [info     ] Download                       action=fetch status=success url=https://www.pgnmentor.com/openings/KIDClassical.zip
2023-07-20 02:40:45 [info     ] Download                       action=fetch status=success url=https://www.pgnmentor.com/openings/NimzoSaemisch.zip
2023-07-20 02:40:46 [info     ] Download                       filename=Kramnik.zip state=complete url=https://www.pgnmentor.com/players/Kramnik.zip
2023-07-20 02:40:46 [info     ] Download                       filename=So.zip state=complete url=https://www.pgnmentor.com/players/So.zip
2023-07-20 02:40:46 [info     ] Download                       filename=NimzoSaemisch.zip state=complete url=https://www.pgnmentor.com/openings/NimzoSaemisch.zip
2023-07-20 02:40:46 [info     ] Download                       filename=Carlsen.zip state=complete url=https://www.pgnmentor.com/players/Carlsen.zip
2023-07-20 02:40:46 [info     ] Download                       filename=GrunfeldFianchetto.zip state=complete url=https://www.pgnmentor.com/openings/GrunfeldFianchetto.zip
2023-07-20 02:40:46 [info     ] Download                       filename=DutchClassical.zip state=complete url=https://www.pgnmentor.com/openings/DutchClassical.zip
2023-07-20 02:40:47 [info     ] Download                       filename=KIDClassical.zip state=complete url=https://www.pgnmentor.com/openings/KIDClassical.zip
~/Documents/asyncio_demo/main.py executed in 3.86 seconds.

```

