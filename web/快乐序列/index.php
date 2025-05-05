<?php
highlight_file(__FILE__);
class SecretKeeper {
    private $key;
    public $data;
    
    public function __construct($key) {
        $this->key = $key;
        $this->data = "Nothing to see here";
    }
    
    public function __destruct() {
        if ($this->key === "Sup3rS3cr3tK3y!") {
            $filename = '/flag.txt';
            if (file_exists($filename)) {
                echo file_get_contents($filename);
            }
        }
    }
    public function __toString() {
        return $this->key;
    }
}

class User {
    public $username;
    public $isAdmin;
    
    public function __construct($username) {
        $this->username = $username;
        $this->isAdmin = false;
    }
    
    public function __toString() {
        return $this->username . ($this->isAdmin ? " (Admin)" : "");
    }
}

if (isset($_GET['data'])) {
    $data = base64_decode($_GET['data']);
    $user = unserialize($data);
    echo "Welcome back, " . $user;
} else {
    $defaultUser = new User('guest');
    echo "Welcome, guest! Try to login by passing ?data= parameter";
}
?>