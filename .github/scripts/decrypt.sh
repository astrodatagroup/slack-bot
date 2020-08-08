#!/bin/sh

gpg --quiet --batch --yes --decrypt --passphrase="$GPG_PASSPHRASE" --output secrets.tar.gz secrets.tar.gz.gpg
tar -xf secrets.tar.gz
