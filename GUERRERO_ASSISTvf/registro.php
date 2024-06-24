<?php

$conexion = mysqli_connect("localhost", "root", "pao140902GCH", "registro_usuarios") or die("Problemas en la conexión");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los datos del formulario
    $nombre_usuario = $_POST["nombre_usuario"];
    $numero_telefono = $_POST["numero_telefono"];
    $correo_electronico = $_POST["correo_electronico"];

    // Insertar los datos en la base de datos
    $sql = "INSERT INTO usuarios (nombre_usuario, numero_telefono, correo_electronico) VALUES ('$nombre_usuario', '$numero_telefono', '$correo_electronico')";

    if ($conexion->query($sql) === TRUE) {
       //Script para dar de alta los datos
echo'<script type="text/javascript">
alert("El usuario fue dado de alta");
</script>';?>
<?php
include("registro.html");

?>
<?php
    } else {
        echo "Error al registrar usuario: " . $conexion->error;
    }

    // Cerrar la conexión a la base de datos
    mysqli_close($conexion);
}
?>
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>