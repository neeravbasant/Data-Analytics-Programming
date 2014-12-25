import json
import re
import urllib
from bs4 import BeautifulSoup as bs

def contractAsJson(filename):
    
    final_output = dict()
    
    file = urllib.urlopen(filename).read()
    soup = bs(file)
    
    # Getting the stock value
    x = soup.find(attrs = {"class":"time_rtq_ticker"}).get_text()
    final_output["currPrice"] = float(x.encode('ascii','ignore'))
    
    
    # Getting the link for all the expiration dates
    lst1 = []
    for node in soup.find_all('a'):
        link =  node.get('href', None)
        if len(re.findall('^[/q/op?s=].*m=[0-9]*-[0-9][0-9].*', link)) != 0:
            lst1.append("http://finance.yahoo.com" + (re.findall('^[/q/op?s=].*m=[0-9]*-[0-9][0-9].*', link)[0]).replace('&','&amp;'))            
    final_output["dateUrls"] = lst1    
    
    
    # Getting the CALL and PUT options
    lst = []

    for y in soup.findAll('td', attrs={'class': 'yfnc_h'}):
        if y.has_attr('nowrap'):
            if re.match("[A-Z]+\d+([C])", [x.text for x in y.parent.contents][1]):
                temp = dict()
                temp["Strike"] = y.parent.contents[0].string.encode('ascii','ignore')       
                temp["Symbol"] = "".join(re.findall(r"([A-Z]+)[0-9]+[A-Z]+[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Date"] = "".join(re.findall(r"[A-Z]+([0-9]+)[A-Z]+[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Type"] = "".join(re.findall(r"[A-Z]+[0-9]+([A-Z]+)[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Last"] = y.parent.contents[2].string.encode('ascii','ignore')
                temp["Change"] = y.parent.contents[3].text.encode('ascii','ignore')
                temp["Bid"] = y.parent.contents[4].string.encode('ascii','ignore')
                temp["Ask"] = y.parent.contents[5].string.encode('ascii','ignore')
                temp["Vol"] = y.parent.contents[6].string.encode('ascii','ignore')
                temp["Open"] = y.parent.contents[7].string.encode('ascii','ignore')
    
                lst.append(temp)
            
    for y in soup.findAll('td', attrs={'class': "yfnc_tabledata1"}):
        if y.has_attr('nowrap'):
            if re.match("[A-Z]+\d+([C])", [x.text for x in y.parent.contents][1]):
                temp = dict()
                temp["Strike"] = y.parent.contents[0].string.encode('ascii','ignore')       
                temp["Symbol"] = "".join(re.findall(r"([A-Z]+)[0-9]+[A-Z]+[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Date"] = "".join(re.findall(r"[A-Z]+([0-9]+)[A-Z]+[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Type"] = "".join(re.findall(r"[A-Z]+[0-9]+([A-Z]+)[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Last"] = y.parent.contents[2].string.encode('ascii','ignore')
                temp["Change"] = y.parent.contents[3].text.encode('ascii','ignore')
                temp["Bid"] = y.parent.contents[4].string.encode('ascii','ignore')
                temp["Ask"] = y.parent.contents[5].string.encode('ascii','ignore')
                temp["Vol"] = y.parent.contents[6].string.encode('ascii','ignore')
                temp["Open"] = y.parent.contents[7].string.encode('ascii','ignore')
    
                lst.append(temp)
                
                
    for y in soup.findAll('td', attrs={'class': "yfnc_tabledata1"}):
        if y.has_attr('nowrap'):
            if re.match("[A-Z]+\d+([P])", [x.text for x in y.parent.contents][1]):
                temp = dict()
                temp["Strike"] = y.parent.contents[0].string.encode('ascii','ignore')       
                temp["Symbol"] = "".join(re.findall(r"([A-Z]+)[0-9]+[A-Z]+[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Date"] = "".join(re.findall(r"[A-Z]+([0-9]+)[A-Z]+[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Type"] = "".join(re.findall(r"[A-Z]+[0-9]+([A-Z]+)[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Last"] = y.parent.contents[2].string.encode('ascii','ignore')
                temp["Change"] = y.parent.contents[3].text.encode('ascii','ignore')
                temp["Bid"] = y.parent.contents[4].string.encode('ascii','ignore')
                temp["Ask"] = y.parent.contents[5].string.encode('ascii','ignore')
                temp["Vol"] = y.parent.contents[6].string.encode('ascii','ignore')
                temp["Open"] = y.parent.contents[7].string.encode('ascii','ignore')
    
                lst.append(temp)
                
    for y in soup.findAll('td', attrs={'class': 'yfnc_h'}):
        if y.has_attr('nowrap'):
            if re.match("[A-Z]+\d+([P])", [x.text for x in y.parent.contents][1]):
                temp = dict()
                temp["Strike"] = y.parent.contents[0].string.encode('ascii','ignore')       
                temp["Symbol"] = "".join(re.findall(r"([A-Z]+)[0-9]+[A-Z]+[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Date"] = "".join(re.findall(r"[A-Z]+([0-9]+)[A-Z]+[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Type"] = "".join(re.findall(r"[A-Z]+[0-9]+([A-Z]+)[0-9]+", y.parent.contents[1].string.encode('ascii','ignore')))
                temp["Last"] = y.parent.contents[2].string.encode('ascii','ignore')
                temp["Change"] = y.parent.contents[3].text.encode('ascii','ignore')
                temp["Bid"] = y.parent.contents[4].string.encode('ascii','ignore')
                temp["Ask"] = y.parent.contents[5].string.encode('ascii','ignore')
                temp["Vol"] = y.parent.contents[6].string.encode('ascii','ignore')
                temp["Open"] = y.parent.contents[7].string.encode('ascii','ignore')
    
                lst.append(temp)
            
    newlist = sorted(lst, key=lambda k: int(k["Open"].replace(',', '')), reverse = True) 
    final_output["optionQuotes"] = newlist
    
    jsonQuoteData = json.dumps(final_output, indent=4, sort_keys = True)
   
    return jsonQuoteData