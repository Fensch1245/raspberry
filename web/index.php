
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 

$result = shell_exec('sudo python /home/pi/raspberry/get_config.py');
$results_array = json_decode($result);
echo "<p>".$results_array."</p>";

echo "<br/>"; 
echo exec('ls -l /home/pi/raspberry/get_info.py');
echo "<br/>"; 
echo exec('ls -l /home/pi/raspberry/get_config.py');
         ?>
