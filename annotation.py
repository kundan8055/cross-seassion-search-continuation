#!C:/Users/kundan.KUNDAN/AppData/Local/Programs/Python/Python36/python
print("Content-Type: text/html")
#print('<br>')
print()
print("<body bgcolor=\"#ffe6e6\">")
import cgi
import mysql.connector
from collectmachinedata import MachineData
from labeldata import *
from mysql.connector import Error
#from databasehandler import DatabaseHandler
print("<h1>Thanks</h1>")
print("<hr/>")
try:
    conn = mysql.connector.connect(host='localhost', database='annotation', user='root', password='')
    if conn.is_connected():
        print("")
except Error as e:
    print(e)
#dataobj=DatabaseHandler()
#conn=dataobj.getConnection()
cur=conn.cursor()
cur.execute("select count(*) from parameters")
count=cur.fetchall()
noOfData=count[0][0]
#print(noOfData)
cur=conn.cursor()
cur.execute("SELECT count FROM urlhistory ORDER BY sn DESC LIMIT 1")
host_count=cur.fetchone()
#print(host_count)
host_fincount=host_count[0]
#print(host_fincount)
cur=conn.cursor()
cur.execute("SELECT url,date,sno from count_table")
host_count=cur.fetchone()
#print(host_count)
if(host_count!=None):
   host_finurl=host_count[0]
   host_predate=host_count[1]
   host_sno=host_count[2]
#print(host_count[0])
#print(host_count[1])
#print(host_count[2])
#print(host_fincount)
if(host_fincount>4):
    print("<h5 bgcolor=\"red\">It will continue in near future</h5>")
    print("<h6>you have visited this site previously on </h6>"+"<h6 bgcolor=\"blue\">"+host_predate.strftime("%Y-%m-%d %H:%M:%S")+"</h6>")
    print("you can visit your previous visited url and can continue your previous search")
    print('<a href='+host_finurl+'">'+host_finurl+'</a>')
else:
	  #print(noOfData)
    form=cgi.FieldStorage()
    intent=form.getvalue("Intent type")
    motiv=form.getvalue("Motivation")
    comp=form.getvalue("Complexity")
    work=form.getvalue("Work")
    cont=form.getvalue("Continue")
    time=form.getvalue("Time")
    predictList=[intent,motiv,comp,work,time]
    #print(predictList)
    labelobj=LabelData(predictList)
    predictList=labelobj.labelList()
    #print(predictList)
    #labelize(predictList)
    #dbobj=MachineData()
    #print(noOfData)
    totalData=20
    #print(noOfData)
    if (noOfData<totalData):
	      #print(noOfData)
	      cur=conn.cursor()
	      cur.execute("insert into parameters(intent_type,motivation,complexity,work_fun,continue_not,time_sensitivity) values(%s,%s,%s,%s,%s,%s)",(intent,motiv,comp,work,cont,time))
	      #cur=conn.cursor()
	      dbobj=MachineData(conn)
	      predicted=dbobj.collectData([predictList])
	      if(predicted==1):
		      print("It is considered to be continued.")
	      else:
		      print("It is NOT considered to be continued .")
    else:
	      #print("kundan")
	      dbobj=MachineData(conn)
	      predicted=dbobj.collectData([predictList])
	      if(predicted==1):
                      print("<h5 bgcolor=\"red\">It will continue in near future</h5>")
                      if(host_count==None):
                         print("It has not been visited in last few days")
                      if(host_count!=None):
                         print("<h6>you have visited this site previously on </h6>"+"<h6 bgcolor=\"blue\">"+host_predate.strftime("%Y-%m-%d %H:%M:%S")+"</h6>")
                         print("you can visit your previous visited url and can continue your previous search")
                         print('<a href='+host_finurl+'">'+host_finurl+'</a>')
	      else:
		      print("It is NOT considered to be continued. ")
    '''cur.execute("select urls from urlhistory order by sn DESC limit 1")
    currUrl=cur.fetchall()
    url=currUrl[0][0]
    cur=conn.cursor()
    str="select urls,date from urlhistory where urls='"+url+"' order by sn DESC limit 2"
    cur.execute(str)
    preUrl=cur.fetchall()
    if(len(preUrl)==2):
           preurl=preUrl[1][0]
           date=preUrl[1][1]
           print("<br>")
           print("You have visited previously this site on ",end="")
           print(date)
           print('<a href='+preurl+'">'+preurl+'</a>')
    else:
           print("<br>")
           print("You have visited previously this site on ",end="")
           print('20-11-2018')
           preurl="https://mail.google.com/mail/u/0/#inbox/FMfcgxvzLhjcsfHjdwZFwFwQVJCcNhJK"
           print('<a href='+preurl+'">'+preurl+'</a>')'''
cur=conn.cursor()
cur.execute("DELETE FROM count_table")
print("</body>");
conn.commit()
cur.close()
conn.close()