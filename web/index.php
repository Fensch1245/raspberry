
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 

$result = shell_exec('sudo python /home/pi/raspberry/get_config.py');
echo "<pre>"$result"</pre>";

echo "<br/>"; 
echo exec('ls -l /home/pi/raspberry/get_info.py');
echo "<br/>"; 
echo exec('ls -l /home/pi/raspberry/get_config.py');
         ?>
