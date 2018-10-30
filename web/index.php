<html>
<head>
 <meta name="viewport" content="width=device-width" />
 <title>LED Control</title>
 </head>
         <body>
         Torsteuerung
         <form method="get" action="index.php">
                 <input type="submit" value="ON" name="on">

         </form>
         <?php

         $setmode17 = shell_exec("/usr/local/bin/gpio -g mode 4 out");
         if(isset($_GET['on'])){
                 $gpio_on = shell_exec("/usr/local/bin/gpio -g write 4 0");
                 echo "Tor aktiviert!";

                SLEEP(1);
shell_exec("/usr/local/bin/gpio -g write 4 1");





         }

         ?>
         </body>
 </html>
