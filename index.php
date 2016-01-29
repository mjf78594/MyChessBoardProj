<?php
require_once '/Users/mjf78594/Documents/MyChessBoardProj/vendor/autoload.php';
$loader = new Twig_Loader_Filesystem('/Users/mjf78594/Documents/MyChessBoardProj/twig/');
$twig = new Twig_Environment($loader);
for($i = 0; $i < 8; $i++){
  for($j = 0; $j <8; $j++){
    if($i % 2 == 0){
      if($j % 2 == 0){
        $color_array[$i][$j] = 'White';
      }else{
        $color_array[$i][$j] = 'Black';
      }
    }else{
      if($j % 2 == 0){
        $color_array[$i][$j] = 'Black';
      }else{
        $color_array[$i][$j] = 'White';
      }
    }
  }
}
$html = $twig->render('board.html', array(
	'color_array' => $color_array,
  "test" => "hello world"
	));
echo $html;
?>
