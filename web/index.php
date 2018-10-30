
         <?php
 echo "Version 1";
 echo exec('whoami');
 exec('python /home/pi/raspberry/web/test/temp_control.py',$output,$retval);
echo( $output[0] ." is output and ".$retval. " is return");


		
         ?>
