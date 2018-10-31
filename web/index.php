<html>
<head>
 <meta name="viewport" content="width=device-width" />
 <title>Temp-Control</title>
 </head>
         <body>

         <form method="get" action="index.php">
                 <input type="submit" value="wadu" name="on">

         </form>
  
		 
		 <?php
		   
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 


         ?>
</html>