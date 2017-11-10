# coding: utf-8

import json
import sys

def get_title(data):
    return data['name']

def get_cards_name(data):
    output = []
    cards = data['lists']
    for each_card in cards:
        output.append(each_card['name'])
    return output

def get_card_content(data, card_name):
    output = {}
    contents = data['actions']
    for each_content in contents:
        print each_content['data']['list']['name']
        # if each_content['data']['list']['name'] == card_name:
        #     print each_content['data']['card']['name']
            # output[each_content['data']['card']['name']] = output[each_content['data']['text']]
    # return output

def trello2md():
    jsonfile = 'exported.json'
    outfile = 'output.md'
    with open(jsonfile, 'r') as f:
        data = json.load(f)
        title = get_title(data)
        all_cards = get_cards_name(data)
        print all_cards

    with open(outfile, 'w') as f:
        pass



if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print "Usage: python trello2md.py [exported json file] [output markdown file]"
    # else:
    #     trello2md()
    trello2md()