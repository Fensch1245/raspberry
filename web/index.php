
<html>
<body>

<form name='form' method='post' action="index.php">

Name: <input type="text" name="name" id="name" ><br/>

<input type="submit" name="submit" value="Submit">  

</form>
</body>
</html>

         <?php
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 


         ?>
