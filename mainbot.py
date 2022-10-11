import requests 
url = 'https://www.tssouthernpower.com/OnlineBillEnquiryDetails.do'
for i in range (1111, 1111):
    d = {'uscno':str(i), 'eroHidden':'Ok'}
    x = requests.post(url, data = d)
    if '14-1-211/613/2' in x.text:
        print(i)