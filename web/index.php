<html>
<form name="update" method="post" >
	<input type="text" name="idtest" value="<?php echo exec('sudo python /home/pi/raspberry/get_config.py'); ?>" />
    <button name = "update" type="submit"> Update charts </button>
</form>
</html>
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 
$test = $_POST['idtest'];
echo $test;

if (isset($_POST['update']))
{
    echo exec('python ch_config.py DEFAULT set_temp '".$test."'");
}

         ?>
