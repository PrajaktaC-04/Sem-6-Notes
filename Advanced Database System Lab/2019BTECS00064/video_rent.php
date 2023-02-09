<!DOCTYPE HTML>
<html>
<head>
    <title>Bootstrap Login</title>
    <!-- bootstrap-3.3.7 -->
    <link rel="stylesheet" href="bootstrap-3.3.7/css/bootstrap.min.css">
    <script src="bootstrap-3.3.7/js/bootstrap.min.js"></script>
    <!-- JQUERY -->
    <script type="text/javascript" language="javascript" src="jquery/jquery.js"></script>
    <link href="style/style.css" rel="stylesheet" type="text/css" media="all" />
    <script type="text/javascript" language="javascript" src="style/style.js"></script>
</head>
<body>
    <div class="navbar navbar-default navbar-static-top" role="navigation">
       <div class="container">
           <div class="navbar-header">
               <a class="navbar-brand" href="index.php">Home</a>
               <a class="navbar-brand" href="video_rent.php">Rent</a>
               <a class="navbar-brand" href="video_submit.php">Submit</a>
               <!-- <a class="navbar-brand" href="#">Navbar 3</a>
               <a class="navbar-brand" href="#">Navbar 4</a> -->
               <!-- <a class="navbar-brand pull-right" href="logout.php?destroy"> <span class="glyphicon glyphicon-off"></span> Logout </a> -->
               <a class="navbar-brand pull-right"><span class="glyphicon glyphicon-user"></span> <?=$_SESSION['name'];?> </a>
           </div>
        </div>
    </div>
    <div class="container">
        <div class="card card-container">
            <img id="profile-img" class="profile-img-card" src="img/avatar_2x.png" />
            <p id="profile-name" class="profile-name-card"></p>
            <form class="form-signin" action="" method="POST">
                <span id="reauth-email" class="reauth-email"></span>
                <input type="text" id="inputText" name="video" class="form-control" placeholder="Video URL" required autofocus>
                <input type="text" id="inputText" name="customer" class="form-control" placeholder="Customer Name" required>
                <input type="text" id="inputText" name="dateout" class="form-control" placeholder="Date Out" required>
                <input type="text" id="inputText" name="dateduein" class="form-control" placeholder="Date Due In" required>
                <br>
                <button class="btn btn-lg btn-primary btn-block btn-signin" type="submit" name="login">Sign in</button>
            </form>
        </div>
    </div>
</body>
</html>
<?php
include "db_con.php";
IF(ISSET($_POST['login'])){
$videoURL = $_POST['video'];
$customer = $_POST['customer'];
$dateout = $_POST['dateout'];
$dateduein = $_POST['dateduein'];
$cek = mysql_num_rows(mysql_query("INSERT INTO Rent_Info (video_id,customer_name,date_out,date_due_in) VALUES('$videoURL','$customer','$dateout','$dateduein')"));
// $data = mysql_fetch_array(mysql_query("SELECT * FROM user_login WHERE email='$email' AND password='$password'"));
IF($cek == True)
{
//  session_start();
//  $_SESSION['email'] = $data['email'];
//  $_SESSION['name'] = $data['full_name'];
 echo "<script language=\"javascript\">alert(\"Data inserted Successfully \");document.location.href='index.php';</script>";
}else{
 echo "<script language=\"javascript\">alert(\"Data Insrtion Failed\");document.location.href='vide_rent.php';</script>";
}
}
?>
