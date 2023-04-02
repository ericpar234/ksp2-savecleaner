# ksp2-savecleaner
A json parser for ksp2 saves to remove any extra objects. Use at your own risk. Cleans out duplicate "TravelLogData"->"ObjectEvents" that seems to multiply in the save .json. Tested once on KSP2 v0.1.1.0

0. Find your save files (Mine are at `\AppData\LocalLow\Intercept Games\Kerbal Space Program 2\Saves\SinglePlayer\A New Hope`)
1. Make a back up of your save file
2. run `python ksp2-savecleaner.py save.json fixed_save.json` (where save.json is your original save and fixed_save.json is your new save file)
3. Make a copy of save.meta and call it fixed_save.meta.
    
    - Edit fixed_save.meta:  Ensure "Filepath" on line 5 points to fixed_save.json
    - Edit fixed_save.json:  Ensure "Filepath" on line 6 points to fixed_save.json