<?php

$email = $_POST["email"];
$subject = $_POST["subject"];
$message = $POST["message"];

require "vendor/autoload.php";

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;

$mail = new PHPMailer(true);

$mail->isSMTP();
$mail->SMTPAuth = true;
$mail->Host = "smtp.gmail.com";
$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
$mail->Username = "vistafpv25@gmail.com";
$mail->Password = "password";

$mail->setFROM($email, $name);
$mail->addAddress("vistafpv25@gmail.com", "VistaFPV");

$mail->Subject = $subject;
$mail->Body = $message;

$mail->send();

echo "email sent";

?>