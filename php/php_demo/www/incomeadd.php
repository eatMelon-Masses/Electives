<?php
require_once 'function_core.php';
require_once 'db.php';
$type=$_POST['type'];
$money=trim($_POST['money']);
$remark=$_POST['remark'];

$type=mysqli_real_escape_string($connect, $type);
$money=mysqli_real_escape_string($connect, $money);
$remark=mysqli_real_escape_string($connect, $remark);

$sql = "INSERT INTO income(money, type, mark) VALUES ('$type','$money','$remark')";
$result = mysqli_query($connect,$sql);

$core = new function_core();
if($result)
{
    $core->data_success('添加成功');
}
else {
    $core->data_error($result);
}
mysqli_close($connect);
?>