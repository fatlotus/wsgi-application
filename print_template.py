FRONT = """
<style type='text/css'>
*{margin:0;padding:0;}
.page{text-align:center;padding-top:4in;page-break-before:always;}
img{width:1in;margin-bottom:0.5in;}
p{font:1em Monaco,monospace;}
h1{font:2em Bebas;word-spacing:0.15ex;text-align:center;margin:0.5em 0;}
ul{width:4in;margin:0 auto;background-color:#eee;border-radius:0.5em;overflow:hidden;border:1px solid #ccc;}
ul li{display:block;padding:1em;border-bottom:1px solid #ddd;;}
ul li{font:1em Helvetica,sans-serif;}
ul li code{font:13px Monaco,monospace;}
</style>
<div class='front'>
<h1>The Eleventh Hour</h1>
<ul>%{UL}%</ul>
</div>
<script type='text/javascript'>
window.onload = function() {
  window.print();
  window.location.href = '/politburo';
}
</script>
"""

EACH_PAGE = """
<div class='page'>
<img src='/Minecraft_Logo.png'/>
<p>http://fatlotus.com/%{URL}%</p>
</div>
"""

def render_page(people):
  ul = '\n'.join(['<li>%s (<code>%s</code>)</li>' % person for person in people])
  
  chunks = [ FRONT.replace("%{UL}%", ul) ] + [ EACH_PAGE.replace('%{URL}%', person[1]) for person in people ]
  
  return str(''.join(chunks))