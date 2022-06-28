#!/usr/bin/python3

import vt
import time 
import pandas as pd
import csv


key = "KEY" #vt api key 

url_list = [ "https://bing.com", "http://acmetoy.com"] #test urls 

with open('loop.csv', 'w') as f: #writing the looped output to a csv 
    writer=csv.writer(f,delimiter=',')
    for url in url_list:
        with vt.Client(key) as client:    # using with to automatically close the session
            #REF: https://virustotal.github.io/vt-py/quickstart.html#get-information-about-an-url
            url_id = vt.url_id(url)
            url_obj = client.get_object("/urls/{}".format(url_id))
            result = url_obj.last_analysis_stats 
            result_string = str(result) #converting the vt output to a string 
            extracted_result=result_string.replace("{","").replace("}","").replace("'","").replace("harmless: ","").replace(" malicious: ","").replace(" suspicious: ","").replace(" undetected: ","").replace(" timeout: ","") #removeing all the excess characaters. 
            data=url+","+extracted_result #creating the string which should go as a row into a csv. 
            writer.writerow([data])

        time.sleep(5) #sleep in seconds 



df = pd.read_csv("loop.csv",delimiter=',')
#header_list = ['URL', 'Harmless', 'Malicous','Suspicious', 'Undetected', 'Timeout'] 
df.to_csv("scoresApplied.csv") 
print(df)
