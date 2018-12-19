<?php
require_once 'function_core.php';
require_once 'db.php';
session_start();
$username = trim($_POST['username']);
$password = trim(md5($_POST['password']));
$email = trim($_POST['email']);
$tel = trim($_POST['tel']);
$sql = "insert into db_user(username,password,email,tel) VALUES ('".$username."','".$password."','".$email."','".$tel."')";
$result = mysqli_query($connect,$sql);
$core = new function_core();

if($result){
    $core->data_success(array('username' => $username));
    $_SESSION['is_login'] = 1;
    $_SESSION['username'] = $username;
}else{
    $core->data_error('注册失败');
}

mysqli_close($connect);
?>