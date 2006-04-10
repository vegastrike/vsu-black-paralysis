<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml" version="1.0">
    <xsl:output method="xml" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" version="1.0" indent="yes" />
    
    <xsl:template match="text()" />
    
    <xsl:template match="/">
        <html>
            
            <head>
                <meta name="Author" content="Daniel Aleksandrow" />
                <meta name="Copyright" content="Black-Paralysis" />
                <meta name="keywords" content="vegastrike space spaceship" />
                <link rel="stylesheet" type="text/css" href="black-paralysis.css" />
                <title>VSU: Black-Paralysis</title>
            </head>
            
				<body>
            
					<h1>VSU: Black-Paralysis</h1>

					<xsl:call-template name="header-menu" />
                
					<div class="body">
						<h2> ... news</h2>
						<xsl:apply-templates select="//item" />
					</div>
                
					<div class="footer-text">
						&#169; 2004 Black-Paralysis
						<br/>
						<xsl:call-template name="datemod" />
					</div>

					<xsl:call-template name="imagelinks" />

					<xsl:call-template name="statscounter" />

            </body>
        </html>
        
    </xsl:template>
    
    <xsl:template match="item">
        <fieldset>
            <legend>
            <xsl:value-of select="title" />
            <xsl:text> -- </xsl:text>
            <xsl:value-of select="pubDate" />
            </legend>
            <xsl:value-of disable-output-escaping="yes" select="description" />
        </fieldset>
    </xsl:template>
    
    <xsl:template name="imagelinks">
		<div class="footer-images">
			<a href="http://validator.w3.org/check?uri=referer">
				<img class="footer" src="http://www.w3.org/Icons/valid-xhtml10" height="31" width="88" alt="Valid XHTML 1.0!" />
			</a>

			<a href="http://jigsaw.w3.org/css-validator/check/referer">
				<img class="footer" src="http://jigsaw.w3.org/css-validator/images/vcss" width="88" height="31" alt="Valid CSS!" />
			</a>

			<a href="http://sourceforge.net">
				<img class="footer" src="http://sourceforge.net/sflogo.php?group_id=68733&amp;type=1" width="88" height="31" alt="SourceForge.net Logo" />
			</a>
		</div>
    </xsl:template>
    
    <xsl:template name="datemod">
        <span class="datemod">
            <xsl:text>This page last modified on </xsl:text>
            <xsl:value-of select="//channel/lastBuildDate" />
        </span>
    </xsl:template>
    
    <xsl:template name="header-menu">
                <div class="header-menu">
                    <xsl:text>:&#160;</xsl:text>
                    <a href="index.html" class="menu-item">news</a>
                    <xsl:text>&#160;:&#160;:&#160;</xsl:text>
                    <a href="screenshots.html" class="menu-item">screenshots</a>
                    <xsl:text>&#160;:&#160;:&#160;</xsl:text>
                    <a href="download.html" class="menu-item">download</a>
                    <xsl:text>&#160;:&#160;:&#160;</xsl:text>
                    <a href="about.html" class="menu-item">about</a>
                    <xsl:text>&#160;:&#160;:&#160;</xsl:text>
                    <a href="https://sourceforge.net/projects/black-paralysis" class="menu-item">sourceforge.net</a>
                    <xsl:text>&#160;:</xsl:text>
                </div>
    </xsl:template>
    
    <xsl:template name="statscounter">
      <xsl:comment>Start of StatCounter Code</xsl:comment>
        <xsl:text disable-output-escaping="yes">
          <![CDATA[
            <script type="text/javascript">
              <!--
                var sc_project=559740;
                var sc_partition=4;
                //-->
            </script>
          ]]>
        </xsl:text>
      <script type="text/javascript" src="http://www.statcounter.com/counter/counter_xhtml.js" />
      <noscript>
        <div class="statcounter">
          <a class="statcounter" href="http://www.statcounter.com/">
            <img class="statcounter" src="http://c5.statcounter.com/counter.php?sc_project=559740&amp;amp;java=0" alt="web page hit counter" />
          </a>
        </div>
      </noscript>
      <xsl:comment>End of StatCounter Code</xsl:comment>
    </xsl:template>

</xsl:stylesheet>
