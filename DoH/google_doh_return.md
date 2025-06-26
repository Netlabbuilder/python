Below is the sample return from google_doh.py script (`"Status": 0` means `NoError`, more DNS return codes are found here [IANA DNS RCODES](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6))
```
{
 "Status": 0,
 "TC": false,
 "RD": true,
 "RA": true,
 "AD": false,
 "CD": false,
 "Question": [
  {
   "name": "microsoft.com.",
   "type": 1
  }
 ],
 "Answer": [
  {
   "name": "microsoft.com.",
   "type": 1,
   "TTL": 2010,
   "data": "104.212.67.197"
  }
 ]
}
```
