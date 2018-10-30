
         <?php
 
 exec('python /home/pi/raspberry/temp_control.py',$output,$retval);
echo( $output[0] ." is output and ".$retval. " is return");

		
         ?>
