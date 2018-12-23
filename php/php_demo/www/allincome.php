<?php
require_once 'function_core.php';
require_once 'db.php';




$sql = "select type, money, create_time from income";
$result = mysqli_query($connect,$sql);

$core = new function_core();
if($result->num_rows > 0)
{
    $output;
    $count=0;
     while ($row = mysqli_fetch_assoc($result))
      {
        $temp;
        $temp['type']=$row['type'];
        $temp['money']=$row['money'];
        $temp['createTime']=$row['create_time'];
        $output[$count++]=$temp;
      }
    $core->data_success(urldecode(json_encode($output)));

}
else {
    $core->data_error($result);
}
mysqli_close($connect);
?>