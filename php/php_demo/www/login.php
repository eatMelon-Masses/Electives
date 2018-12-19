<?php
if($_SESSION['is_login'] == 1){
    $core->data_error('已登录');
}
require_once 'function_core.php';
require_once 'db.php';
session_start();
$username=$_POST['username'];
$password=md5(trim($_POST['password']));
$sql = "SELECT * FROM db_user where username='".$username."' and password='".$password."'";
$result = mysqli_query($connect,$sql);
$rows = mysqli_fetch_row($result);
$core = new function_core();
if($rows['password']==$password)
{
    $core->data_success($rows);
    $_SESSION['is_login'] = 1;
    $_SESSION['username'] = $username;
}
else {
    $core->data_error('登录名或密码错误');
}
mysqli_close($connect);
?>