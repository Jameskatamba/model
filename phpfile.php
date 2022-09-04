<?php

$Rainfall = $_POST['Rainfall'];
$Temperature = $_POST['Temperature'];
$Humidity = $_POST['Humidity'];
$Day = $_POST['Day'];

$command = escapeshellcmd("python pythonfile.py $Rainfall $Temperature $Humidity $Day");
$output = shell_exec($command);
echo $output;

?>

