<html>
<head>
 <meta name="viewport" content="width=device-width" />
 <title>Temp-Control</title>
 </head>
         <body>

         <form method="get" action="index.php">
			<input type="text" name="input_value">
            <input type="submit" name="Speichern" value=input_value>

         </form>
  
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 


         ?>
</html>