#!/usr/bin/env bash
set -Eeuo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <fedora_version> <git_tag>" >&2
  echo "Example: $0 43 v0.3.5" >&2
  exit 1
fi

FEDORA_VERSION="$1"
GIT_REF="$2"

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTDIR="${HERE}/out"
mkdir -p "$OUTDIR"

REPO_URL="https://github.com/galister/motoc"
IMAGE="azukirepo-motoc-fedora${FEDORA_VERSION}:clean"

echo "==> Build image (Fedora ${FEDORA_VERSION})"
docker build --no-cache \
  --build-arg "FEDORA_VERSION=${FEDORA_VERSION}" \
  -t "$IMAGE" \
  -f "${HERE}/Dockerfile" \
  "${HERE}"

echo "==> Run container build"
docker run --rm -t \
  -v "${HERE}":/work:Z \
  -v "${OUTDIR}":/out:Z \
  -e REPO_URL="$REPO_URL" \
  -e GIT_REF="$GIT_REF" \
  "$IMAGE" \
  bash /work/container-build.sh

echo
echo "✅ RPMs are in ${OUTDIR}"
ls -lh "${OUTDIR}"
