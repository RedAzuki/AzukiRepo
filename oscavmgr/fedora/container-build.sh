#!/usr/bin/env bash
set -Eeuo pipefail

: "${REPO_URL:?REPO_URL required}"
: "${GIT_REF:?GIT_REF required}"

NAME=oscavmgr
TOPDIR="$HOME/rpmbuild"
SPECS="$TOPDIR/SPECS"
SOURCES="$TOPDIR/SOURCES"

mkdir -p "$SPECS" "$SOURCES"

echo "==> Clone $REPO_URL ($GIT_REF)"
rm -rf "/tmp/${NAME}"
git clone --recursive "$REPO_URL" "/tmp/${NAME}"
cd "/tmp/${NAME}"
git checkout "$GIT_REF"

TAG="$(git describe --exact-match --tags)"
VERSION="${TAG#v}"

COMMIT="$(git rev-parse --short HEAD)"
DATE="$(date -u +%Y%m%d)"

echo "==> VERSION=$VERSION COMMIT=$COMMIT"

TARBALL="${NAME}-${VERSION}.tar.gz"
git archive --format=tar --prefix="${NAME}-${VERSION}/" HEAD | gzip -9 > "${SOURCES}/${TARBALL}"

cp -v /work/oscavmgr.spec "$SPECS/oscavmgr.spec"

rpmbuild -ba \
  --define "_version ${VERSION}" \
  "$SPECS/oscavmgr.spec"

find "$TOPDIR/RPMS" -type f -name "*.rpm" -exec cp -v {} /out/ \;
find "$TOPDIR/SRPMS" -type f -name "*.src.rpm" -exec cp -v {} /out/ \;

echo "==> Done"
