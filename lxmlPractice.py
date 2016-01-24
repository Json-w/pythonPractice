from lxml import etree

html = '''\
 <html>
  <head>
     <script type="text/javascript" src="evil-site"></script>
     <link rel="alternate" type="text/rss" src="evil-rss">
     <style>
       body {background-image: url(javascript:do_evil)};
       div {color: expression(evil)};
     </style>
   </head>
   <body onload="evil_function()">
     <!-- I am interpreted for EVIL! -->
     <a href="javascript:evil_function()">a link</a>
     <a href="#" onclick="evil_function()">another link</a>
     <p onclick="evil_function()">a paragraph</p>
     <div style="display: none">secret EVIL!</div>
     <object> of EVIL! </object>
     <iframe src="evil-site"></iframe>
     <form action="evil-site">
       Password: <input type="password" name="password">
    </form>
    <blink>annoying EVIL!</blink>
    <div id="test"> this is a div
        <a href="evil-site">spam spam SPAM!</a>
    </div>
    <image src="evil!">
  </body>
 </html>'''

selector = etree.HTML(html)

# 提取标签文本
print(selector.xpath('//a/text()'))

# 提取指定属性标签的文本
print(selector.xpath('//a[@href="evil-site"]/text()'))

# 获取标签属性值
print(selector.xpath('//a/@href'))

# starts-with的用法
print(selector.xpath('//a[starts-with(@href,"evil")]/text()'))

# string(.) 获取标签套标签的文本

data = selector.xpath('//div[@id="test"]')[0]
content = data.xpath('string(.)')
print(type(data))
print(content)
