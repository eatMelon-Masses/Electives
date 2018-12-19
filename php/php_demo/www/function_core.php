<?php

class function_core{

    function data_success($data = array()){
        echo json_encode( array('status' => true, 'datas' => $data ) );exit;
    }

    function data_error($error){
        echo json_encode( array('status' => false, 'error' => $error ) );exit;
    }
}