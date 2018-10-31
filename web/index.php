
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 

$output = shell_exec('ls -lart');
echo "<pre>$output</pre>";


echo "<br/>"; 
echo exec('ls -l /home/pi/raspberry/get_info.py');
echo "<br/>"; 
echo exec('ls -l /home/pi/raspberry/get_config.py');
         ?>
