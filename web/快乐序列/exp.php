<?php
class SecretKeeper {
    private $key = "Sup3rS3cr3tK3y!";
}

$obj = new SecretKeeper();
echo base64_encode(serialize($obj));
?>