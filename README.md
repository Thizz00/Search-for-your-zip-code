```python
import requests
headers = { 
                   "apikey": "Your-Api-key-from-zipcodebase.com"}
                   params = (
                   ("city",self.lineEdit.text()),
                   ("country",self.lineEdit_2.text()),
                   );
                   response = requests.get('https://app.zipcodebase.com/api/v1/code/city', headers=headers, params=params);
```
\
\
\
\
\
![alt text](Zrzut ekranu 2022-06-28 203925.png)

