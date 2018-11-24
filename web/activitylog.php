
<form method="post">
	<button name ="dellog" type="submit">Logdatei leeren</button>
</form>

<form action="http://192.168.2.200">
    <input type="submit" value="Hauptseite" />
</form>
<form action="http://192.168.2.200/log.php">
    <input type="submit" value="Logverwaltung" />
</form>

 <?php
   if(isset($_POST['dellog']))
        {
exec('sudo truncate -s 0 /home/pi/raspberry/activity.log');
}

echo nl2br( file_get_contents('/home/pi/raspberry/activity.log') );
 ?>