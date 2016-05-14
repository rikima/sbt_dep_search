#!/usr/bin/env python

import sys
import requests
import json

url="http://search.maven.org/solrsearch/select"

def execute(query):
    r = requests.get(url, params=dict(q=query))
    data = r.json()
    for i, d in enumerate(data.get('response').get('docs')):
        print("#%d\t" %(i), end="")
        
        g = d.get('g')
        a = d.get('a')
        v = d.get('latestVersion')

        sbt_setting = 'libraryDependencies += "{g}" % "{a}" % "{v}"'.format(g=g, a=a, v=v)
    
        print(sbt_setting)
        print(json.dumps(d, sort_keys=True, indent=2))



if __name__ == '__main__':
    query = " ".join(sys.argv[1:]).strip()
    if not query or len(query) == 0:
        print("usage: sbt_dep_search.py [query]")
        sys.exit(1)

    execute(query)
