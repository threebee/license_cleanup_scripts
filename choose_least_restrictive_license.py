import json

license_ordering = {
    'Public Domain': 1,
    'WTFPL': 2,
    'Unlicense': 2,
    '0BSD': 2,
    'MIT': 3,
    'JSON': 4,
    'Apache-2.0': 5,
    'BSD-2-Clause': 6,
    'BSD-3-Clause': 7,
    'W3C': 8,

    'EPL-2.0': 9,
    'EPL-1.0': 10,
    'CDDL-1.0': 11,
    'CDDL-1.1': 12,
    'MPL-2.0': 13,
    'MPL-1.1': 14,

    'LGPL-3.0': 15,
    'LGPL-2.1': 16,
    'GPL-2.0-with-classpath-exception': 17,
    'GPL-2.0': 18
}

if __name__ == "__main__":
    combined_json_path = '/Users/anuj.agarwal/Desktop/licenses/standard_json/combined.json'
    output_path = '/Users/anuj.agarwal/Desktop/licenses/combined_final.json'

    # Read json
    with open(combined_json_path) as fp:
        json_object = json.load(fp)

    for item, value in json_object.items():
        least_restrictive_license = None
        old_list = value["licenses"]
        if type(old_list) != list:
            old_list = [old_list]
        if len(old_list) == 1 and len(value["licenses_standardised"]) == 1:
            value['least_restrictive_license'] = value["licenses_standardised"][0]
        elif len(old_list) != 0 and len(old_list) == len(value["licenses_standardised"]) and len(
                set(value["licenses_standardised"]) - set(license_ordering.keys())) == 0:
            standard_license_list = list(set(value["licenses_standardised"]))
            standard_license_list.sort(key=lambda val: license_ordering[val])
            value['least_restrictive_license'] = standard_license_list[0]
        else:
            print(f'Manually review: {item}  {old_list}  {value["licenses_standardised"]}')

    # Write json
    with open(output_path, 'w') as outfile:
        json.dump(json_object, outfile)