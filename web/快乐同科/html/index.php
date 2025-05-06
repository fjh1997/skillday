<?php
include "flag.php";
highlight_file(__FILE__);

if (isset($_REQUEST['passwd']) && $_REQUEST['passwd'] === '1') {
    if ($flag !== false) {
        echo $flag;
    } else {
        echo "Error: flag未找到";
    }
} else {
    echo "错误，你的权限不够";
}
?>