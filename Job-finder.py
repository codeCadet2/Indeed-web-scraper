from bs4 import BeautifulSoup
import requests


#scrape the data and get in string
def getdata(url):
    r = requests.get(url)
    return r.text

#get html using parse
def html_code(url):

    #pass html data
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    #return html 
    return(soup)

#filter data
def job_data(soup):

    #finding html string
    data_str = ''
    for item in soup.find_all('a', class_='jobtitle turnstilelink'):
        data_str = data_str = item.get_text()
    result_1 = data_str.split('\n')
    return(result_1)

def company_data(soup):
    #find the data + convert to string
    data_str = ''
    result = ''
    for item in soup.find_all('div', class_='sjcl'):
        data_str = data_str = item.get_text()
    result_1 = data_str.split('\n')

    res = []
    for i in range(1, len(result_1)):
        if len(result_1[i]) > 1:
            res.append(result_1[i])
    return(res)

if __name__ == '__main__':
    #data for url
    job = 'python+developer'
    Location = 'Remote&sc'
    url = 'https://ca.indeed.com/jobs?q=' + job + '&l='+ Location

    soup = html_code(url)

    job_res = job_data(soup)
    com_res = company_data(soup)

    temp = 0
    for i in range(1, len(job_res)):
        j = temp
        for j in range(temp, 2+temp):
            print('company name and address: ' + (com_res[j]))
        
        temp = j
        print('Job : ' + job_res[i])
        print('----------------------------')
    



