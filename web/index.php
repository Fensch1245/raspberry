 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 
echo "<br/>"; 

if(isset($_POST['update']))
        {
$temp = $_POST['idtest'];
shell_exec('sudo python /home/pi/raspberry/ch_config.py DEFAULT set_temp '.escapeshellarg($temp));
echo "<meta http-equiv='refresh' content='0'>";
}

 ?>

<html>
<form name="update" method="post" >
	<input type="text" name="idtest" value="<?php echo exec('sudo python /home/pi/raspberry/get_config.py'); ?>" />
    <button name = "update" type="submit">Speichern</button>
</form>
</html>
		 
		
