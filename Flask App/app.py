# Import Dependencies
import os 
import json 
import re 

from flask import Flask, request, render_template, jsonify 

app = Flask(__name__)
# Configuring the folder to upload input file
app.config['UPLOAD_FOLDER'] = 'static'
# Configuring pretty printing for JSON response
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# Overriding the sorting of keys for jsonify
app.config['JSON_SORT_KEYS'] = False


# List to contain all relevant lines from input file 
file_lines = []
# List of dictionary items for final JSON output
result = []

@app.route('/fileinput', methods=['GET', 'POST'])
def process_log_input():
    # Variable to store the name of the file
    filename = ""

    if request.method == 'POST':
        print(request)

        if request.files.get('file'):
            # Read the file
            file = request.files['file']

            # Read the filename
            filename = file.filename

            # Create a path to the Uploads folder 
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the file to the Uploads folder 
            file.save(filepath)
            
            # Open the saved file and read its contents
            with open(filepath) as lf_handle:
                for line in lf_handle:                
                    # Strip each line of any leading and trailing whitespace 
                    line = line.strip()
                    # Strip lines that begin with line numbers and/or whitespace 
                    if line[0].isdigit():
                        line = line[3:]
                    # Pick only relevant lines to process and append to list
                    if line.startswith('['):
                        file_lines.append(line)
    
                # Regex pattern to match function name following specific rules
                pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'

                # Loop through each line of the file
                for line in file_lines:
                    # Create an empty dictionary for each entry
                    dictitem = {}
                    # Split each line into separate entities for every JSON field 
                    lineitems = line.split(" ")

                    for item in lineitems:
                        if "ENTER" in item:
                            dictitem["operation"] = "ENTRY"
                        if "EXIT" in item:
                            dictitem["operation"] = "EXIT"
                        if item.startswith("/"):
                            dictitem["filename"] = item.split(":")[0]
                            dictitem["line_number"] = item.split(":")[1]
                        if re.match(pattern, item):
                            dictitem["name"] = item 
                        if item == '0':
                            dictitem["name"] = "anonymous"

                    result.append(dictitem)

            # Variable to hold the final JSON output
            data = {}
            data["result"] = result

            # Print JSON output to the console
            print(json.dumps(data, indent=4, sort_keys=False))

            # Return the JSON response of final result
            return jsonify(data)

    return render_template('fileupload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

