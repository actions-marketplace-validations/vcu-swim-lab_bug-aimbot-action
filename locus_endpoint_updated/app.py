from flask import Flask, request, jsonify
from locus2 import *
import json

app = Flask(__name__)
app.debug = True

@app.route('/locus', methods=['GET', 'POST'])
def endpoint():
    # get required data
    r = request.get_json()
    print(r)
    print(r["title"])
    print(r["body"])
    print(r["url"])
    print(r["openDate"])
    print(r["repoName"])
    print(r["issueId"])
    print(r["issueNumber"])
    url_for_indexing = r["url"]
    description_for_indexing = r["body"]
    title_for_indexing = r["title"]
    repoName = r["repoName"]
    issueNum = r["issueNumber"]
    openDate = r["openDate"]
    openDate = openDate.replace("T", " ")
    openDate = openDate.replace("Z", " ")
    url_for_indexing = url_for_indexing.replace("git:", "https:")
    url_for_indexing = url_for_indexing.replace(".git", "")
    # call functions
    
    folder_of_repo = cloneRepo(url_for_indexing)

    make_bugreport(repoName, issueNum, openDate, title_for_indexing, description_for_indexing)

    # now time to create the config file

    createConfig(folder_of_repo)

    # figure out a way to pass this info and automate locus

    runLocus()
   
    #return the ranking as json
    output = readOutput()
    print(output)
    json_output = json.dumps(output)
    parsed_output = json_output.replace("\\t", " ")
    parsed_output2 = parsed_output.replace("\\n", "\n")
    commits = []
    for row in parsed_output2.splitlines()[0:5]:
        commits += [row.split(" ")[2]]
    
    parsed_commits = " ".join(commits)
    print(parsed_commits)
    return parsed_commits
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
