<html>
<form name="update" method="post" >
    <button name = "update" type="submit"> Update charts </button>
</form>
</html>
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_config.py');

if (isset($_POST['update']))
{
    echo exec('sudo python /home/pi/raspberry/control.py');
}

         ?>
