
         <?php
 echo "Version 1";
 echo "<br/>";
 echo exec('whoami');
 echo "<br/>";
 echo exec('sudo python /home/pi/raspberry/get_temp.py');
 echo "<br/>";
 echo exec('ls -l /home/pi/raspberry/temp_control.py');	
echo "<br/>"; 


    echo "Current user is: " . get_current_user();
    echo "Command output is " . shell_exec("sudo python /home/pi/raspberry/temp_control.py");

         ?>
