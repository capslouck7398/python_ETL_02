from urllib import request as ur
import json , time , firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

with open('ETL_02.txt','r') as f:
  apiurl2 = f.read()

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

url_array = ["3369301","3369303","312591","312605","3369296","2515397","3369300","313567","3369298","3369297","315040","315078","3369306","314999","3369299","3369302","313812",
]
for i in url_array:
  nowTime = int(time.time())
  struct_time = time.localtime(nowTime)
  timeString = time.strftime("%Y-%m-%d-%I:%M:%S-%P", struct_time)
  respone = json.loads(ur.urlopen("https://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"+i+"?apikey="+apiurl2).read().decode('utf-8'))
  doc_ref = db.collection("homework").document("student02").collection("test02")
  doc_ref.document('Taiwan-W-'+i+"-"+timeString).set({'weather':respone})


