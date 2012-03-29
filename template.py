
MAIN_PAGE = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
  <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
  <title>Minecraft Party</title>
  <link rel="stylesheet" href="/bebas/stylesheet.css" type="text/css" media="screen" title="no title" charset="utf-8"/>
  <style type='text/css'>
  *{margin:0;padding:0;}
  html{background-color:#eee;}
  body{width:50em;margin:2em auto;position:relative;}
  h1{font:3em/2em Bebas,sans-serif;word-spacing:0.15ex;padding-left:2.4em;}
  h1{background:url(/Minecraft_Logo.png) no-repeat;background-size:2em;margin-bottom:1em;}
  p{font:1em/1.7em Georgia,serif;margin-bottom:1em;}
  .letter{position:absolute;width:63%;text-align:justify;}
  .header{margin-bottom:2em;}
  .sig{text-align:right;margin-top:3em;}
  .comments{position:absolute;right:0;left:66%;background-color:#fff;border:1px solid #ddd;padding:1em;top:13em;}
  .comments h2{font:bold 0.7em Helvetica,sans-serif;text-transform:uppercase;}
  .comments form{height:7em;position:relative;margin:0.5em 0;}
  .comments textarea{position:absolute;top:0;left:0;right:0;bottom:2em;padding:1em;}
  .comments textarea.default{color:#555;}
  .comments input{position:absolute;bottom:0;right:0;}
  .comments label{position:absolute;bottom:0;left:0;font:0.75em sans-serif;color:#222;}
  .comments label input{position:static;}
  .comments #overlay{position:absolute;top:0;bottom:0;left:0;right:0;padding:1.5em 1em;text-align:center;}
  .comments #overlay{z-index:999;background-color:#333;opacity:0;color:#fff;font:bold 2em Helvetica,sans-serif;}
  .comments #overlay{-webkit-transition:opacity 0.2s linear;}
  .comments #overlay.fadeout{opacity:0;}
  .comments #overlay.fadein{opacity:0.5;}
  a{color:#333;}
  a:hover{color:#39c;}
  pre{white-space:pre-wrap;background-color:#111;padding:1em;font:13px Monaco,monospace;color:#eee;}
  </style>
</head>
<body>
  <h1>The Eleventh Hour</h1>
  <div class='comments'>
  %{OVERLAY}%
  <h2>Can you come?</h2>
  <form method='post'>
  <textarea name='value' class='default'>Any allergies? Transportation Questions?</textarea>
  <label><input type='checkbox' name='replyall'/> Send to everyone.</label>
  <input type='submit' value='Save Comment'/>
  </form>
  </div>
  <div class='letter'>
  <p class='header'>Agents:</p>

  <p>The time has come. As many of you have been informed on-line and off-, Bond Air is a go. Yes, I went there. Even in this economy, bonds provide a modicum of stability for those of us in our selected profession. For the same reason &#x2014; to confuse the more astute of you &#x2014; the timing for the mission will not coincide with eleven o'clock. Puns await those that arrive early &#x2014; -er than about one o'clock PM in the afternoon &#x2014; or without digital conveyance. The meeting will convene at The Club, which naturally resides at 5712 Harper South. On the other end of the spectrum &#x2014; owing to the lateness of the hour, and the mild suggestion of class the following morning &#x2014; the bash will be bashed at six. Please leave before then.</p>

  <p>Minecraft will not be our only entertainment, but, dishes willing, the party will be an ample source thereof. Naturally, siblings are invited, where appropriate, as the Minister has always had my heightened regard. Naturally, A Feast [ pizza or sandwiches &#x2014;ed ] will likely be served, and, as before, the Agency may arrange cookies. The House-warmers naturally have left us well-prepared, but in regard to special equipment &#x2014; software modifications et. al. &#x2014; the Minister has yet to arrange matters.</p>

  <p>Ah: that leaves us the remaining feature: <i>when</i> this event is to occur. Haw haw haw. We must convene on eleventh, March Sunday. Naturally, the Minister will disavow any knowledge of your existence should you be compromised or killed. In that vein, Special Branch has prepared a video for your entertainment. (<a href="http://youtu.be/hKxN9I_eRTs">youtu.be/hKxN9I_eRTs</a>) and Q sends his regards. I'm really proud of this one &#x2014; try not to lose it.</p>

  <p class='sig'>&#x2014;<br/>
  Horace E. Lephant,<br/>
  khakimaroon@gmail.com</p>
  </div>
  <script type='text/javascript'>
  var txt = document.getElementsByTagName('textarea')[0];
  txt.onfocus = function() {
    if (txt.value == txt.defaultValue) {
      txt.setAttribute('class', '');
      txt.value = '';
    }
  }
  txt.onblur = function() {
    txt.value = txt.value.trim();

    if (txt.value == "" || txt.value == txt.defaultValue) {
      txt.value = txt.defaultValue;
      txt.setAttribute('class', 'default');
    }
  }
  var overlay = document.getElementById('overlay');
  setTimeout(function() { overlay.setAttribute('class', 'fadein'); }, 0);
  setTimeout(function() { overlay.setAttribute('class', 'fadeout'); }, 2000);
  setTimeout(function() { overlay.parentNode.removeChild(overlay); }, 3000);
  </script>
</body>
</html>

"""
