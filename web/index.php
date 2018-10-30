
         <?php
 echo "Version 1";
 exec('python /home/pi/raspberry/temp_control.py',$output,$retval);
echo( $output[1] ." is output and ".$retval. " is return");

		
         ?>
