# AzukiRepo

AzukiRepo is a work in progress. It's a Linux package repository for VR games and tools.


## Sign and Upload Stuff
```
rpm --addsign out/*.rpm
cp out/*.rpm ~/repo/redazuki/fedora/43/x86_64/

createrepo_c --update repo/redazuki/fedora/43/x86_64/

gpg --batch --yes --armor --detach-sign \
  -o repo/redazuki/fedora/43/x86_64/repodata/repomd.xml.asc \
  repo/redazuki/fedora/43/x86_64/repodata/repomd.xml

aws s3 sync repo/redazuki/ s3://azukirepo/ --delete

aws cloudfront create-invalidation \
  --distribution-id ERCEX6I52VKU2 \
  --paths "/fedora/43/x86_64/repodata/*"
```