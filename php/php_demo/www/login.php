<?php
require_once 'function_core.php';
require_once 'db.php';

$username=mysqli_real_escape_string($connect,$_POST['username']);
$password=mysqli_real_escape_string($connect,trim($_POST['password']));
$sql = "SELECT username,password FROM db_user where username='$username'";
$result = mysqli_query($connect,$sql);
$rows = mysqli_fetch_row($result);
$core = new function_core();
if($rows[1]==$password)
{
    $core->data_success($rows);
    $_SESSION['is_login'] = 1;
    $_SESSION['username'] = $username;
}
else {
    $core->data_success($rows);
    $core->data_error('登录名或密码错误');
}
mysqli_close($connect);
?>