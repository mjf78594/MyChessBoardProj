<?php
require_once '/Users/mjf78594/Documents/MyChessBoardProj/vendor/autoload.php';
$loader = new Twig_Loader_Filesystem('/Users/mjf78594/Documents/MyChessBoardProj/twig/');
$twig = new Twig_Environment($loader);
$color_array = array(for($i =0; $i < 8; $i++){
  array(for($j = 0; $j < 8; $j++){
    if($i % 2 === 0){
      if($j %2 === 0){
        <td bgcolor="Black"></td>
      }
    }elseif ($i % 2 != 0) {
      if($j % 2 === 0) {
        <td bgcolor="White"></td>
      }
    }elseif ($j % 2 === 0) {
      <td bgcolor="Black"></td>
    }else {
      <td bgcolor="White"></td>
    }
  })
});
$html = $twig->render('board.html', array(
	'color_array' => $color_array,
  "test" => "hello world"
	));
echo $html;
?>
