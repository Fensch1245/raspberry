<?php
 if(isset($_POST['dellog']))
        {
shell_exec('truncate -s 0 /home/pi/raspberry/log.log');
}
?>

<form action="http://192.168.2.200">
	</br>
    <input type="submit" value="Hauptseite" />
	<button name = "dellog" type="submit">Logdatei leeren</button>
</form>
		
 <?php
echo nl2br( file_get_contents('/home/pi/raspberry/log.log') );
 ?>