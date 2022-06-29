#!/usr/bin/python3

import vt
import time 
import pandas as pd
import csv


key = "KEY" #vt api key 

#reading in the cleaned csv 
read_csv = pd.read_csv("inputCleaned.csv")
url_list = read_csv['URL'].tolist()

#url_list = [ "https://bing.com", "http://acmetoy.com"] #test urls 

with vt.Client(key) as client:    # using with to automatically close the session
    with open('loop.csv', 'w') as f: #writing the looped output to a csv 
        writer=csv.writer(f,delimiter=',')
        for url in url_list:
            #REF: https://virustotal.github.io/vt-py/quickstart.html#get-information-about-an-url
            try:
                url_id = vt.url_id(url)
                url_obj = client.get_object("/urls/{}".format(url_id))
                result = url_obj.last_analysis_stats 
            except vt.APIError as e: # Catch APIError as a result of rate limitations and try again
                print(f"API ERR ({str(e.code)}): {e}")
                time.sleep(5)
                continue

            data = [url]
            for k, v in result.items():
                data.append(v)

            #result_string = str(result) #converting the vt output to a string
            #extracted_result=result_string.replace("{","").replace("}","").replace("'","").replace("harmless: ","").replace(" malicious: ","").replace(" suspicious: ","").replace(" undetected: ","").replace(" timeout: ","") #removeing all the excess characaters. 
            #data=url+","+extracted_result #creating the string which should go as a row into a csv. 
            writer.writerow(data)
            print(data)

            time.sleep(16) #sleep in seconds 

