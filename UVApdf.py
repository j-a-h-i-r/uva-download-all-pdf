'''
 Python Program to fetch pdf of problem statement from UVA online judge
'''


'''
  Volume Range
  > 1 - 17
  > 100 - 132
'''

import requests
import os

'''
 - Change the rootDir to where you want to save the downloaded pdfs
'''

baseUrl = r'https://uva.onlinejudge.org/external/'
rootDir = r'M:/python/UVAPDF2'

for vol in (list(range(1, 17+1)) +
          list(range(100, 132+1))):
    pdfDir = os.path.join(rootDir, str(vol))

    if os.path.exists(pdfDir) is False:
        os.makedirs(pdfDir)

    volume = str(vol)
    
    for prob in range (0, 100):
        problem = str(vol*100 + prob)
        probUrl = baseUrl + volume + r'/' + problem + '.pdf'

        res = requests.get(probUrl)

        file = problem + '.pdf'
        print('Downloading: ' + file)

        if(res.status_code == 200):
            with open( os.path.join(pdfDir, file) , 'wb' ) as fp:
                fp.write(res.content)
        else:
            print("File Invalid")
