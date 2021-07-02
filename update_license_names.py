import json

license_map = {
    "Apache-2.0": "Apache-2.0",
    "Apache 2": "Apache-2.0",
    "Apache 2.0": "Apache-2.0",
    "Apache 2.0 License": "Apache-2.0",
    "Apache License, version 2.0": "Apache-2.0",
    "Apache License 2.0": "Apache-2.0",
    "Apache License Version 2.0": "Apache-2.0",
    "Apache License, 2.0": "Apache-2.0",
    "Apache License, Version 2.0": "Apache-2.0",
    "Apache Software License - Version 2.0": "Apache-2.0",
    "Apache Software Licenses": "Apache-2.0",
    "Apache V2": "Apache-2.0",
    "The Apache License, Version 2.0": "Apache-2.0",
    "The Apache Software License, Version 2.0": "Apache-2.0",
    "ASL, version 2": "Apache-2.0",
    "ASF 2.0": "Apache-2.0",
    "BSD-2-Clause-FreeBSD": "BSD-2-Clause-FreeBSD",
    'BSD 2-Clause "Simplified" License': "BSD-2-Clause",
    'BSD 2-Clause "Simplified"': "BSD-2-Clause",
    "BSD 2-clause": "BSD-2-Clause",
    "BSD-2-Clause": "BSD-2-Clause",
    "BSD 2-Clause": "BSD-2-Clause",
    "BSD 2-Clause License": "BSD-2-Clause",
    "FreeBSD": "BSD-2-Clause",
    'BSD 3-Clause "New" or "Revised" License': "BSD-3-Clause",
    "BSD 3-clause": "BSD-3-Clause",
    "BSD-3-Clause": "BSD-3-Clause",
    "BSD 3-Clause": "BSD-3-Clause",
    "BSD 3-clause License w/nuclear disclaimer": "BSD-3-Clause",
    "3-Clause BSD License": "BSD-3-Clause",
    "BSD New license": "BSD-3-Clause",
    "New BSD License": "BSD-3-Clause",
    "The New BSD License": "BSD-3-Clause",
    "Revised BSD": "BSD-3-Clause",
    "https://svn.codehaus.org/proxytoys/trunk/LICENSE.txt": "BSD-3-Clause",
    "Modified BSD": "BSD-3-Clause",
    "BSD licence": "BSD-3-Clause",
    "MIT": "MIT",
    "MIT license": "MIT",
    "MIT License": "MIT",
    "The MIT License": "MIT",
    "jQuery license": "MIT",
    "Bouncy Castle Licence": "MIT",
    "Eclipse Distribution License - v 1.0": "MIT",
    "Eclipse Distribution License v. 1.0": "MIT",
    "EDL 1.0": "MIT",
    "CDDL 1.1": "CDDL-1.1",
    "CDDL + GPLv2 with classpath exception": "CDDL-1.1",
    "Common Development and Distribution License (CDDL) v1.0": "CDDL-1.0",
    "CDDL/GPLv2+CE": "CDDL-1.0",
    "Eclipse Public License - v 1.0": "EPL-1.0",
    "Eclipse Public License 1.0": "EPL-1.0",
    "Eclipse Public License - Version 1.0": "EPL-1.0",
    "Eclipse Public License, Version 1.0": "EPL-1.0",
    "EPL 2.0": "EPL-2.0",
    "Eclipse Public License - v 2.0": "EPL-2.0",
    "Eclipse Public License v. 2.0": "EPL-2.0",
    "GNU General Public License, version 2, with the Classpath Exception": "GPL-2.0-with-classpath-exception",
    "GPL, Version 2, With Classpath Exception": "GPL-2.0-with-classpath-exception",
    "GPL2 w/ CPE": "GPL-2.0-with-classpath-exception",
    "GPL2, with the classpath exception": "GPL-2.0-with-classpath-exception",
    "The GNU General Public License, Version 2": "GPL-2.0",
    "GPLv2": "GPL-2.0",
    "GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1": "LGPL-2.1",
    "GNU Lesser General Public License, Version 2.1": "LGPL-2.1",
    "LGPL 2.1": "LGPL-2.1",
    "LGPL, version 2.1": "LGPL-2.1",
    "LGPLv2.1": "LGPL-2.1",
    "The JSON License": "JSON",
    "JSON": "JSON",
    "MPL 1.1": "MPL",
    "Mozilla Public License 2.0": "MPL-2.0",
    "MPL-2.0": "MPL-2.0",
    "W3C license": "W3C",
    "WTFPL": "WTFPL",
    "X11": "X11",
    "Public Domain": "Public Domain",
    "UnboundID SCIM2 SDK Free Use License": "https://github.com/pingidentity/scim2/blob/master/resource/LICENSE-UnboundID-SCIM2.txt",
    "zlib License": "Zlib",
    "ISC License": "ISC",
    "ISC": "ISC",
    "BSD":"BSD",
    "AFLv2.1": "AFL-2.1",
    "Unlicense": "Unlicense",
    "WTFPL": "WTFPL",
}

if __name__ == "__main__":
    license_json_read_path = "/Users/anuj.agarwal/Desktop/licenses/original_json/js.json"
    license_json_write_path = "/Users/anuj.agarwal/Desktop/licenses/standard_json/js.json"
    language = 'js'

    # Read json
    with open(license_json_read_path) as fp:
        json_object = json.load(fp)

    for item, value in json_object.items():
        old_list = value["licenses"]
        if type(old_list) != list:
            old_list = [old_list]
        new_list = []
        for entry in old_list:
            if entry.strip() in license_map:
                new_list.append(license_map[entry.strip()])
            else:
                print(f"License could not be standardised for: {item} {entry}")

        # Add/Update following keys:
        value["licenses_standardised"] = new_list
        value["language"] = language

    # Write json
    with open(license_json_read_path, 'w') as outfile:
        json.dump(json_object, outfile)
