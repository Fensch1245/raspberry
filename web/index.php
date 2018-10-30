
         <?php
 echo "Version 1";
 exec('python /home/pi/raspberry/temp_control.py',$output,$retval);
echo( $output[0] ." is output and ".$retval. " is return");

foreach ($output as $item) {
	echo "item";
    echo $item;
}
		
         ?>
