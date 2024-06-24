<?php

$conexion = mysqli_connect("localhost", "root", "pao140902GCH", "registro_usuarios") or die("Problemas en la conexión");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los datos del formulario
    $nombre_usuario_s = $_POST["nombre_usuario_s"];
    $sugerencia = $_POST["sugerencia"];
    $numero_telefono_s = $_POST["numero_telefono_s"];
    $correo_electronico_s = $_POST["correo_electronico_s"];

    // Insertar los datos en la base de datos
    $sql = "INSERT INTO sugerencias (nombre_usuario_s, sugerencia, numero_telefono_s, correo_electronico_s) VALUES ('$nombre_usuario_s', '$sugerencia', '$numero_telefono_s', '$correo_electronico_s')";

    if ($conexion->query($sql) === TRUE) {
       //Script para dar de alta los datos
echo'<script type="text/javascript">
alert("La sugerencia se ha enviado correctamente");
</script>';?>
<?php
include("sugerencias.html");

?>
<?php
    } else {
        echo "Error al registrar usuario: " . $conexion->error;
    }

    // Cerrar la conexión a la base de datos
    mysqli_close($conexion);
}
?>
