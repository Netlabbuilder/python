Python scripts to perform remote Domain Name System resolution via the HTTPS protocol - DNS over HTTPS (DoH) using public APIs from Google and Cloudflare.

Sample return:
***
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

***

