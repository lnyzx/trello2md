# coding: utf-8

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Text:
    def __init__(self, card_name, content):
        self.card_name = card_name
        self.content = content

class Card:
    def __init__(self, card_name, desc, text, list_id):
        self.card_name = card_name
        self.desc = desc
        self.text = text
        self.list_id = list_id

class Lists:
    def __init__(self, list_name, card):
        self.list_name = list_name
        self.card = card

def get_title(data):
    return data['name']

def get_all_lists(data, all_cards):
    out = []
    for each_list in data['lists']:
        list_card = []
        list_name = each_list['name']
        list_id = each_list['id']
        for each_card in all_cards:
            if each_card.list_id == list_id:
               list_card.append(each_card) 
        this_list = Lists(list_name, list_card)
        out.append(this_list)
    return out

def get_all_cards(data, all_texts):
    out = []
    for each_card in data['cards']:
        list_id = each_card['idList']
        desc = each_card['desc']
        card_name = each_card['name']
        card_text = []
        for each_text in all_texts:
            if each_text.card_name == card_name:
                card_text.append(each_text)
        this_card = Card(card_name, desc, card_text, list_id)
        out.append(this_card)
    return out

def get_all_texts(data):
    out = []
    for each_text in data['actions']:
        try:
            each_text['data']['text']
        except:
            pass
        else:
            this_text = Text(each_text['data']['card']['name'], each_text['data']['text'])
            out.append(this_text)
    return out


def trello2md():
    jsonfile = sys.argv[1]
    outfile = sys.argv[2]
    with open(jsonfile, 'r') as f:
        data = json.load(f)
        title = get_title(data)
        all_text = get_all_texts(data)
        all_cards = get_all_cards(data, all_text)
        all_lists = get_all_lists(data, all_cards)

    with open(outfile, 'w') as f:
        for each_list in all_lists:
            f.write("# " + each_list.list_name + '\r\n'+ '\r\n')
            for each_card in each_list.card:
                f.write("## " + each_card.card_name + '\r\n'+ '\r\n')
                if each_card.desc != '':
                    f.write(">" + each_card.desc + '\r\n'+ '\r\n')
                for each_text in each_card.text:
                    f.write("```" + '\r\n')
                    f.write(each_text.content + '\r\n'+ '\r\n')
                    f.write("```" + '\r\n')



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: python trello2md.py [exported json file] [output markdown file]"
    else:
        trello2md()
