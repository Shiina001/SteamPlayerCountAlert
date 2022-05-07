#Made by Shiina_0
import time
import requests
from win10toast import ToastNotifier #Needs to be pip installed

id = #Game's Steam id
sleep_time = #Time between pings
players_threshold = #self-explanatory

toaster = ToastNotifier()

while True:
    response = requests.get('https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid=' + str(id))
    player_count = response.json()['response']['player_count']

    print(f"Last player count: {player_count}")
    if int(player_count) >= players_threshold:
        toaster.show_toast("PLayer count alert", f"Player count is: {player_count}")

    time.sleep(sleep_time)
