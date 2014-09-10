<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
    xmlns:html="http://www.w3.org/TR/REC-html40"
    xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
    xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>XML Sitemap for PILOSA.EU</title>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <style type="text/css">
                    body {
                        background: #fff;
                        color: #333;
                        font-family: Helvetica, Arial, sans-serif;
                        font-size: 12px;
                    }
                    p {
                        margin: 0;
                    }
                    table {
                        margin-top: 20px;
                    }
                    table tr.odd {
                        background-color: #eee;
                    }
                    table tr th {
                        font-size: 11px;
                        text-align: left;
                    }
                    table tr td {
                        font-size: 11px;
                        padding-right: 20px;
                    }
                </style>
            </head>
            <body>
                <h1>XML Sitemap for PILOSA.EU</h1>
                <p>Generated by <a href="https://pypi.python.org/pypi/pelican-extended-sitemap">extended-sitemap plugin</a> for <a href="http://docs.getpelican.com/">Pelican</a>.</p>
                <p>More about sitemaps can be found on <a href="http://sitemaps.org">sitemaps.org</a></p>
                <p>URLs contained in this sitemap: <xsl:value-of select="count(sitemap:urlset/sitemap:url)"/></p>
                <table cellspacing="0">
                    <thead>
                        <tr>
                            <th>URL</th>
                            <th>Priority</th>
                            <th>Change Frequency</th>
                            <th>Last Change</th>
                        </tr>
                    </thead>
                    <tbody>
                        <xsl:for-each select="sitemap:urlset/sitemap:url">
                            <tr>
                                <xsl:if test="position() mod 2 = 1">
                                    <xsl:attribute name="class">odd</xsl:attribute>
                                </xsl:if>
                                <td>
                                    <xsl:variable name="url">
                                        <xsl:value-of select="sitemap:loc"/>
                                    </xsl:variable>
                                    <a href="{$url}"><xsl:value-of select="sitemap:loc"/></a>
                                </td>
                                <td>
                                    <xsl:value-of select="concat(sitemap:priority*100,'%')"/>
                                </td>
                                <td>
                                    <xsl:value-of select="sitemap:changefreq"/>
                                </td>
                                <td>
                                    <xsl:value-of select="sitemap:lastmod"/>
                                </td>
                            </tr>
                        </xsl:for-each>
                    </tbody>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>