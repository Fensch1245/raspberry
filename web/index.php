
         <?php
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_temp.py');
echo "<br/>"; 

         ?>
