 <?php
		   
echo "<b>Aktuell gemessene Temperatur im Raum:</b>";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_temp.py');
echo " °C";
echo "<br/>"; 
echo "<br/>"; 

if(isset($_POST['update']))
        {
$temp = $_POST['idtest'];
shell_exec('sudo python /home/pi/raspberry/ch_config.py DEFAULT set_temp '.escapeshellarg($temp));
$heater = $_POST['heater'];
shell_exec('sudo python /home/pi/raspberry/ch_config.py DEFAULT set_temp '.escapeshellarg($heater));
echo "<meta http-equiv='refresh' content='0'>";
}

 ?>

<html>
<form name="update" method="post" >
	<b> Eingestellte Temperatur: </b> </br>
	<input type="text" name="idtest" value="<?php echo exec('sudo python /home/pi/raspberry/get_config.py'); ?>" />
    <input type="text" name="heater" value="<?php echo exec('sudo python /home/pi/raspberry/get_config_heater.py'); ?>" />
	<button name = "update" type="submit">Speichern</button>
	
	
</form>
</html>
		 
		
