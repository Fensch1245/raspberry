 <?php
  if(isset($_POST['dellog']))
        {
echo exec('echo hi');
}
 ?>

<form method="post">
	<button name ="dellog" type="submit">Logdatei leeren</button>
</form>

<form action="http://192.168.2.200">
	</br>
    <input type="submit" value="Hauptseite" />
</form>
		
 <?php
echo nl2br( file_get_contents('/home/pi/raspberry/log.log') );
 ?>