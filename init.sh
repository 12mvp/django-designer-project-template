VE_PATH=`pwd | grep -o '[^/]*$'`

sudo mkdir -p /opt/$VE_PATH/virt/
sudo chown -R `whoami` /opt/$VE_PATH
virtualenv -p python2.7 /opt/$VE_PATH/virt/
. /opt/$VE_PATH/virt/bin/activate
pip install -r requirements.txt

mv README.md INSTALL.md
cat README.tmpl.md|sed 's/<proj>/'$VE_PATH'/' > README.md
cat README.md
rm README.tmpl.md

