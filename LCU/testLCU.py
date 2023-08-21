import os

import requests
import urllib3

urllib3.disable_warnings()


class LCUConnector:
    @staticmethod
    def check_exist(lockfile_path):
        return os.path.exists(lockfile_path)

    @staticmethod
    def read_file(lockfile_path):
        lockfile = open(lockfile_path, "r")
        data = lockfile.read().split(":")
        data_dict = {
            "port": data[2],
            "url": "https://127.0.0.1:{}".format(data[2]),
            "auth": "riot:{}".format(data[3]),
            "connection_method": data[4]
        }
        return data_dict

    @staticmethod
    def connect(lockfile_path="default"):
        if lockfile_path == "default":
            lockfile_path = "C:\\Riot Games\\League of Legends\\lockfile"
        if LCUConnector.check_exist(lockfile_path):
            return LCUConnector.read_file(lockfile_path)
        else:
            raise Exception("Couldn't read lockfile!\nThis could mean that either the \
                             path is not the right or the League Client is not opened!")


if __name__ == "__main__":
    lcu_data = LCUConnector.connect()
    print(lcu_data)
    help(lcu_data)


    def help(lcu_data, p=False):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/Help"
        request = requests.post(url, headers=headers, verify=False)
        request_json = request.json()
        if p == True:
            xtra.jprint(request_json)
        return request_json


class xtra:
    def get_champion_name_by_id(id):
        version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
        champion_id = {}
        champs_req = requests.get(F"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()
        for x in list(champs_req["data"]):
            champ_id = champs_req["data"][x]["key"]
            champion_id[champ_id] = x
        champ_name = champion_id[str(id)]
        return champ_name

    def get_champion_name_by_id_list(id_list):
        version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
        champion_id = {}
        champ_list = []
        champs_req = requests.get(F"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()
        for x in list(champs_req["data"]):
            champ_id = champs_req["data"][x]["key"]
            champion_id[champ_id] = x
        for x in id_list:
            champ_name = champion_id[str(x)]
            champ_list.append(champ_name)
        return champ_list

    def base64encode(text):
        text = base64.b64encode(text.encode("ascii")).decode("ascii")
        return text

    def jprint(json_parsed):
        print(json.dumps(json_parsed, indent=4, sort_keys=True))
