import json

if __name__ == "__main__":
    java_json_path = '/Users/anuj.agarwal/Desktop/licenses/standard_json/java.json'
    go_json_path = '/Users/anuj.agarwal/Desktop/licenses/standard_json/go.json'
    js_json_path = '/Users/anuj.agarwal/Desktop/licenses/standard_json/js.json'
    output_path = '/Users/anuj.agarwal/Desktop/licenses/standard_json/combined.json'

    output_map = {}
    for file_path in ((java_json_path, 'java'), (go_json_path, 'go'), (js_json_path, 'js')):
        language = file_path[1]
        with open(file_path[0]) as fp:
            json_object = json.load(fp)
        for key, value in json_object.items():
            output_map[f'{language}:{key}'] = value

    with open(output_path, 'w') as outfile:
        json.dump(output_map, outfile)
