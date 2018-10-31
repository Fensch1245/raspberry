
<html>
<body>


<form action="index.php" method="POST">
<input type="text" name="input_value">
<input type="submit" name="submit">


</body>
</html>

         <?php
		 
		 if (isset($_POST['submit']))
  {
  // Execute this code if the submit button is pressed.
  $formvalue = $_POST['input_value'];
  }
  
echo "Aktuell gemessene Temperatur:";
echo "<br/>"; 
echo exec('sudo python /home/pi/raspberry/get_info.py');
echo "<br/>"; 


         ?>
