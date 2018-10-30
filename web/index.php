<html>
<head>
 <meta name="viewport" content="width=device-width" />
 <title>LED Control</title>
 </head>
         <body>
         Torsteuerung wadu hek
         <form method="get" action="index.php">
                 <input type="submit" value="ON" name="on">

         </form>
		 
         <?php
 
 exec('python /home/pi/raspberry/temp_control.py',$output,$retval);
        echo "<prev>";
        var_dump($output);
        print_r("My Farm");
        print_r(" out  ".$output[0]);
        print_r(" ret  ".$retval[0]);
		
         ?>
         </body>
 </html>
