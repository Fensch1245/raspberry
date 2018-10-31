
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 

echo exec('sudo python /home/pi/raspberry/get_config.py 2>&1');



echo "<br/>"; 
echo exec('ls -l /home/pi/raspberry/get_info.py');
echo "<br/>"; 
echo exec('ls -l /home/pi/raspberry/get_config.py');
         ?>
