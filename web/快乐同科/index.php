<?php
if (isset($_REQUEST['passwd']) && $_REQUEST['passwd'] === '1') {
    $flag = file_get_contents('flag.txt');
    if ($flag !== false) {
        echo $flag;
    } else {
        echo "Error: flag.txt 未找到";
    }
} else {
    echo "错误，你的权限不够";
}
?>