<?php
require_once 'function_core.php';
session_start();
$core = new function_core();
if($_SESSION['is_login'] == 1){
    $core->data_error('您已登录');
}
$username = $_POST['username'];
if($username){
    unset($_SESSION['username']);
    $core->data_success();
}