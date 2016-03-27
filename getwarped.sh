#!/bin/sh

set -eo pipefail

APP_ROOT=/opt/app-root

VERSION=0

while [ "$#" != "0" ]; do
    case "$1" in
        --version=*)
            VERSION=`echo $1 | sed -e 's/--version=//'`
            ;;
        --version)
            VERSION=$2
            shift
            ;;
        --app-root=*)
            APP_ROOT=`echo $1 | sed -e 's/--app-root=//'`
            ;;
        --app-root)
            APP_ROOT=$2
            shift
            ;;
    esac

    shift
done

BINDIR=${BINDIR:-$APP_ROOT/bin}
TMPDIR=${TMPDIR:-$APP_ROOT/tmp}

case "$VERSION" in
    0)
        VERSION=0.17.0
        ;;
esac

PACKAGE=https://codeload.github.com/GrahamDumpleton/warpdrive/tar.gz/$VERSION

curl -SL -o /tmp/warpdrive.tar.gz $PACKAGE \
  && tar -xC $APP_ROOT  --strip-components=1 -f /tmp/warpdrive.tar.gz \
    warpdrive-$VERSION/warpdrive warpdrive-$VERSION/s2i \
  && rm -f /tmp/warpdrive.tar.gz

mkdir -p $APP_ROOT/bin
mkdir -p $APP_ROOT/tmp

chmod g+ws $APP_ROOT/bin
chmod g+ws $APP_ROOT/tmp

cat >> $APP_ROOT/bin/warpdrive << !
#!/bin/sh
exec $APP_ROOT/warpdrive/bin/warpdrive "\$@"
!

chmod +x $APP_ROOT/bin/warpdrive

PIP_DISABLE_PIP_VERSION_CHECK=1
export PIP_DISABLE_PIP_VERSION_CHECK

virtualenv $APP_ROOT

PATH=$APP_ROOT/bin:$PATH

pip install -U pip

find $APP_ROOT -type d -exec chmod g+ws {} \;

find $APP_ROOT -perm 2755 -exec chmod g+w {} \;
find $APP_ROOT -perm 0644 -exec chmod g+w {} \;

if [ -f $APP_ROOT/etc/scl_enable ]; then
    echo ". $APP_ROOT/warpdrive/etc/shell-init" >> $APP_ROOT/etc/scl_enable
fi
