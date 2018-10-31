<html>
<head>
 <meta name="viewport" content="width=device-width" />
 <title>Temp-Control</title>
 </head>
         <body>

         <form method="get" action="index.php">
			<input type="text" name="input_value" value="<?php echo($wadu); ?>">
            <input type="submit" name=input_value value="Speichern">

         </form>
  
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 

$wadu = "HEK";

         ?>
</html>