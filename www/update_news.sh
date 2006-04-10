#! /bin/sh
#
# Updates the news from the rss feed

echo "News is ... "
xsltproc -o news.html resources/sfnews.xslt "http://sourceforge.net/export/rss2_projnews.php?group_id=68733&rss_fulltext=1"

if [ -s news.html ]; then
  echo "updating."
  if [ -s index.html ]; then
    echo "Backing up index.html"
    mv index.html index.html.old
  fi
  mv news.html index.html
else
  echo "not updating."
fi
echo "Done."

