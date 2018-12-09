<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "annotation";
$url1=$_POST['a'];
$url2=$_POST['b'];
$myconn = new mysqli($servername, $username, $password, $dbname); // Create connection
if ($myconn->connect_error) {     // Check connection
    die("Connection failed: " . $myconn->connect_error);
}
$curr_date = date('Y-m-d H:i:s');
$sql_prehost="select * from urlhistory where host='$url2' and DATEDIFF('$curr_date',date)<3";
if($sql_prehost_query=$myconn->query($sql_prehost)){
}else
{
   echo "Error: " . $sql_prehost . "<br>" . $myconn->error;
}
if($sql_prehost_query->num_rows > 0){
$row=$sql_prehost_query->fetch_array();
$occur=$row['count'];
$occur++;
$count_sno=$row['sn'];
$count_url=$row['urls'];
$count_date=$row['date'];
echo $count_date;
$count_sql="INSERT INTO count_table(sno,url,date) VALUES('$count_sno','$count_url','$count_date')";
if ($myconn->query($count_sql) === TRUE) {
    echo "Page+ saved!";
} else {
    echo "Error: " . $sql . "<br>" . $myconn->error;
}
$sql = "INSERT INTO urlhistory (urls,host,count) VALUES ('$url1','$url2','$occur')";
if ($myconn->query($sql) === TRUE) {
    echo "Page+ saved!";
} else {
    echo "Error: " . $sql . "<br>" . $myconn->error;
}
$sql_count_update="DELETE FROM urlhistory WHERE sn='$count_sno'";
if($myconn->query($sql_count_update)===TRUE){

}else{
	echo "Error: " .$sql_count_update . "<br>" . $myconn->error;
}
}else
{
$sql = "INSERT INTO urlhistory (urls,host) VALUES ('$url1','$url2')";
if ($myconn->query($sql) === TRUE) {
    echo "Page+ saved!";
} else {
    echo "Error: " . $sql . "<br>" . $myconn->error;
}
}
$myconn->close();
?>