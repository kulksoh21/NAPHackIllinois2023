from flask import Flask
import flask
import json

app = Flask(__name__)


class Filter:
    def __init__(self, base_needs: str):
        with open(base_needs, 'r') as f:  
            dict_set = {}
            current_word = ""
            needs_list = [word[:-1] if word[-1] == '\n' else word for word in f.readlines()]
            for word in needs_list:
                if word[-1] == ':':
                    current_word = word[:-1]
                    dict_set[current_word] = set({})
                    continue
                if current_word == "Bedding":
                    dict_set[current_word].add((word, ""))
                elif current_word != "":
                    dict_set[current_word].add(word)
        self.dict_set = dict_set
        self.dict_properties = {}

    def add_property(self, property: str, amenities: list, bed_size: str):
        self.dict_properties[property] = (set(amenities), bed_size)

    @app.route('/nap', methods=["GET"])
    def nap(self, property: str):
        bedding_set = set({})
        for pair in self.dict_set["Bedding"]:
            bedding_set.add((pair[0], self.dict_properties[property][1]))
        dict_nap = {"Bedding" : bedding_set}
        for category in self.dict_set.keys():
            if category != "Bedding":
                dict_nap[category] = self.dict_set[category] - self.dict_properties[property][0]
        with open("test.json", "r") as f:
            data = json.load(f)
            data.append(dict_nap)

            return flask.jsonify(data)
        
if __name__ == "__main__":
    f1 = Filter("needs.txt")
    print(f1.dict_set["Bedding"])
    f1.add_property("Dean", ["Microwave"], "King")
    app.run("localhost", 5000)

