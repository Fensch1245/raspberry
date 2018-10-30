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

   
shell_exec("/home/pi/raspberry/temp_control.py");
        

         ?>
         </body>
 </html>
