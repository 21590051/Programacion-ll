<?php
	
	$mysqli = new mysqli('localhost:3308', 'root', 'root', 'personal');
	
	if($mysqli->connect_error){
		
		die('Error en la conexion' . $mysqli->connect_error);
		
	}
?>
