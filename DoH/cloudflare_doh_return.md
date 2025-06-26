Below is the sample return from cloudflare_doh.py script (`"Status": 0` means `NoError`, more DNS return codes are found here [IANA DNS RCODES](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6))
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
   "name": "microsoft.com",
   "type": 28
  }
 ],
 "Answer": [
  {
   "name": "microsoft.com",
   "type": 28,
   "TTL": 1656,
   "data": "2603:1020:201:10::10f"
  },
  {
   "name": "microsoft.com",
   "type": 28,
   "TTL": 1656,
   "data": "2603:1010:3:3::5b"
  },
  {
   "name": "microsoft.com",
   "type": 28,
   "TTL": 1656,
   "data": "2603:1030:20e:3::23c"
  },
  {
   "name": "microsoft.com",
   "type": 28,
   "TTL": 1656,
   "data": "2603:1030:b:3::152"
  },
  {
   "name": "microsoft.com",
   "type": 28,
   "TTL": 1656,
   "data": "2603:1030:c02:8::14"
  }
 ]
}

```
